import { Location } from './location.model';

export interface Region {
  id?: number;
  name: string;
  displayName: string;
  locations?: Location[];
}
