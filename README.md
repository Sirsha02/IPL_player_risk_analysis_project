# IPL Player Valuation & Risk Modeling

A quantitative data science project that treats cricketers as financial assets, applying risk modeling techniques to evaluate IPL player performance and auction valuation.

## Project Overview

This project tackles a key problem in T20 cricket analytics: **How can we objectively compare players across different roles and quantify the investment risk associated with acquiring them?** By applying financial risk concepts like **Value at Risk (VaR)** and **Monte Carlo simulation** to player performance data, this model provides a framework for data-driven decision-making in player auctions.

## Objectives

- **Standardize Performance Metrics:** Create a unified "Player Impact Score" for direct comparison between batsmen and bowlers
- **Quantify Risk:** Calculate Value-at-Risk (VaR) to measure downside performance risk
- **Optimize Portfolios:** Develop a framework to build optimal player portfolios under budget constraints

## Project Structure

IPL-Risk-Modeling/
1.preprocessing.ipynb          # Data cleaning, merging, and initial aggregation
2.impact_score.ipynb           # Calculating batting and bowling impact scores
utils.py                       # Utility functions for data loading and calculations
outputs/                       # Processed data and results

