import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { Run } from '../models/run.model';

@Injectable({ providedIn: 'root' })
export class RunStateService {
  private _runs = new BehaviorSubject<Run[]>([]);
  runs$ = this._runs.asObservable();

  setRuns(runs: Run[]) {
    this._runs.next(runs);
  }
}
