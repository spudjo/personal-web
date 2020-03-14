import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';
import {HttpClientModule} from '@angular/common/http';

import {AppComponent} from './app.component';
import {GuestbookApiService} from './guestbook/guestbook-api.service';

import {GuestbookFormComponent} from './guestbook/guestbook-form.component';
import {RouterModule, Routes} from '@angular/router';
import {GuestbookComponent} from './guestbook/guestbook.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';

const appRoutes: Routes = [
  { path: 'new-guestbook-post', component: GuestbookFormComponent },
  { path: '', component: GuestbookComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    GuestbookFormComponent,
    GuestbookComponent,
    HeaderComponent,
    FooterComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(
      appRoutes,
    ),
  ],
  providers: [GuestbookApiService],
  bootstrap: [AppComponent]
})
export class AppModule {}
