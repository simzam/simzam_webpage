# simzam.com

Welcome to the source code for simzam.com! A creative project that explores and documents my journey as a fullscale developer. A changing canvas for experimentation with various web technologies and continuous skill development. During the COVID-19 pandemic, I rediscovered my passion for drawing after many years. simzam.com showcase and catalog my evolving artwork. It's an ever-evolving learning platform, where I can experiment with web technologies. 

## Technology Stack
The project's technology stack is intentionally designed to be minimal and straightforward, focusing on essential components:

### Backend:
- **Django:** This Python-based web framework forms the core of simzam.com.
- **Wagtail CMS:** For content management. A developer-friendly CMS built on Django.
- **SQLite:** A lightweight and serverless relational database for data storage.

### Frontend:
- **Webpack:** A module bundler that efficiently manages JavaScript and assets.
- **JavaScript:** Enhancing interactivity and dynamic behavior throughout our web pages.
- **HTMX:** Enabling powerful AJAX requests and dynamic HTML content updates for responsive user experiences.
- **Bootstrap:** A widely-used frontend framework that simplifies responsive web design and UI development.
- **SCSS (Sass):** Our CSS preprocessor for improved maintainability and organization.

### File Storage:
- **Amazon S3 (Simple Storage Service):** Our project relies on Amazon S3, a cloud-based object storage service, to securely store and serve images for our web application.

## Development status
The first version of "simzam.com" was hosted by "PythonAnywhere". Very convienient, but most of the devops remains hidden. Therefore I have moved the domain and will use either AWS EC2 or Lightsail for hosting. The services at AWS are currently a bit overwhelming

## Development Status

The initial version of "simzam.com" was hosted on "PythonAnywhere." It was a convenient choice, but it hid most of the infrastructure for hosting. As a result, I've decided to move the domain and explore hosting options on either AWS EC2 or Lightsail. 

I have struggled with coding functionality for handling both image and text content. It has been a hassle and Wagtail CMS solves this very neatly. Wagtail also separates the content and the code in a very nice way. Even though code and content is both made by me, the separation is comfortable. 
