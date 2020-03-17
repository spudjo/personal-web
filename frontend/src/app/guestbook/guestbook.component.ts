import {Component, OnDestroy, OnInit} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {Guestbook} from './guestbook.model';
import {GuestbookApiService} from './guestbook-api.service';
import {Router} from "@angular/router";

@Component({
  selector: 'guestbook',
  templateUrl: './guestbook.component.html',
  styleUrls: ['./guestbook.component.css']
})
export class GuestbookComponent implements OnInit, OnDestroy 
{
  guestbook = {
    name: '',
    message: '',
  };

  guestbookListSubs: Subscription;
  guestbookList: Guestbook[];

  constructor(private guestbookApi: GuestbookApiService, private router: Router) {}

  ngOnInit() 
  {
    this.guestbookListSubs = this.guestbookApi
      .getGuestbook()
      .subscribe(res => {this.guestbookList = res;},console.error);
  }

  ngOnDestroy() 
  {
    this.guestbookListSubs.unsubscribe();
  }

  updateName(event: any) 
  {
    this.guestbook.name = event.target.value;
  }

  updateMessage(event: any) 
  {
    this.guestbook.message = event.target.value;
  }

  saveGuestbook() 
  {
    this.guestbookApi.saveGuestbook(this.guestbook)
      .subscribe(() => this.router.navigate(['/guestbook']),error => alert(error.message));
  }

}