import { CommonModule } from '@angular/common';
import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-new-run-card',
  imports: [MatCardModule, MatIconModule, MatButtonModule, CommonModule],
  templateUrl: './new-run-card.component.html',
  styleUrl: './new-run-card.component.scss'
})

export class NewRunCardComponent {
  
}
