import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from './material.module';
import { ListaRealizacaoComponent, CreateRealizacaoComponent, EditRealizacaoComponent, ShowRealizacaoComponent } from '../_components/realizacao/index';
import { RealizacaoService } from '../_services';
import { DashboardRealizacaoComponent } from '../_components/realizacao/dashboard/dashboard.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    MaterialModule
  ],
  declarations: [
    ListaRealizacaoComponent,
    CreateRealizacaoComponent,
    EditRealizacaoComponent,
    ShowRealizacaoComponent,
    DashboardRealizacaoComponent
  ],
  exports: [
    ListaRealizacaoComponent,
    CreateRealizacaoComponent,
    EditRealizacaoComponent,
    ShowRealizacaoComponent,
    DashboardRealizacaoComponent
  ],
  providers: [RealizacaoService]
})
export class RealizacaoModule { }
