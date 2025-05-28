import { Component, Input } from '@angular/core';
import { Region } from '../models/region.model';

@Component({
  selector: 'app-region-card',
  imports: [],
  templateUrl: './region-card.component.html',
  styleUrl: './region-card.component.scss',
})
export class RegionCardComponent {
  @Input() region!: Region;
}
