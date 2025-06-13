import { Component, inject, signal } from '@angular/core';
import { RunStateService } from '../shared/services/run-state.service';
import { Run } from '../shared/models/run.model';
import { Location } from '../shared/models/location.model';
import { CommonModule } from '@angular/common';
import { Region } from '../shared/models/region.model';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatSelectModule } from '@angular/material/select';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { LocationTypesService } from '../shared/services/location-type.service';
import { LocationType } from '../shared/models/location-type.model';
import { Store } from '@ngrx/store';
import { AppState } from '../shared/store';
import { selectRegions } from '../shared/store/cache/cache.selectors';
import {
  clearSelectedLocationTypes,
  setSelectedLocationTypes,
} from '../shared/store/location-type/location-type.actions';

@Component({
  selector: 'app-run',
  imports: [CommonModule, MatCheckboxModule, MatExpansionModule, MatAutocompleteModule],
  templateUrl: './run.component.html',
  styleUrl: './run.component.scss',
})
export class RunComponent {
  private store = inject(Store<AppState>);
  runName = signal('');
  runs: Run[] = [];
  regions: Region[] = [];
  locationTypes: LocationType[] = [];
  selectedLocationTypes: LocationType[] = [];
  regions$ = this.store.select(selectRegions);
  allSelected: boolean = false;

  constructor(private runStateService: RunStateService, private locationTypesService: LocationTypesService) {}

  ngOnInit(): void {
    this.runStateService.runs$.subscribe((runs) => {
      this.runs = runs;
    });
    this.getLocationTypes();
    this.getRegions();
  }

  getRegions(): void {
    this.regions$.subscribe((regions) => {
      this.regions = regions;
    });
  }

  getLocationTypes(): void {
    this.locationTypesService.getAllLocationTypes().subscribe((locationTypes) => {
      this.locationTypes = locationTypes;
      this.selectedLocationTypes = [...locationTypes];
      this.allSelected = locationTypes.length > 0;
      this.store.dispatch(setSelectedLocationTypes({ locationTypes: this.selectedLocationTypes }));
    });
  }

  toggleAllLocationTypes(checked: boolean): void {
    this.allSelected = checked;
    if (checked) {
      this.selectedLocationTypes = this.locationTypes.map((type) => type);
      this.store.dispatch(setSelectedLocationTypes({ locationTypes: this.selectedLocationTypes }));
    } else {
      this.selectedLocationTypes = [];
      this.store.dispatch(clearSelectedLocationTypes());
    }
  }

  toggleLocationType(locationType: LocationType, checked: boolean): void {
    if (checked) {
      this.selectedLocationTypes = [...this.selectedLocationTypes, locationType];
      this.store.dispatch(setSelectedLocationTypes({ locationTypes: this.selectedLocationTypes }));
    } else {
      this.selectedLocationTypes = this.selectedLocationTypes.filter((type) => type.id !== locationType.id);
      this.store.dispatch(setSelectedLocationTypes({ locationTypes: this.selectedLocationTypes }));
    }
  }

  getLocationsForRegion(region: Region): Location[] {
    if (this.selectedLocationTypes.length === 0) {
      return [];
    } else {
      const selectedTypeIds = this.selectedLocationTypes.map((type) => type.id);
      const locations = (region.locations ?? []).filter((location) => {
        return selectedTypeIds.includes(location.locationType.id);
      });
      return locations;
    }
  }
}
