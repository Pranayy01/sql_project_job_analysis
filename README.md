# sql_project_job_analysis
# 📊 Data Analyst Jobs & Skills Analysis

**A SQL-driven analysis of Data Analyst job postings** to discover top-paying jobs, in-demand skills, and the most optimal skills (high demand + high salary).

---

## 🔎 Project Overview

This repository analyzes job postings for the role *Data Analyst* and extracts insights about:
- Top-paying job postings
- Skills required by the top-paying jobs
- The most in-demand skills by count
- Skills that offer the best balance of demand and average salary

SQL queries used:
- `1_top_paying_jobs.sql`
- `2_top_paying_job_skills.sql`
- `3_in-demand_skills.sql`
- `top_paying_skills.sql`
- `most_optimal_skills.sql`

Result files (already included):
- `Result_!.json` — Top paying jobs
- `result_2.json` — skills for top paying jobs
- `result_3.json` — in-demand skills
- `result_4.json` — demand + avg salary (optimal skills)
- `result_5.json` — top paying skills (avg salary)

---

## 📈 Visuals

The repository includes visuals generated from the JSON outputs:

- `images/top_in_demand_skills.png` — Top 10 in-demand skills (by count)
- `images/top_paying_skills.png` — Top 15 skills by average salary
- `images/demand_vs_salary_scatter.png` — Demand vs Average Salary (helps find high-demand, high-pay skills)

If these images are missing, generate them using the included script: `generate_visuals.py`.

---

## 🛠 How to generate visuals

1. Create a virtual environment (recommended):
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
