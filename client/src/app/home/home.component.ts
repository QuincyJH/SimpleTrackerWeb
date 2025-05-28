import { CommonModule } from '@angular/common';
import { Component, inject, signal } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { RunsService } from '../shared/services/runs.service';
import { MatDialog } from '@angular/material/dialog';
import { NewRunDialog } from '../shared/dialogs/new-run-dialog/new-run-dialog.component';
import { Run } from '../shared/models/run.model';
import { SavedRunCardComponent } from '../shared/components/saved-run-card/saved-run-card.component';
import { RunStateService } from '../shared/services/run-state.service';

@Component({
  selector: 'app-home',
  imports: [MatCardModule, MatIconModule, MatButtonModule, CommonModule, SavedRunCardComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss',
})
export class HomeComponent {
  dialog = inject(MatDialog);
  runName = signal('');
  runs: Run[] = [];

  constructor(private runsService: RunsService, private runStateService: RunStateService) {}

  ngOnInit(): void {
    this.runStateService.runs$.subscribe((runs) => {
      this.runs = runs;
    });
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
}
