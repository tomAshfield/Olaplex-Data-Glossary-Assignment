import streamlit as st

st.title(":green[Net Promoter Score (NPS)]")
st.divider()
st.write("""
**Definition**: Net Promoter Score (NPS) measures customer satisfaction and loyalty by asking 
customers how likely they are to recommend Olaplex products on a scale of 1 to 10.

**Business Relevance**: NPS is valuable for gauging overall customer sentiment and identifying 
potential promoters or detractors, helping Olaplex tailor its customer engagement and support efforts.

**Calculation**: NPS is calculated as:
\[
NPS = \% \text{ of Promoters} - \% \text{ of Detractors}
\]
where Promoters score 9-10, Passives score 7-8, and Detractors score 0-6.
""")