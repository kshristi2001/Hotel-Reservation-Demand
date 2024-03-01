#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[2]:


#Load the data
df = pd.read_csv('hotel_bookings.csv')
df.head(10)


# In[3]:


# Strips leading and trailing whitespace from all string values in the dataframe
df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)


# In[4]:


#Display information about the dataframe df
df.info()


# In[5]:


# Retrieve the dimensions (number of rows and columns) of the dataframe 'df'
df.shape


# In[6]:


# Provide summary statistics for columns in the dataframe 'df'
df.describe()


# In[7]:


# Count the number of missing values (NaN) in each column of the dataframe
df.isnull().sum()


# In[8]:


# Remove the columns with high null values.
df.drop(['company','agent'],axis = 1, inplace = True)


# In[9]:


#dropping all the null values
df.dropna(inplace = True)


# In[10]:


import pandas as pd
df.to_csv('preprocessed_data.csv', index=False)


# In[11]:


# Select only rows where the value in the 'adr' column is less than 5000
df = df[df['adr']<5000]


# In[12]:


# Create a bar plot showing the count of canceled and not canceled reservations
cancelled_perc = df['is_canceled'].value_counts(normalize = True)
print(cancelled_perc)

plt.figure(figsize = (5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','canceled'],df['is_canceled'].value_counts(), edgecolor = 'k',width = 0.7)
plt.show()


# In[13]:


# Create a count plot to visualize reservation status (canceled/not canceled) in different hotels.
plt.figure(figsize=(8, 4))
ax1 = sns.countplot(x='hotel', hue='is_canceled', data=df, palette='Blues')
legend_labels, _ = ax1.get_legend_handles_labels()
plt.title('Reservation status in different hotels', size=20)
plt.xlabel('Hotel')
plt.ylabel('Number of reservations')
plt.show()


# In[14]:


#calculate the percentage of canceled and not canceled reservations in the city hotel.
city_hotel = df[df['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[15]:


#calculate the percentage of canceled and not canceled reservations in the Resort hotel.
resort_hotel = df[df['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[16]:


# Plot the average daily rate over time for both resort and city hotels.
plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Resort Hotel', fontsize = 30)
plt.plot(resort_hotel.index,resort_hotel['adr'], label = 'Resort Hotel')
plt.plot(city_hotel.index,city_hotel['adr'], label = 'City Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[17]:


# Create a heatmap to visualize the correlation matrix between different features in the DataFrame.
plt.figure(figsize=(15,10))
cor_matrix=df.corr()
sns.heatmap(cor_matrix,annot=True)


# In[18]:


# Plot the average daily rate (ADR) per month for canceled reservations.
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])
df['month'] =df['reservation_status_date'].dt.month
plt.figure(figsize=(15, 8))
plt.title('ADR per month', fontsize=30)
sns.barplot(x='month', y='adr', data=df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())
plt.legend(fontsize=20)
plt.show()


# In[19]:


# Plot the count of reservations per month, distinguishing between canceled and not canceled reservations.
plt.figure(figsize = (16,8))
ax1 = sns.countplot(x = 'month',hue = 'is_canceled',data = df,palette = 'bright')
legend_labels,_ = ax1. get_legend_handles_labels()
plt.title('Reservation status per month',size = 20)
plt.xlabel('month')
plt.ylabel('number of reservations')
plt.legend(['not canceled','canceled'])
plt.show()


# In[20]:


# Plot a pie chart to visualize the distribution of canceled reservations among the top 10 countries.
cancelled_data = df[df['is_canceled'] == 1]
top_10_country = cancelled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 countries with reservation canceled')
plt.pie(top_10_country,autopct = '%.2f',labels = top_10_country.index)
plt.show()


# In[ ]:




