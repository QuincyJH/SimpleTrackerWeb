import { Injectable } from '@angular/core';
import { environment } from '../../environments/environment';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable()
export class BaseService {
  protected baseUrl = environment.api_domain;
  readonly route: string = '';

  get url(): string {
    return `${this.baseUrl}${this.route}`;
  }

  constructor(protected _httpClient: HttpClient) {}

  protected get<T>(route: string, options?: object): Observable<T> {
    return this._httpClient.get<T>(`${this.baseUrl}/${route}`, options);
  }

  protected post<T>(route: string, body: any, options?: object): Observable<T> {
    return this._httpClient.post<T>(`${this.baseUrl}/${route}`, body, options);
  }

  protected put<T>(route: string, body: any, options?: object): Observable<T> {
    return this._httpClient.put<T>(`${this.baseUrl}/${route}`, body, options);
  }

  protected delete<T>(route: string, options?: object): Observable<T> {
    return this._httpClient.delete<T>(`${this.baseUrl}/${route}`, options);
  }
}
