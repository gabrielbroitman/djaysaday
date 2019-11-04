import { Component, OnInit } from '@angular/core';
import { HumorService } from '../../../_services/index';
import { Humor } from '../../../_models/index';

@Component({
  selector: 'app-show-humor',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.scss']
})
export class ShowHumorComponent implements OnInit {
  id: number;
  keyword: string;
  humor: Humor[] = [];

  constructor(public humorService: HumorService) { }

  ngOnInit() {
    this.show(this.id);
  }

  show(id) {
    this.humorService.show(id).subscribe(res => {

    }, error => {
      console.error(error);
    });
  }
}
