import { Component, OnInit, Input, OnChanges } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { RealizacaoService } from '../../../_services/index';
import { Realizacao, Paginate } from '../../../_models/index';

@Component({
	selector: 'app-lista-realizacao',
	templateUrl: './all.component.html',
	styleUrls: ['./all.component.scss']
})
export class ListaRealizacaoComponent implements OnInit, OnChanges {
	keyword: string = '';
	@Input() rank: boolean = false;

	realizacoes: Realizacao[];

	constructor(public realizacaoService: RealizacaoService, public route: ActivatedRoute, public router: Router) {

	}

	ngOnInit() {
		if (this.rank === true) {
			this.maisRealizadas();
		} else {
			this.all();
		}

	}

	ngOnChanges(): void {

	}

	maisRealizadas() {
		this.realizacaoService.realizacaoMaisUtilizada().subscribe(res => {
			console.log(res);
			this.realizacoes = res;

		}, error => {
			// for testing 
			// this.realizacoes = [{unique_column:1, column_1:'Value 1', column_2:'Value 2', column_3:'Value 3'}];
			console.error(error);
		});
	}

	all() {
		this.realizacaoService.all().subscribe(res => {
			console.log(res);
			this.realizacoes = res;

		}, error => {
			// for testing 
			// this.realizacoes = [{unique_column:1, column_1:'Value 1', column_2:'Value 2', column_3:'Value 3'}];
			console.error(error);
		});
	}

	destroy(unique_column) {
		if (confirm('Are you Sure ?')) {
			this.realizacaoService.destroy(unique_column).subscribe(res => {

			}, error => {
				console.error(error);
			});
		}
	}

	sortResults(sortBy) {

	}

	createArray(from, to) {
		let result: any = [];
		for (var i = from; i <= to; i++) {
			result.push(i);
		}
		return result;
	}
}
