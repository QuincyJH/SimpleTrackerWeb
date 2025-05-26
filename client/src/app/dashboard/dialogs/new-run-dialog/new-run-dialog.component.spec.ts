import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NewRunDialogComponent } from './new-run-dialog.component';

describe('NewRunDialogComponent', () => {
  let component: NewRunDialogComponent;
  let fixture: ComponentFixture<NewRunDialogComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NewRunDialogComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NewRunDialogComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
