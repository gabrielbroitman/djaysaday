import { Component, OnInit } from '@angular/core';
import { RealizacaoService } from '../../../_services/index';
import { Realizacao } from '../../../_models/index';

@Component({
  selector: 'app-show-realizacao',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.scss']
})
export class ShowRealizacaoComponent implements OnInit {
  id: number;
  keyword: string;
  realizacao: Realizacao[] = [];

  constructor(public realizacaoService: RealizacaoService) { }

  ngOnInit() {
    this.show(this.id);
  }

  show(id) {
    this.realizacaoService.show(id).subscribe(res => {

    }, error => {
      console.error(error);
    });
  }
}
