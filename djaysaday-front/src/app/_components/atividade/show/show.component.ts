import { Component, OnInit } from '@angular/core';
import { AtividadeService } from '../../../_services/index';
import { Atividade } from '../../../_models/index';

@Component({
  selector: 'app-show-atividade',
  templateUrl: './show.component.html',
  styleUrls: ['./show.component.scss']
})
export class ShowAtividadeComponent implements OnInit {
  id: number;
  keyword: string;
  atividade: Atividade[] = [];

  constructor(public atividadeService: AtividadeService) { }

  ngOnInit() {
    this.show(this.id);
  }

  show(id) {
    this.atividadeService.show(id).subscribe(res => {

    }, error => {
      console.error(error);
    });
  }
}
