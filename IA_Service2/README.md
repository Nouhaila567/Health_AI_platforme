# 🏥 Health IA Service

Service d'intelligence artificielle médicale — API REST complète
pour assister les médecins dans le diagnostic.

> Projet réalisé en Data Science — Python · FastAPI · Scikit-learn · Groq API

---

## 🔍 Fonctionnalités

| Endpoint | Description | Technologie |
|---|---|---|
| `POST /predict/diabetes` | Prédiction risque diabète | Random Forest — 78%+ |
| `POST /predict/cardio` | Prédiction risque cardiovasculaire | Gradient Boosting — 82%+ |
| `POST /symptoms/analyze` | Analyse symptômes en langage naturel | Règles cliniques |
| `POST /summary/patient` | Résumé IA du dossier patient | Groq / Llama 3.1 |
| `POST /chat/medical` | Chatbot médecin conversationnel | Groq / Llama 3.1 |
| `POST /notify/appointment` | Email rappel rendez-vous | Resend |

---

## 🛠 Stack technique

- **Python 3.11** + **FastAPI** — API REST avec documentation Swagger auto
- **Scikit-learn** — modèles ML entraînés sur datasets médicaux réels
- **Groq API (Llama 3.1)** — résumé clinique et chatbot conversationnel
- **Pydantic** — validation stricte des données médicales
- **Resend** — notifications email HTML
- **Docker** — containerisation pour déploiement cloud

---

## 🚀 Lancer le projet

### 1. Cloner le repo
git clone https://github.com/ton-username/ia_service2.git
cd ia_service2

### 2. Installer les dépendances
pip install -r requirements.txt

### 3. Configurer les variables d'environnement
Crée un fichier .env à la racine :
GROQ_API_KEY=ta_cle_groq
RESEND_API_KEY=ta_cle_resend

### 4. Entraîner les modèles ML
python models/train_diabetes.py
python models/train_cardio.py

### 5. Lancer le serveur
uvicorn main:app --reload --port 8001

### 6. Ouvrir la documentation
http://localhost:8001/docs

---

## 📊 Datasets utilisés
- Pima Indians Diabetes Database (Kaggle)
- Heart Disease UCI (Kaggle)

---
