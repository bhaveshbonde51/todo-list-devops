\# DEVOPS MINI PROJECT REPORT



\## Title

\*\*End-to-End DevOps Pipeline for a To-Do List Application\*\*



\## 1. Introduction

The To-Do List Application is a web-based task management system developed using Python Flask and SQLite. The project applies DevOps practices to automate testing, build a Docker image, deploy the application locally, and monitor application metrics.



\## 2. Problem Statement

To design and implement a simple CI/CD pipeline for a To-Do List Application using modern DevOps tools.



\## 3. Objectives

\- Develop a working application.

\- Use Git and GitHub for source control.

\- Automate testing using GitHub Actions and Pytest.

\- Containerize the application using Docker.

\- Deploy using Docker Compose.

\- Monitor metrics using Prometheus and Grafana.



\## 4. System Architecture

Application source code → GitHub → GitHub Actions → Automated tests → Docker image build → Docker Compose deployment → Prometheus monitoring → Grafana dashboard.



\## 5. Software and Tools

Python, Flask, SQLite, HTML, CSS, Bootstrap, Git, GitHub, GitHub Actions, Pytest, Docker, Docker Compose, Prometheus, and Grafana.



\## 6. Application Implementation

The application supports adding, viewing, completing, and deleting tasks. SQLite stores task information. The `/health` endpoint reports application health, and `/metrics` exposes metrics for Prometheus.



\## 7. Version Control

The source code is maintained in a GitHub repository. Git tracks changes, while GitHub provides centralized source control and stores the project files.



GitHub repository URL: \[Insert repository URL]



\## 8. Continuous Integration

GitHub Actions runs when code is pushed to the main branch or when a pull request targets the main branch. The workflow installs Python dependencies, executes automated tests, and builds the Docker image.



Evidence: \[Insert screenshot of a successful GitHub Actions run]



\## 9. Testing

Tests are written using Pytest to verify the home page, task creation, empty task handling, health endpoint, and metrics endpoint.



Command:



`python -m pytest -v`



Actual test result: \[Insert the real output]



Evidence: \[Insert screenshot of test results]



\## 10. Docker Containerization and Deployment

A Dockerfile packages the Flask application and its dependencies. Docker Compose starts the application, Prometheus, and Grafana.



Command:



`docker compose up -d --build`



Deployment result: \[Insert actual result]



Evidence: \[Insert screenshot of running containers and the application]



\## 11. Monitoring

Prometheus scrapes the Flask `/metrics` endpoint. Grafana uses Prometheus as a data source to display application metrics.



Prometheus target status: \[Insert actual status]



Grafana dashboard result: \[Insert actual result]



Evidence: \[Insert screenshots of Prometheus targets and Grafana dashboard]



\## 12. Results and Discussion

Summarize the observed application behavior, automated test results, Docker deployment, CI workflow status, and monitoring results using evidence collected during execution.



\## 13. Challenges and Solutions

Record actual challenges encountered during setup, testing, containerization, or monitoring, together with the solutions used.



\## 14. Conclusion

The project demonstrates an integrated DevOps workflow from source code management and automated testing to containerized local deployment and monitoring. It provides practical experience with commonly used DevOps tools.



\## 15. Future Scope

The project can be extended with Docker Hub publishing, remote deployment, additional tests, authentication, and more monitoring metrics.



\## 16. Group Details

Student names: \[Enter all group members]



Class/Batch: \[Enter details]



Faculty name: \[Enter details]



