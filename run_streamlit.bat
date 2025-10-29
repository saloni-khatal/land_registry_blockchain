@echo off
cd /d "C:\path\to\your\project"
start "" streamlit run app.py
timeout /t 5 >nul
start http://localhost:8501
