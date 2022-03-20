# Django REST Framework & Docker

**Author**: Clarissa
**Version**: 1.0.2 (increment the patch/fix version number if you make more commits past your first submission)

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for this class. (i.e. What's your problem domain?) -->
Use Django REST Framework to create an API, then “containerize” it with Docker.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
Rebuild a custom version of Things API demo project from scratch.

Replace things_project and Thing with your own application and model.

Your model must have at least as many fields as demo’s model.

Your model must have one field that is a foreign key to user.

NOTE: You are not required to build any templates for this lab.

Modify provided unit tests in demo to work for your project.

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. -->
Language: Python
Virtual Environment: venv
Django
Docker

## Change Log
<!-- Use this area to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Application now has a fully-functional express server, with a GET route for the location resource. -->

3/15 - Django implemented, models created

3/19 - Docker implemented, test created and passing

## Estimates
<!-- See below -->
Estimate of time needed to complete: 5 hours

Start time: 3/15
Finish time: 3/19

Actual time needed to complete: 4 hours

## Credit and Collaborations
<!-- Give credit (and a link) to other people or resources that helped you build this application. -->
Roger Huba

---
---

# Permissions & Postgresql

**Author**: Clarissa
**Version**: 1.0.0 (increment the patch/fix version number if you make more commits past your first submission)

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for this class. (i.e. What's your problem domain?) -->
Build upon previous lab by adding Permissions and Postgresql Database

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
**Django REST Framework**:

- Make your site a DRF powered API as you did in previous lab.

- Adjust project’s permissions so that only authenticated user’s have access to API.

- Add a custom permission so that only author of blog post can update or delete it.

- Add ability to switch user’s directly from browsable API.

**Docker**:

- Enter docker-compose up --build to start your site

- add postgres 11 as a service
  
  - (not required to include a volume so that data can persist when container is shut down.)

- Go to browsable api and confirm site properly restricts users based on their permissions.

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. -->
Language: Python
Virtual Environment: venv
Django
Docker

## Change Log
<!-- Use this area to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:

01-01-2001 4:59pm - Application now has a fully-functional express server, with a GET route for the location resource. -->

## Estimates
<!-- See below -->
Estimate of time needed to complete: 5 hours

Start time: 3/19
Finish time:

Actual time needed to complete:

## Credit and Collaborations
<!-- Give credit (and a link) to other people or resources that helped you build this application. -->