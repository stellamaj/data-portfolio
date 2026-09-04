# AI-Powered Data Cleaning Workflow

This project demonstrates an AI-powered automated workflow for cleaning CSV data before analysis. Data cleaning is a strong candidate for automation because it happens frequently, often involves repetitive steps with predictable outcomes, and automation can reduce effort, time and cost. The workflow uses Power Automate to detect newly added CSV files, use AI to identify data type and format issues that may not be obvious from column labels alone, apply rule based cleaning steps, and notify a Data Analyst for final review before the data is used for analysis.

## Building the workflow in Power Automate

## Project overview

| Question | Answer |
|---|---|
| The problem, and who it affects | Data cleaning involves repetitive tasks that can take time and delay analysis. This affects Data Analysts who regularly prepare data for analysis. |
| The trigger | A new CSV file is added to the designated OneDrive or SharePoint folder. |
| One risk | AI could incorrectly identify a data type or format issue. |
| The safeguard | A Data Analyst reviews the cleaned file before it is used for analysis. |