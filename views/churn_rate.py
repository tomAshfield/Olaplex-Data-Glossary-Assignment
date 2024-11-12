import streamlit as st

st.title(":green[Customer Churn Rate (CCR)]")
st.divider()
st.write("""
**Definition**: Churn Rate represents the percentage of customers who stop purchasing Olaplex 
products within a specific time period.

**Business Relevance**: Reducing churn rate is critical for maintaining revenue and customer 
loyalty, and helps Olaplex identify potential areas for improvement in customer retention.

**Calculation**: Churn Rate is calculated as:
\[
\text{Churn Rate} = \frac{\text{Customers Lost During Period}}{\text{Total Customers at Start of Period}} \times 100
\]
""")
