import os, time, Queue, requests, json, urllib
from threading import Thread
from purl import URL
from django.shortcuts import render
from django.core.exceptions import FieldDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from backend.models import Sensors, Clusters
from backend.serializers import SensorsSerializer, ClustersSerializer


BIGDATA_SCHEME = 'http'
BIGDATA_HOST = 'ec2-54-202-7-99.us-west-2.compute.amazonaws.com'

# Create your views here.


@login_required()
def home_page(request, *args, **kwargs):
    sensors = Sensors.objects.values()
    sensors = list(sensors)
    clusters = Clusters.objects.values()
    clusters = list(clusters)

    clusters_range = []
    for i in range(0, len(clusters)):
        clusters_range.append(i)

    backend_data = {}
    backend_data['clusters_range'] = clusters_range
    datas = {}
    datas['sensors'] = sensors
    datas['clusters'] = clusters
    datas = json.dumps(datas)
    backend_data['datas'] = datas
    backend_data['sensors'] = sensors
    backend_data['clusters'] = clusters
    return render(request, 'backend/home.html', {'backend_data': backend_data})


@login_required()
def all_clusters_sensors_web(request):
    if request.method == 'GET':
        sensors = Sensors.objects.values()
        sensors = list(sensors)
        clusters = Clusters.objects.values()
        clusters = list(clusters)
        datas = {}
        datas['sensors'] = sensors
        datas['clusters'] = clusters
        datas = json.dumps(datas)
        return HttpResponse(datas, status=200)
    return HttpResponse('forbidden', status=401)


@login_required()
def test_api(request):
    return HttpResponse('test_api_secret', status=200)

