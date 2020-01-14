import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { RealizacaoService, AtividadeService } from '../../../_services/index';
import { Realizacao, Atividade } from '../../../_models/index';
import { ActivatedRoute, Router } from '@angular/router';
import { DatePipe, Location } from '@angular/common';

@Component({
	selector: 'app-edit-realizacao',
	templateUrl: './edit.component.html',
	styleUrls: ['./edit.component.scss']
})
export class EditRealizacaoComponent implements OnInit {
	unique_column: number;
	keyword: string;
	realizacao: Realizacao;
	atividades: Atividade[] = [];
	idRealizacao: number;

	constructor(
		private _location: Location,
		public realizacaoService: RealizacaoService,
		public route: ActivatedRoute,
		public atividadeService: AtividadeService,
		public router: Router,
		public datePipe: DatePipe) {

		this.realizacao = new Realizacao();
	}

	ngOnInit() {
		

		this.route.params.subscribe(params => {
			this.idRealizacao = params['id'];
			console.log(this.atividades);
		})

		this.buscarModelo();
	}


	buscarModelo() {
		this.realizacaoService.show(this.idRealizacao).subscribe(res => {
			this.realizacao = res;
			this.atividades[0] = res.atividade;
			this.realizacao.data_realizacao = this.datePipe.transform(res.data_realizacao, 'yyyy-MM-ddThh:mm');
			console.log(this.realizacao);
		});

	}



	update() {
		this.realizacaoService.update(this.realizacao).subscribe(res => {
			console.log(res);
		}, error => {
			console.error(error);
		});
	}

	delete() {
		this.realizacaoService.destroy(this.realizacao.id).subscribe(res => {
			this.router.navigate(['/' + this.realizacaoService.module]);
		}, error => {
			console.error(error);
		});
	}

	voltar() {
		this._location.back();
	}
}
