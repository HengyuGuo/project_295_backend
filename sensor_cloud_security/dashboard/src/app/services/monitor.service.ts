import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { AppConst } from '../constants/app-const';

@Injectable()
export class MonitorService {

  private serverPath:string = AppConst.serverPath;

  constructor(private http:Http) { }

  getSensorList(){
    let url = this.serverPath+"/sensors";

    let tokenHeader = new Headers({
      'Content-Type' : 'application/json',
      'x-auth-token' : localStorage.getItem("xAuthToken")
    });
    return this.http.get(url, {headers : tokenHeader});
  }

  getSensor(id: number){
    let url = this.serverPath+"/sensor/"+id;

    let tokenHeader = new Headers({
      'Content-Type' : 'application/json',
      'x-auth-token' : localStorage.getItem("xAuthToken")
    });
    return this.http.get(url, {headers : tokenHeader});
  }

}
