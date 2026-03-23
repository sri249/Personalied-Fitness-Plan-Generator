---
title: FitPlan AI
emoji: 🏋️
colorFrom: green
colorTo: blue
sdk: streamlit
sdk_version: "1.36.0"
app_file: app.py
pinned: false
---

# FitPlan AI — Personalized Fitness Plan Generator

## 🚀 Milestone 4: Application Finalization & Deployment

---

## 🎯 Objective

The objective of this milestone is to finalize the FitPlan AI application by enhancing user experience, ensuring proper validation, implementing smooth navigation, handling errors effectively, and preparing the application for deployment.

---

## ✨ Key Features

### 🔐 Authentication System
- User Signup using Email & Password
- Secure Login verification
- 6-digit OTP generation after login
- Email-based OTP verification
- Resend OTP functionality
- Restricted dashboard access after verification

---

### 📊 Input Validation
- Validated all fields such as:
  - Name
  - Age
  - Height
  - Weight
- Prevented empty or invalid inputs
- Ensured realistic data ranges

---

### 🎨 Improved User Interface
- Clean and responsive UI using Streamlit
- Organized layout using columns
- Better readability of output

---

### 🔄 Navigation System
- Smooth page navigation using Streamlit session state
- Flow includes:
  - Signup → Login → OTP → Dashboard → Fitness Plan

---

### 🤖 AI Model Integration
- Integrated Hugging Face LLM via API
- Dynamic prompt generation using:
  - Name
  - Age
  - BMI Category
  - Fitness Goal
  - Fitness Level
  - Equipment
- Generates structured **5-day workout plans**

---

### ⚠️ Error Handling
- Handles invalid inputs gracefully
- Prevents application crashes
- Displays user-friendly error messages
- Handles AI failures safely

---

## 🧠 Technologies Used

- Python  
- Streamlit  
- SQLite Database  
- Hugging Face Inference API  
- SMTP (Email OTP System)  

---

## 📁 Project Structure
FitPlan-AI/
└── Milestone4/
├── app.py
├── database.py
├── auth.py
├── model_api.py
├── prompt_builder.py
├── requirements.txt
├── README.md
└── screenshots/
---

## ⚙️ Environment Variables

Add these in **Hugging Face Spaces → Settings → Variables and Secrets**:


HF_TOKEN = your_huggingface_token
EMAIL_USER = your_email@gmail.com

EMAIL_PASS = your_app_password

---

## 🧪 Testing Performed

- Signup functionality tested  
- Login validation tested  
- OTP generation and email delivery verified  
- OTP verification tested  
- Resend OTP functionality verified  
- Dashboard access control confirmed  
- AI workout plan tested with multiple inputs  

---

## 📸 Screenshots

The `screenshots/` folder includes:

- Signup Page  
- Login Page  
- OTP Email Received  
- OTP Verification  
- Dashboard  
- Generated Workout Plan  

---

## 🌐 Deployment

The application is deployed on Hugging Face Spaces:
https://huggingface.co/spaces/Srividhya09/AI-Fitness-Plan-Generator

---

## 🏁 Conclusion

Milestone 4 successfully completes the FitPlan AI application with secure authentication, AI-based workout plan generation, improved user experience, and full deployment readiness. The application is now stable, user-friendly, and ready for demonstration.
