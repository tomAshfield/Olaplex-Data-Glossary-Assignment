import streamlit as st

st.title("Sales Conversion Rate (SCR)")
st.divider()
st.write("""
**:green[Definition:]** Sales Conversion Rate is the percentage of 
leads or visitors that convert into customers. 


**:blue[Business Relevance:]** Understanding the conversion rate 
allows us to evaluate the effectiveness of sales and marketing 
efforts. 

**:red[Formula:]** Sales Conversion Rate is calculated as:
""")

st.image("./assets/scr_formula.png")
st.divider()

st.write(":orange[Sales Conversion Rate (SCR) Playground]")

st.write("""
In the formula:
- **Conversions:** the number of leads who became customers.
- **Leads:** the total number of potential customers.
""")

# Input fields for number of leads and conversions
conversions = st.number_input("Number of Conversions", min_value=0, step=1, value=225)
leads = st.number_input("Number of Leads", min_value=1, step=1, value=500)

# SCR Calculation
scr = (conversions / leads) * 100

st.write(f"Sales Conversion Rate = {scr:.2f}%")

st.divider()

st.write("""**:violet[Interpretations:]**
- A **higher SCR** indicates better performance in converting leads to customers.
- A **lower SCR** may indicate the need to optimize sales or marketing strategies.
""")
