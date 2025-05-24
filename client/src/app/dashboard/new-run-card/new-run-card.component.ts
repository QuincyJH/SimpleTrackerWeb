import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatIconModule } from '@angular/material/icon';


@Component({
  selector: 'app-new-run-card',
  imports: [MatCardModule, MatIconModule],
  templateUrl: './new-run-card.component.html',
  styleUrl: './new-run-card.component.scss'
})
export class NewRunCardComponent {

}
