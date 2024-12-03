import streamlit as st
from Scrap import getQueryBasedOnQuestion
from demo_main import channelInformationwithThumbnail, setDbValues
import pandas as pd

tab1, tab2 = st.tabs(["Youtube", "Questions"])
questions = [
    'What are the names of all the videos and their corresponding channels?',
    'Which channels have the most number of videos, and how many videos do they have?',
    'What are the top 10 most viewed videos and their respective channels?',
    'How many comments were made on each video, and what are their corresponding video names?',
    'Which videos have the highest number of likes, and what are their  corresponding channel names?',
    'What is the total number of likes and dislikes for each video, and what are their corresponding video names?',
    'What is the total number of views for each channel, and what are their corresponding channel names?',
    'What are the names of all the channels that have published videos in the year 2022?',
    'What is the average duration of all videos in each channel, and what are their corresponding channel names?',
    'Which videos have the highest number of comments, and what are their corresponding channel names?'
]
def callOnClick(channelId):
    if channelId:
        setDbValues(channelId)

def getChanelData(channelId):
    if(channelId):
        response = channelInformationwithThumbnail(channelId)
        if(response):
            expander = st.expander("See channel details")
            expander.image(response['thumbnails']['medium']['url'])
            expander.write(f'''
                channel Name:- {response['channel_name']}  
                description:- {response['channel_description']}
                Subscribe count {response['channel_sub_count']}           
            ''')
        callOnClick(channelId)
        
def getQueryData(option):
    return getQueryBasedOnQuestion(questions.index(option))
    


with tab1:
    st.header("Youtube Details")
    with st.form("my_form"):
        channelId = st.text_input('Enter Channel Id:-')
        if len(channelId) > 0:
            getChanelData(channelId)
        st.form_submit_button('Scrap')

        
with tab2:
    st.header("Questions And Answer Details")
    option = st.selectbox('Pick a questions', questions)
    if option:
        data = getQueryData(option)
        if data:
            df = pd.DataFrame(data['rows'], columns=data["columns"])
            st.table(df)

    




