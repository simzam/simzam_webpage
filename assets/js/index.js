// Comment
import Alpine from 'alpinejs'

window.htmx = require('htmx.org');
//import './class-tools';

window.Alpine = Alpine
Alpine.start()

import 'bootstrap';
document.documentElement.setAttribute('data-theme', 'dark');

document.querySelector('[data-switch-dark]').addEventListener('click', function() {
  document.body.classList.toggle('dark');
});

// import * as PIXI from 'pixi.js'


// ENDTE ENDNTE
/// TEST F
