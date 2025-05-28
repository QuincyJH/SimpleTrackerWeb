import { Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { RunComponent } from './run/run.component';
import { HomeComponent } from './home/home.component';

export const routes: Routes = [
  //   { path: '', component: DashboardComponent },
  //   { path: 'run/:id', component: RunComponent },
  {
    path: '',
    component: DashboardComponent,
    children: [
      { path: '', component: HomeComponent },
      { path: 'run/:id', component: RunComponent },
    ],
  },
];
