import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Atividade } from '../../../_models/index';
import { AtividadeService } from '../../../_services/atividade.service';

@Component({
	selector: 'app-create-atividade',
	templateUrl: './create.component.html',
	styleUrls: ['./create.component.scss']
})
export class CreateAtividadeComponent implements OnInit {
	unique_column: number;
	keyword: string;
	atividade = {};

	constructor(public atividadeService: AtividadeService, public router: Router) { }

	ngOnInit() {
		this.create();
	}

	create() {

	}

	store() {
		console.log(this.atividade);
		this.atividadeService.store(this.atividade).subscribe(res => {
			if (res) {
				this.router.navigate(['/' + this.atividadeService.module + '/edit/' + res.id]);
			}
		}, error => {
			console.error(error);
		});
	}
}
