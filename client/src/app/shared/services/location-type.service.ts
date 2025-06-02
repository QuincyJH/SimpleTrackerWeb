import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from '../api/base.service';
import { LocationType } from '../models/location-type.model';

@Injectable({
  providedIn: 'root',
})
export class LocationTypesService extends BaseService {
  override readonly route = 'location-types';

  constructor(protected _http: HttpClient) {
    super(_http);
  }

  getLocationType(location_type_id: Number): Observable<LocationType[]> {
    return this.get<LocationType[]>(`${this.route}/${location_type_id}`);
  }

  getAllLocationTypes(): Observable<LocationType[]> {
    return this.get<LocationType[]>(this.route);
  }
}
