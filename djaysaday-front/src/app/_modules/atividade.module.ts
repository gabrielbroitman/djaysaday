import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from './material.module';
import { ListaAtividadeComponent, CreateAtividadeComponent, EditAtividadeComponent, ShowAtividadeComponent } from '../_components/atividade/index';
import { AtividadeService } from '../_services';
import { DashboardAtividadeComponent } from '../_components/atividade/dashboard/dashboard.component';

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
    ShowAtividadeComponent,
    DashboardAtividadeComponent
  ],
  exports: [
    ListaAtividadeComponent,
    CreateAtividadeComponent,
    EditAtividadeComponent,
    ShowAtividadeComponent,
    DashboardAtividadeComponent
  ],
  providers: [AtividadeService]
})
export class AtividadeModule { }
