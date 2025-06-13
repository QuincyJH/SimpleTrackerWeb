import { Action, createReducer, on } from '@ngrx/store';
import { setSelectedLocationTypes, clearSelectedLocationTypes } from './location-type.actions';
import { LocationType } from '../../models/location-type.model';

export const locationTypesReducer = createReducer<LocationType[], Action>(
  [],
  on(setSelectedLocationTypes, (_, { locationTypes }) => locationTypes),
  on(clearSelectedLocationTypes, () => []),
);
