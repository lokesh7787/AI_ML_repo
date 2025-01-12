#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import re
import numpy as np


# In[2]:


df1 = pd.read_csv('DDW_B18_0800_NIC_FINAL_STATE_RAJASTHAN-2011.csv',encoding='ISO-8859-1')
df2 = pd.read_csv('DDW_B18_1200_NIC_FINAL_STATE_ARUNACHAL_PRADESH-2011.csv',encoding='ISO-8859-1')
df3 = pd.read_csv('DDW_B18_1400_NIC_FINAL_STATE_MANIPUR-2011.csv',encoding='ISO-8859-1')
df4 = pd.read_csv('DDW_B18_1500_NIC_FINAL_STATE_MIZORAM-2011.csv',encoding='ISO-8859-1')
df5 = pd.read_csv('DDW_B18_1900_NIC_FINAL_STATE_WEST_BENGAL-2011.csv',encoding='ISO-8859-1')
df6 = pd.read_csv('DDW_B18sc_0700_NIC_FINAL_STATE_NCT_OF_DELHI-2011.csv',encoding='ISO-8859-1')
df7 = pd.read_csv('DDW_B18sc_1600_NIC_FINAL_STATE_TRIPURA-2011.csv',encoding='ISO-8859-1')
df8 = pd.read_csv('DDW_B18sc_2000_NIC_FINAL_STATE_JHARKHAND-2011.csv',encoding='ISO-8859-1')
df9 = pd.read_csv('DDW_B18sc_2400_NIC_FINAL_STATE_GUJARAT-2011.csv',encoding='ISO-8859-1')
df10 = pd.read_csv('DDW_B18sc_2700_NIC_FINAL_STATE_MAHARASHTRA-2011.csv',encoding='ISO-8859-1')
df11 = pd.read_csv('DDW_B18sc_2900_NIC_FINAL_STATE_KARNATAKA-2011.csv',encoding='ISO-8859-1')
df12 = pd.read_csv('DDW_B18sc_3000_NIC_FINAL_STATE_GOA-2011.csv',encoding='ISO-8859-1')
df13 = pd.read_csv('DDW_B18sc_3200_NIC_FINAL_STATE_KERALA-2011.csv',encoding='ISO-8859-1')
df14 = pd.read_csv('DDW_B18sc_3300_NIC_FINAL_STATE_TAMIL_NADU-2011.csv',encoding='ISO-8859-1')
df15 = pd.read_csv('DDW_B18sc_3400_NIC_FINAL_STATE_PUDUCHERRY-2011.csv',encoding='ISO-8859-1')
df16 = pd.read_csv('DDW_B18st_0200_NIC_FINAL_STATE_HIMACHAL_PRADESH-2011.csv',encoding='ISO-8859-1')
df17 = pd.read_csv('DDW_B18st_0500_NIC_FINAL_STATE_UTTARAKHAND-2011.csv',encoding='ISO-8859-1')
df18 = pd.read_csv('DDW_B18st_0900_NIC_FINAL_STATE_UTTAR_PRADESH-2011.csv',encoding='ISO-8859-1')
df19 = pd.read_csv('DDW_B18st_1000_NIC_FINAL_STATE_BIHAR-2011.csv',encoding='ISO-8859-1')
df20 = pd.read_csv('DDW_B18st_1100_NIC_FINAL_STATE_SIKKIM-2011.csv',encoding='ISO-8859-1')
df21 = pd.read_csv('DDW_B18st_1300_NIC_FINAL_STATE_NAGALAND-2011.csv',encoding='ISO-8859-1')
df22 = pd.read_csv('DDW_B18st_1800_NIC_FINAL_STATE_ASSAM-2011.csv',encoding='ISO-8859-1')
df23 = pd.read_csv('DDW_B18st_2100_NIC_FINAL_STATE_ODISHA-2011.csv',encoding='ISO-8859-1')


# In[3]:


df1.head()


# In[4]:


#All dataset into single dataset
mergedData = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11,df12,df13,df14,df15,df16,df16,df17,df18,df19,df20,df21,df22,df23])


# In[5]:


#checking  null values
mergedData.info()


# In[6]:


