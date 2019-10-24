import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute, ParamMap } from '@angular/router';
import { AtividadeService } from '../../../_services/index';
import { Atividade, Paginate } from '../../../_models/index';

@Component({
  selector: 'app-lista-atividade',
  templateUrl: './all.component.html',
  styleUrls: ['./all.component.scss']
})
export class ListaAtividadeComponent implements OnInit {
	pageNo: number=1;
	keyword: string='';
	perPage: number=10;
	sortBy: string='column_1';
	orderBy: string='desc';
	atividades: Atividade[] = [];
	paginate: Paginate;
	
	constructor(public atividadeService: AtividadeService, public route: ActivatedRoute, public router: Router) {
		this.route.params.subscribe(val => {
			this.pageNo = parseInt(val.page_no);
		});
	}

	ngOnInit() {
		this.all();
	}

	all() {
    	this.atividadeService.all(this.pageNo, this.keyword, this.perPage, this.sortBy, this.orderBy).subscribe(res => {
    		this.paginate = res['atividades'];
    		this.atividades = res['atividades'].data;
    		this.paginate.pages = this.createArray(1, this.paginate.last_page);
	    }, error => {
	    	// for testing 
    		// this.atividades = [{unique_column:1, column_1:'Value 1', column_2:'Value 2', column_3:'Value 3'}];
	    	console.error(error);
	    });
    }

    destroy(unique_column) {
    	if(confirm('Are you Sure ?')) {
    		this.atividadeService.destroy(unique_column).subscribe(res => {
	    		
		    }, error => {
		    	console.error(error);
		    });
    	}	
    }

    sortResults(sortBy) {
    	this.sortBy = sortBy;
    	this.orderBy = (this.orderBy == 'desc') ? 'asc' : 'desc';
    	this.all();
    }

    createArray(from, to) {
    	let result:any = [];
    	for (var i = from; i <= to; i++) {
    		result.push(i);
    	}
    	return result;
    }
}
