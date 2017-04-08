import { Injectable } from '@angular/core';
import { Http, Headers } from '@angular/http';
import { Observable } from 'rxjs/Observable';
import { AppConst} from '../constants/app-const';
import { Router } from '@angular/router';

@Injectable()
export class LoginService {
  private serverPath:string = AppConst.serverPath;

  constructor(private http:Http, private router:Router) { }

  sendCredential(username: string, password: string) {
  	let url = this.serverPath+'/o/token/';
  	let clientID = 'SlKw3Yq8ibiEVDIL6Qg9mY0neOL7mbzLnsbRRDqV';
  	let clientSecret = 'SlKw3Yq8ibiEVDIL6Qg9mY0neOL7mbzLnsbRRDqV';
  	let encodedCredentials = btoa(username+":"+password);
  	let basicHeader = "Basic "+encodedCredentials;
  	let body = 'grant_type=password&username=adminadmin&password=adminadmin&client_id=SlKw3Yq8ibiEVDIL6Qg9mY0neOL7mbzLnsbRRDqV&client_secret=kKx6fsTPGObEC1Ngd7ha9Y4tyLzNc5UppMfBu1f2VWpPKpsWOlUWpV21Wu65dhDWdHA4wLWpNEqHRd3xKvEqKroDQDOiEjOq91eiA7KirNoMIh0AWYtKL8cD1tvNb3CL'
	// let encodedCredentials = btoa(postData);
  	let headers = new Headers({
  		'Content-Type' : 'application/x-www-form-urlencoded',
  		// 'Authorization' : basicHeader
  	});


  	return this.http.post(url, body, {headers: headers});
  }

  checkSession() {
  	let url = this.serverPath+'/checkSession';
  	let headers = new Headers({
  		'x-auth-token' : localStorage.getItem('xAuthToken')
  	});

  	return this.http.get(url, {headers: headers});
  }

  logout() {
  	let url = this.serverPath+'/user/logout';
  	let headers = new Headers({
  		'x-auth-token' : localStorage.getItem('xAuthToken')
  	});

  	return this.http.post(url, '', {headers: headers});
  }

}
