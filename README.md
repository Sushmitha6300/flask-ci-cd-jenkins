# CI/CD Pipeline for Flask App using Jenkins, Docker & Terraform on AWS

This project demonstrates how to set up a complete CI/CD pipeline for a simple Python Flask web application. Jenkins automates the build and deployment process using Docker, and infrastructure is provisioned on AWS using Terraform.

---

## Table of Contents

**Project Structure**
**Tools & Technologies Used**
**Prerequisites**
**Infrastructure Setup with Terraform**
**Jenkins & Docker Installation**
**Jenkins Configuration**
**Outcome**
**Author**

---

## Project Structure
```bash
flask-ci-cd-jenkins/
│
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   ├── terraform.tfvars
│   ├── outputs.tf
│   ├── flask_key
│   └── flask_key.pub
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── Jenkinsfile
│
├── .gitignore
└── README.md
```

---

## Tools & Technologies Used

- **Terraform –** Infrastructure as Code (IaC)
- **AWS EC2 –** Hosting Jenkins and the Flask app
- **Jenkins –** Continuous Integration and Deployment
- **Docker –** Containerizing the Flask application
- **GitHub –** Source Code Management
- **Flask –** Python-based web application framework

---

## ✅ Prerequisites

Before starting, ensure you have:

✅ Terraform installed and available in your system path

✅ An AWS account (access keys configured for Terraform)

✅ A GitHub account with a public repo for this project

✅ A Docker Hub account (for storing built images)

---

### Infrastructure Setup with Terraform

**1. Clone the repo**
```bash
git clone https://github.com/Sushmitha6300/flask-ci-cd-jenkins.git
cd flask-ci-cd-jenkins/terraform
```

**2. Generate SSH key pair**
```bash
ssh-keygen -t rsa -b 4096 -f flask_key
```

**3. Initialize Terraform and provision infrastructure**
```bash
terraform init
terraform plan
terraform apply
```

**Note the EC2 Public IP from the Terraform output.**

---

### Jenkins & Docker Installation

**SSH into the EC2 instance using the private key:**
```bash
ssh -i ./flask_key ubuntu@ec2-public-ip
```

**Then run the following setup:**
```bash
# Update system packages
sudo apt update -y
sudo apt upgrade -y

# Install Docker
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
sudo usermod -aG docker ubuntu

# Install Java (required for Jenkins)
sudo apt update -y
sudo apt install -y curl gnupg2 fontconfig openjdk-17-jdk
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt update -y
sudo apt install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins
sudo systemctl status jenkins

# Jenkins Docker permission
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

---

### Jenkins Configuration

**Access Jenkins**
```bash
http://ec2-public-ip:8080
```
**Unlock Jenkins**

Run the following command on the instance to get the initial password:
```bash
sudo cat /var/lib/jenkins/secrets/
```

Copy the password and paste it into the Jenkins setup screen.

Create Admin User and install suggested plugins

**Install required plugins**

- Docker Pipeline
- Docker Commons
- GitHub Integration
- Git Parameter Plugin
- Pipeline: GitHub or Git
- Pipeline: Stage View
- Blue Ocean 

**Add DockerHub credentials under:**

Jenkins → Manage Jenkins → Credentials → Global → Add Credentials

ID: dockerhub-credentials

Username: your-dockerhub-username

Password: DockerHub personal access token

**How to Create a Docker Hub Personal Access Token**

You’ll need a Personal Access Token (PAT) instead of your Docker password for secure authentication in Jenkins.

**Steps:**

- Log in to Docker Hub
- Click on your profile icon → Go to "Account Settings"
- From the left sidebar, click on "Personal cccess tokens"
- Now click on "Generate new token"
- Provide "Access token description", such as jenkins-token
- Select "Expiration date"
- Set "Access permissions to "Read, Write, Delete"
- Click "Generate"
- Copy the generated token and save it securely — you won’t be able to see it again.
- Use this token as the password when adding DockerHub credentials in Jenkins:

---

### GitHub Integration & Pipeline Setup

**Push the project to GitHub**

- Create a Public GitHub Repository named flask-ci-cd-jenkins
- Push Your Project Folder to GitHub
- In your terminal, navigate to flask-ci-cd-jenkins folder and run:
```bash
git init
git remote add origin https://github.com/your-username/flask-ci-cd-jenkins.git
git add .
git commit -m "Initial commit for CI/CD Node.js app with Jenkins and Terraform"
git push -u origin main
```

**Make sure to replace your-username with your actual GitHub username**

### Set up the Jenkins pipeline
- Go to Jenkins → New Item → Enter a name → Select Pipeline
- Under Pipeline script from SCM:
- SCM: Git
- Repository URL: your GitHub repo URL
- In the "Branch Specifier" field, change the default value from */master to */main to match your GitHub branch name.
- Script Path: app/Jenkinsfile
- Click Save, then Build Now

---

## Outcome

You now have a complete CI/CD pipeline for a Flask application using Jenkins, Docker, and Terraform on AWS

## About Me

Hey there! I’m Sushmitha, an aspiring DevOps Engineer passionate about automating infrastructure and streamlining deployments.

Currently, I’m building hands-on projects to master the DevOps lifecycle — from infrastructure as code to CI/CD and monitoring.

Always eager to learn, experiment, and take on new challenges in the cloud and DevOps world.

**Let’s connect!**

- **LinkedIn:** www.linkedin.com/in/sushmitha-ande
- **GitHub:** https://github.com/Sushmitha6300
