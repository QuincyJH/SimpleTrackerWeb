import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewRunCardComponent } from './new-run-card.component';

describe('NewRunCardComponent', () => {
  let component: NewRunCardComponent;
  let fixture: ComponentFixture<NewRunCardComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NewRunCardComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewRunCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
