import { CommonModule } from '@angular/common';
import { Component, inject, model } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import {
  MAT_DIALOG_DATA,
  MatDialogActions,
  MatDialogClose,
  MatDialogContent,
  MatDialogModule,
  MatDialogRef,
  MatDialogTitle,
} from '@angular/material/dialog';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';

@Component({
  selector: 'app-new-run-dialog',
  standalone: true,
  imports: [
    MatDialogModule,
    CommonModule,
    MatFormFieldModule,
    MatInputModule,
    FormsModule,
    MatButtonModule,
    MatDialogTitle,
    MatDialogContent,
    MatDialogActions,
    MatDialogClose,
  ],
  templateUrl: './new-run-dialog.component.html',
  styleUrl: './new-run-dialog.component.scss',
})
export class NewRunDialog {
  dialogref = inject(MatDialogRef<NewRunDialog>);
  data = inject(MAT_DIALOG_DATA);
  runName = model(this.data.runName);

  onClose(): void {
    this.dialogref.close();
  }

  createRun(): void {}
}
