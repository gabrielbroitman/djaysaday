import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Atividade, TIPOS_ATIVIDADE } from '../../../_models/index';
import { Location } from '@angular/common';
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
	tiposAtividade = TIPOS_ATIVIDADE;


	constructor(public atividadeService: AtividadeService, public router: Router, private _location: Location) { }

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

	voltar() {
		this._location.back();
	}
}
