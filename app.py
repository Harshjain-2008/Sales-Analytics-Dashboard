import streamlit as st
import sales_dashboard as sd

df = sd.load_data()

st.title("📊 SALES ANALYTICS DASHBOARD")

# KPIs
st.subheader("Total Revenue")
st.write(sd.total_revenue(df))

st.subheader("Total Profit")
st.write(sd.total_profit(df))

# Dataset
if st.button("Show Dataset"):
    st.dataframe(df)

# Charts representation
st.subheader("Best Selling Products")
st.bar_chart(sd.best_selling(df))

st.subheader("Revenue by Product")
st.bar_chart(sd.revenue_by_product(df))

st.subheader("Monthly Sales")
st.bar_chart(sd.monthly_sales(df))

st.subheader("City Wise Sales")
st.bar_chart(sd.city_sales(df))

st.subheader("Category Profit")
st.bar_chart(sd.category_profit(df))

st.subheader("Top Customers")
st.bar_chart(sd.top_customers(df))

# Search Product 
product = st.text_input("Search Product")

if product:
    st.dataframe(sd.search_product(df, product))

# Filter Month
month = st.selectbox("Select Month", df['Month'].unique())

st.dataframe(sd.filter_month(df, month))