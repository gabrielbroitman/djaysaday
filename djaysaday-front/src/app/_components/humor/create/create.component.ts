import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Humor, Nivel, Realizacao, Sensacao } from '../../../_models/index';
import { HumorService } from '../../../_services/humor.service';
import { AtividadeService, RealizacaoService } from '../../../_services';
import { Location } from '@angular/common';

@Component({
	selector: 'app-create-humor',
	templateUrl: './create.component.html',
	styleUrls: ['./create.component.scss']
})
export class CreateHumorComponent implements OnInit {
	unique_column: number;
	keyword: string;
	humor: Humor;
	realizacoes: Realizacao[];
	sensacoes: Sensacao[];

	realizacoesHumor = [];
	sensacoesHumor = [];
	selecionadosRealizacao = [];
	selecionadosSensacao = [];

	niveis = Nivel;





	constructor(public humorService: HumorService, private _location: Location, public atividadeService: AtividadeService, public realizacaoService: RealizacaoService, public router: Router) {
		this.humor = new Humor();
		this.selecionadosRealizacao = [];
		this.selecionadosSensacao = [];
	}

	ngOnInit() {
		this.realizacaoService.all().subscribe(res => this.realizacoes = res);
		this.humorService.allSensacoes().subscribe(res => {
			this.sensacoes = res;
			console.log(res);
			this.sensacoes.forEach(sensacao => this.selecionadosSensacao.push(false));
		});

	}

	adicionaSensacao(event, index: number) {
		if (this.sensacoesHumor.includes(this.sensacoes[index])) {
			this.sensacoesHumor.splice(this.sensacoesHumor.indexOf(this.sensacoes[index]), 1);
		} else if (!this.sensacoesHumor.includes(this.sensacoes[index])) {
			this.sensacoesHumor.push(this.sensacoes[index]);
		}
		this.selecionadosSensacao[index] = event;
		console.log(this.sensacoesHumor);
	}

	adicionaRealizacao(event, index: number) {
		if (this.realizacoesHumor.includes(this.realizacoes[index])) {
			this.realizacoesHumor.splice(this.sensacoesHumor.indexOf(this.realizacoes[index]), 1);
		} else if (!this.realizacoesHumor.includes(this.realizacoes[index])) {
			this.realizacoesHumor.push(this.realizacoes[index]);
		}
		this.selecionadosRealizacao[index] = event;
		console.log(this.realizacoesHumor);
	}


	store() {
		console.log(this.humor);
		this.humor.realizacoes = this.realizacoesHumor;
		this.humor.sensacoes = this.sensacoesHumor;
		this.humorService.store(this.humor).subscribe(res => {
			if (res) {
				this.router.navigate(['/' + this.humorService.module + '/edit/' + res.id]);
			}
		}, error => {
			console.error(error);
		});
	}

	voltar() {
		this._location.back();
	}
}
