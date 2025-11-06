# COVID Keyword Evolution Analysis 

This repository contains selected Python scripts from a multi-stage Natural Language Processing (NLP) pipeline developed to analyze the evolution of public discourse during the COVID-19 pandemic on Twitter. The project focuses on extracting, normalizing, comparing, and visualizing high-frequency keywords across time using both traditional (word counts) and algorithmic (RAKE, YAKE) methods.

## Included Scripts

All scripts are presented in the top-level directory:

- `step1_merge_keywords.py`: Lemmatizes keywords and maps them to unified concepts via a custom synonym dictionary.

- `step2_filter_keywords.py`: Filters meaningless terms and calculates keyword lifespan metrics (e.g., `span_months`, `max_consecutive_months`).

- `step3_heatmap_4views.py`: Generates a heatmap of keyword intensities across four perspectives (Normal Word Count, YAKE, RAKE, Combined).

- `step3.2_plot_keyword_trend.py`: Visualizes monthly trends of selected keywords using Z-score normalization.

- `step3.3_RAKE_YAKE.py`: Compares RAKE and YAKE keyword sets using Jaccard and RBO similarity metrics; generates normalized word clouds.

- `step3.4_count_distribution.py`: Analyzes frequency distribution of evergreen vs. bursty keywords.

- `scatter_draw.py`: Creates a customized scatter plot of keyword lifespan with intelligent fan-out label positioning for overlapping points.

## 🚫 Data and Output Disclaimer

Due to privacy and data usage policies, raw tweet data, intermediate `.csv` files, and generated figures are not included in this repository. This repository only provides clean, modular Python code for keyword extraction, normalization, analysis, and visualization.

> This work was accepted by **CSCI 2025** and is currently under manuscript revision for publication with **Springer Nature**.

## Programming Supplement Purpose

This repository is submitted as part of a graduate application to demonstrate proficiency in programming, text mining, and data visualization using Python. For access to the full pipeline or project details, please contact the author.

---

Dan Li  
📧 Email: dannli@myyahoo.com  
🔗 GitHub: [https://github.com/YOUR_USERNAME/covid-keyword-analysis](https://github.com/YOUR_USERNAME/covid-keyword-analysis)
