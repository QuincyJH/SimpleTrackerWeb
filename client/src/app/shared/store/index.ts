import { ActionReducerMap } from '@ngrx/store';
import { cacheLocationsReducer, cacheRegionsReducer } from './cache/cache.reducers';
import { locationTypesReducer } from './location-type/location-type.reducers';

export interface AppState {
  cacheLocations: ReturnType<typeof cacheLocationsReducer>;
  cacheRegions: ReturnType<typeof cacheRegionsReducer>;
  locationTypes: ReturnType<typeof locationTypesReducer>;
}

export const reducers: ActionReducerMap<AppState> = {
  cacheLocations: cacheLocationsReducer,
  cacheRegions: cacheRegionsReducer,
  locationTypes: locationTypesReducer,
};
