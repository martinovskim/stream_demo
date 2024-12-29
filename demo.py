import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("ireland_data.csv")

# Sidebar filters
st.sidebar.title("Filters")
year_filter = st.sidebar.selectbox("Select Year:", sorted(data['Year'].unique()))
category_filter = st.sidebar.selectbox("Select Category:", data['Category'].unique())

# Filter data based on sidebar selections
filtered_data = data[(data['Year'] == year_filter) & (data['Category'] == category_filter)]

# Line chart: Time Trends
st.header("Price Trends Over Time")
fig, ax = plt.subplots()
filtered_data.groupby('Week Number')['Price'].mean().plot(ax=ax)
ax.set_title(f"Weekly Price Trends ({category_filter}, {year_filter})")
st.pyplot(fig)

# Bar chart: Category Comparison
st.header("Average Prices by Category")
avg_prices = data.groupby('Category')['Price'].mean()
st.bar_chart(avg_prices)

# Display raw data
st.header("Filtered Data")
st.dataframe(filtered_data)