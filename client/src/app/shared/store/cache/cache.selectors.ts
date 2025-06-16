import { createSelector, createFeatureSelector } from '@ngrx/store';
import { Region } from '../../models/region.model';
import { Item } from '../../models/item.model';

export const selectRegionsState = createFeatureSelector<Region[]>('cacheRegions');

export const selectRegions = createSelector(selectRegionsState, (state) => state);

export const selectItemsState = createFeatureSelector<Item[]>('cacheItems');

export const selectItems = createSelector(selectItemsState, (state) => state);
