import { createAction, props } from '@ngrx/store';
import { Region } from '../../models/region.model';

export const setLocationsCache = createAction('[Cache] Set Locations Cache', props<{ locations: any[] }>());
export const clearLocationsCache = createAction('[Cache] Clear Locations Cache');

export const setRegionsCache = createAction('[Cache] Set Regions Cache', props<{ regions: Region[] }>());
export const clearRegionsCache = createAction('[Cache] Clear Regions Cache');
