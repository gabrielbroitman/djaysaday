import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from './material.module';
import { ListaAtividadeComponent, CreateAtividadeComponent, EditAtividadeComponent, ShowAtividadeComponent } from '../_components/atividade/index';
import { AtividadeService } from '../_services';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    MaterialModule
  ],
  declarations: [
    ListaAtividadeComponent,
    CreateAtividadeComponent,
    EditAtividadeComponent,
    ShowAtividadeComponent
  ],
  exports: [
    ListaAtividadeComponent,
    CreateAtividadeComponent,
    EditAtividadeComponent,
    ShowAtividadeComponent
  ],
  providers: [AtividadeService]
})
export class AtividadeModule { }
