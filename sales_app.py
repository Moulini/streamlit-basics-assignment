
# sales_app.py

import streamlit as st
import pandas as pd

# --- Task 1: App Title and Subheader ---
st.title("Sales Dashboard")
st.subheader("Explore sales data by product category")

# --- Task 1: Create a hardcoded DataFrame ---
data = {
    "Product": ["Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories"],
    "Sales": [1500, 2500, 1200, 800, 600]
}

df = pd.DataFrame(data)

# --- Task 2: Sidebar for filtering ---
selected_category = st.sidebar.selectbox(
    "Select Category",
    options=df["Category"].unique()
)

# Filter DataFrame based on selection
filtered_df = df[df["Category"] == selected_category]

# --- Main content: display filtered DataFrame ---
st.dataframe(filtered_df)

# --- Display a line chart of Sales for the selected category ---
st.line_chart(filtered_df["Sales"])