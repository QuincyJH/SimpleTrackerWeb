import { Component, signal } from '@angular/core';
import { RunStateService } from '../shared/services/run-state.service';
import { RunsService } from '../shared/services/runs.service';
import { Run } from '../shared/models/run.model';
import { CommonModule } from '@angular/common';
import { RegionsService } from '../shared/services/regions.service';
import { Region } from '../shared/models/region.model';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatExpansionModule } from '@angular/material/expansion';
import { LocationTypesService } from '../shared/services/location-type.service';
import { LocationType } from '../shared/models/location-type.model';

@Component({
  selector: 'app-run',
  imports: [CommonModule, MatCheckboxModule, MatExpansionModule],
  templateUrl: './run.component.html',
  styleUrl: './run.component.scss',
})
export class RunComponent {
  runName = signal('');
  runs: Run[] = [];
  regions: Region[] = [];
  locationTypes: LocationType[] = [];

  constructor(
    private runsService: RunsService,
    private runStateService: RunStateService,
    private regionsService: RegionsService,
    private locationTypesService: LocationTypesService,
  ) {}

  ngOnInit(): void {
    this.runStateService.runs$.subscribe((runs) => {
      this.runs = runs;
    });
    this.getLocationTypes();
    this.getRegions();
  }

  getRegions(): void {
    this.regionsService.getAllLocationsbyRegion().subscribe((regions) => {
      this.regions = regions;
    });
  }

  getLocationTypes(): void {
    this.locationTypesService.getAllLocationTypes().subscribe((locationTypes) => {
      this.locationTypes = locationTypes;
    });
  }
}
