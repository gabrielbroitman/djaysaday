import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map } from 'rxjs/operators';
import { environment } from '../../environments/environment';

@Injectable()
export class AuthenticationService {
    public token: string;
    public headers: HttpHeaders;
    public readonly apiUrl = environment.apiUrl + '/auth';
    public readonly baseUrl = environment.baseUrl;

    constructor(public http: HttpClient) {
        // set token if saved in local storage
        var currentUser = JSON.parse(localStorage.getItem('user'));
        this.token = currentUser && currentUser.token;
    }

    isLoggedIn() {
        if (localStorage.getItem('user')) {
            return true;
        }
        return false;
    }

    buscarUsuario(pk: number): Observable<any> {
        return this.http.get(this.apiUrl+ '/user/getuserlogado/' + pk)
    }

    login(email: string, password: string): Observable<any> {
        return this.http.post(this.apiUrl + '/login/', { username: email, password: password })
            .pipe(
                map((response: Response) => {
                    // login successful if there's a jwt token in the response
                    this.token = response['token'];
                    let expiresIn = response['expires_in'];
                    if (this.token) {
                        // store expiresIn and jwt token in local storage to keep user logged in between page refreshes
                        localStorage.setItem('user',
                            JSON.stringify({ expires_in: expiresIn, token: this.token, username: email }));
                    }
                    return response;
                })
            );
    }

    register(username: string, email: string, password: string): Observable<any> {
        return this.http.post(this.apiUrl + '/signup/', {  email: email, username: username, password1: password, password2: password })
            .pipe(
                map((response: Response) => {
                    // register successful if there's a jwt token in the response
                    this.token = response['token'];
                    let expiresIn = response['expires_in'];
                    if (this.token) {
                        // store expiresIn and jwt token in local storage to keep user logged in between page refreshes
                        localStorage.setItem('user',
                            JSON.stringify({ expires_in: expiresIn, token: this.token, username: username }));
                    }
                    return response;
                })
            );
    }

    logout(): void {
        // clear token remove user from local storage to log user out
        this.token = null;
        localStorage.removeItem('user');
    }

    sendPasswordResetEmail(email: string): Observable<any> {
        return this.http.post(this.apiUrl + '/password/reset/', { email: email })
            .pipe(
                map((response: Response) => {
                    return response;
                })
            );
    }

    resetPassword(newPassword: string, confirmedPassword: string, token: string, uid: string): Observable<any> {
        return this.http.post(this.apiUrl + '/password/reset/confirm/', {uid:uid, new_password1: newPassword, new_password2: confirmedPassword, token: token })
            .pipe(
                map((response: Response) => {
                    return response;
                })
            );
    }

}
