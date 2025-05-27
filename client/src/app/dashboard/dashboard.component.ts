import { Component, inject, signal, ViewChild } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatDialog } from '@angular/material/dialog';
import { CommonModule } from '@angular/common';
import { NewRunDialog } from '../shared/dialogs/new-run-dialog/new-run-dialog.component';
import { RunsService } from '../shared/services/runs.service';
import { Run } from '../shared/models/run.model';
import { SavedRunCardComponent } from '../shared/components/saved-run-card/saved-run-card.component';
import { MatSidenav, MatSidenavModule } from '@angular/material/sidenav';
import { NavigationBarComponent } from '../shared/components/navigation-bar/navigation-bar.component';

@Component({
  selector: 'app-dashboard',
  imports: [
    MatCardModule,
    MatIconModule,
    MatButtonModule,
    CommonModule,
    SavedRunCardComponent,
    MatSidenavModule,
    NavigationBarComponent,
  ],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss',
})
export class DashboardComponent {
  @ViewChild('drawer') sidenav!: MatSidenav;
  recentRun = false;
  runName = signal('');
  dialog = inject(MatDialog);
  runs: Run[] = [];

  constructor(private runsService: RunsService) {
    this.getRuns();
  }

  openNewRunDialog(): void {
    const dialogRef = this.dialog.open(NewRunDialog, { data: { runName: this.runName() } });

    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        this.runName.set(result);
        const newRun: Run = {
          name: result,
        };
        this.runsService.createRun(newRun).subscribe((response) => {
          //console.log(response);
        });
      }
    });
  }

  getRuns(): void {
    this.runsService.getRuns().subscribe((runs) => {
      this.runs = runs;
    });
  }

  toggleSidenav() {
    this.sidenav.toggle();
  }
}
