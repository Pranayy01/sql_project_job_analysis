
---

# 🐍 `generate_visuals.py` (script to create visuals)

Save the following as `generate_visuals.py` in your repo root and run it. It creates three PNGs inside `images/`.

```python
import os
import json
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# --- Config ---
FILES = {
    "in_demand": "result_3.json",   # demand_count
    "top_paying_skills": "result_5.json",  # avg_salary
    "demand_salary": "result_4.json"  # demand_count + avg_salary
}
OUT_DIR = Path("images")
OUT_DIR.mkdir(exist_ok=True)

# --- Helper to load JSON into DataFrame ---
def load_json_to_df(path):
    if not Path(path).exists():
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    return df

# 1) Top In-Demand Skills (bar chart)
def plot_in_demand():
    df = load_json_to_df(FILES["in_demand"])
    # ensure numeric
    if "demand_count" in df.columns:
        df["demand_count"] = pd.to_numeric(df["demand_count"], errors="coerce")
    df = df.sort_values("demand_count", ascending=False).head(12)
    plt.figure(figsize=(10,6))
    plt.barh(df["skills"].astype(str)[::-1], df["demand_count"][::-1])
    plt.xlabel("Demand Count")
    plt.title("Top In-Demand Skills (by postings)")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "top_in_demand_skills.png", dpi=150)
    plt.close()

# 2) Top Paying Skills (bar chart)
def plot_top_paying_skills():
    df = load_json_to_df(FILES["top_paying_skills"])
    if "avg_salary" in df.columns:
        df["avg_salary"] = pd.to_numeric(df["avg_salary"], errors="coerce")
    # top 15 by avg_salary
    df = df.sort_values("avg_salary", ascending=False).head(15)
    plt.figure(figsize=(10,6))
    plt.barh(df["skills"].astype(str)[::-1], df["avg_salary"][::-1])
    plt.xlabel("Average Salary")
    plt.title("Top Paying Skills (average salary)")
    plt.tight_layout()
    plt.savefig(OUT_DIR / "top_paying_skills.png", dpi=150)
    plt.close()

# 3) Demand vs Average Salary scatter (to find optimal skills)
def plot_demand_vs_salary():
    df = load_json_to_df(FILES["demand_salary"])
    # expected columns: skills, demand_count, avg_salary
    for col in ["demand_count", "avg_salary"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["demand_count", "avg_salary"])
    plt.figure(figsize=(10,7))
    plt.scatter(df["demand_count"], df["avg_salary"], s=60)
    # label some top points (optional)
    # annotate top 10 by avg_salary
    top_by_salary = df.sort_values("avg_salary", ascending=False).head(10)
    for _, row in top_by_salary.iterrows():
        plt.annotate(row["skills"], (row["demand_count"], row["avg_salary"]), textcoords="offset points", xytext=(5,5), fontsize=8)
    plt.xlabel("Demand Count")
    plt.ylabel("Average Salary")
    plt.title("Skill Demand vs Average Salary")
    plt.grid(True, linestyle="--", linewidth=0.5, alpha=0.6)
    plt.tight_layout()
    plt.savefig(OUT_DIR / "demand_vs_salary_scatter.png", dpi=150)
    plt.close()

def main():
    try:
        plot_in_demand()
        print("Saved images/top_in_demand_skills.png")
    except Exception as e:
        print("Failed to plot in-demand:", e)

    try:
        plot_top_paying_skills()
        print("Saved images/top_paying_skills.png")
    except Exception as e:
        print("Failed to plot top-paying skills:", e)

    try:
        plot_demand_vs_salary()
        print("Saved images/demand_vs_salary_scatter.png")
    except Exception as e:
        print("Failed to plot demand vs salary:", e)

if __name__ == "__main__":
    main()
