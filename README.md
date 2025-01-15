# Industrial Human Resource Geo-Visualization

# Overview

 1. Description: This project analyzes workforce data across various industries and geographies in India. It provides insights into workforce distribution by gender, industry, and state using an interactive dashboard.

 2. Objective: Enable policymakers and businesses to make data-driven decisions by exploring workforce trends and demographics.

# Features

  1. nteractive Dashboard:

     1. Filter by state and industry categories.
     2. Visualize workforce distribution and gender ratios.
        
  2. Visualizations:

       1. Bar and pie charts for industry and demographic insights.
     
  4. Key Metrics:

       1. Gender Ratio, Urban-to-Rural Ratio, and State-wise Trends.

# Technologies Used

  1. Programming Languages & Tools:

     1. Python
     2. Streamlit: For building an interactive dashboard.
     3. Plotly: For creating dynamic visualizations.
     4. Pandas: For data manipulation.
     5. NLTK: For Natural Language Processing to categorize industries.

# Setup Instructions
  1. Clone the Repository:
     
     1. https://github.com/lokesh7787/AI_ML_repo.git
        
  2. Install Dependencies:

     1. pip install -r requirements.txt
  
  3. Run the Application:

     1. streamlit run dashboard.py

  # Dataset Details
  1. Source: Census of India 2011

     
  2. Key Fields:

     1. State_Code
     2. Industry Name
     3. Total_Workers_Total_Persons
     4. Total_Workers_Total_Males
     5. Total_Workers_Total_Females

# Approach

  1. Data Cleaning:
     
     1. Removed null values and standardized column names.
    
     2. Processed text fields with NLP for categorization.

  3. Feature Engineering:
     
     1. Calculated Gender Ratio and Urban-to-Rural Ratio.

  5. Visualization:

     1. Used Plotly for creating interactive and aesthetically pleasing charts.

  7. Dashboard Design:

     1. Designed filters for customized data exploration.

# How to Use the Dashboard

   1. Filters:

      1. Use the sidebar to select specific states or industry categories.

   2. Charts:

      1. Explore bar and pie charts for workforce distribution. 

   3. Data Table:

      1. View the filtered dataset directly in the dashboard.


# Insights from the Project

  1. Top 5 States with Highest Gender Ratios:

     1. Displays states where the workforce gender imbalance is most significant.

  2. Industry Distribution:

     1. Highlights key industries contributing to the workforce by geography.

  3. Emerging vs. Traditional Industries:

     1. Comparison of workforce trends in established and emerging sectors.

# Future Enhancements

 1. Include workforce trends over time.
 2. Add a predictive model for workforce demand in emerging industries.
 3. Incorporate geospatial visualizations using Mapbox.

# Contributors

  1. Name : Lokesh S

  2. Email : lokesh7787@gmail.com

# Screenshots

 1. The Streamlit dashboard.

 2. Visualizations (e.g., charts for gender ratio and industry distribution).

![Screenshot 2025-01-13 at 4 48 12 PM](https://github.com/user-attachments/assets/cb4e3cd4-3a91-41f6-bf7f-6dc1ed6d7eeb)

![Screenshot 2025-01-13 at 4 49 12 PM](https://github.com/user-attachments/assets/9615a46a-c892-4e30-8525-fe656af610ba)

![Screenshot 2025-01-13 at 4 49 40 PM](https://github.com/user-attachments/assets/18c0a1db-859b-4ed6-a334-ae764ddc6f4e)

![Screenshot 2025-01-13 at 4 50 09 PM](https://github.com/user-attachments/assets/caedd4e2-455f-4530-a5ef-cbbdcbd84828)

# Linkedin post video 

 1. https://www.linkedin.com/feed/update/urn:li:activity:7284533926147080192/
