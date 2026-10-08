# Python Automation Toolkit: Fiverr Market Research

A portfolio case study showing how I used Python, pandas, reusable analysis modules, and Jupyter notebooks to turn collected Fiverr gig data into a dataset that could be explored and compared.

This project sits at the intersection of **data preparation, exploratory analysis, visualization, and text analysis**. The goal was not just to collect rows of marketplace data, but to make that data useful for understanding service offerings, prices, delivery timelines, and the language sellers use to describe their work.

## What the workflow does

1. **Load and inspect source data** — examine columns, data types, missing values, and consistency across source tables.
2. **Clean and combine data** — join related tables, standardize column names, handle missing values, and prepare a master dataset for analysis.
3. **Explore the market** — summarize prices and delivery timelines, search text fields, and inspect common values and data-quality issues.
4. **Analyze listing language** — use a separate notebook to explore recurring words and terms in gig text.
5. **Communicate findings** — create charts that make pricing, delivery, and text patterns easier to review.

## Project artifacts

- **[View the project page](./)** — screenshots and a guided overview of the workflow.
- **[Source repository](https://github.com/CristylePGarrard/Fiverr-consulting-toolkit)** — project code, data-workflow modules, and notebooks.
- **[Initial data analysis notebook](https://github.com/CristylePGarrard/Fiverr-consulting-toolkit/blob/main/notebooks/Fiverr_Initial_Data_Analysis.ipynb)** — initial inspection, cleaning, joining, and exploratory analysis.
- **[NLP text analysis notebook](https://github.com/CristylePGarrard/Fiverr-consulting-toolkit/blob/main/notebooks/Fiverr_NLP_Text_Analysis.ipynb)** — exploratory analysis of listing text.
- **[Python source modules](https://github.com/CristylePGarrard/Fiverr-consulting-toolkit/tree/main/src)** — data loading, cleaning, ETL, quality checks, feature helpers, and analysis functions.
- **[Portfolio screenshots and charts](https://github.com/CristylePGarrard/Fiverr-consulting-toolkit/tree/main/portfolio)** — visual examples captured during development.

## Tools and techniques

- Python
- pandas
- Jupyter Notebook
- Data loading, joins, cleaning, and normalization
- Exploratory data analysis (EDA)
- Data-quality and missing-value checks
- Matplotlib / Seaborn visualizations
- Exploratory keyword and text analysis

## What I learned / what this demonstrates

The work demonstrates a practical progression from raw inputs to analysis: inspect the data before relying on it, make transformations repeatable, keep reusable logic in Python modules where possible, and use visualizations to communicate patterns. It also separates exploratory notebook work from reusable functions so the project can continue to grow.

The text analysis is exploratory rather than a production NLP model. The repository should be treated as a project in progress, not as a finished commercial market-research product.

## Notes on data and reproducibility

The source repository organizes raw and processed data separately. Data files may not be included in every checkout, and results depend on the source data available locally. Review the notebooks and source modules for the current workflow and expected inputs before running them.

---

*Part of [Cristyle Garrard's portfolio](https://cristylepgarrard.github.io/Portfolio/).*
