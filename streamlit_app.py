import streamlit as st
from streamlit_extras.stylable_container import stylable_container

# Define pages
home_page = st.Page(
    "views/home.py",
    title="Home",
    icon=":material/home:",
    default=True
)

clv_page = st.Page(
    "views/clv.py",
    title="Customer Lifetime Value",
    icon=":material/calendar_month:"
)

nps_page = st.Page(
    "views/nps.py",
    title="Net Promoter Score",
    icon=":material/mood:"
)

conversion_rate_page = st.Page(
    "views/conversion_rate.py",
    title="Sales Conversion Rate",
    icon=":material/group_add:"
)

churn_rate_page = st.Page(
    "views/churn_rate.py",
    title="Customer Churn Rate",
    icon=":material/percent:"
)

sku_page = st.Page(
    "views/sku.py",
    title="Stock Keeping Unit",
    icon=":material/barcode_scanner:"
)

om_page = st.Page(
    "views/operation_margin.py",
    title="Operation Margin",
    icon=":material/paid:"
)

ep_page = st.Page(
    "views/ep.py",
    title="Employee Productivity",
    icon=":material/monitoring:"
)

# --- Place the search bar above navigation ---
#search_query = st.text_input("Search Concepts")

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Intro": [home_page],
        "Marketing Concepts": [clv_page, churn_rate_page, nps_page, conversion_rate_page],
        "Operation Concepts": [om_page, ep_page],
        "Inventory Concepts": [sku_page],
    }
)

# --- SHARED ON ALL PAGES ---
st.logo("assets/ODG_logo4.png", size="large")

# --- RUN NAVIGATION ---
pg.run()

