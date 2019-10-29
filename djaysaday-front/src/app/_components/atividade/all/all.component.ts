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
	keyword: string='';

	atividades: Atividade[];
	
	constructor(public atividadeService: AtividadeService, public route: ActivatedRoute, public router: Router) {
		
	}

	ngOnInit() {
		this.all();
	}

	all() {
    	this.atividadeService.all().subscribe(res => {
    		console.log(res);
    		this.atividades = res;
    		
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
    	
    }

    createArray(from, to) {
    	let result:any = [];
    	for (var i = from; i <= to; i++) {
    		result.push(i);
    	}
    	return result;
    }
}
