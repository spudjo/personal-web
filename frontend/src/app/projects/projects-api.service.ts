import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import { GITHUB_API_URL } from '../env';
import { Project } from './projects.model';

@Injectable()
export class ProjectApiService 
{
    constructor(private http: HttpClient) { }

    private static _handleError(err: HttpErrorResponse | any) 
    {
        return Observable.throw(err.message || 'Error: Unable to complete request.');
    }

    // GET list of public, future events
    getProjects(): Observable<Project[]> 
    {
        return this.http
            .get<Project[]>(`${GITHUB_API_URL}`)
            .catch(ProjectApiService._handleError);
    }
}