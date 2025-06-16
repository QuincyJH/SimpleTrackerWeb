import { Action, createReducer, on, select } from '@ngrx/store';
import { Run } from '../../models/run.model';
import { clearSelectedRun, setSelectedRun } from './current-run.actions';

export const currentRunReducer = createReducer<Run | null, Action>(
  null,
  on(setSelectedRun, (_, { selectedRun }) => selectedRun),
  on(clearSelectedRun, () => null),
);
