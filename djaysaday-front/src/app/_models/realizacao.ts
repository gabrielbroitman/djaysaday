import { Atividade } from './atividade';

export class Realizacao {
	id: number;
	data_realizacao;
	descricao: string;
	atividade: Atividade;

	constructor(){
		this.data_realizacao = undefined;
		this.descricao = undefined;
	}

}
