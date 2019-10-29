import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';

@Injectable()
export class AuthGuard implements CanActivate {
  
   constructor(public router: Router) { }

   canActivate() {
	   if (localStorage.getItem('user')) {
		   console.log("PODE!")
	       // logged in so return true
	       return true;
	   }	   
	   // not logged in so redirect to login page
	   localStorage.clear();
	   console.log("NAO PODE!")
	   this.router.navigate(['/login']);
	   return false;
	}
}
