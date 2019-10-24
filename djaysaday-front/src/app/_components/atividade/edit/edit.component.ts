import { Component, OnInit } from '@angular/core';
import { AtividadeService } from '../../../_services/index';
import { Atividade } from '../../../_models/index';

@Component({
  selector: 'app-edit-atividade',
  templateUrl: './edit.component.html',
  styleUrls: ['./edit.component.scss']
})
export class EditAtividadeComponent implements OnInit {
	unique_column:number;
	keyword:string;
	atividade;
	
	constructor(public atividadeService: AtividadeService) { }

	ngOnInit() {
		this.edit(this.unique_column);
	}

	edit(unique_column) {
		this.atividade={unique_column:1, column_1:'Value 1', column_2:'Value 2', column_3:'Value 3'};
    }

    update(unique_column, atividade) {
    	this.atividadeService.update(unique_column, atividade).subscribe(res => {
    		
	    }, error => {
	    	console.error(error);
	    });
    }
}
