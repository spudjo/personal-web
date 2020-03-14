import {Component} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {GuestbookApiService} from "./guestbook-api.service";
import {Router} from "@angular/router";

@Component({
  selector: 'gusetbook-form',
  templateUrl: './guestbook-form.component.html'
})
export class GuestbookFormComponent 
{
  guestbook = {
    name: '',
    message: '',
  };

  constructor(private guestbookApi: GuestbookApiService, private router: Router) { }

  updateName(event: any) {
    this.guestbook.name = event.target.value;
  }

  updateMessage(event: any) {
    this.guestbook.message = event.target.value;
  }

  saveGuestbook() 
  {
    this.guestbookApi
      .saveGuestbook(this.guestbook)
      .subscribe(() => this.router.navigate(['/']),error => alert(error.message));
  }
}