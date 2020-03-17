import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';

@Injectable()
export class HeaderTitleService {
  title = new BehaviorSubject('Initial Title');

  setTitle(title: string) {
    this.title.next(title);
  }
}