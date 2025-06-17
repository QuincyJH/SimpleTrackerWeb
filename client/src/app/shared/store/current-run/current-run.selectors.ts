import { createSelector, createFeatureSelector } from '@ngrx/store';
import { Run } from '../../models/run.model';

export const selectCurrentRunState = createFeatureSelector<Run>('currentRun');
export const selectCurrentRun = createSelector(selectCurrentRunState, (state) => state);
