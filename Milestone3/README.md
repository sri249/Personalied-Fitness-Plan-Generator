---
title: AI Fitness Plan Generator
emoji: 🏋️
colorFrom: blue
colorTo: purple
sdk: streamlit
sdk_version: "1.36.0"
app_file: app.py
pinned: false
---

# AI Fitness Plan Generator
## Milestone 3: Login System with OTP Verification

### Objective
The objective of Milestone 3 is to implement a secure authentication system for the AI Fitness Plan Generator application. This milestone introduces user signup, login verification, OTP-based email authentication, and restricted dashboard access.

---

## Features Implemented

### 1. User Signup
Users can register using their **Email ID and Password**.  
The credentials are securely stored in a **SQLite database**.

### 2. User Login
Users can log in using their registered credentials.  
The system verifies the credentials from the database.

### 3. OTP Generation
After successful login, a **6-digit OTP (One-Time Password)** is generated.

### 4. Email OTP Verification
The generated OTP is sent to the user's registered email address.  
Users must enter the OTP correctly to proceed.

### 5. Secure Dashboard Access
Only users who successfully verify the OTP are allowed to access the application dashboard.

---

## Technologies Used

- Python
- Streamlit
- SQLite Database
- SMTP Email Service
- Session State Authentication

---

These should be added in **Hugging Face Spaces → Settings → Variables and Secrets**.

---

## Screenshots

Screenshots of the application are stored in the `screenshots` folder, including:

- Signup Page
- Login Page
- OTP Email Received
- OTP Verification Page
- Dashboard Access

---

## Deployment

The application is deployed using **Hugging Face Spaces with Streamlit**.

Deployment Link:

https://huggingface.co/spaces/Srividhya09/AI-Fitness-Plan-Generator

---

## Conclusion

Milestone 3 successfully implements a secure authentication system with OTP verification. This ensures that only verified users can access the AI Fitness Plan Generator dashboard, improving application security and user management.

## Project Structure
