#!/usr/bin/env python
# coding: utf-8

# In[164]:


import requests


# In[165]:


standings_url = "https://fbref.com/en/comps/9/Premier-League-Stats"


# In[166]:


data=requests.get(standings_url)


# In[167]:


data.status_code


# In[168]:


standings_url


# In[169]:


import pandas as pd
from bs4 import BeautifulSoup


# In[170]:


soup = BeautifulSoup(data.text)


# In[171]:


standings_table=soup.select('table.stats_table')[0]


# In[172]:


links=standings_table.find_all('a')


# In[173]:


links=[l.get("href") for l in links]


# In[174]:


links=[l for l in links if '/squads/' in l]


# In[175]:


links


# In[176]:


team_urls = [f"https://fbref.com{l}" for l in links] 


# In[177]:


team_urls


# In[178]:


# Extract match stats
team_url=team_urls[0]
team_url2=team_urls[1]
team_url3=team_urls[2]
team_url4=team_urls[3]
team_url5=team_urls[4]
team_url6=team_urls[5]
team_url7=team_urls[6]
team_url8=team_urls[7]
team_url9=team_urls[8]
team_url10=team_urls[9]
team_url11=team_urls[10]
team_url12=team_urls[11]
team_url13=team_urls[12]
team_url14=team_urls[13]
team_url15=team_urls[14]
team_url16=team_urls[15]
team_url17=team_urls[16]
team_url18=team_urls[17]
team_url19=team_urls[18]
team_url20=team_urls[19]


# In[179]:


data=requests.get(team_url)
data1=requests.get(team_url2)
data2=requests.get(team_url3)
data3=requests.get(team_url4)
data4=requests.get(team_url5)
data5=requests.get(team_url6)
data6=requests.get(team_url7)
data7=requests.get(team_url8)
data8=requests.get(team_url9)
data9=requests.get(team_url10)
data10=requests.get(team_url11)
data11=requests.get(team_url12)
data12=requests.get(team_url13)
data13=requests.get(team_url14)
data14=requests.get(team_url15)
data15=requests.get(team_url16)
data16=requests.get(team_url17)
data17=requests.get(team_url18)
data18=requests.get(team_url19)
data19=requests.get(team_url20)


# In[ ]:





# In[180]:


matches=pd.read_html(data.text, match="Scores & Fixtures ")
matches1=pd.read_html(data1.text, match="Scores & Fixtures ")
matches2=pd.read_html(data2.text, match="Scores & Fixtures ")
matches3=pd.read_html(data3.text, match="Scores & Fixtures ")
matches4=pd.read_html(data4.text, match="Scores & Fixtures ")
matches5=pd.read_html(data5.text, match="Scores & Fixtures ")
matches6=pd.read_html(data6.text, match="Scores & Fixtures ")
matches7=pd.read_html(data7.text, match="Scores & Fixtures ")
matches8=pd.read_html(data8.text, match="Scores & Fixtures ")
matches9=pd.read_html(data9.text, match="Scores & Fixtures ")
matches10=pd.read_html(data10.text, match="Scores & Fixtures ")
matches11=pd.read_html(data11.text, match="Scores & Fixtures ")
matches12=pd.read_html(data12.text, match="Scores & Fixtures ")
matches13=pd.read_html(data13.text, match="Scores & Fixtures ")
matches14=pd.read_html(data14.text, match="Scores & Fixtures ")
matches15=pd.read_html(data15.text, match="Scores & Fixtures ")
matches16=pd.read_html(data16.text, match="Scores & Fixtures ")
matches17=pd.read_html(data17.text, match="Scores & Fixtures ")
matches18=pd.read_html(data18.text, match="Scores & Fixtures ")
matches19=pd.read_html(data19.text, match="Scores & Fixtures ")


# In[181]:


matches[0]


# In[182]:


matches1[0]


# In[183]:


matches2[0]


# In[184]:


