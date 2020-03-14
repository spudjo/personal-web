import {Component, OnDestroy, OnInit} from '@angular/core';
import {Subscription} from 'rxjs/Subscription';
import {Guestbook} from './guestbook.model';
import {GuestbookApiService} from './guestbook-api.service';

@Component({
  selector: 'guestbook',
  templateUrl: './guestbook.component.html'
})
export class GuestbookComponent implements OnInit, OnDestroy 
{
  guestbookListSubs: Subscription;
  guestbookList: Guestbook[];

  constructor(private guestbookApi: GuestbookApiService) {}

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
}