\# To-Do List Application — DevOps Mini Project



\## 1. Project Overview



The To-Do List Application is a simple web-based application that allows users to add, complete, and delete tasks. The project demonstrates an end-to-end DevOps workflow using Git, GitHub, GitHub Actions, Docker, Docker Compose, Prometheus, and Grafana.



\## 2. Problem Statement



Design and implement a simple CI/CD pipeline for a To-Do List Application. The project covers application development, version control, automated testing, containerization, local deployment, and monitoring.



\## 3. Objectives



\- Develop a working To-Do List web application.

\- Maintain source code using Git and GitHub.

\- Automate testing and Docker image building using GitHub Actions.

\- Containerize the application using Docker.

\- Deploy the application using Docker Compose.

\- Monitor application metrics using Prometheus and Grafana.

\- Document the implementation and test results.



\## 4. Technology Stack



\- Programming language: Python

\- Web framework: Flask

\- Database: SQLite

\- Frontend: HTML, CSS, Bootstrap

\- Version control: Git and GitHub

\- CI automation: GitHub Actions

\- Testing: Pytest

\- Containerization: Docker

\- Deployment: Docker Compose

\- Monitoring: Prometheus and Grafana



\## 5. Application Features



\- Add a new task.

\- View all tasks.

\- Mark a task as completed or undo completion.

\- Delete a task.

\- View total, pending, and completed task counts.

\- Check application health using the `/health` endpoint.

\- Expose application metrics through the `/metrics` endpoint.



\## 6. Project Structure



```text

todo-list-devops/

├── app.py

├── requirements.txt

├── Dockerfile

├── docker-compose.yml

├── prometheus.yml

├── README.md

├── .gitignore

├── templates/

│   └── index.html

├── static/

│   └── style.css

├── tests/

│   └── test\_app.py

└── .github/

&#x20;   └── workflows/

&#x20;       └── ci-cd.yml

```



\## 7. DevOps Workflow



1\. Develop the application using Python Flask.

2\. Track and manage code using Git.

3\. Push source code to GitHub.

4\. Trigger GitHub Actions when code is pushed to the main branch or a pull request targets main.

5\. Install dependencies and run automated Pytest tests.

6\. Build the Docker image.

7\. Deploy the application and monitoring services using Docker Compose.

8\. Collect application metrics using Prometheus.

9\. Visualize metrics using Grafana.



\## 8. Build and Testing



Install the dependencies:



```bash

python -m pip install -r requirements.txt

```



Run the tests:



```bash

python -m pytest -v

```



Record the actual test output and attach a screenshot to the project report.



\## 9. Docker Deployment



Build and start the services:



```bash

docker compose up -d --build

```



Check running services:



```bash

docker compose ps

```



Stop the services:



```bash

docker compose down

```



\## 10. Application and Monitoring URLs



\- To-Do List Application: http://localhost:5000

\- Application Health Check: http://localhost:5000/health

\- Application Metrics: http://localhost:5000/metrics

\- Prometheus Targets: http://localhost:9090/targets

\- Grafana: http://localhost:3000



\## 11. Monitoring



Prometheus collects metrics exposed by the Flask application. Grafana connects to Prometheus and displays the collected data through a dashboard.



Example Prometheus query:



```promql

todo\_http\_requests\_total

```



\## 12. Results



Complete this section after testing the project:



\- Application status: \[Record actual result]

\- Pytest result: \[Record actual number of passing tests]

\- Docker deployment: \[Record actual result]

\- Prometheus target status: \[Record actual status]

\- Grafana dashboard: \[Record actual result]

\- GitHub Actions: \[Record actual workflow result]



\## 13. Conclusion



The project demonstrates practical DevOps concepts by combining application development, version control, automated testing, Docker containerization, local deployment, and monitoring. It provides a foundation for understanding how software moves from development to a monitored running application.



\## 14. Future Enhancements



\- Publish Docker images to Docker Hub.

\- Add automatic deployment to a remote server.

\- Add more automated tests.

\- Introduce authentication and user-specific tasks.

\- Add further monitoring metrics and dashboard panels.



