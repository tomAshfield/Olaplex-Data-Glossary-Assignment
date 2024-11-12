import streamlit as st

st.title("Net Promoter Score (NPS)")
st.divider()
st.write("""
**:green[Definition:]** Net Promoter Score (NPS) is a metric used to 
measure customer loyalty and satisfaction with a company's products 
or services.

**:blue[Business Relevance:]** NPS is a leading indicator of company 
growth because it measures customer loyalty, which in turn affects 
the likelihood of customer referrals and contract renewals.

**:red[Formula:]** NPS is calculated as:
""")
left_co, cent_co,last_co = st.columns([1,10,1])
with cent_co:
    st.image('./assets/NPS_formula.jpg')

st.divider()

st.write(":orange[Net Promoter Score (NPS) Playground]")

st.write("""
In the formula:
- **Promoters:** customers who rate 9-10.
- **Passives:** customers who rate 7-8.
- **Detractors:** customers who rate 0-6.
""")

# Input fields for Promoters, Passives, and Detractors
promoters = st.number_input("Number of Promoters", min_value=0, step=1, value=50)
passives = st.number_input("Number of Passives", min_value=0, step=1, value=30)
detractors = st.number_input("Number of Detractors", min_value=0, step=1, value=20)

# NPS Calculation
total_respondents = promoters + passives + detractors
if total_respondents > 0:
    nps = ((promoters - detractors) / total_respondents) * 100
else:
    nps = 0

# Display the NPS result
st.write(f"Net Promoter Score = {nps:.2f}%")

st.divider()

st.write("""**:violet[Interpretation:]**
- A **positive NPS** indicates more loyal customers.
- A **negative NPS** indicates more dissatisfied customers.
""")