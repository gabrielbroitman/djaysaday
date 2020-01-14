export class Atividade {
	id: number;
	data_criacao: Date;
	descricao: string;
	nome: string;
	tipoAtividade: string;
}


export const TIPOS_ATIVIDADE = [{
    nome: 'Física',
    codigo: 'F',
    descricao: 'Atividade física.'
  },
  {
    nome: 'Substância',
    codigo: 'S',
    descricao: 'Atividade referente a um consumo de substância.'
  },
  {
    nome: 'Alimento',
    codigo: 'A',
    descricao: 'Atividade referente a alimentação.'
  },
  {
    nome: 'Outros',
    codigo: 'O',
    descricao: 'Tipo de atividade diferente dos citados.'
  },
];
