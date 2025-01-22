# Title 

AI-Driven Supply Chain Disruption Predictor and Inventory Optimization System

## Description

This project aims to develop an advanced AI-powered system that revolutionizes supply chain management by monitoring global supply chain data, predicting potential disruptions, and optimizing inventory levels accordingly. By leveraging LLMs like OpenAI GPT, Meta LLaMA for natural language processing and data analysis, integrating with Google Sheets, and utilizing Slack or Email for real-time alerts, the system will provide predictive insights on supply chain risks and automate inventory adjustments. This comprehensive solution will enable businesses to proactively manage supply chain disruptions, optimize inventory levels, and maintain operational continuity in the face of global uncertainties.

## Roadmap

- Data Collection and Pre-Processing

- Model Development

- Integration: Connect predictive models to ERP systems and notification platforms.

- Dashboard Development

- Testing and Validation

- Deployment

  ## Acknowledgements

 - [Designing RESTful APIs](https://www.udacity.com/course/designing-restful-apis--ud388)
 - [Version Control with Git](https://www.udacity.com/course/version-control-with-git--ud123)
 - [Dataset](https://www.kaggle.com/datasets/chakilamvishwas/imports-exports-15000/data)


---

# Milestone 2: Comprehensive Workflow for News Data Analysis

In **Milestone 2**, I accomplished three major steps to perform data processing, risk analysis, and sentiment analysis on news articles. Below is a detailed summary of each step:


## **Step 1: Fetch News Data**
- **Objective**: To gather and structure news data from an external source for further analysis.
- **Process**:
  1. Used **NewsAPI** with a provided API key to fetch news articles related to a specific query (e.g., "supply chain disruption").
  2. Processed the retrieved data into a structured format, suitable for storage and analysis.
  3. Created functions to:
     - Save news data into a CSV file.
     - Aggregate the news data into a **DataFrame** for easier manipulation and structured representation.
- **Output**: A CSV file named `news_data.csv` containing the raw and processed news data, ready for the next stages of analysis.


## **Step 2: Risk Analysis**
- **Objective**: To analyze the collected news articles and identify associated risks by leveraging a pre-trained **Large Language Model (LLM)**.
- **Process**:
  1. **API Integration**:
     - Defined a list of risk factors (e.g., logistical, environmental, geopolitical).
  2. **LLM Model from hugging face**:
     - Used the Hugging Face pre-trained model **"sentence-transformers/all-MiniLM-L6-v2"** for natural language processing.
  3. **LLM Analysis**:
     - Encoded the predefined risk factors into embeddings using the model.
     - Encoded the text of the news articles and calculated similarity scores between the articles and the risk factors.
     - Assigned numeric risk scores to each article based on the highest similarity score.
  4. **Output**:
     - The processed risk data was saved in a CSV file named `news_import_export_risks_file(1).csv`, containing each article's text and also a CSV file named `news_import_export_risks_file(3).csv`,containing each article's text, corresponding risk scores, and the highest risk score.


## **Step 3: Sentiment Analysis**
- **Objective**: To evaluate the sentiment of the news articles (positive, negative, or neutral).
- **Process**:
  1. Downloaded and utilized the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** lexicon for sentiment analysis.
  2. Processed each article's text to compute sentiment scores:
     - Positive, negative, and neutral sentiment probabilities.
     - Overall sentiment polarity score (compound value).
  3. Saved the sentiment analysis results into a CSV file.
- **Output**: A CSV file named `news_sentiment_analysis.csv` containing sentiment scores for each news article.

---

# Milestone 3: Predictive Disruption Modeling & ERP Integration Module

This project focuses on analyzing warehouse data for the clothing industry to monitor stock utilization, assess risk factors, and provide actionable insights. It generates a synthetic dataset based on real-world constraints and provides a framework for data analysis.

## **Step 1: Milestone 3 Overview**
  1. Generate warehouse data for the product category of clothes.
  2. Analyze the generated data to identify stock utilization patterns, risk factors, and sentiment analysis.
  3. Provide actionable alerts (e.g., BUY, SELL, or MONITOR) based on data analysis.
  4. Save alerts and processed data to CSV files for reporting.

## **Step 2: Features**
  1. Synthetic Dataset Generation:
     - Month: The month of operation.
     - Warehouse Capacity: The total capacity of the warehouse.
     - Monthly Incoming: Number of units received in the warehouse.
     - Monthly Outgoing: Number of units dispatched from the warehouse.
     - Risk Analysis: A qualitative risk assessment (Low, Medium, or High).
     - Sentiment: Market sentiment for the supply chain (Positive, Neutral, or Negative).
  2. Data Analysis:
     - Monitors warehouse utilization and identifies critical conditions.
     - Generates actionable alerts based on:
       - High utilization rates.
       - Low utilization rates.
       - High risks.
       - Negative market sentiment.
  3. Output CSV Files:
     - Saves generated warehouse data to clothing_warehouse_data.csv.
     - Saves actionable alerts to warehouse_alerts.csv.

