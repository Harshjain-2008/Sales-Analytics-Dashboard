import pandas as pd

def load_data():
    df = pd.read_csv("sales_data2.csv")

    df['Date'] = pd.to_datetime(df['Date'])

    df['Revenue'] = df['Quantity'] * df['Price']                # Total Revenue

    df['Total_cost'] = df['Quantity'] * df['Cost_Price']        # Total cost

    df['Profit'] = df['Revenue'] - df['Total_cost']             # Total Profit

    df['Profit_%'] = (df['Profit'] / df['Revenue']) * 100       # Profit percentage

    df['Month'] = df['Date'].dt.month_name()                    # Month name based on sales 

    return df

# DASHBOARD MAIN CODE 

# REVENUE 
def total_revenue(df):
    return df['Revenue'].sum()

# PROFIT 
def total_profit(df):
    return df['Profit'].sum()

# BEST PRODUCT 
def best_selling(df):
    return df.groupby('Product')['Quantity'].sum().sort_values(ascending=False)

# PRODUCT REVENUE 
def revenue_by_product(df):
    return df.groupby('Product')['Revenue'].sum()

# MONTHLY SALES 
def monthly_sales(df):
    return df.groupby('Month')['Revenue'].sum()

# SALES IN CITIES
def city_sales(df):
    return df.groupby('City')['Revenue'].sum()

# PROFIT BASED ON CATEGORY 
def category_profit(df):
    return df.groupby('Category')['Profit'].sum()

# TOP CUSTOMER 
def top_customers(df):
    return df.groupby('Customer')['Revenue'].sum().sort_values(ascending=False)

# SEARCH PRODUCT 
def search_product(df, product):
    return df[df['Product'].str.lower() == product.lower()]

# MONTH 
def filter_month(df, month):
    return df[df['Month'].str.lower() == month.lower()]