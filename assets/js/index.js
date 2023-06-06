window.htmx = require('htmx.org');

import "bootstrap/dist/js/bootstrap.bundle";

document.documentElement.setAttribute('data-theme', 'dark');

document.querySelector('[data-switch-dark]').addEventListener('click', function() {
  document.body.classList.toggle('dark');
});

var scrollToTopBtn = document.getElementById("scrollToTopBtn");
var rootElement = document.documentElement;

function scrollToTop() {
  // Scroll to top logic
  rootElement.scrollTo({
    top: 0,
    behavior: "smooth"
  })
}

scrollToTopBtn.addEventListener("click", scrollToTop);
