import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from './../../environments/environment';

@Component({
  selector: 'app-employee',
  templateUrl: './employee.component.html',
  styleUrls: ['./employee.component.css']
})
export class EmployeeComponent implements OnInit {

  serverData = {} as JSON;
  employeeData = {} as JSON;
  employee = {} as JSON;

  constructor(private httpClient: HttpClient) {
  }

  ngOnInit(): void {
  }

  sayHi() {
    this.httpClient.get(environment.apiUrl).subscribe(data => {
      this.serverData = data as JSON;
      console.log(this.serverData);
    })
  }

  getAllEmployees() {
    this.httpClient.get(environment.apiUrl + 'employees').subscribe(data => {
      this.employeeData = data as JSON;
      console.log(this.employeeData);
    })
  }
  getEmployee() {
    this.httpClient.get(environment.apiUrl + 'employees/1').subscribe(data => {
      this.employee = data as JSON;
      console.log(this.employee);
    })
  }

}
