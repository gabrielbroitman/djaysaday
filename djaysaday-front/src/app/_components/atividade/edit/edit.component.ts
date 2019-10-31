import { Component, OnInit } from '@angular/core';
import { AtividadeService } from '../../../_services/index';
import { Atividade } from '../../../_models/index';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';

@Component({
	selector: 'app-edit-atividade',
	templateUrl: './edit.component.html',
	styleUrls: ['./edit.component.scss']
})
export class EditAtividadeComponent implements OnInit {
	unique_column: number;
	keyword: string;
	atividade;

	constructor(public atividadeService: AtividadeService, public router: Router, public route: ActivatedRoute) { }

	ngOnInit() {
		this.route.params.subscribe(params => {
			let idAtividade = params['id'];

			this.atividadeService.show(idAtividade).subscribe(res => {
				this.atividade = res;
				console.log(this.atividade);
			});
		})
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
			this.router.navigate(['/' + this.atividadeService.module]);
		}, error => {
			console.error(error);
		});
	}
}
