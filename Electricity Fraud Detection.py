#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


import warnings
warnings.filterwarnings("ignore")


# In[3]:


client_train=pd.read_csv("client_train.csv")
invoice_train=pd.read_csv("invoice_train.csv")
client_test=pd.read_csv("client_test.csv")
invoice_test=pd.read_csv("invoice_test.csv")


# In[4]:


client_train


# In[5]:


invoice_train


# In[6]:


df=pd.merge(invoice_train,client_train, on="client_id")
df
df1=pd.merge(invoice_test,client_test, on="client_id")


# In[7]:


df.shape


# In[8]:


df.size


# In[9]:


df.info()


# In[10]:


df.describe()


# In[11]:


corr=df.corr()
fig, ax=plt.subplots(figsize=(14,6))
sns.heatmap(corr, annot=True)
plt.show()


# In[12]:


from sklearn.metrics import mean_squared_error, accuracy_score, roc_auc_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
import lightgbm as lgb


# In[13]:


df.columns


# In[14]:


import xgboost as xgb


# In[15]:


df.head()


# In[16]:


X = df.drop(['client_id', 'invoice_date', 'target', 'counter_statue', 'counter_type', 'creation_date'], axis=1) 
y = df['target']


# In[17]:


object_columns = df.select_dtypes(include='object').columns
object_columns
df[object_columns]=df[object_columns].astype('category')


# In[18]:


df.info()


# In[19]:


model=xgb.XGBClassifier()
model.fit(X,y)


# In[20]:


#perform feature score
importance_scores = model.feature_importances_


# In[21]:


feature_names = X.columns
df_importances = pd.DataFrame({'Feature': feature_names, 'Importance': importance_scores})
df_importances = df_importances.sort_values(by='Importance', ascending=False)


# In[22]:


plt.barh(df_importances['Feature'], df_importances['Importance'])
plt.xlabel('Importance Score')
plt.ylabel('Features')
plt.title('Feature Importances')
plt.show()


# In[23]:


X = df.drop(['client_id', 'invoice_date', 'target', 'counter_statue', 'counter_type', 'creation_date', 'counter_coefficient', 'consommation_level_3', 'reading_remarque'], axis=1) 
y = df['target']


# In[24]:


train_dataset = lgb.Dataset(X, label=y)


# In[25]:


# Define the parameters for the LightGBM model
params = {
    'objective': 'binary',
    'metric': 'auc',
    'boosting_type': 'gbdt',
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9,
    'bagging_fraction': 0.8,
    'bagging_freq': 5,
    'verbose': 0
}


# In[26]:


# Train the LightGBM model
model = lgb.train(params, train_dataset, num_boost_round=100)


# In[28]:


X_test = df1.drop(['client_id', 'invoice_date', 'counter_statue', 'counter_type', 'creation_date', 'counter_coefficient', 'consommation_level_3', 'reading_remarque'], axis=1)


# In[29]:


# Make predictions on the test data
test_predictions = model.predict(X_test)


# In[30]:


submission_df = pd.DataFrame({'client_id': df1['client_id'], 'target': test_predictions})
submission_df


# In[31]:


# Create a new dataframe for modified submission
modified_submission_df = submission_df.groupby('client_id').mean().reset_index()

# Save modified submission file
modified_submission_df.to_csv('nacada.csv', index=False)


# In[32]:


from IPython.display import FileLink

FileLink('nacada.csv')


# In[ ]:




