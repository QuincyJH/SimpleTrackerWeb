import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { BaseService } from '../api/base.service';
import { Item } from '../models/item.model';

@Injectable({
  providedIn: 'root',
})
export class ItemsService extends BaseService {
  override readonly route = 'items';

  constructor(protected _http: HttpClient) {
    super(_http);
  }

  getItem(item_id: Number): Observable<Item> {
    return this.get<Item>(`${this.route}/${item_id}`);
  }

  createItem(item: Item): Observable<Item> {
    return this.post<Item>(this.route, item);
  }

  getAllItems(): Observable<Item[]> {
    return this.get<Item[]>(this.route);
  }
}
