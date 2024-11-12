import streamlit as st
from streamlit_extras.stylable_container import stylable_container

home_page = st.Page(
    "views/home.py",
    title="Home",
    icon = ":material/home:",
    default = True
)

clv_page = st.Page(
    "views/clv.py",
    title="Customer Lifetime Value",
    icon=":material/home:"
)

nps_page = st.Page(
    "views/nps.py",
    title="Net Promoter Score",
    icon=":material/home:"
)

conversion_rate_page = st.Page(
    "views/conversion_rate.py",
    title="Sales Conversion Rate",
    icon=":material/home:"
)

churn_rate_page = st.Page(
    "views/churn_rate.py",
    title="Customer Churn Rate",
    icon=":material/percent:"
)

sku_page = st.Page(
    "views/sku.py",
    title="SKU (Stock Keeping Unit)",
    icon=":material/barcode:"
)


# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Intro": [home_page],
        "Concepts": [clv_page, nps_page, conversion_rate_page, churn_rate_page, sku_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/ODG_logo4.png", size="large")

# --- RUN NAVIGATION ---
pg.run()