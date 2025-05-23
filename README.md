# 🧠 Diabetes Prediction System

A modern, production-grade end-to-end machine learning system that predicts diabetes using deep learning, serves a RESTful API, includes visualization tools, a user-friendly UI, and is fully containerized and cloud-deployable.

![FastAPI](https://img.shields.io/badge/FastAPI-✅-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Docker](https://img.shields.io/badge/Dockerized-Yes-blue)
![CI/CD](https://img.shields.io/github/actions/workflow/status/your-repo/python-ci.yml)

---

## 🚀 Features

- ✅ Deep learning for medical prediction
- 🌐 FastAPI backend with `/predict` endpoint
- 📊 Streamlit UI for interactive predictions
- 🧪 Pytest + GitHub Actions for test automation
- 🐳 Docker + docker-compose ready
- ☁️ Deployable on Render, AWS, Hugging Face Spaces
- 📈 Business intelligence via data visualizations

---

## 🧠 Project Architecture

```
diabetes_prediction_system/
├── README.md
├── requirements.txt
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│   └── diabetes_prediction.ipynb
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── data/
│   │   ├── load_data.py
│   │   └── preprocess.py
│   ├── model/
│   │   ├── builder.py
│   │   ├── train.py
│   │   ├── tuner.py
│   │   └── evaluate.py
│   ├── api/
│   │   ├── app.py
│   │   └── schemas.py
│   ├── utils/
│   │   ├── logger.py
│   │   └── visualization.py
│   └── cloud/
│       ├── docker_helpers.py
│       └── deploy_aws.py
│
├── tests/
│   ├── test_data.py
│   ├── test_model.py
│   └── test_api.py
│
└── frontend/
    ├── public/
    ├── src/
    │   ├── App.js
    │   └── components/
    └── package.json
```

---

## 🧪 Quick Start

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Train model
python src/model/train.py

# Start backend API
uvicorn src.api.app:app --reload

# Launch Streamlit UI
streamlit run deploy_streamlit.py
```

---

## 🔧 Docker Usage

```bash
docker-compose up --build
```

---

## ☁️ Cloud-Ready

| Platform      | Status | Notes                              |
|---------------|--------|-------------------------------------|
| Hugging Face  | ✅     | Streamlit UI support                |
| Render        | ✅     | Docker deploy (FastAPI + model)     |
| AWS           | ✅     | S3 + Docker + retraining scripts    |

---

## 🧠 Insights & BI

```bash
python src/utils/visualization.py
```

Visualizations:
- Class balance
- Correlation matrix
- ROC/AUC curve
- Confusion matrix

---

## 📦 Automation

- **CI/CD**: `.github/workflows/python-ci.yml`
- **Retraining**: `dags/retrain_diabetes.py` (cron or Airflow)

---

## 📄 License

MIT © 2025 — [Daniel Jude]