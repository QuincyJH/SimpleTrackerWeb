import { Component, EventEmitter, Output } from '@angular/core';
import { ThemeToggleComponent } from '../theme-toggle/theme-toggle.component';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatToolbarModule } from '@angular/material/toolbar';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navigation-bar',
  imports: [ThemeToggleComponent, MatIconModule, MatButtonModule, MatToolbarModule],
  templateUrl: './navigation-bar.component.html',
  styleUrl: './navigation-bar.component.scss',
})
export class NavigationBarComponent {
  @Output() openSidenav = new EventEmitter<void>();

  constructor(private router: Router) {}

  onMenuClick() {
    this.openSidenav.emit();
  }

  onHomeClick() {
    this.router.navigate(['/']);
  }
}
