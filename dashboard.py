import streamlit as st
import pandas as pd
import plotly.express as px

from EDA import getFinalDataSet

# Title of the Dashboard
st.title("Industrial Human Resource Geo-Visualization")
st.sidebar.title("Filter Options")


df = getFinalDataSet()
# # Sidebar Filters
# states = st.sidebar.multiselect("Select States", options=df['State_Code'].unique(), default=df['State_Code'].unique())

# # Filtered Data
# filtered_data = df[df['State_Code'].isin(states)]

# # Visualization 1: State-Wise Total Workers
# st.subheader("State-Wise Total Workers")
# statewise_totals = filtered_data.groupby('State_Code')[['Total_Workers_Total_Males', 'Total_Workers_Total_Females', 
# 'Total_Workers_Total_Persons']].sum().reset_index()
# fig1 = px.bar(statewise_totals, x='State_Code', y=['Total_Workers_Total_Males', 'Total_Workers_Total_Females'],
#               title="State-Wise Total Workers by Gender", labels={"value": "Worker Count", "State_Code": "State Code"}, barmode='group')
# st.plotly_chart(fig1)

# # Visualization 2: Gender Ratio Distribution
# st.subheader("Gender Ratio Distribution")
# fig2 = px.box(filtered_data, x='State_Code', y='Gender_Ratio', title="Gender Ratio (Males to Females) by State",
#               labels={"Gender_Ratio": "Gender Ratio", "State_Code": "State Code"})
# st.plotly_chart(fig2)

# # Visualization 3: Urban vs Rural Workers
# st.subheader("Urban vs Rural Worker Distribution")
# urban_rural_totals = filtered_data.groupby('State_Code')[['Total_Urban_Workers', 'Total_Rural_Workers']].sum().reset_index()
# fig3 = px.bar(urban_rural_totals, x='State_Code', y=['Total_Urban_Workers', 'Total_Rural_Workers'],
#               title="Urban vs Rural Worker Distribution by State", labels={"value": "Worker Count", "State_Code": "State Code"}, barmode='group')
# st.plotly_chart(fig3)

# # Data Table
# st.subheader("Filtered Dataset")
# st.dataframe(filtered_data)

# # Sidebar Filters
# states = st.sidebar.multiselect("Select State(s)", options=df['State_Code'].unique(), default=df['State_Code'].unique())
# industries = st.sidebar.multiselect("Select Industry(s)", options=df['NIC_Name'].unique(), default=df['NIC_Name'].unique())

# # Filter Data Based on Sidebar Inputs
# filtered_data = df[(df['State_Code'].isin(states)) & (df['NIC_Name'].isin(industries))]



# high_gender_ratio_states = filtered_data.groupby('State_Code')['Gender_Ratio'].mean().sort_values(ascending=False).head(5)
# st.write("### Top 5 States with Highest Gender Ratio (More Males to Females)")
# st.dataframe(high_gender_ratio_states)



# Sidebar filter for categories
categories = st.sidebar.multiselect("Select Industry Categories", 
                                     options=df['Category'].unique(), 
                                     default=df['Category'].unique())

# Filter data by selected categories
filtered_data = df[df['Category'].isin(categories)]

# Visualization 1: Industry Categories Distribution
with st.expander("Industry Categories Distribution"):
    category_counts = filtered_data['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Count']  # Rename columns
    fig1 = px.bar(category_counts, x='Category', y='Count', 
                title="Industry Categories Distribution",
                labels={'Category': 'Industry Category', 'Count': 'Number of Records'})
    st.plotly_chart(fig1)

# Visualization 2: Worker Distribution by Category
with st.expander("Worker Distribution by Industry Category"):
    category_worker_totals = filtered_data.groupby('Category')[['Total_Workers_Total_Persons']].sum().reset_index()
    fig2 = px.pie(category_worker_totals, names='Category', values='Total_Workers_Total_Persons',
                title="Worker Distribution by Industry Category")
    st.plotly_chart(fig2)

#State-Wise Total Workers by Gender
with st.expander("State-Wise Total Workers by Gender"):
    statewise_totals = filtered_data.groupby('State_Code')[['Total_Workers_Total_Males', 'Total_Workers_Total_Females', 'Total_Workers']].sum().reset_index()
    fig3 = px.bar(statewise_totals, x='State_Code', y=['Total_Workers_Total_Males', 'Total_Workers_Total_Females'],
                title="State-Wise Worker Population by Gender", barmode='group', labels={"value": "Worker Count", "State_Code": "State"})
    st.plotly_chart(fig3)

#Industry-Wise Worker Distribution
with st.expander("Industry-Wise Worker Distribution"):
    industrywise_totals = filtered_data.groupby('NIC_Name')[['Total_Workers_Total_Males', 'Total_Workers_Total_Females', 'Total_Workers']].sum().reset_index()
    fig4 = px.bar(industrywise_totals, x='NIC_Name', y='Total_Workers', title="Total Workers by Industry", 
                labels={"Total_Workers": "Worker Count", "Industry": "Industry"}, text='Total_Workers')
    st.plotly_chart(fig4)

#Gender Ratio Distribution Across States
with st.expander("Gender Ratio Distribution Across States"):
    fig5 = px.box(filtered_data, x='State_Code', y='Gender_Ratio', title="Gender Ratio (Males to Females) by State",
                labels={"Gender_Ratio": "Gender Ratio", "State_Code": "State"})
    st.plotly_chart(fig5)

#Urban vs Rural Workers
with st.expander("Urban vs Rural Workers"):
    urban_rural_totals = filtered_data.groupby('State_Code')[['Main_Workers___Urban____Persons', 'Main_Workers___Rural____Persons']].sum().reset_index()
    fig6 = px.bar(urban_rural_totals, x='State_Code', y=['Main_Workers___Urban____Persons', 'Main_Workers___Rural____Persons'],
                title="Urban vs Rural Workers by State", barmode='group', labels={"value": "Worker Count", "State_Code": "State"})
    st.plotly_chart(fig6)

# Facts and Insights Section
with st.expander("Facts and Insights"):
    top_states = statewise_totals.sort_values(by='Total_Workers', ascending=False).head(5)
    st.write("### Top 5 States with Highest Worker Population")
    st.dataframe(top_states)

#State wise main and marginal workers
with st.expander("State wise main and marginal workers"):
    statewise_TotalWorkers = filtered_data.groupby('State_Code')[['Main_Workers___Total____Persons','Marginal_Workers___Total____Persons']].sum().reset_index()
    fig7 = px.bar(statewise_TotalWorkers, x='State_Code' , y = ['Main_Workers___Total____Persons','Marginal_Workers___Total____Persons'], title="Main vs Marginal workers by State", barmode='group',labels={"value": "Total Worker Count", "State_Code": "State"},)
    st.plotly_chart(fig7)

#Top 5 States with Highest Gender Ratio (More Males to Females
with st.expander("Top 5 States with Highest Gender Ratio (More Males to Females"):
    high_gender_ratio_states = filtered_data.groupby('State_Code')['Gender_Ratio'].mean().sort_values(ascending=False).head(5)
    st.write("### Top 5 States with Highest Gender Ratio (More Males to Females)")
    st.dataframe(high_gender_ratio_states)

#Show raw data (optional)
st.subheader("Filtered Dataset")
st.dataframe(filtered_data)