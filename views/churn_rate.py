import streamlit as st

st.title("Customer Churn Rate (CCR)")
st.divider()
st.write("""
**:green[Definition:]** Churn Rate is the percentage of 
customers who stop doing business with a company 
over a given period of time.

**:blue[Business Relevance:]** Churn rate is a key metric 
for businesses because it can impact many aspects of a 
company, including: Revenue, Customer satisfaction, and 
Loyalty.

**:red[Formula:]** Churn Rate is calculated as:
""")

st.image("./assets/cr_formula.webp")
st.divider()

st.write(":orange[Customer Churn Rate (CCR) Playground]")

st.write("""
In the formula:
- **Lost Customers:** number of customers who stopped doing business.
- **Total Customers:** total customer base at the start of the period.
""")

# Input fields for total customers and lost customers
total_customers = st.number_input("Total Customers at Start of Period", min_value=1, step=1, value=500)
lost_customers = st.number_input("Number of Lost Customers", min_value=0, step=1, value=50)

# CCR Calculation
ccr = (lost_customers / total_customers) * 100

# Display the CCR result
st.write(f"Customer Churn Rate = {ccr:.2f}%")

st.divider()

st.write("""**:violet[Interpretation:]**
- A **high CCR** indicates more customers are leaving, potentially signaling issues with customer satisfaction.
- A **low CCR** indicates a more stable and satisfied customer base.
""")