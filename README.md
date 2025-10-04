# IPL Player Valuation & Risk Modeling

A comprehensive machine learning system that predicts the outcome of IPL cricket matches. This project demonstrates end-to-end data processing pipeline from raw data processing to deployed predictive models.

## Data Sources
- IPL ball-by-ball dataset (2008-2025 seasons)
- 278,000+ ball records
- 64 features per ball 

## Key Features
1. **Data Preprocessing**
- Handles missing values and data inconsistencies
- Standardizes venue names and team names
- Creates match-level summaries from ball-by-ball data
- Handles categorical variable encoding

2. **Feature Engineering**
- Player Impact Scoring:
-- Batting impact (runs, average, strike rate)
-- Bowling impact (wickets, economy, strike rate)
-- All-rounder impact scoring
-- Z-score normalization within seasons

- Team Strength Calculation:
-- Composite team strength from player impacts
-- Separate batting and bowling strength metrics
-- All-rounder contribution weighting
-- Historical season-based strength calculation

- Match Context Features:
-- Target runs and required run rate
-- Venue-specific factors
-- Strength differentials between teams

3. **Machine Learning Models**
- Trained and compared 6 different algorithms:
Logistic Regression - Baseline interpretable model
Random Forest - Robust ensemble method
Gradient Boosting - Sequential error correction
XGBoost - State-of-the-art performance
K-Nearest Neighbors - Distance-based learning
Support Vector Machine - Boundary-based classification

4. **Model Performance**
- Best Model: Support Vector Machine
- Test Accuracy: 72%
