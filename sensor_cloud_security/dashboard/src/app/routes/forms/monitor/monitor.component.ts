import { Component, OnInit } from '@angular/core';
import { Sensor } from '../../../models/sensor';
import { MonitorService } from '../../../services/monitor.service';
import { Params, ActivatedRoute, Router } from '@angular/router';
import { Http } from '@angular/http';
import { AppConst } from '../../../constants/app-const';

@Component({
  selector: 'app-monitor',
  templateUrl: './monitor.component.html',
  styleUrls: ['./monitor.component.scss']
})
export class MonitorComponent implements OnInit {

  private selectedSensor : Sensor;
  private sensorList : Sensor[];
  private serverPath:string = AppConst.serverPath;

  constructor(
      private monitorService : MonitorService,
      private router : Router,
      private http : Http,
      private route : ActivatedRoute
  ) { }

  onSelect(sensor : Sensor){
    this.selectedSensor = sensor;
    this.router.navigate(['/sensorDetail', this.selectedSensor.id])
  }

	ngOnInit() {
		this.route.queryParams.subscribe(params => {
			if(params['sensorList']) {
				console.log("filtered sensor list");
				this.sensorList = JSON.parse(params['sensorList']);
			} else {
				this.monitorService.getSensorList().subscribe(
					res => {
						console.log(res.json());
						this.sensorList = res.json();
					},
					err => {
						console.log(err);
					}
					);
			}
		});

	}

}
