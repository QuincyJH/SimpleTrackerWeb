import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Run } from '../models/run.model';

@Injectable({
  providedIn: 'root',
})
export class RunsService {
  private baseUrl = 'http://mm_backend:8000';
  private apiUrl = '/runs';

  constructor(private http: HttpClient) {}

  getRuns(): Observable<Run[]> {
    return this.http.get<Run[]>(this.baseUrl + this.apiUrl);
  }

  createRun(run: Partial<Run>): Observable<Run> {
    return this.http.post<Run>(this.baseUrl + this.apiUrl, run);
  }
}
