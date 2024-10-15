import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

# Load your data
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)

st.title("Data App Assignment, on Oct 7th")

st.write("### Select Category and Sub-Category")

# Dropdown to select Category
category = st.selectbox('Select a Category', df['Category'].unique())

# Filter the subcategories based on the selected category
sub_categories = df[df['Category'] == category]['Sub_Category'].unique()

# Multi-select to allow the user to pick specific subcategories (e.g., Chairs and Tables)
selected_sub_categories = st.multiselect(f"Select Sub-Categories in {category}", sub_categories)

# Display the selected category and subcategories
st.write(f"Selected Category: {category}")
st.write(f"Selected Sub-Categories: {selected_sub_categories}")

# Filter the dataframe based on the selected subcategories
filtered_df = df[(df['Category'] == category) & (df['Sub_Category'].isin(selected_sub_categories))]

# Display the filtered data
st.dataframe(filtered_df)

# Optional: Show a line chart of sales for the selected subcategories
if not filtered_df.empty:
    sales_chart = filtered_df.groupby('Order_Date')['Sales'].sum().reset_index()
    st.line_chart(sales_chart, x='Order_Date', y='Sales')

# Calculate metrics based on filtered data
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
overall_profit_margin = total_profit / total_sales * 100 if total_sales > 0 else 0

# Display metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Overall Profit Margin", f"{overall_profit_margin:.2f}%")

