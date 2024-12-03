#YouTube Data Harvesting and Warehousing using SQL and Streamlit
Project Overview
This project focuses on harvesting data from the YouTube Data API, managing and storing it in a SQL database, and visualizing it through an interactive Streamlit web application. It demonstrates the integration of Python scripting with APIs, SQL-based data management, and dashboard development using Streamlit for actionable insights.

#Skills You'll Learn
1 --> Python Scripting: Automate data collection and processing tasks.
2 --> YouTube API Integration: Fetch and handle data like video statistics, channel details, and more.
3 --> Data Management with SQL: Store, query, and manage harvested data in a relational database.
4 --> Streamlit Web App Development: Build an interactive user interface for data visualization and analysis.

#Key Features
1) Data Harvesting:
   . Connect to the YouTube Data API to fetch details about channels, videos, and statistics.
2) Data Warehousing:
   . Store the harvested data in a SQL database for efficient querying and management.
3) Interactive Dashboard:
   . Use Streamlit to build a dashboard for analyzing and visualizing YouTube data.
   . Display metrics like:
     . Average video durations per channel.
     . Most-viewed videos.
     . Year-wise analysis of published videos.
4) Scalable and Modular:
   . Codebase is modular for easy updates and enhancements.

#Domain
Social Media: Leverage insights from YouTube, one of the most popular social media platforms, to understand trends and performance metrics.

Project Structure
 Query.py  # SQL scripts and schema definitions
 README.md # Project description and usage instructions
 Scrap.py  # Utility functions for data processing
 demo_main.ipynb #NoteBook main fetching youTube API Data
 demo_main.py # python verson file
 youtube.py  # Streamlit dashboard for data visualization

 #Getting Started
Prerequisites
Python 3.8 or above
SQL database (e.g., MySQL, SQLite)
API key for the YouTube Data API

#Installation
 1 Clone this repository: git clone https://github.com/yourusername/YouTube-Data-Harvesting.git
   cd YouTube-Data-Harvesting

2 Set up the database:
   Create a SQL database using the provided schema in data/database.sql.
3 Configure your API key:
  Add your YouTube Data API key to the config.json or environment variables.
4 Run the Streamlit app: streamlit run app/streamlit_app.py


#Sample Visualizations
  Here are some example visualizations that the dashboard can generate:

  . Average video durations by channel.
  . Most viewed videos.
  . Trends in video publishing over time.

#Future Enhancements
  Add support for additional YouTube metrics (e.g., comments, likes, shares).
  . Implement machine learning models to predict video performance.
  . Support for other social media platforms.

#Contributing
  Contributions are welcome! If you'd like to contribute to this project, please fork the repository and create a pull request.

#License
 This project is licensed under the MIT License.

 Feel free to customize this content further based on your project specifics!


