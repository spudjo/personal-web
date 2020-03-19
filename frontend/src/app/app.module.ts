import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { RouterModule, Routes } from '@angular/router';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';

import { HomeComponent } from './home/home.component';
import { AboutComponent } from './about/about.component';
import { ProjectApiService } from './projects/projects-api.service';
import { ProjectsComponent } from './projects/projects.component';
import { GuestbookApiService } from './guestbook/guestbook-api.service';
import { GuestbookComponent } from './guestbook/guestbook.component';
import { MiscComponent } from './misc/misc.component';
import { NavComponent } from './nav/nav.component';

const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'projects', component: ProjectsComponent },
  { path: 'guestbook', component: GuestbookComponent },
  { path: 'misc', component: MiscComponent },
];

@NgModule({
  declarations: [
    AppComponent,
    HeaderComponent,
    FooterComponent,
    HomeComponent,
    AboutComponent,
    ProjectsComponent,
    GuestbookComponent,
    MiscComponent,
    NavComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    RouterModule.forRoot(
      appRoutes,
    ),
  ],
  providers: [GuestbookApiService, ProjectApiService],
  bootstrap: [AppComponent]
})
export class AppModule { }
