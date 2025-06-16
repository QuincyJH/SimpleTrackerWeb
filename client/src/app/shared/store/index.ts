import { ActionReducerMap } from '@ngrx/store';
import { cacheItemsReducer, cacheLocationsReducer, cacheRegionsReducer } from './cache/cache.reducers';
import { locationTypesReducer } from './location-type/location-type.reducers';
import { currentRunReducer } from './current-run/current-run.reducers';

export interface AppState {
  cacheLocations: ReturnType<typeof cacheLocationsReducer>;
  cacheRegions: ReturnType<typeof cacheRegionsReducer>;
  cacheItems: ReturnType<typeof cacheItemsReducer>;
  locationTypes: ReturnType<typeof locationTypesReducer>;
  currentRun: ReturnType<typeof currentRunReducer>;
}

export const reducers: ActionReducerMap<AppState> = {
  cacheLocations: cacheLocationsReducer,
  cacheRegions: cacheRegionsReducer,
  cacheItems: cacheItemsReducer,
  locationTypes: locationTypesReducer,
  currentRun: currentRunReducer,
};
