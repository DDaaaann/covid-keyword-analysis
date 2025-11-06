# covid-keyword-analysis
NLP pipeline for analyzing keyword evolution in COVID-related Twitter discourse.

This repository contains selected Python scripts from a multi-step Natural Language Processing (NLP) pipeline used to analyze the evolution of public discourse during the COVID-19 pandemic. The project focuses on extracting, normalizing, comparing, and visualizing high-frequency keywords from Twitter data.

## Included Scripts

All scripts are located in the `code/` directory:

- `step1_merge_keywords.py`: Lemmatizes keywords and maps them to unified concepts using a custom synonym dictionary.
  
- `step2_filter_keywords.py`: Filters meaningless terms and calculates keyword lifespan (e.g., `span_months`, `max_consecutive_months`).

- `step3_heatmap_4views.py`： Keyword Heat Map (4 Perspectives： NormalWordCounts, Yake, Rake, AllCombined)

- `step3.2_plot_keyword_trend.py`: Visualizes keyword trends over time using Z-score normalization.
  
- `step3.3_RAKE_YAKE.py`: Compares RAKE and YAKE extracted keyword sets using Jaccard and RBO similarity, and generates cleaned WordClouds.
- `scatter_draw.py`: Generates a customized scatter plot of keyword lifespan with smart fan-out label positioning to avoid overlapping.

## Note on Data and Output

Due to data privacy concerns, raw tweet data, intermediate `.csv` files, and final plots are not included in this repository. Only core code logic is provided.
The project has been accepted byCSCI 2025 and is currently revising the manuscript in preparation for publication in SpringerNature.

## Programming Supplement

This repository supports a graduate school application as a demonstration of programming, NLP, and data visualization skills. For questions or access to the full pipeline, please contact the author directly.

---

Dan Li  
contact email: dannli@myyahoo.com
