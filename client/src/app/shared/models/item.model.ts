import { ItemType } from './item-type.model';

export interface Item {
  id?: number;
  name: string;
  displayName: string;
  itemType: ItemType;
}
