import { Component, Input } from '@angular/core';
import { Run } from '../../models/run.model';
import { DatePipe } from '@angular/common';
import { MatCardModule } from '@angular/material/card';

@Component({
  selector: 'app-saved-run-card',
  imports: [MatCardModule],
  providers: [DatePipe],
  templateUrl: './saved-run-card.component.html',
  styleUrl: './saved-run-card.component.scss',
})
export class SavedRunCardComponent {
  @Input() run!: Run;

  constructor(private datePipe: DatePipe) {}

  formatDateToLocal(dateString: string | Date | undefined): string | null {
    return this.datePipe.transform(dateString, 'y MMMM d h:mm:ss a') || '';
  }
}
