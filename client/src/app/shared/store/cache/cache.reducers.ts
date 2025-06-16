import { Action, createReducer, on } from '@ngrx/store';
import { Region } from '../../models/region.model';
import {
  clearItemsCache,
  clearLocationsCache,
  clearRegionsCache,
  setItemsCache,
  setLocationsCache,
  setRegionsCache,
} from './cache.actions';
import { Item } from '../../models/item.model';

export const cacheLocationsReducer = createReducer<Location[], Action>(
  [],
  on(setLocationsCache, (_, { locations }) => locations),
  on(clearLocationsCache, () => []),
);

export const cacheRegionsReducer = createReducer<Region[], Action>(
  [],
  on(setRegionsCache, (_, { regions }) => regions),
  on(clearRegionsCache, () => []),
);

export const cacheItemsReducer = createReducer<Item[], Action>(
  [],
  on(setItemsCache, (_, { items }) => items),
  on(clearItemsCache, () => []),
);
