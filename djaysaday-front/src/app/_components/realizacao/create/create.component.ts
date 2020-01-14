import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Realizacao, Atividade } from '../../../_models/index';
import { RealizacaoService } from '../../../_services/realizacao.service';
import { AtividadeService } from '../../../_services';
import { Location } from '@angular/common';

@Component({
	selector: 'app-create-realizacao',
	templateUrl: './create.component.html',
	styleUrls: ['./create.component.scss']
})
export class CreateRealizacaoComponent implements OnInit {
	unique_column: number;
	keyword: string;
	realizacao: Realizacao;
	atividades: Atividade[];

	constructor(private _location: Location, public realizacaoService: RealizacaoService, public atividadeService: AtividadeService,public router: Router) { 
		this.realizacao = new Realizacao();
	}

	ngOnInit() {
		this.atividadeService.all().subscribe(res => this.atividades = res);
	}

	create() {

	}

	store() {
		console.log(this.realizacao);
		this.realizacaoService.store(this.realizacao).subscribe(res => {
			if (res) {
				this.router.navigate(['/' + this.realizacaoService.module + '/edit/' + res.id]);
			}
		}, error => {
			console.error(error);
		});
	}

	voltar() {
		this._location.back();
	}
}
