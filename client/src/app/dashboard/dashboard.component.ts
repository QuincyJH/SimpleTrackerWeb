import { Component, ViewChild } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { CommonModule } from '@angular/common';
import { RunsService } from '../shared/services/runs.service';
import { RunStateService } from '../shared/services/run-state.service';
import { Run } from '../shared/models/run.model';
import { MatSidenav, MatSidenavModule } from '@angular/material/sidenav';
import { NavigationBarComponent } from '../shared/components/navigation-bar/navigation-bar.component';
import { RouterOutlet } from '@angular/router';
import { SavedRunCardComponent } from '../shared/components/saved-run-card/saved-run-card.component';

@Component({
  selector: 'app-dashboard',
  imports: [
    MatCardModule,
    MatIconModule,
    MatButtonModule,
    CommonModule,
    MatSidenavModule,
    NavigationBarComponent,
    RouterOutlet,
    SavedRunCardComponent,
  ],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss',
})
export class DashboardComponent {
  @ViewChild('drawer') sidenav!: MatSidenav;
  recentRun = false;
  runs: Run[] = [];

  constructor(private runsService: RunsService, private runStateService: RunStateService) {
    this.getRuns();
  }

  getRuns(): void {
    this.runsService.getRuns().subscribe((runs) => {
      this.runs = runs;
      this.runStateService.setRuns(runs);
    });
  }

  toggleSidenav() {
    this.sidenav.toggle();
  }
}
