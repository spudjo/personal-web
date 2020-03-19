import {Component, OnDestroy, OnInit} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {Project} from './projects.model';
import {ProjectApiService} from './projects-api.service';
import {Guestbook} from '../guestbook/guestbook.model';
import {GuestbookApiService} from '../guestbook/guestbook-api.service';

@Component({
  selector: 'app-projects',
  templateUrl: './projects.component.html',
  styleUrls: ['./projects.component.css']
})
export class ProjectsComponent implements OnInit, OnDestroy 
{
  projectListSubs: Subscription;
  projectList: Project[];
  
  constructor(private projectbookApi: ProjectApiService) {}

  ngOnInit() 
  {
    this.projectListSubs = this.projectbookApi
      .getProjects()
      .subscribe(res => {this.projectList = res;},console.error);
  }

  ngOnDestroy() 
  {
    this.projectListSubs.unsubscribe();
  }
}