# GCP Flask Deployment Lab

This repository contains the complete source code for a Python Flask web application designed to be deployed to multiple Google Cloud Platform services. The application itself is a simple, educational page that explains the basics of a CI/CD pipeline.

This project is built as part of a guided lab to demonstrate and practice cloud-native deployment patterns.

##  Features

* A simple, educational Flask web page that teaches a basic DevOps concept.
* A fully containerized setup using Docker.
* Complete configuration files for multiple deployment targets:
    * Google App Engine (`app.yaml`)
    * Google Kubernetes Engine (GKE) (`kubernetes-config.yaml`)
    * Google Cloud Run (via Docker image)

##  Core Technologies

* **Backend:** Python 3.9, Flask
* **WSGI Server:** Gunicorn
* **Containerization:** Docker
* **Cloud Platform:** Google Cloud Platform (GCP)
    * App Engine
    * Google Kubernetes Engine (GKE)
    * Cloud Run
    * Cloud Build
    * Artifact Registry

## 💻 Local Development Setup

You can run this application on your local machine. Here’s how:

### Prerequisites

* [Git](https://git-scm.com/) installed.
* [Python 3.9+](https://www.python.org/downloads/) installed.

### Step-by-Step Instructions

1.  **Clone the repository:**
   Open your terminal or command prompt and clone [this repository](https://github.com/LindiweD-Collab/gcp-deployment-lab.git) to your local machine by running the following command:
   ```bash
   git clone https://github.com/LindiweD-Collab/gcp-deployment-lab.git
   ```

2.  **Navigate into the directory:**
    ```bash
    cd gcp-deployment-lab
    ```

3.  **Create and activate a virtual environment:**
    This is a best practice to keep project dependencies isolated.

    * On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\Activate
        ```

4.  **Install the required packages:**
    With your virtual environment active, install the libraries from the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run the application:**
    Now, you can start the Flask development server.
    ```bash
    python main.py
    ```

6.  **View in your browser:**
    Open your favorite web browser and navigate to the following address:
    [http://127.0.0.1:8080](http://127.0.0.1:8080)

    You should see the "CI/CD Pipeline" educational page running locally!

## ☁️ Deployment to Google Cloud

This repository is ready for deployment. The key configuration files are:
* **`Dockerfile`**: Defines the instructions for building a portable container image of the application.
* **`app.yaml`**: A simple configuration for deploying to the App Engine Standard environment.
* **`kubernetes-config.yaml`**: A declarative manifest for deploying the application with 3 replicas and a public-facing Load Balancer on Google Kubernetes Engine.

---
