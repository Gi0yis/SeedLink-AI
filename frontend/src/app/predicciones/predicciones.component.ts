import { Component } from '@angular/core';

@Component({
  selector: 'app-predicciones',
  templateUrl: './predicciones.component.html',
  styleUrls: ['./predicciones.component.css']
})
export class PrediccionesComponent {
  cultivos = [
    { nombre: 'Maíz', porcentaje: 92, 'temperatura': '12°', 'humedad': '7%', 'lluvia': '4mm', riego: 'Moderado', tiempoCosecha: 120 },
    { nombre: 'Trigo', porcentaje: 85, 'temperatura': '22°', 'humedad': '3%', 'lluvia': '30mm', riego: 'Bajo', tiempoCosecha: 110 },
    { nombre: 'Arroz', porcentaje: 78, 'temperatura': '33°', 'humedad': '1%', 'lluvia': '12mm', riego: 'Alto', tiempoCosecha: 150 },
    // Agrega más cultivos según sea necesario
  ];
}