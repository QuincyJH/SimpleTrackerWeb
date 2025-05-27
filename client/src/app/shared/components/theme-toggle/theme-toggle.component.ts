import { Component, inject } from '@angular/core';
import { MatSlideToggleChange, MatSlideToggleModule } from '@angular/material/slide-toggle';
import { DOCUMENT } from '@angular/common';
import { MatIconModule } from '@angular/material/icon';

@Component({
  selector: 'app-theme-toggle',
  imports: [MatIconModule, MatSlideToggleModule],
  templateUrl: './theme-toggle.component.html',
  styleUrl: './theme-toggle.component.scss',
  host: { ngSkipHydration: 'true' },
})
export class ThemeToggleComponent {
  private document = inject(DOCUMENT);

  onThemeChange(event: MatSlideToggleChange) {
    this.document.body.classList.toggle('dark');
  }
}
