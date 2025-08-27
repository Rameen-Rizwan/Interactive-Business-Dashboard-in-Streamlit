import streamlit as st
import pandas as pd
import plotly.express as px

# ===============================
# Load Dataset
# ===============================
df = pd.read_csv("C:/Users/luqma/Downloads/archive/superstore.csv")

# ===============================
# Sidebar Filters
# ===============================
st.sidebar.header("📌 Filters")

market = st.sidebar.multiselect(
    "Select Market:",
    options=df["Market"].unique(),
    default=df["Market"].unique()
)

category = st.sidebar.multiselect(
    "Select Category:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

sub_category = st.sidebar.multiselect(
    "Select Sub-Category:",
    options=df["Sub.Category"].unique(),
    default=df["Sub.Category"].unique()
)

# Apply Filters
df_selection = df.query(
    "Market == @market & Category == @category & `Sub.Category` == @sub_category"
)

# ===============================
# KPIs
# ===============================
total_sales = int(df_selection["Sales"].sum())
total_profit = int(df_selection["Profit"].sum()) if "Profit" in df_selection.columns else 0

# ===============================
# Custom CSS
# ===============================
st.markdown(
    """
    <style>
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Custom KPI Card Style */
    .card {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    .metric-label {
        font-size: 18px;
        font-weight: bold;
        color: #FF4B4B;
    }
    .metric-value {
        font-size: 28px;
        font-weight: bold;
        color: #FAFAFA;
    }
    </style>
    """, unsafe_allow_html=True
)

# ===============================
# Dashboard Title
# ===============================
st.title("📊 Global Superstore Dashboard")

# KPI Cards
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        f"""
        <div class="card">
            <div class="metric-label">Total Sales</div>
            <div class="metric-value">${total_sales:,}</div>
        </div>
        """, unsafe_allow_html=True
    )
with col2:
    st.markdown(
        f"""
        <div class="card">
            <div class="metric-label">Total Profit</div>
            <div class="metric-value">${total_profit:,}</div>
        </div>
        """, unsafe_allow_html=True
    )

st.markdown("---")

# ===============================
# Tabs
# ===============================
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Sales Trend", "👥 Customers"])

# Tab 1 - Overview
with tab1:
    sales_by_category = (
        df_selection.groupby("Category")[["Sales"]].sum().reset_index()
    )
    fig_category = px.bar(
        sales_by_category,
        x="Category",
        y="Sales",
        title="Sales by Category",
        color="Category"
    )
    st.plotly_chart(fig_category, use_container_width=True)

    if "Profit" in df_selection.columns:
        profit_by_market = (
            df_selection.groupby("Market")[["Profit"]].sum().reset_index()
        )
        fig_profit = px.pie(
            profit_by_market,
            names="Market",
            values="Profit",
            title="Profit Distribution by Market"
        )
        st.plotly_chart(fig_profit, use_container_width=True)

# Tab 2 - Sales Trend
with tab2:
    sales_trend = (
        df_selection.groupby("Order.Date")[["Sales"]].sum().reset_index()
    )
    fig_trend = px.line(
        sales_trend,
        x="Order.Date",
        y="Sales",
        title="Sales Trend Over Time",
        markers=True
    )
    st.plotly_chart(fig_trend, use_container_width=True)

# Tab 3 - Customer Insights
with tab3:
    top_customers = (
        df_selection.groupby("Customer.Name")[["Sales"]].sum().reset_index()
        .sort_values(by="Sales", ascending=False).head(5)
    )
    fig_customers = px.bar(
        top_customers,
        x="Customer.Name",
        y="Sales",
        title="Top 5 Customers by Sales",
        color="Sales"
    )
    st.plotly_chart(fig_customers, use_container_width=True)
