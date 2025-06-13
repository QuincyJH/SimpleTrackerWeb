import { createAction, props } from '@ngrx/store';

export const setSelectedLocationTypes = createAction(
  '[Location] Set Selected Location Type',
  props<{ locationTypes: any[] }>(),
);
export const clearSelectedLocationTypes = createAction('[Location] Clear Selected Location Type');
