<<<<<<< HEAD
# NeuroAI Multi-Agent System

### AI-Powered Dataset Analysis & Project Planning Platform

## Overview

NeuroAI is a **multi-agent AI platform** designed to analyze datasets and automatically generate insights, project plans, and structured reports.

The system simulates a team of AI agents that collaborate to interpret data, analyze tools and projects, allocate employees, and generate a final report in **PDF format**.

This project was built as part of the **NeuraX 2.0 AIML Challenge**, where the objective is to create an **Autonomous AI Agent capable of converting client requirements into a development workflow**.

---

# System Architecture

The platform follows a **multi-agent architecture** where each agent has a specific responsibility.

User Input
↓
FastAPI Backend
↓
Agent Manager
↓
Dataset Analysis Agents
↓
Discussion Engine
↓
PDF Report Generator

---

# Agents in the System

### Planner Agent

Responsible for interpreting the task and generating the **overall development workflow** for the project.

### Research Agent

Analyzes the **AI tools dataset** and evaluates technologies required for the system.

### Dataset Intelligence Agent

Processes datasets and extracts useful information.

### Data Analyst Agent

Performs deeper analysis such as:

* project clustering
* performance insights
* trend analysis

### Visualization Agent

Can be used for generating visual summaries of dataset insights.

### Code Interpreter Agent

Handles data processing logic and computations.

### Writer Agent

Combines insights from all agents into a structured response.

### Report Generator Agent

Creates a **PDF report** summarizing the final analysis.

---

# Supported Dataset Types

The system currently supports four types of inputs.

## 1. AI Tools Dataset

The system analyzes tools used in AI systems and assigns **quality ratings**.

Example Output:

* Large Language Models – Rating 9.5
* Vector Database / RAG – Rating 9.2
* SQL Database – Rating 8.8
* Redis Cache – Rating 8.5
* Docker / Kubernetes – Rating 8+

Purpose:
Identify the best technology stack for the AI system.

---

## 2. Project History Dataset

Projects are analyzed and grouped into clusters based on success metrics.

Clusters:
High Success Projects
Medium Complexity Projects
Rapid Development Projects

Insights include:

* success patterns
* team size impact
* recommended development strategies

---

## 3. Employees Dataset

Employees are analyzed based on experience, skills, and workload.

The system automatically generates a **project team allocation plan**.

Example:

Data Engineer → Employee_38
Machine Learning Engineer → Employee_368
Data Scientist → Employee_468
Backend Developer → Employee_416
Frontend Developer → Employee_72
DevOps Engineer → Employee_330

This ensures balanced workload distribution.

---

## 4. Requirement Document

When a client requirement document is provided, the AI agent generates a **complete development workflow**.

Example Workflow:

1. Data Collection → Data Engineer
2. NLP Model Training → ML Engineer
3. Knowledge Base Indexing → Data Scientist
4. API Development → Backend Developer
5. Chat Interface Development → Frontend Developer
6. Deployment & Monitoring → DevOps Engineer

---

# Features

• Multi-Agent AI architecture
• Automatic dataset analysis
• AI tool evaluation and ranking
• Project clustering and insights
• Employee workload distribution
• Client requirement interpretation
• Automated PDF report generation
• REST API built using FastAPI
• Frontend interface built with Next.js

---

# Technology Stack

Backend
FastAPI
Python
Pandas

Frontend
Next.js
React

Data Processing
Pandas

Report Generation
ReportLab

---

# Project Folder Structure

backend
app
data
neurax_employees_dataset.csv
neurax_tools_dataset.csv
neurax_projects_dataset.csv
neurax_project_history_dataset.csv

modules
agent_manager.py
dataset_loader.py
discussion_engine.py
pdf_generator.py
file_responses.py

routes
api_routes.py

main.py

frontend
pages
components
styles

---

# Installation

Clone the repository

git clone <repository_url>

Navigate to project folder

cd neuroai

Create virtual environment

python -m venv .venv

Activate environment

Windows

.venv\Scripts\activate

Install dependencies

pip install fastapi uvicorn pandas reportlab python-multipart

---

# Running the Backend

Navigate to backend folder

cd backend

Start the FastAPI server

uvicorn app.main:app --reload

Open API documentation

http://127.0.0.1:8000/docs

---

# Running the Frontend

Navigate to frontend folder

cd frontend

Install dependencies

npm install

Start the development server

npm run dev

Open browser

http://localhost:3000

---

# Example Workflow

1. Upload a dataset
2. System identifies dataset type
3. Corresponding AI agent processes the data
4. Insights are generated
5. Writer agent prepares final response
6. Report generator creates PDF output

---

# Expected Output

The system returns:

• dataset analysis
• AI tool evaluation
• project insights
• employee allocation plan
• AI generated development workflow
• downloadable PDF report

---

# Future Improvements

• Real AI model integration for dynamic analysis
• Automatic dataset detection using machine learning
• Agent memory system
• Graph-based project clustering
• Advanced data visualization dashboard

---

# Author

Meghana Edam
Electronics And Communication Engineering 

Shravanthi (Nani)
Computer Science Engineering Student

Project developed for **NeuraX 2.0 – AIML Autonomous Agent Challenge**

---

# License

This project is intended for educational and research purposes.
=======
# Autotask
>>>>>>> 676090cdc398a1afae5ce78f470c505fe3309478
