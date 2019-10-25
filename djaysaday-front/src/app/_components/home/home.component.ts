import { Component, OnInit, OnChanges } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit, OnChanges {

  public title: string = 'Angular 7';

  constructor() { }

  ngOnInit() {
  }

  ngOnChanges() {
    let currentUser = JSON.parse(localStorage.getItem('user'));
    console.log(currentUser);

  }

  openOptions() {
    window.document.getElementById('dashboard-button').click();
  }

}
