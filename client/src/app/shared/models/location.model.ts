import { LocationType } from './location-type.model';

export interface Location {
  id?: number;
  name: string;
  displayName: string;
  regionId?: number;
  locationType: LocationType;
}
