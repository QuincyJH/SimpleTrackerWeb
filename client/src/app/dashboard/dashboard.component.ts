import { Component } from '@angular/core';
import { NewRunCardComponent } from './new-run-card/new-run-card.component';

@Component({
  selector: 'app-dashboard',
  imports: [NewRunCardComponent],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent {

}
