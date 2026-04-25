# ACEest Fitness & Gym DevOps Project

![CI Pipeline](https://github.com/harisastha6/aceest-fitness-devops/actions/workflows/main.yml/badge.svg)

This project demonstrates the implementation of a **CI/CD pipeline** for the ACEest Fitness & Gym management system using modern DevOps practices.

## Project Objective

The objective of this assignment is to design and implement an automated DevOps workflow that ensures:

* Version control using **Git & GitHub**
* Automated testing using **Pytest**
* Containerization using **Docker**
* Continuous Integration using **GitHub Actions**
* Build verification using **Jenkins**

---

## Application Overview

The ACEest Fitness application is a **Python-based fitness management system** that allows gym administrators to:

* Manage client information
* Track workouts and exercises
* Monitor client progress
* Generate fitness reports
* Manage membership details

The application is built using **Python, Tkinter, SQLite, and Matplotlib**.

---

## Project Structure

aceest-fitness-devops
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
├── README.md
│
├── tests
│   └── test_app.py
│
└── .github
  └── workflows
    └── main.yml

---

## Running the Application Locally

Install the required dependencies:

pip install -r requirements.txt

Run the application:

python app.py

---

## Running Unit Tests

Run automated tests using Pytest:

pytest

---

## Docker Instructions

Build Docker image:

docker build -t aceest-fitness .

Run Docker container:

docker run aceest-fitness

---

## CI/CD Pipeline

This project implements **Continuous Integration using GitHub Actions**.

The pipeline is automatically triggered whenever code is pushed to the repository.

### Pipeline Stages

1. Checkout repository
2. Setup Python environment
3. Install project dependencies
4. Run automated tests
5. Build Docker image

This ensures that the application builds successfully and passes all tests before deployment.

---

## Jenkins Integration

Jenkins is used as a secondary build validation system.

The Jenkins pipeline performs the following tasks:

* Pull source code from GitHub
* Install dependencies
* Execute unit tests
* Build the Docker image

This ensures the application builds successfully in a controlled environment.

---

## Technologies Used

* Python
* SQLite
* Tkinter
* Docker
* GitHub Actions
* Jenkins
* Pytest

---

## Author

DevOps Assignment
ACEest Fitness & Gym
## System Workflow

Developer → GitHub → GitHub Actions (CI) → Jenkins (Build) → Docker Image

This workflow ensures continuous integration and build validation.
## CI/CD Flow Explanation

- GitHub Actions is triggered on every push
- It installs dependencies and runs Pytest
- It builds the Docker image
- Jenkins performs additional build verification
- Ensures application reliability and consistency
## Future Improvements

- Convert GUI application to REST API using Flask
- Add deployment using Kubernetes
- Integrate monitoring tools like Prometheus
