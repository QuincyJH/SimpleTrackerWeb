import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, tap } from 'rxjs';
import { Region } from '../models/region.model';
import { BaseService } from '../api/base.service';

@Injectable({
  providedIn: 'root',
})
export class RegionsService extends BaseService {
  override readonly route = 'regions';

  constructor(protected _http: HttpClient) {
    super(_http);
  }

  getRegions(): Observable<Region[]> {
    return this.get<Region[]>(this.route).pipe(tap((response) => console.log('SSR API response:', response)));
  }

  createRun(region: Region): Observable<Region> {
    return this.post<Region>(this.route, region);
  }

  getAllLocationsbyRegion(): Observable<Region[]> {
    return this.get<Region[]>(`${this.route}/get-all-locations-by-region/`);
  }
}
