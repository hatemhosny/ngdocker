import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

declare var window: any;

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  apiUrl = 'http://' + window.location.hostname + ':3000';
  products = [];

  constructor(private httpClient: HttpClient) {}

  getData() {
    this.httpClient.get(this.apiUrl).subscribe((res: any) => {
      console.log(res);
      this.products = res.products;
    });
  }
}
