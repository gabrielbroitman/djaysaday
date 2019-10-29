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
		this.atividadeService.all().subscribe(res => {
			this.atividade = res[0];
			console.log(this.atividade);
		});
	}


    update() {
    	this.atividadeService.update(this.atividade).subscribe(res => {
    		console.log(res);
	    }, error => {
	    	console.error(error);
	    });
	}
	
	delete() {
    	this.atividadeService.destroy(this.atividade.id).subscribe(res => {
    		console.log(res);
	    }, error => {
	    	console.error(error);
	    });
    }
}
