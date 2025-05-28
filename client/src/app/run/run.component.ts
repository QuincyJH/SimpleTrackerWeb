import { Component, signal } from '@angular/core';
import { RunStateService } from '../shared/services/run-state.service';
import { RunsService } from '../shared/services/runs.service';
import { Run } from '../shared/models/run.model';
import { CommonModule } from '@angular/common';
import { RegionsService } from '../shared/services/regions.service';
import { Region } from '../shared/models/region.model';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatExpansionModule } from '@angular/material/expansion';

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

  constructor(
    private runsService: RunsService,
    private runStateService: RunStateService,
    private regionsService: RegionsService,
  ) {}

  ngOnInit(): void {
    this.runStateService.runs$.subscribe((runs) => {
      this.runs = runs;
    });
    this.getRegions();
  }

  getRegions(): void {
    this.regionsService.getRegions().subscribe((regions) => {
      this.regions = regions;
      console.log('Regions:', regions);
    });
  }
}
