#!/usr/bin/env python
# coding: utf-8

# In[53]:


import pandas as pd


# In[54]:


prefix = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/'
url = f'{prefix}/yellow_tripdata_2021-01.csv.gz'
url


# In[55]:


df = pd.read_csv(url)


# In[56]:


df.head()


# In[57]:


len(df)


# In[58]:


df


# In[59]:


dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    prefix + 'yellow_tripdata_2021-01.csv.gz',
    dtype=dtype,
    parse_dates=parse_dates
)


# In[60]:


len(df)


# In[61]:


df.head()


# In[62]:


df['tpep_pickup_datetime']


# In[63]:


df


# In[64]:


from sqlalchemy import create_engine
engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')


# In[65]:


df_iter= pd.read_csv(
    url,
    dtype=dtype,
    parse_dates=parse_dates,
    iterator=True,
    chunksize=100000,
)


# In[66]:


df_iter


# In[67]:


#!uv add tqdm


# In[68]:


from tqdm.auto import tqdm


# In[69]:


for df_chunk in tqdm(df_iter):
    df_chunk.to_sql(name='yellow_taxi_data', con=engine,if_exists='append') 


# In[70]:


#df=next(df_iter)


# In[71]:


df


# In[ ]:




