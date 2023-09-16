# Simzam's Homepage

Welcome to Simzam's Homepage project! This is a small-scale web development project aimed at providing a platform for experimenting with various web technologies and honing new skills.

During the COVID-19 pandemic, I rediscovered my passion for drawing after many years. This project serves as a way to digitally present and catalog my artwork. It's an ever-evolving learning platform, and new features will be added as I continue to explore and learn.

## Technology Stack

The project's stack is intentionally designed to be small, maintainable, and simple. SQLite has been chosen for data storage due to its lightweight nature and suitability for projects with minimal database writes.

However, it's important to note that the current stack lacks certain elements such as a dedicated web server, containerization, continuous integration/continuous deployment (CI/CD) pipelines, and any form of logging or testing.

### Backend:
- **Django:** Django, a Python-based web framework, serves as the foundation of our web application.
- **Database:** We utilize SQLite, a lightweight and serverless relational database system, for data storage.

### Frontend Technologies:
Our frontend is designed to be minimal yet effective, consisting of:
1. **Webpack:** We employ Webpack as our module bundler to efficiently manage JavaScript and assets.
2. **JavaScript:** JavaScript enhances interactivity and dynamic behavior throughout our web pages.
3. **HTMX:** Leveraging HTMX, we enable powerful AJAX requests and dynamic HTML content updates, contributing to responsive and dynamic user experiences.
4. **Bootstrap:** Bootstrap, a widely-used frontend framework, simplifies responsive web design and UI component development.
5. **SCSS (Sass):** SCSS serves as our CSS preprocessor, enhancing maintainability and organization.

### File Storage:
- **Amazon S3 (Simple Storage Service):** Our project relies on Amazon S3, a cloud-based object storage service, to securely store and serve images for our web application.

## How to Run it in Development?

### Initial Setup:
1. Create a virtual environment at the project's root level and activate it:
   ```bash
   virtualenv .venv
   source .venv/bin/activate
   ```

To begin with the project, follow these steps:

1. If this is your first time starting the project, create and migrate the database.
2. Configure environment variables by creating a file named '.env' based on the '.env.example' template.
3. Once the project is set up, you can test it using the Django development test server. We utilize a local SQLite database for development and automatically reload and package CSS and TS/JS files using Webpack.

## TODO

Here are the tasks on our to-do list:
1. Complete the README documentation to provide comprehensive project information.
2. Containerize the project using Docker for easier deployment and scaling.

Feel free to reach out if you have any questions or require further assistance with the project.
```

Please note that this presentation puts all the content in a single code block for your convenience. You can copy and paste this block into your Markdown editor or README file.
