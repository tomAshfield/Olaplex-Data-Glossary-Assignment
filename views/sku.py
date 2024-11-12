import streamlit as st

st.title("Stock Keeping Unit (SKU)")
st.divider()
st.write("""
**:green[Definition:]** A Stock Keeping Unit (SKU) is a 
unique identifier for a product or service that's used in 
inventory management and retail.

**:blue[Business Relevance:]** A SKU is a unique 
alphanumeric code that's assigned to a product or service 
to track it in inventory. SKUs are important for managing 
inventory, supply chain, and customer experience.

**:red[Example:]**
""")

st.image("./assets/sku_example.png")

st.divider()
st.write("""
**:violet[Interpretation]**
- **Efficient Inventory Management**: By using SKUs, a company can track each item accurately, 
  allowing for efficient stock management, reducing overstock and understock situations.
- **Enhanced Customer Experience**: SKUs enable quicker and more accurate order processing 
  and tracking, which contributes to a smoother customer experience.
- **Sales and Analytics Insights**: SKUs allow companies to analyze sales trends, 
  identify popular items, and make data-driven decisions for inventory and marketing strategies.
- **Improved Supply Chain Coordination**: SKUs help streamline the supply chain 
  by ensuring that all parties (suppliers, warehouses, and stores) use a unified tracking method.
""")
