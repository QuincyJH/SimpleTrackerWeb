import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SavedRunCardComponent } from './saved-run-card.component';

describe('SavedRunCardComponent', () => {
  let component: SavedRunCardComponent;
  let fixture: ComponentFixture<SavedRunCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SavedRunCardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SavedRunCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
