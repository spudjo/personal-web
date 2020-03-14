import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { GuestbookApiService } from './guestbook/guestbook-api.service';
import { Guestbook } from './guestbook/guestbook.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  guestbookListSubs: Subscription;
  guestbookList: Guestbook[];

  constructor(private examsApi: GuestbookApiService) {
  }

  ngOnInit() {
    this.guestbookListSubs = this.examsApi
      .getExams()
      .subscribe(res => {
        this.guestbookList = res;
      },
        console.error
      );
  }

  ngOnDestroy() {
    this.guestbookListSubs.unsubscribe();
  }
}