import { Routes, RouterModule } from '@angular/router';
import { RegisterComponent, LoginComponent, ForgotPasswordComponent, ResetPasswordComponent } from './_components/auth/index';
import { HomeComponent } from './_components/home/home.component';
import { AuthGuard } from './_guards/auth.guard';
import { AllDummyComponent, CreateDummyComponent, EditDummyComponent, ShowDummyComponent } from './_components/dummy/index';
import { CreateAtividadeComponent, EditAtividadeComponent, ShowAtividadeComponent, ListaAtividadeComponent } from './_components/atividade';

const appRoutes: Routes = [
	{ path: 'login', component: LoginComponent },
	{ path: 'register', component: RegisterComponent },
	{ path: 'forgot-password', component: ForgotPasswordComponent },
	{ path: 'reset-password/:token', component: ResetPasswordComponent },
	{
		path: 'atividade', canActivate: [AuthGuard],
		children: [
			{ path: '', redirectTo: 'all', pathMatch: 'full' },
			{
				path: 'all',
				children: [
					{ path: '', redirectTo: '1', pathMatch: 'full' },
					{ path: ':page_no', component: ListaAtividadeComponent },
				]
			},
			{ path: 'create', component: CreateAtividadeComponent },
			{ path: 'edit/:id', component: EditAtividadeComponent },
			{ path: 'show/:id', component: ShowAtividadeComponent }
		]
	},
	{ path: '', component: HomeComponent },
	{ path: '**', redirectTo: '' }
];

export const routing = RouterModule.forRoot(appRoutes);
