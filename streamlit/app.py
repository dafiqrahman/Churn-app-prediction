import streamlit as st
import os
# Custom imports
from multipage import MultiPage
# import your pages here
from pages import individual_pred, batch_pred, home, explore

# st.set_page_config(layout="wide")
# Create an instance of the app
app = MultiPage()

# Title of the main page
st.markdown("<h1 style='text-align: center;'>Churn Prediction Application</h1>",
            unsafe_allow_html=True)

# Add all your applications (pages) here
app.add_page('Home', home.app)
app.add_page('Explore', explore.app)
app.add_page("Individual Prediction", individual_pred.app)
app.add_page("Batch Prediction", batch_pred.app)
# The main app
app.run()
