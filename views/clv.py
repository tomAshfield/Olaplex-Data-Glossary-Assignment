import streamlit as st

st.title("Customer Lifetime Value (CLV)")
st.divider()
st.write("""
**:green[Definition:]** CLV is the total revenue a business can 
expect from a customer over their entire relationship, including repeat business, upselling, and cross-selling.

**:blue[Business Relevance:]** CLV is essential for assessing 
long-term profitability, guiding Olaplex’s investment in marketing to acquire and retain loyal customers.

**:red[Formula:]** CLV can be calculated as:
""")
st.image("./assets/clv_formula.png")
st.divider()

st.write(":orange[Customer Lifetime Value (CLV) Playground]")

st.write("""
This calculator helps you estimate the Customer Lifetime Value (CLV) based on the following inputs:
- **Average Purchase Value**: How much, on average, a customer spends per purchase.
- **Purchase Frequency**: The number of purchases a customer makes per year.
- **Average Customer Lifespan**: The average number of years a customer remains with Olaplex.
""")

# Input fields
avg_purchase_value = st.number_input("Average Purchase Value ($)", min_value=0.0, step=1.0, value=50.0)
purchase_frequency = st.number_input("Purchase Frequency (per year)", min_value=0, step=1, value=4)
customer_lifespan = st.number_input("Average Customer Lifespan (years)", min_value=0, step=1, value=3)

# CLV calculation
clv = avg_purchase_value * purchase_frequency * customer_lifespan

st.write(f"Customer Lifetime Value = ${clv:,.2f}")

st.divider()

# Interpretation
st.write("""
**:violet[Interpretation]**:
- A **higher CLV** means that each customer is more valuable over time, 
   which can justify greater investment in customer acquisition and retention strategies.
- A **lower CLV** suggests limited long-term revenue from each customer, 
   indicating that the company may need to focus on increasing purchase frequency, 
   customer retention, or average purchase value.
""")
