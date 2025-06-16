import { createAction, props } from '@ngrx/store';
import { Region } from '../../models/region.model';
import { Item } from '../../models/item.model';

export const setLocationsCache = createAction('[Cache] Set Locations Cache', props<{ locations: any[] }>());
export const clearLocationsCache = createAction('[Cache] Clear Locations Cache');

export const setRegionsCache = createAction('[Cache] Set Regions Cache', props<{ regions: Region[] }>());
export const clearRegionsCache = createAction('[Cache] Clear Regions Cache');

export const setItemsCache = createAction('[Cache] Set Items Cache', props<{ items: Item[] }>());
export const clearItemsCache = createAction('[Cache] Clear Items Cache');
