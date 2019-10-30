import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { environment } from '../../environments/environment';

@Injectable()
export class AtividadeService {
	public readonly apiUrl = environment.apiUrl;
    public readonly baseUrl = environment.baseUrl;
    public module:string = 'atividade';

    constructor(public http: HttpClient) {
        
    }

    all(): any {
    	return this.http.get(this.apiUrl+'/'+this.module+'/listar');
    }

    atividadeMaisUtilizada(): any {
    	return this.http.get(this.apiUrl+'/'+this.module+'/listar/rank');
    }

    create() {
        return this.http.get(this.apiUrl+'/'+this.module+'/create');
    }

    store(obj): any {
    	return this.http.post(this.apiUrl+'/'+this.module+'/nova/', obj );
    }

    edit(id) {
        return this.http.get(this.apiUrl+'/'+this.module+'/'+id+'/edit');
    }

    show(id) {
        return this.http.get(this.apiUrl+'/'+this.module+'/'+id );
    }

    update(obj) {
    	return this.http.put(this.apiUrl+'/'+this.module+'/' + obj.id + '/edit/', obj );
    }

    destroy(id) {
    	return this.http.delete(this.apiUrl+'/'+this.module+'/'+id);
    }
}