# Rename columns to clean names
mergedData.columns = mergedData.columns.str.strip()               # Remove leading/trailing spaces
mergedData.columns = mergedData.columns.str.replace(' ', '_')     # Replace spaces with underscores
mergedData.columns = mergedData.columns.str.replace('-', '_')     # Replace dashes with underscores
mergedData.columns = mergedData.columns.str.replace('/', '_')     # Replace slashes with underscores
mergedData.columns = mergedData.columns.str.replace('`', '')      # Remove backticks
mergedData.rename(columns={'India_States':'States'},inplace=True) # Rename column name India/States to States



# In[7]:


# List of columns to clean
columns_to_clean = ['State_Code', 'District_Code', 'Division', 'Group', 'Class']

# Remove backticks (`) from the specified columns
for col in columns_to_clean:
    mergedData[col] = mergedData[col].astype(str).str.replace('`', '', regex=False)


# In[8]:


#feature engineer

#Add columns for Total Workers (Main + Marginal) at different levels
mergedData['Total_Workers_Total_Persons'] = mergedData['Main_Workers___Total____Persons'] + mergedData['Marginal_Workers___Total____Persons']

#calculating gender wise total workers
mergedData['Total_Workers_Rural_Males'] = mergedData['Main_Workers___Rural___Males'] + mergedData['Marginal_Workers___Rural___Males']
mergedData['Total_Workers_Rural_Females'] = mergedData['Main_Workers___Rural___Females'] + mergedData['Marginal_Workers___Rural___Females']
mergedData['Total_Workers_Urban_Males'] = mergedData['Main_Workers___Urban___Males'] + mergedData['Marginal_Workers___Urban___Males']
mergedData['Total_Workers_Urban_Females'] = mergedData['Main_Workers___Urban___Females'] + mergedData['Marginal_Workers___Urban___Females']
mergedData['Total_Workers_Total_Males'] = mergedData['Total_Workers_Rural_Males'] + mergedData['Total_Workers_Urban_Males']
mergedData['Total_Workers_Total_Females'] = mergedData['Total_Workers_Rural_Females'] + mergedData['Total_Workers_Urban_Females']
mergedData['Total_Workers'] = mergedData['Total_Workers_Total_Males'] + mergedData['Total_Workers_Total_Females']

#Radio 
mergedData['Total_Urban_Workers'] = (mergedData['Main_Workers___Urban____Persons'] + mergedData['Marginal_Workers___Urban____Persons'])
mergedData['Total_Rural_Workers'] = (mergedData['Main_Workers___Rural____Persons'] + mergedData['Marginal_Workers___Rural____Persons'])
mergedData['Urban_Rural_Ratio'] = mergedData['Total_Urban_Workers'] / mergedData['Total_Rural_Workers']

# Handle infinite or missing values in Gender_Ratio
mergedData['Gender_Ratio'] = np.where(
    mergedData['Total_Workers_Total_Females'] == 0,
    np.nan,  # Assign NaN where division by zero occurs
    mergedData['Total_Workers_Total_Males'] / mergedData['Total_Workers_Total_Females']
)

# Replace NaN or inf values
mergedData['Gender_Ratio'].replace([np.inf, -np.inf], np.nan, inplace=True)
mergedData['Gender_Ratio'].fillna(0, inplace=True)  # Replace NaN with 0 (or another value)
    

# Keyword-based categorization
def categorize_industry(industry):
    if any(keyword in industry for keyword in ['retail', 'trade', 'shop']):
        return 'Retail'
    elif any(keyword in industry for keyword in ['poultry', 'farming', 'agriculture']):
        return 'Agriculture'
    elif any(keyword in industry for keyword in ['manufacture', 'factory', 'production']):
        return 'Manufacturing'
    else:
        return 'Other'
    


# In[9]:


#NLP

#clean and tokenize the text
mergedData['Cleaned_NIC_Name'] = mergedData['NIC_Name'].str.lower().apply(
        lambda x: re.sub(r'[^a-z\s]', '', str(x)))
    

# Create the stopwords set
stop_words = set(stopwords.words('english'))

# Apply tokenization and remove stopwords
mergedData['Tokens'] = mergedData['Cleaned_NIC_Name'].apply(
    lambda x: [word for word in word_tokenize(x) if word not in stop_words]
)

mergedData['Category'] = mergedData['Cleaned_NIC_Name'].apply(categorize_industry)

def getFinalDataSet():
    return mergedData


# In[10]:


#checking after replace space and backticks
mergedData.head(100)


# In[11]:


mergedData.to_csv('final_data.csv', index=False)

