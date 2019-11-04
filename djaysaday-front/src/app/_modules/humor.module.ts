import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MaterialModule } from './material.module';
import { ListaHumorComponent, CreateHumorComponent, EditHumorComponent, ShowHumorComponent } from '../_components/humor/index';
import { HumorService } from '../_services';
import { DashboardHumorComponent } from '../_components/humor/dashboard/dashboard.component';

@NgModule({
  imports: [
    CommonModule,
    RouterModule,
    FormsModule,
    ReactiveFormsModule,
    MaterialModule
  ],
  declarations: [
    ListaHumorComponent,
    CreateHumorComponent,
    EditHumorComponent,
    ShowHumorComponent,
    DashboardHumorComponent
  ],
  exports: [
    ListaHumorComponent,
    CreateHumorComponent,
    EditHumorComponent,
    ShowHumorComponent,
    DashboardHumorComponent
  ],
  providers: [HumorService]
})
export class HumorModule { }
