import { createSelector, createFeatureSelector } from '@ngrx/store';
import { Region } from '../../models/region.model';

export const selectRegionsState = createFeatureSelector<Region[]>('cacheRegions');

export const selectRegions = createSelector(selectRegionsState, (state) => state);
