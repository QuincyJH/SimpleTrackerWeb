import { createAction, props } from '@ngrx/store';
import { Run } from '../../models/run.model';

export const setSelectedRun = createAction('[Run] Set Selected Run', props<{ selectedRun: Run }>());
export const clearSelectedRun = createAction('[Run] Clear Selected Run');
