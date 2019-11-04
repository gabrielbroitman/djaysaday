import { Realizacao } from '.';

export class Humor {
	id: number;
	nome: string;
	nivel: number;
	data_criacao: Date;
	descricao: string;
	realizacoes: Realizacao[];
	sensacoes: Sensacao[];
}

export class Sensacao {
	id: number;
	nome: string;
	descricao: string;
	nivel: number;
}

export const Nivel = [
	{ codigo: 0, valor: 'Muito negativo' },
	{ codigo: 1, valor: 'Negativo' },
	{ codigo: 2, valor: 'Neutro' },
	{ codigo: 3, valor: 'Positivo' },
	{ codigo: 4, valor: 'Muito positivo' }

]