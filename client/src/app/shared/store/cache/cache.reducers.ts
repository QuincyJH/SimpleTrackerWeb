import { Action, createReducer, on } from '@ngrx/store';
import { Region } from '../../models/region.model';
import { clearLocationsCache, clearRegionsCache, setLocationsCache, setRegionsCache } from './cache.actions';

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
