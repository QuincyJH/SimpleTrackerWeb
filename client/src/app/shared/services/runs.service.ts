import { HttpClient } from '@angular/common/http';
import { Injectable, OnDestroy } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { Run } from '../models/run.model';
import { BaseService } from '../api/base.service';

@Injectable({
  providedIn: 'root',
})
export class RunsService extends BaseService {
  override readonly route = 'runs';

  constructor(protected _http: HttpClient) {
    super(_http);
  }

  getRuns(): Observable<Run[]> {
    return this.get<Run[]>(this.route);
  }

  createRun(run: Run): Observable<Run> {
    return this.post<Run>(this.route, run);
  }

  updateRun(run: Run): Observable<Run> {
    return this.put<Run>(`${this.route}/${run.id}`, run);
  }

  deleteRun(runId: string): Observable<void> {
    return this.delete<void>(`${this.route}/${runId}`);
  }
}
