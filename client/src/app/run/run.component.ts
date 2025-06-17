import { Component, inject, signal } from '@angular/core';
import { Run } from '../shared/models/run.model';
import { Location } from '../shared/models/location.model';
import { CommonModule } from '@angular/common';
import { Region } from '../shared/models/region.model';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatExpansionModule } from '@angular/material/expansion';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { LocationTypesService } from '../shared/services/location-type.service';
import { LocationType } from '../shared/models/location-type.model';
import { Store } from '@ngrx/store';
import { AppState } from '../shared/store';
import { selectItems, selectRegions } from '../shared/store/cache/cache.selectors';
import {
  clearSelectedLocationTypes,
  setSelectedLocationTypes,
} from '../shared/store/location-type/location-type.actions';
import { Item } from '../shared/models/item.model';
import { FormControl, FormsModule, ReactiveFormsModule } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { ScrollingModule } from '@angular/cdk/scrolling';
import { debounceTime, Observable, Subject } from 'rxjs';
import { selectCurrentRun } from '../shared/store/current-run/current-run.selectors';
import { RunsService } from '../shared/services/runs.service';

@Component({
  selector: 'app-run',
  imports: [
    CommonModule,
    MatCheckboxModule,
    MatExpansionModule,
    MatAutocompleteModule,
    MatFormFieldModule,
    ReactiveFormsModule,
    MatInputModule,
    ScrollingModule,
    FormsModule,
  ],
  templateUrl: './run.component.html',
  styleUrl: './run.component.scss',
})
export class RunComponent {
  private store = inject(Store<AppState>);
  private saveSubject = new Subject<void>();
  runName = signal('');

  run: Run | null = null;
  regions: Region[] = [];
  locationTypes: LocationType[] = [];
  selectedLocationTypes: LocationType[] = [];

  regions$ = this.store.select(selectRegions);
  items$ = this.store.select(selectItems);
  filteredItems$!: Observable<Item[]>;

  allSelected: boolean = false;

  constructor(private locationTypesService: LocationTypesService, private runService: RunsService) {
    this.saveSubject.pipe(debounceTime(2000)).subscribe(() => this.saveSelections());
  }

  ngOnInit(): void {
    this.store.select(selectCurrentRun).subscribe((currentRun) => {
      this.run = currentRun;
    });
    this.getLocationTypes();
    this.getRegions();
  }

  getRegions(): void {
    this.regions$.subscribe((regions) => {
      this.regions = regions.map((region) => ({
        ...region,
        locations: (region.locations ?? []).map((location) => ({
          ...location,
          selected: false,
          formControl: new FormControl(null),
        })),
      }));
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

  saveSelections(): void {
    if (!this.run) return;

    const selections = {
      selectedLocationTypeIds: this.selectedLocationTypes.map((type) => type.id),
      regions: this.regions
        .map((region) => ({
          id: region.id,
          name: region.name,
          locations: (region.locations ?? [])
            .filter((location) => location.selected)
            .map((location) => ({
              locationId: location.id,
              locationName: location.name,
              selected: location.selected,
              selectedItemId: location.formControl?.value?.id ?? null,
              selectedItemName: location.formControl?.value?.displayName ?? null,
            })),
        }))
        .filter((region) => region.locations.length > 0),
    };

    const updatedRun = {
      ...this.run,
      data: JSON.stringify(selections),
    };

    this.runService.updateRun(updatedRun).subscribe(() => {
      console.log('Run selections saved successfully');
    });
  }

  onUserChange(): void {
    this.saveSubject.next();
  }

  displayFn(item: Item | null): string {
    return item ? item.displayName : '';
  }

  regionsFiltered() {
    return this.regions.filter((region) => this.getLocationsForRegion(region).length > 0);
  }
}
