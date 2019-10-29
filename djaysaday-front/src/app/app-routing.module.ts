import { Routes, RouterModule } from '@angular/router';
import { RegisterComponent, LoginComponent, ForgotPasswordComponent, ResetPasswordComponent } from './_components/auth/index';
import { HomeComponent } from './_components/home/home.component';
import { AuthGuard } from './_guards/auth.guard';
import { CreateAtividadeComponent, EditAtividadeComponent, ShowAtividadeComponent, ListaAtividadeComponent } from './_components/atividade';

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
			{ path: 'create', component: CreateAtividadeComponent },
			{ path: 'edit/:id', component: EditAtividadeComponent },
			{ path: ':id', component: EditAtividadeComponent },
			{ path: '', component: ListaAtividadeComponent, pathMatch: 'full' },
		]
	}
];

export const routing = RouterModule.forRoot(appRoutes);
