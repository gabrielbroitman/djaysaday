import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { HumorService, RealizacaoService } from '../../../_services/index';
import { Humor, Realizacao, Sensacao, Nivel } from '../../../_models/index';
import { ActivatedRoute, Router } from '@angular/router';
import { DatePipe, Location } from '@angular/common';

@Component({
	selector: 'app-edit-humor',
	templateUrl: './edit.component.html',
	styleUrls: ['./edit.component.scss']
})
export class EditHumorComponent implements OnInit {
	unique_column: number;
	keyword: string;
	humor: Humor;
	realizacoes: Realizacao[];
	sensacoes: Sensacao[];
	niveis = Nivel;
	idHumor: number;


	realizacoesHumor = [];
	sensacoesHumor = [];
	selecionadosRealizacao = [];
	selecionadosSensacao = [];



	constructor(public humorService: HumorService, private _location:Location, public realizacaoService: RealizacaoService, public datePipe: DatePipe, public router: Router, public route: ActivatedRoute) {
		this.humor = new Humor();
	}

	ngOnInit() {
		this.realizacaoService.all().subscribe(res => this.realizacoes = res);
		this.humorService.allSensacoes().subscribe(res => { this.sensacoes = res; console.log(res); });
		this.route.params.subscribe(params => {
			this.idHumor = params['id'];
			console.log(this.humor);
		})
		this.buscarModelo();

	}


	buscarModelo() {
		this.humorService.show(this.idHumor).subscribe(res => {
			this.humor = res;
			//this.humor.data_criacao = this.datePipe.transform(res.data_criacao, 'yyyy-MM-ddThh:mm');
			console.log(this.humor);
		});

	}



	update() {
		this.humor.realizacoes = this.realizacoesHumor;
		this.humor.sensacoes = this.sensacoesHumor;
		this.humorService.update(this.humor).subscribe(res => {
			this.humor.data_criacao = this.datePipe.transform(res.data_criacao, 'yyyy-MM-ddThh:mm');
			console.log(res);
		}, error => {
			console.error(error);
		});
	}

	delete() {
		this.humorService.destroy(this.humor.id).subscribe(res => {
			this.router.navigate(['/' + this.humorService.module]);
		}, error => {
			console.error(error);
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

	voltar() {
		this._location.back();
	}
}
