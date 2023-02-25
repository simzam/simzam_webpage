window.htmx = require('htmx.org');

document.documentElement.setAttribute('data-theme', 'dark');

document.querySelector('[data-switch-dark]').addEventListener('click', function() {
  document.body.classList.toggle('dark');
});
