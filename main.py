from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def main():
    # We're now creating a more detailed model to pass to the template.
    # This model contains the text and data for our DevOps lesson.
    model = {
        "title": "A DevOps Primer",
        "header": "The CI/CD Pipeline",
        "description": "Continuous Integration (CI) and Continuous Deployment (CD) is a cornerstone of modern DevOps. It's the practice of automating the software delivery process, allowing teams to build, test, and deploy code more frequently and reliably. Below are the core stages of a typical pipeline.",
        "pipeline_stages": [
            {
                "name": "Code",
                "icon": "bi-code-slash",
                "description": "Developers write code and push changes to a shared repository (like Git)."
            },
            {
                "name": "Build",
                "icon": "bi-box-seam",
                "description": "The new code is automatically compiled and packaged into a runnable artifact (like a Docker image)."
            },
            {
                "name": "Test",
                "icon": "bi-clipboard2-check",
                "description": "Automated tests run against the build to check for bugs and ensure quality before release."
            },
            {
                "name": "Deploy",
                "icon": "bi-rocket-takeoff",
                "description": "If tests pass, the build is automatically deployed to a production environment (like Cloud Run or GKE)."
            }
        ]
    }
    return render_template('index.html', model=model)

if __name__ == "__main__":
    # The port is read from an environment variable, defaulting to 8080
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
