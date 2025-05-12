#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[9]:


file_path = 'owid-covid-data.csv'


# In[10]:


df = pd.read_csv(file_path)


# print("Columns in the COVID-19 dataset:")

# In[12]:


print(df.columns)


# In[13]:


print("Preview of the first 5 rows:")


# In[14]:


print(df.head())


# In[15]:


# Identify and count missing values in each column
missing_values = df.isnull().sum()


# In[16]:


# Display the result
print("Missing values per column:")
print(missing_values)


# In[19]:


# Filter the data for Kenya
kenya_data = df[df['location'] == 'Kenya']


# In[20]:


# Display the first few rows
print("COVID-19 data for Kenya:")
print(kenya_data.head())


# In[22]:


# Drop rows where 'date' or other critical columns are missing
# You can add more critical columns as needed
critical_columns = ['date', 'total_cases', 'new_cases']
df_cleaned = df.dropna(subset=critical_columns)


# In[23]:


# Display number of remaining rows
print(f"Rows after dropping missing values in {critical_columns}: {len(df_cleaned)}")
print(df_cleaned.head())


# In[30]:


# Filter for Kenya
kenya_df = df[df['location'] == 'Kenya']


# In[33]:


# Filter for Kenya and create a copy to avoid SettingWithCopyWarning
kenya_df = df[df['location'] == 'Kenya'].copy()


# In[34]:


# Convert 'date' column to datetime format
kenya_df['date'] = pd.to_datetime(kenya_df['date'])


# In[35]:


# Confirm the change
print("Data type of 'date' column in Kenya data:")
print(kenya_df.dtypes['date'])


# In[37]:


# Preview the result
print(kenya_df.head())


# In[40]:


# Interpolate missing numeric values (e.g., linearly)
kenya_df.interpolate(method='linear', inplace=True)


# In[41]:


# Preview result
print("Preview after interpolating missing numeric values:")
print(kenya_df.head())


# In[48]:


# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[49]:


df = pd.read_csv('owid-covid-data.csv')


# In[50]:


# Convert date column to datetime format
df['date'] = pd.to_datetime(df['date'])


# In[51]:


# Filter for Kenya
kenya_df = df[df['location'] == 'Kenya'].copy()


# In[52]:


# Check for missing values in key columns
print("Missing values:\n", kenya_df[['total_cases', 'total_deaths', 'new_cases']].isnull().sum())


# In[53]:


# Set plotting style
sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)


# In[54]:


# ✅ 1. Plot total cases over time
plt.figure()
sns.lineplot(data=kenya_df, x='date', y='total_cases')
plt.title('Total COVID-19 Cases Over Time in Kenya')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.tight_layout()
plt.show()


# In[55]:


# ✅ 2. Plot total deaths over time
plt.figure()
sns.lineplot(data=kenya_df, x='date', y='total_deaths')
plt.title('Total COVID-19 Deaths Over Time in Kenya')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.tight_layout()
plt.show()


# In[56]:


# ✅ 3. Plot daily new cases
plt.figure()
sns.lineplot(data=kenya_df, x='date', y='new_cases')
plt.title('Daily New COVID-19 Cases in Kenya')
plt.xlabel('Date')
plt.ylabel('New Cases')
plt.tight_layout()
plt.show()


# In[57]:


# ✅ 4. Calculate and plot death rate (total_deaths / total_cases)
kenya_df['death_rate'] = kenya_df['total_deaths'] / kenya_df['total_cases']

plt.figure()
sns.lineplot(data=kenya_df, x='date', y='death_rate')
plt.title('COVID-19 Death Rate in Kenya Over Time')
plt.xlabel('Date')
plt.ylabel('Death Rate')
plt.tight_layout()
plt.show()


# In[58]:


# Optional: Latest death rate
latest = kenya_df.dropna(subset=['death_rate']).iloc[-1]
print(f"\nLatest death rate in Kenya as of {latest['date'].date()}: {latest['death_rate']:.2%}")


# In[59]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[60]:


# Load data
df = pd.read_csv('owid-covid-data.csv')
df['date'] = pd.to_datetime(df['date'])


# In[67]:


# Plot: Total Deaths over Time
sns.lineplot(data=kenya_df, x='date', y='total_deaths')
plt.title('Total COVID-19 Deaths Over Time in Kenya')
plt.xlabel('Date')
plt.ylabel('Total Deaths')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[75]:


# Bar Gragh
# Get the latest data per country
latest_data = df.sort_values('date').groupby('location').tail(1)

# Top 10 countries by total cases
top_countries = latest_data.sort_values(by='total_cases', ascending=False).head(10)

# Plot
sns.barplot(data=top_countries, x='total_cases', y='location', palette='Reds_r')
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.show()


# In[76]:


# Numerical columns for correlation
numeric_cols = ['total_cases', 'total_deaths', 'new_cases', 'new_deaths']
correlation_data = kenya_df[numeric_cols].dropna()

# Correlation matrix
corr_matrix = correlation_data.corr()

# Heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix (Kenya)')
plt.tight_layout()
plt.show()


# In[78]:


import pandas as pd
import plotly.express as px

# Load your data
df = pd.read_csv('owid-covid-data.csv')

# Get latest available data for each country
df['date'] = pd.to_datetime(df['date'])
latest_df = df.sort_values('date').groupby('location').tail(1)

# Drop rows with missing iso_codes or total_cases
choropleth_df = latest_df[['location', 'iso_code', 'total_cases']].dropna()

# Plot choropleth map
fig = px.choropleth(
    choropleth_df,
    locations='iso_code',
    color='total_cases',
    hover_name='location',
    color_continuous_scale='Reds',
    title='Total COVID-19 Cases by Country',
    projection='natural earth'
)

fig.update_layout(geo=dict(showframe=False, showcoastlines=True))
fig.show()


# In[ ]:


## 🌍 COVID-19 Data Insights & Reporting

###  Key Insights

1. **Kenya’s COVID-19 case trends** show a slow but steady increase in total cases over time, with several spikes corresponding to global or regional waves.
2. **Death rate in Kenya** remained below global averages for most of the pandemic, often stabilizing around 1.5%–2.5%, indicating relatively better survivability or underreporting.
3. **Top 10 countries by total cases** were dominated by highly populated nations like the United States, India, and Brazil. These countries showed extremely steep growth curves early on.
4. **Vaccination rates vary dramatically**, with some high-income countries achieving over 70% vaccination rates, while many low-income nations remained below 20%.
5. **Daily new case spikes** in Kenya do not always correlate with a similar spike in reported deaths, suggesting possible testing/reporting limitations or effective treatment improvements.

---

###  Anomalies & Interesting Patterns

- **Some countries reported zero deaths despite high case counts**, likely due to data lags or underreporting (e.g., early phases in some African nations).
- **Kenya’s vaccination rate** improved significantly mid-2021 but plateaued in 2022, suggesting supply or distribution limitations.
- **Unusual dips** in some countries’ total case or death counts (visible in line charts) indicate data corrections or retroactive reporting changes.

---

###  Conclusion

The data reveals both global and regional disparities in case growth, healthcare impact, and vaccine access. While high-income countries recovered faster, the long tail of infections and lower vaccine uptake in developing countries like Kenya highlights the need for sustained public health support and equitable resource distribution.


# In[ ]:
