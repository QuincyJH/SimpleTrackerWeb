import { Component, Input } from '@angular/core';
import { Run } from '../../models/run.model';
import { DatePipe } from '@angular/common';
import { MatCardModule } from '@angular/material/card';
import { Router } from '@angular/router';

@Component({
  selector: 'app-saved-run-card',
  imports: [MatCardModule],
  providers: [DatePipe],
  templateUrl: './saved-run-card.component.html',
  styleUrl: './saved-run-card.component.scss',
})
export class SavedRunCardComponent {
  @Input() run!: Run;

  constructor(private datePipe: DatePipe, private router: Router) {}

  formatDateToLocal(dateString: string | Date | undefined): string | null {
    return this.datePipe.transform(dateString, 'y MMMM d h:mm:ss a') || '';
  }

  onRunSelected(): void {
    if (this.run && this.run.id) {
      this.router.navigate(['/run', this.run.id]);
    }
  }
}
