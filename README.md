# 🚀 CI/CD Pipeline with GitHub Actions, Docker, and Minikube 

This project demonstrates a full CI/CD pipeline using:
- 🐙 GitHub Actions for automation
- 🐳 Docker & Docker Hub for containerization
- 📦 Minikube for local Kubernetes deployment

---

## 🛠 Tech Stack

+ GitHub       
+ Docker       
+ Docker Hub   
+ GitHub Actions 
+ Minikube
+ Kubectl  

---

## 📁 Project Structure

```
├── app.py
├── README.md
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── deployment.yml
├── service.yml
└── .github/
  └── workflows/
    └── ci-cd.yml
```

---

## ⚙️ CI/CD Workflow Overview

### ✅ Trigger: 
On push to the `master` branch

### 🔧 GitHub Actions Workflow:

1. 🧾 Checkout Code  
2. 🔐 Log in to Docker Hub  
3. 🔨 Build Docker image  
4. 📤 Push to Docker Hub  

---

### 🔗 Docker Hub Image

[utkarshjain01/my-flask-app-el](https://hub.docker.com/r/utkarshjain01/my-flask-app-el)

---

### 🚀 Deploy Locally Using Minikube

#### 1. Start Minikube

```minikube start --driver=docker```

#### 2. Apply Kubernetes files

```kubectl apply -f deployment.yml```

```kubectl apply -f service.yml```

#### 3. Access the App

```minikube service py-app-service```

This will output something like:

| NAMESPACE |      NAME      | TARGET PORT |            URL             |
|-----------|----------------|-------------|----------------------------|
| default   | py-app-service |        5000 | ```http://<minikube-ip>:30007``` |

📌 Copy the URL shown in the last column and paste it into your browser to access the app.

![Screenshot 2025-06-21 192708](https://github.com/user-attachments/assets/1a5110d0-b254-4333-b20c-cb0d0a9a2ed3)

---

### 🙌 Conclusion

This project showcases a full, cloud-free CI/CD pipeline using modern DevOps tooling — fully automating build, test, and deploy to a local Kubernetes cluster. Ideal for local testing or development pipelines.

---

## ✍️ Author 
Utkarsh Jain

[LinkedIn](https://www.linkedin.com/in/utkarsh-jain02/)
