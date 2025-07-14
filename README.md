# 💊 Drug Dosage Recommender

A cool and aesthetic ML-powered web app that recommends safe drug dosages based on **age**, **weight**, and **medical condition**. Built with Flask, Linear Regression, Redis cache, and deployed on Render!

![App Screenshot](app/static/pill.png)

## 🚀 Features

- 📊 Predicts recommended dosage using ML model
- ⚙️ Caches predictions with Redis
- 🎨 Fun, modern UI with emojis & animations
- 🌐 Deployed live: [Click here to visit](https://drug-dosage-recommender.onrender.com/)

## 🛠️ Tech Stack

- Python, Flask
- Scikit-learn, Pandas
- Redis (for caching)
- HTML, CSS (custom style)
- Deployed on **Render**
- Version controlled with **GitHub**

## 📦 Installation

```bash
git clone https://github.com/yashitiwary/drug-dosage-recommender.git
cd drug-dosage-recommender
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python train_model.py
python run.py
