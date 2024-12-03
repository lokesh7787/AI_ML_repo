#!/usr/bin/env python
# coding: utf-8

# In[11]:


import googleapiclient.discovery
from Scrap import addNewDataChannelTable
from Scrap import addNewDataCommentTable
from datetime import datetime
from Scrap import addNewDataVideoTable


# In[12]:


api_service_name = "youtube"
api_version = "v3"


# In[ ]:


api_key = "Your API Key Data"


# In[14]:


youtube = googleapiclient.discovery.build(
api_service_name, api_version, developerKey=api_key)


# In[15]:


def handleDateTimeFormate(time_str):
    try:
        time_obj = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%S.%fZ')
    except ValueError:
        # Fallback to parsing without microseconds
        time_obj = datetime.strptime(time_str, '%Y-%m-%dT%H:%M:%SZ')
    return time_obj


# In[16]:


def getCommentsListData(video_id):
    comments_response = youtube.commentThreads().list(
        part="snippet,replies",
        videoId=video_id
    )
    comments_response = comments_response.execute()
    comment_information={}
    for comment in comments_response['items']:
        comment_information = {
               "Comment_Id": comment['snippet']['topLevelComment']['id'],
               "Comment_Text": comment['snippet']['topLevelComment']['snippet']['textDisplay'],
               "Comment_Author": comment['snippet']['topLevelComment']['snippet']['authorDisplayName'],
               "Comment_PublishedAt": handleDateTimeFormate(comment['snippet']['topLevelComment']['snippet']['publishedAt']), 
               "Channel_id":comment['snippet']['channelId'],
               "video_id":comment['snippet']['videoId']
               }
        addNewDataCommentTable(comment_information)


# In[17]:


def getPlayListData(playlist_id):
    playlist_videos = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id
    )
    playlist_videos = playlist_videos.execute()
    for item in playlist_videos['items']:
        video_id = item['snippet']['resourceId']['videoId']
        video_response = youtube.videos().list(
            part='snippet,statistics,contentDetails',
            id=video_id
            ).execute()
        if video_response['items']:
            video_info=  {
                "Video_Id": video_id,
                "Video_Name": video_response['items'][0]['snippet']['title'] if 'title' in video_response['items'][0]['snippet'] else "Not Available",
                "Video_Description": video_response['items'][0]['snippet']['description'],
                'Channel_id':video_response['items'][0]['snippet']['channelId'],
                'commentCount':video_response['items'][0]['statistics']['commentCount'],
                "view_Count":video_response['items'][0]['statistics']['viewCount'],
                "like_count":video_response['items'][0]['statistics']['likeCount'],
                "dis_like_Count":video_response['items'][0]['statistics']['dislikeCount'] if 'dislikeCount' in video_response['items'][0]['statistics'] else "0" ,
                "durations":video_response['items'][0]['contentDetails']['duration'],
                "published_date":handleDateTimeFormate(video_response['items'][0]['snippet']['publishedAt'])
                }
            addNewDataVideoTable(video_info)
            getCommentsListData(video_info['Video_Id'])
            


# In[18]:


def channelInformationwithThumbnail(channel_id):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id= channel_id
    )
    response = request.execute()
    
    return{
        'channel_id':response['items'][0]['id'],
        'channel_name':response['items'][0]['snippet']['title'],
        'channel_description' : response['items'][0]['snippet']['description'],
        'channel_publishedAt': handleDateTimeFormate(response['items'][0]['snippet']['publishedAt']),
        'playlists_id' : response['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
        'channel_sub_count': response['items'][0]['statistics']['subscriberCount'],
        'channel_viewCount':response['items'][0]['statistics']['viewCount'] ,
        'channel_videoCount':response['items'][0]['statistics']['videoCount'],
        'thumbnails': response['items'][0]['snippet']['thumbnails']
        } 

def channelInformation(channel_id):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id= channel_id
    )
    response = request.execute()
    
    channelInfo = {
        'channel_id':response['items'][0]['id'],
        'channel_name':response['items'][0]['snippet']['title'],
        'channel_description' : response['items'][0]['snippet']['description'],
        'channel_publishedAt': handleDateTimeFormate(response['items'][0]['snippet']['publishedAt']),
        'playlists_id' : response['items'][0]['contentDetails']['relatedPlaylists']['uploads'],
        'channel_sub_count': response['items'][0]['statistics']['subscriberCount'],
        'channel_viewCount':response['items'][0]['statistics']['viewCount'] ,
        'channel_videoCount':response['items'][0]['statistics']['videoCount']
        }
    addNewDataChannelTable(channelInfo)
    getPlayListData(channelInfo['playlists_id'])


# In[ ]:



    


# In[19]:


#UC4M6aYfOcZBZHoBaNtYXpYA - Tech with Arul
#UC_x5XG1OV2P6uZZ5FSM9Ttw - Google for Developers
#UCos_WjZSSpb2YH9M3YLoVug - chill and grow
#UC-hisIZlnsImYe7Y5M4qVFA - Hope AI
#UC2YVnH6aMky1SMdmlo5S9-A - majaa matrix
#UC-NLi5VEcehN-h589hdw-wA - because
#UCma2b1uVLajAq9nHSEJh9HQ - shriram vasudevan
#UC-tWbnw1b6Y5Wbo0145-0nQ - future scientist
#UC_Xt2fhRqHpv3wdRH88FXHA - Mls media creation
#UCciec0jLXOATJAp2UfLRREg - yohavinthedal



# In[ ]:





# In[20]:


def setDbValues(channelId):
    channelInformation(channelId)
        
    

