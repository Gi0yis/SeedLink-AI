import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CultivosComponent } from './cultivos/cultivos.component';
import { HomeComponent } from './home/home.component';
import { PrediccionesComponent } from './predicciones/predicciones.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'cultivos', component: CultivosComponent },
  { path: 'predicciones', component: PrediccionesComponent },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: '**', redirectTo: '/home' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
