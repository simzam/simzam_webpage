window.htmx = require('htmx.org');

import "bootstrap/dist/js/bootstrap.bundle";

document.documentElement.setAttribute('data-theme', 'dark');

document.querySelector('[data-switch-dark]').addEventListener('click', function() {
  document.body.classList.toggle('dark');
});
