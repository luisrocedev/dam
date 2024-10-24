import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { SaludoComponent } from './saludo/saludo.component';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet,SaludoComponent],

  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'miprimerproyecto';
}
