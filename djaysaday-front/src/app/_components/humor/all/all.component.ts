import { Component, OnInit, Input, OnChanges } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { HumorService } from '../../../_services/index';
import { Humor, Paginate } from '../../../_models/index';

@Component({
	selector: 'app-lista-humor',
	templateUrl: './all.component.html',
	styleUrls: ['./all.component.scss']
})
export class ListaHumorComponent implements OnInit, OnChanges {
	keyword: string = '';
	@Input() rank: boolean = false;

	humores: Humor[];

	constructor(public humorService: HumorService, public route: ActivatedRoute, public router: Router) {

	}

	ngOnInit() {
		if (this.rank === true) {
			this.all();
		} else {
			this.all();
		}

	}

	ngOnChanges(): void {

	}

	maisRealizadas() {
		this.humorService.humorMaisUtilizada().subscribe(res => {
			console.log(res);
			this.humores = res;

		}, error => {
			// for testing 
			// this.realizacoes = [{unique_column:1, column_1:'Value 1', column_2:'Value 2', column_3:'Value 3'}];
			console.error(error);
		});
	}

	all() {
		this.humorService.all().subscribe(res => {
			console.log(res);
			this.humores = res;

		}, error => {
			// for testing 
			// this.realizacoes = [{unique_column:1, column_1:'Value 1', column_2:'Value 2', column_3:'Value 3'}];
			console.error(error);
		});
	}

	destroy(unique_column) {
		if (confirm('Are you Sure ?')) {
			this.humorService.destroy(unique_column).subscribe(res => {

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
