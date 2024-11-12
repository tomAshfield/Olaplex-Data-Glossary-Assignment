import streamlit as st

# Title and Introduction
#st.title("OLAPLEX Data Glossary")
st.image("./assets/ODG_logo4.png")
st.divider()
st.subheader("An Interactive Business Glossary for Non-Technical Stakeholders")

# Project Overview
st.write("""
Welcome to the OLAPLEX Data Glossary! An interactive web app that is designed to provide clear, accessible explanations of key business and technical terms, making it easy for team members across departments to understand and work with data-related concepts.

### Project Overview
This prototype glossary offers a user-friendly, searchable interface that distinguishes between business definitions and relevant technical details, ensuring clarity for both technical and non-technical stakeholders.

**Goals of the Project:**
- **:green[Accessibility:]** Make data-related terms and metrics easily understandable for non-technical users.
- **:blue[Clarity:]** Provide clear business definitions with optional technical details for deeper understanding.
- **:red[Scalability:]** Lay the groundwork for a resource that can grow with OLAPLEX's evolving data needs.

### Future Vision
For future iterations, I envision a fully scalable version with expanded content, seamless integration into OLAPLEX’s Snowflake environment, and advanced filtering and navigation options to further enhance user experience.

Thank you for exploring this prototype. I look forward to your feedback!
""")

# Instructions for Use
st.write("### Instructions")
st.write("""
- Use the navigation bar to find specific terms or metrics.
- Click on a term to view its full definition, including any associated technical details.
- Reach out to the designated expert if you have further questions about a term.
""")

# Footer
st.write("---")
st.write("**Developed by:** Thomas Ashfield")
st.write("For questions about this demo, please contact me at [tashfield715@gmail.com](mailto:tashfield715@gmail.com)")
