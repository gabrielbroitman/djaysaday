import { Component, OnInit, OnChanges } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit, OnChanges {

  public title: string = 'JsADay';

  constructor() { }

  ngOnInit() {
  }

  ngOnChanges() {


  }

  openOptions() {
    window.document.getElementById('dashboard-button').click();
  }

}
