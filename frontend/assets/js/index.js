//import bootstrap from 'bootstrap';
// Import the htmx library (make sure it's included in your HTML)
// import '../style/main.scss'

// import 'htmx.org';

// window.htmx = require('htmx.org');
// Function to handle the response and update the page content
// function handleResponse(target, content) {
//   target.innerHTML = content;
// }

// document.addEventListener('DOMContentLoaded', () => {
//   // Get the button element
//   const loadButton = document.getElementById('loadDataButton');

//   // Add an event listener to the button to trigger the htmx request
//   loadButton.addEventListener('click', (event) => {
//     // Prevent the default button click behavior
//     event.preventDefault();

//     // Use htmx to make a GET request to a URL and update a target element
//     htmx.ajax({
//       url: 'https://jsonplaceholder.typicode.com/posts/1',
//       target: '#output', // The element where the response will be placed
//       method: 'get',
//       onSwap: handleResponse, // Custom function to handle the response
//     });
//   });
// });
document.documentElement.setAttribute('data-theme', 'dark');

document.querySelector('[data-switch-dark]').addEventListener('click', function() {
  document.body.classList.toggle('dark');
});
