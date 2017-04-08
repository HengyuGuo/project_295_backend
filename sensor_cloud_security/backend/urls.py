from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # --- web url ---
    url(r'^$', auth_views.login, {'template_name': 'backend/login.html'}, name='login'),
    url(r'^app/logout$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^app$', views.home_page, name='home'),
    url(r'^app/all_clusters_sensors$', views.all_clusters_sensors_web, name='all_clusters_sensors_web'),
    url(r'^app/clusters/(?P<pk>[0-9]+)$', views.cluster_detail_update_web, name='cluster_detail_update_web'),
    url(r'^app/testsecret$', views.test_api, name='test_api'),





    # --- rest api url ---
    # url(r'^$', views.index, name='index'),
    url(r'^sensors$', views.sensor_list_deploy),
    # url(r'^get/sensors$', views.sensor_list),
    url(r'^sensors/(?P<pk>[0-9]+)$', views.sensor_detail_update),
    # url(r'^update/sensors/(?P<pk>[0-9]+)$', views.sensor_update),
    url(r'^clusters$', views.cluster_list_deploy),
    # url(r'^get/clusters$', views.cluster_list),
    url(r'^clusters/(?P<pk>[0-9]+)$', views.cluster_detail_update),
    url(r'^clusters_sensors/(?P<cluster_id>[0-9]+)$', views.cluster_sensor),
    # url(r'^update/clusters/(?P<pk>[0-9]+)$', views.cluster_update),
    url(r'^all_clusters_sensors$', views.all_clusters_sensors),
    url(r'^all_clusters_sensors_dummy$', views.all_clusters_sensors_dummy),
    url(r'^leach$', views.run_leach),

    url(r'^feedlog$', views.feed_log),
    url(r'^analysis_result$', views.get_analysis_result),
    url(r'^reset_attack$', views.reset_attack),
]

urlpatterns = format_suffix_patterns(urlpatterns)

"""
documents:

Login required:

Sensors:

GET     http://localhost:8000/sensors               ->      show all sensors info
GET     http://localhost:8000/get/sensors/1         ->      show sensor id 1 detail info
POST    http://localhost:8000/sensors               ->      deploy a sensor
PUT     http://localhost:8000/update/sensors/1      ->      update sensor id 1 info


Clusters:

GET     http://localhost:8000/clusters              ->      show all clusters info
GET     http://localhost:8000/clusters/1            ->      show cluster id 1 detail info
POST    http://localhost:8000/clusters              ->      deploy a cluster
PUT     http://localhost:8000/clusters/1            ->      update cluster id 1 info
GET     http://localhost:8000/clusters_sensors/1    ->      show all sensors info in cluster id 1

Sensor and clusters:

GET     http://localhost:8000/all_clusters_sensors  ->      show all clusters and sensors info
GET     http://localhost:8000/all_clusters_sensors_dummy -> show all clusters and sensors info (dummy data)

Leach:

GET     http://localhost:8000/leach                 ->      start running leach protocol


Testing:

GET     http://localhost:8000/secret                ->      testing for oauth2 login


"""
