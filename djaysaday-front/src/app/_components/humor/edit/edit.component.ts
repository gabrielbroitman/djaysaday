import { Component, OnInit, ChangeDetectorRef } from '@angular/core';
import { HumorService, RealizacaoService } from '../../../_services/index';
import { Humor, Realizacao, Sensacao, Nivel } from '../../../_models/index';
import { ActivatedRoute, Router } from '@angular/router';
import { DatePipe } from '@angular/common';

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

	constructor(public humorService: HumorService, public realizacaoService: RealizacaoService, public router: Router, public route: ActivatedRoute) {
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
		this.humorService.update(this.humor).subscribe(res => {
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
}