@login_required()
def cluster_detail_update_web(request, pk):
    if request.method == 'GET':
        try:
            clusters = Clusters.objects.get(pk=pk)
        except Clusters.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            clusters = Clusters.objects.filter(id=pk).values()
        response = {'response': list(clusters)}
        return Response(response)
    elif request.method == 'PUT':
        try:
            cluster = Clusters.objects.get(pk=pk)
        except Clusters.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            cluster_data = json.loads(urllib.unquote(request.body))
            serializer = ClustersSerializer(cluster, data=cluster_data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            clusters = Clusters.objects.filter(id=pk).values()
        response = {'response': list(clusters)}

        sensors = Sensors.objects.values()
        sensors = list(sensors)
        clusters = Clusters.objects.values()
        clusters = list(clusters)

        clusters_range = []
        for i in range(0, len(clusters)):
            clusters_range.append(i)

        backend_data = {}
        backend_data['clusters_range'] = clusters_range
        data_dic = {}
        data_dic['sensors'] = sensors
        data_dic['clusters'] = clusters
        data_str = json.dumps(data_dic)
        backend_data['data_str'] = data_str
        backend_data['sensors'] = sensors
        backend_data['clusters'] = clusters
        return render(request, 'backend/login.html', {'backend_data': backend_data})
    else:
        return Response('not supported', status=404)

@login_required()
@api_view(['GET', 'POST'])
def sensor_list_deploy(request):
    """
    list all sensors
    """
    if request.method == 'GET':
        sensors = Sensors.objects.values()
        response = {'response': list(sensors)}
        return Response(response)
    else:
        serializer = SensorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@login_required()
@api_view(['GET', 'PUT'])
def sensor_detail_update(request, pk):
    """
    retrieve, update or delete a sensors instance
    """
    if request.method == 'GET':
        try:
            sensors = Sensors.objects.get(pk=pk)
        except Sensors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            sensors = Sensors.objects.filter(id=pk).values()
        response = {'response': list(sensors)}
        return Response(response)
    else:
        try:
            sensor = Sensors.objects.get(pk=pk)
        except Sensors.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = SensorsSerializer(sensor, data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            sensor = Sensors.objects.filter(id=pk).values()
        response = {'response': list(sensor)}
        return Response(response)


# @login_required()
# @api_view(['PUT'])
# def sensor_update(request, pk):
#     """
#     update cluster information
#     """
#     try:
#         sensor = Sensors.objects.get(pk=pk)
#     except Sensors.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     else:
#         serializer = SensorsSerializer(sensor, data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         sensor = Sensors.objects.filter(id=pk).values()
#     response = {'response': list(sensor)}
#     return Response(response)


# @login_required()
# @api_view(['POST'])
# def sensor_deploy(request):
#     """
#     deploy a sensor
#     """
#     serializer = SensorsSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required()
@api_view(['GET', 'POST'])
def cluster_list_deploy(request):
    """
    list all clusters
    """
    if request.method == 'GET':
        clusters = Clusters.objects.values()
        response = {'response': list(clusters)}
        return Response(response)
    else:
        serializer = ClustersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required()
@api_view(['GET', 'PUT'])
def cluster_detail_update(request, pk):
    """
    retrieve cluster detail information
    """
    if request.method == 'GET':
        try:
            clusters = Clusters.objects.get(pk=pk)
        except Clusters.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            clusters = Clusters.objects.filter(id=pk).values()
        response = {'response': list(clusters)}
        return Response(response)
    else:
        try:
            cluster = Clusters.objects.get(pk=pk)
        except Clusters.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ClustersSerializer(cluster, data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            clusters = Clusters.objects.filter(id=pk).values()
        response = {'response': list(clusters)}
        return Response(response)


@login_required()
@api_view(['GET'])
def cluster_sensor(request, cluster_id):
    """
    retrieve cluster detail information
    """
    try:
        clusters = Clusters.objects.get(pk=cluster_id)
    except Clusters.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        sensors = Sensors.objects.filter(cluster_id=cluster_id).values()
    response = {'response': list(sensors)}
    return Response(response)

@login_required()
@api_view(['GET'])
def all_clusters_sensors(request):
    response = {}
    response['response'] = {}
    response['response']['sensors'] = []
    response['response']['clusters'] = []
    sensors = Sensors.objects.values()
    response['response']['sensors'] = list(sensors)
    clusters = Clusters.objects.values()
    response['response']['clusters'] = list(clusters)
    return Response(response)


@login_required()
@api_view(['GET'])
def all_clusters_sensors_dummy(request):
    response = {}
    response['response'] = {}
    clusters = [{
        "operation": False,
        "message": "sensor nodes got attacked",
        "health": "warning",
        "id": 1
      },
      {
        "operation": True,
        "message": "",
        "health": "ok",
        "id": 2
      }]
    response['response']['clusters'] = clusters
    sensors = [{
        "manufacture": "Capgo",
        "message": "blackhole_attack",
        "longitude": -122.431297,
        "sensor_type": "temperature",
        "health": "bad",
        "latitude": 37.773972,
        "operation": False,
        "cluster_id_id": 1,
        "id": 1
      },
      {
        "manufacture": "ThomasNet",
        "message": "",
        "longitude": -122.469233,
        "sensor_type": "pressure",
        "health": "ok",
        "latitude": 37.699466,
        "operation": True,
        "cluster_id_id": 2,
        "id": 6
      },
      {
        "manufacture": "InvenSense",
        "message": "",
        "longitude": -122.480059,
        "sensor_type": "motion",
        "health": "ok",
        "latitude": 37.829216,
        "operation": True,
        "cluster_id_id": 3,
        "id": 11
      }]
    response['response']['sensors'] = sensors
    return Response(response)


# @login_required()
# @api_view(['PUT'])
# def cluster_update(request, pk):
#     """
#     update cluster information
#     """
#     try:
#         cluster = Clusters.objects.get(pk=pk)
#     except Clusters.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     else:
#         serializer = ClustersSerializer(cluster, data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()
#         clusters = Clusters.objects.filter(id=pk).values()
#     response = {'response': list(clusters)}
#     return Response(response)


# @login_required()
# @api_view(['POST'])
# def cluster_deploy(request):
#     """
#     deploy a cluster
#     """
#     serializer = ClustersSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required()
@api_view(['GET'])
def run_leach(request):
    queue = Queue()
    t = Thread(target=leach, args=(queue,))
    t.setDaemon(True)
    t.start()
    return Response()


def leach(queue):
    while True:
        print('leach running...')
        clusters = Clusters.objects.values()
        for cluster in clusters:
            cluster_id = cluster['id']
            try:
                cluster_obj = Clusters.objects.get(pk=cluster_id)
            except Clusters.DoesNotExist:
                continue
            else:
                cluster_obj = Clusters.objects.filter(id=cluster_id).values()
                if 'pending' in cluster_obj[0]['message'] and 'unavailable' in cluster_obj[0]['health']:
                    Clusters.objects.filter(id=cluster_id).update(health='ok', message='')

            sensors = Sensors.objects.filter(cluster_id=cluster_id).values()

            for sensor in sensors:
                if 'pending' in sensor['message'] and 'unavailable' in sensor['health']:
                    Sensors.objects.filter(pk=sensor['id']).update(health='ok', message='')

            sensors = Sensors.objects.filter(cluster_id=cluster_id).values()
            input_file_name = 'input_' + str(cluster_id) + '.txt'
            if sensors and cluster_obj[0]['operation']:
                try:
                    with open(input_file_name, 'w') as file_write_object:
                        for sensor in sensors:
                            if sensor['operation']:
                                file_write_object.write(str(sensor['id']) + '\t')
                                file_write_object.write(str(sensor['longitude']) + '\t')
                                file_write_object.write(str(sensor['latitude']) + '\n')
                    os.system('./wsn ' + input_file_name + ' 3' + ' 1')
                except FileNotFoundError:
                    continue
        time.sleep(10)


def parse_log(log_filename):
    lines = []
    parsed_results = []
    try:
        with open(log_filename, 'r') as file_read_object:
            lines = file_read_object.read().splitlines()
    except FileNotFoundError:
        return
    for line in lines:
        if '----' in line:
            continue
        parsed_results.append(line)
    return parsed_results


def send_log_to_bigdata(log_filename):
    url = URL(scheme=BIGDATA_SCHEME, host=BIGDATA_HOST, path='/backend/bigdata/feedlog')
    parsed_results = parse_log(log_filename)
    """
    {
        "connection_id": "con_nnnnn",
        "current_CH_id": "aaa",
        "from_node_id": "xxx",
        "from_node_cluster_id": "xxx000n",
        "traffic_pattern": "feature_0_value, feature_1_value.......feature_41_value",
        "to_node_id": "yyy",
        "to_node_cluster_id": "yyy000n",
        "timestamp": "yyyymmddhhmmss"
    }
    """
    for result in parsed_results:
        cluster_id = log_filename.split('/')[-1].split('.')[0].split('_')[-1]
        data = {}
        data['connection_id'] = result[0]
        data['current_CH_id'] = result[4]
        data['from_node_id'] = result[1]
        data['from_node_cluster_id'] = cluster_id
        col = result.split('\t')
        traffic_pattern = ''
        comma = ''
        for i in range(1, 19):
            traffic_pattern += comma
            traffic_pattern += col[i]
            comma = ', '
        data['traffic_pattern'] = traffic_pattern
        data['to_node_id'] = result[4]
        data['to_node_cluster_id'] = cluster_id
        data['timestamp'] = result[2]

        # check if response is not 200
        time.sleep(5)

@login_required()
@api_view(['GET'])
def feed_log(request):
    url = URL(scheme=BIGDATA_SCHEME, host=BIGDATA_HOST, path='/backend/bigdata/feedlog')
    response = requests.post(url, data=None)
    return Response()

@login_required()
@api_view(['GET'])
def get_analysis_result(request):
    """
    {
        "rstlst": [
            {
            "connection_id": "con_0001",
            "current_CH_id": "aaa",
            "from_node_id": "xxx",
            "from_node_cluster_id": "xxx000n",
            "attacktype": "Normal/Probe/R2L/U2R/DOS",
            "to_node_id": "yyy",
            "to_node_cluster_id": "yyy000n",
            "timestamp": "yyyymmddhhmmss"
            },
        ]
    }
    :return:
    """
    url = URL(scheme=BIGDATA_SCHEME, host=BIGDATA_HOST, path='/backend/bigdata/refresh')
    # results = requests.get(url)
    # if results.ok:
    if True:
        datas = {'rstlst':[{'attacktype':'blackhole_attack'}]}
        # datas = results.json()
        for data in datas['rstlst']:
            # node_id = data['from_node_id']
            # cluster_id = data['from_node_cluster_id']
            node_id = 1
            cluster_id = 1
            try:
                sensor = Sensors.objects.get(pk=node_id)
            except Sensors.DoesNotExist:
                continue
                # return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                sensor_info = Sensors.objects.filter(id=node_id).values()
                sensor_info = sensor_info.get()
                sensor_info['operation'] = False
                sensor_info['health'] = 'bad'
                sensor_info['message'] = data['attacktype']
                sensor_info['cluster_id'] = cluster_id
                sensor_info = json.dumps(sensor_info)
                sensor_info = json.loads(sensor_info)
                serializer = SensorsSerializer(sensor, data=sensor_info)
                if not serializer.is_valid():
                    continue
                    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                sensor_info = Sensors.objects.filter(id=node_id).values()

            try:
                cluster = Clusters.objects.get(pk=cluster_id)
            except Clusters.DoesNotExist:
                continue
                # return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                cluster_info = Clusters.objects.filter(id=cluster_id).values()
                cluster_info = cluster_info.get()
                cluster_info['operation'] = False
                cluster_info['health'] = 'warning'
                cluster_info['message'] = 'sensor nodes got attacked'
                cluster_info['id'] = cluster_id
                cluster_info = json.dumps(cluster_info)
                cluster_info = json.loads(cluster_info)
                import pdb;pdb.set_trace()
                serializer = ClustersSerializer(cluster, data=cluster_info)
                if not serializer.is_valid():
                    continue
                    # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                serializer.save()
                cluster_info = Clusters.objects.filter(id=cluster_id).values()

    return Response()


@login_required()
@api_view(['GET'])
def reset_attack(request):
    """
    {
        "connection_id": "",
        "action": "",
        "timestamp": "yyyymmddhhmmss",
        "comment": ""
    }
    """
    url = URL(scheme=BIGDATA_SCHEME, host=BIGDATA_HOST, path='/backend/bigdata/attcksolved')
    results = requests.post(url, data=None)
    return Response()