df_list = [matches[0], matches1[0], matches2[0], matches3[0], matches4[0], matches5[0], matches6[0], matches7[0], matches8[0], matches9[0], matches10[0], matches11[0], matches12[0], matches13[0], matches14[0], matches15[0], matches16[0], matches17[0], matches18[0], matches19[0]]
# Concatenate the dataframes vertically to merge the datasets
merged_df = pd.concat(df_list)
# Reset the index of the merged dataframe
merged_df.reset_index(drop=True, inplace=True)
# Save the merged dataframe to a new CSV file
merged_df.to_csv("merged_matches.csv", index=False)


# In[185]:


merged_df


# In[186]:


from IPython.display import FileLink
# Save the merged dataframe to a new CSV file
merged_df.to_csv("merged_matches.csv", index=False)
# Generate a clickable link to the saved file
FileLink("merged_matches.csv")


# # STOP HERE, THE CODE BELOW INCLUDES SHOOTING STATS.THE ABOVE CODE ONLY HAS (SCORES AND FIXTURES DATA)

# In[187]:


soup=BeautifulSoup(data.text)


# In[188]:


links=soup.find_all('a')


# In[189]:


links=[l.get("href") for l in links]


# In[190]:


links = [l for l in links if l and 'all_comps/shooting/' in l]


# In[191]:


links


# In[192]:


data = requests.get(f"https://fbref.com{links[0]}")


# In[ ]:





# In[193]:


# read our shooting stats
shooting=pd.read_html(data.text, match="Shooting")[0]


# In[194]:


# Top 5 rows of our shooting data
shooting.head()


# In[195]:


# drop the top level index
shooting.columns=shooting.columns.droplevel()


# In[196]:


shooting.head()


# In[197]:


# lets combine matches dataframe and shooting dataframe
shooting.columns


# In[198]:


matches[0].columns


# In[199]:


# merge the two dataframes
team_data = matches[0].merge(shooting[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")


# In[200]:


team_data


# In[201]:


# lets scrap data for multiple teams for multiple seasons(from 2020 to 2023)
years=list(range(2023,2020, -1))


# In[202]:


years


# In[203]:


all_matches=[]


# In[204]:


standings_url="https://fbref.com/en/comps/9/Premier-League-Stats"


# In[205]:


import time
for year in years:
    data = requests.get(standings_url)
    soup = BeautifulSoup(data.text)
    standings_table = soup.select('table.stats_table')[0]

    links = [l.get("href") for l in standings_table.find_all('a')]
    links = [l for l in links if '/squads/' in l]
    team_urls = [f"https://fbref.com{l}" for l in links]
    
    previous_season = soup.select("a.prev")[0].get("href")
    standings_url = f"https://fbref.com{previous_season}"
    
    for team_url in team_urls:
        team_name = team_url.split("/")[-1].replace("-Stats", "").replace("-", " ")
        data = requests.get(team_url)
        matches = pd.read_html(data.text, match="Scores & Fixtures ")[0]
        soup = BeautifulSoup(data.text)
        links = [l.get("href") for l in soup.find_all('a')]
        links = [l for l in links if l and 'all_comps/shooting/' in l]
        data = requests.get(f"https://fbref.com{links[0]}")
        shooting = pd.read_html(data.text, match="Shooting")[0]
        shooting.columns = shooting.columns.droplevel()
        try:
            team_data = matches.merge(shooting[["Date", "Sh", "SoT", "Dist", "FK", "PK", "PKatt"]], on="Date")
        except ValueError:
            continue
        team_data = team_data[team_data["Comp"] == "Premier League"]
        
        team_data["Season"] = year
        team_data["Team"] = team_name
        all_matches.append(team_data)
        time.sleep(1)


# In[ ]:


team_url.split("/")[-1].replace("-stats", "").replace("-"," ")


# In[ ]:


match_df=pd.concat(all_matches)


# In[ ]:


match_df


# In[ ]:


match_df.columns=[c.lower() for c in match_df.columns]


# In[ ]:


match_df.to_csv("scrapped_data.csv")


# In[ ]:


match_df


# In[ ]:





# In[ ]:





# In[ ]:




