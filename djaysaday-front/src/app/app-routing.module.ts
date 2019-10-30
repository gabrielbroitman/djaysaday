import { Routes, RouterModule } from '@angular/router';
import { RegisterComponent, LoginComponent, ForgotPasswordComponent, ResetPasswordComponent } from './_components/auth/index';
import { HomeComponent } from './_components/home/home.component';
import { AuthGuard } from './_guards/auth.guard';
import { CreateAtividadeComponent, EditAtividadeComponent, ShowAtividadeComponent, ListaAtividadeComponent } from './_components/atividade';
import { DashboardAtividadeComponent } from './_components/atividade/dashboard/dashboard.component';

const appRoutes: Routes = [
	{ path: '', component: HomeComponent, pathMatch: 'full' },
	//{ path: '**', redirectTo: '' },
	{ path: 'login', component: LoginComponent },
	{ path: 'register', component: RegisterComponent },
	{ path: 'forgot-password', component: ForgotPasswordComponent },
	{ path: 'reset-password/:uid/:token', component: ResetPasswordComponent },

	//ATIVIDADE ROUTER
	{
		path: 'atividade', canActivate: [AuthGuard],
		children: [
			{ path: 'listar', component: ListaAtividadeComponent },
			{ path: 'create', component: CreateAtividadeComponent },
			{ path: 'edit/:id', component: EditAtividadeComponent },
			{ path: ':id', component: EditAtividadeComponent },
			{ path: '', component: DashboardAtividadeComponent, pathMatch: 'full' },
		]
	}
];

export const routing = RouterModule.forRoot(appRoutes);
