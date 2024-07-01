# -*- coding: utf-8 -*-
"""Copy_of_Final_V2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/17qI91WubtuAwoPqlvf8u6Gcow00ZofU_
"""

#!pip install altair

pip install streamlit

pip install seaborn

#import altair as alt
import pandas as pd
import numpy as np
import streamlit as st

import streamlit as st

st.write("Hello World")
!streamlit run Copy_of_FinalV1.py

# Dataset is downloaded from Kaggle site and kept at data directory.
# Link of Dataset :https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023
#Link to the modified Dataset in my Github: https://github.com/Solomon1533/Test1/blob/main/Test1.csv

data = pd.read_csv("https://raw.githubusercontent.com/Solomon1533/Test1/main/Test1.csv")
data.head(5)

data.tail(5)

data.shape

"""Droping the duplicate rows  
This is often a handy thing to do because a huge data set as in often have some duplicate data which might be disturbing, so here I remove all the duplicate value from the data-set if there are any.
"""

duplicate_rows_data = data[data.duplicated()]
print("number of duplicate rows: ", duplicate_rows_data.shape)



chart_data = data.groupby('Country')['Subscriber'].mean()
chart_data

"""Checking the types of data  
Here we check for the datatypes because sometimes int or float would be stored as a string.
"""

data.dtypes

"""Wikipedia Definition,

In descriptive statistics, a box plot is a method for graphically depicting groups of numerical data through their quartiles. Box plots may also have lines extending vertically from the boxes (whiskers) indicating variability outside the upper and lower quartiles, hence the terms box-and-whisker plot and box-and-whisker diagram. Outliers may be plotted as individual points.  

Herein all the plots, we can find some points are outside the box they are none other than outliers.
"""

import seaborn as sns
sns.boxplot(x=data['Views'])

import seaborn as sns
sns.boxplot(x=data['Subscriber'])

data['Country'].max()

data['Country'].min()

"""Scatterplot
The following two scatter plot shows different perspectives. We generally use scatter plots to find the correlation between two variables. Here the scatter plots are plotted between Country and Unemployment rate and we can see the plot below. With the plot given below, we can easily draw a trend line. These features provide a good scattering of points.
"""

# @title Views vs Population

from matplotlib import pyplot as plt
# Convert 'Catagories' to string type if it contains numerical values
data['Catagories'] = data['Catagories'].astype(str)

data.plot(kind='scatter', x='Views', y='Catagories', s=32, alpha=.8)
plt.gca().spines[['top', 'right',]].set_visible(False)

fig, ax = plt.subplots(figsize=(10,6))
ax.scatter(data['Country_Abb'], data['Unemployment_ Rate'])
ax.set_xlabel('Country')
ax.set_ylabel('Unemployment_Rate')
ax.set_title('Country VS Unemployment_rate')
plt.show()

#Distribution of catagories by Pie Chart
import plotly.express as px # Import the plotly.express module and give it the alias 'px'

data['Subscriber'] = data['Subscriber'].astype(int)
#data['Catagories'] = data['Catagories'].astype('category').cat.codes
fig3 = px.pie(data, values='Subscriber', names='Catagories', color_discrete_sequence=px.colors.qualitative.Pastel)
fig3.show()

for col in data.columns:
    null_counter = data[col].isnull().sum()
    null_percent = null_counter/len(data) * 100
    print(f'There are {null_counter} ({null_percent:.2f}%) null values in {col}')

data_Catagories = data.dropna(subset = ['Catagories'])
data_Country = data.dropna(subset = ['Country'])
Catagories_medians = data_Catagories.groupby('Catagories')['Subscriber'].median()
median_order = Catagories_medians.sort_values(ascending = False).index

fig, ax = plt.subplots(figsize=(14, 6))
g = sns.boxplot(data = data_Catagories,
                x = 'Subscriber',
                y = 'Catagories',
                order = median_order,
                color = 'gray'
                )
ax.set_title('Distribution of Subscribers by Category')
ax.set_xlabel('Number of Subscribers')
ax.set_ylabel('Catagories')
plt.show()

"""By looking at this plot, ordered by median, we can see that for most categories, the center of distribution is really similar. "Trailers" stands out for having a median that is higher than the others.

We can also see that the Interquartile Range and the number of outliers varies more in some of these categories.

Something that might have something to do with these variations is the size of the sample in this specific dataset (which already contains well performing channels). Perhaps these categories with lesser variation also have fewer registers.
"""

fig, ax = plt.subplots(figsize=(14, 6))
sns.countplot(
    data = data_Catagories,
    #x = 'Catagories'
    y = 'Catagories',
    order = median_order,
    color = 'gray')

ax.set_title('Count of Channels by Category')
ax.set_xlabel('Number of Channels')
ax.set_ylabel('Category')
plt.show()

data_geo_Subscriber = data_Country.groupby('Country')['Subscriber'].mean().reset_index()
data_geo_Subscriber = data_geo_Subscriber.rename(columns = {'Subscriber': "Subscriber (millions)"})
px.choropleth(data_geo_Subscriber,
                    locations="Country",
                    locationmode='country names',
                    color='Subscriber (millions)',
                    color_continuous_scale=px.colors.sequential.YlGn ,
                    title="Average number of Subscribers by Country"
             )



import altair as alt
alt.Chart(data).mark_bar().encode(
    x = 'Country',
    y = 'Subscriber'

  )

import altair as alt

alt.Chart(data).mark_point().encode(
    x="Population",
    y="Views",
    color=alt.Color("Country", scale=alt.Scale(scheme="spectral")),
    tooltip=["Country", "Population"]
).properties(
  width=500,
  height=200
)

#Test your knowledge. How do we facet charts
c1 = alt.Chart(data).mark_circle().encode(
    x = "Catagories",
    y = "Country",
)

c2 = alt.Chart(data).mark_circle().encode(
    x = "Catagories",
    y = "Views",
)

c1|c2

#Going back to our scatterplot, we can also add in a little more information to this plot.
#Let's add in some color to differentiate different regions of the world
alt.Chart(data).mark_point().encode(
    x = 'Country',
    y = 'Catagories',
    color = 'Country'
)

"""X-axis (Mean of Population): The position of a point along the x-axis tells you the average population size of the group it represents. Points further to the right indicate groups with larger average populations.
Y-axis (Mean of Subscriber): The position of a point along the y-axis tells you the average number of subscribers for the group it represents. Points higher up indicate groups with more subscribers on average   

Overall Interpretation:

By looking at the position of the points in the scatter plot, you can get a sense of the relationship between average population size and average number of subscribers across different groups.  




"""

import altair as alt

# Replace 'CorrectColumnName' with the actual name of the column in your DataFrame
selection = alt.selection_single(fields=['CorrectColumnName'])

base = alt.Chart(data).properties(width=300, height=250)

scat = base.mark_circle().encode(
    x='mean(Population)',
    y='mean(Subscriber)',
    size='count()',
    tooltip=['Country', alt.Tooltip('count()', title='big cities')],  # Use the correct column name
    color=alt.condition(selection, 'Country', alt.value('lightgreen'))  # And here as well
).add_selection(selection)

hist = base.mark_bar(color="lightblue").encode(
    x=alt.X('Population', bin=alt.Bin(maxbins=30)),
    y='count()',
).transform_filter(selection)

scat | hist

"""Overall Interpretation:

By looking at the position of the points in the scatter plot, you can get a sense of the relationship between average population size and average number of subscribers across different groups.


"""

import plotly.express as px

# Creating a scatter plot using plotly express (px)
plot = px.scatter(
    x=data["Subscriber"],
    y=data["Views"],
    color=data["Catagories"],
    size=data["Views"],
    hover_name=data["YouTuber"],
    color_discrete_sequence=["red", "blue", "green", "orange", "green",
                             "yellow", "purple", "black"]  # Add more colors if you have more categories
)

# Updating the layout of the plot
plot.update_layout(
    xaxis=dict(title="Subscriber"),
    yaxis=dict(title="Views"),
    title="Relationship between Views and Subscribers",
    title_x=0.48
)

# Displaying the plot
plot.show()

"""For the youtube data, I split by Origin, compute the mean of the subscribers, and then combine the results. In Pandas, the operation looks in the below graph:

Here I use the mean formula to calculate each countries mean value.   
$Mean(X)=\sum_{i=1}^n \frac{X}{n}$
"""

print(data['Catagories'].dtype)  # Check data type
print(data['Catagories'].unique()) # Print unique categories

data['Catagories'] = data['Catagories'].astype('category')

data.groupby('Country')['Subscriber'].mean()

"""The below graph is an exact reflection of the above Mean data calculation."""

alt.Chart(data).mark_bar().encode(
    y='Country',
    x='mean(Subscriber)'
)

"""Customizing the interval selection  
The alt.selection_interval() function takes a number of additional arguments; for example, by specifying encodings, we can control whether the selection covers x, y, or both:
"""



import altair as alt
# Assuming 'data' is a pandas DataFrame available in the environment
interval = alt.selection_interval(encodings=['x'])

alt.Chart(data).mark_point().encode(
    x='Catagories',  # Corrected typo: 'Categories' instead of 'Catagories'
    y='Subscriber',
    color=alt.condition(interval, 'Country', alt.value('lightgray'), type='nominal')  # Explicitly set 'Country' type
).add_selection(
    interval
)

"""The correlation matrix shows how strongly different numerical variables in the dataset are related to each other. Each cell in the matrix represents the correlation coefficient between a pair of variables.   
So, when you see a correlation of 0.1 between "Population" and "Views", it means there's a weak positive relationship between those two things. In simpler terms:

Positive Relationship: As the population increases, the number of views tends to increase as well, but not very reliably.
Weak: The relationship isn't very strong. There are likely many other factors influencing the number of views besides just the size of the population.  

Here's a way to think about correlation values in general:

1.0: Perfect positive correlation. When one variable goes up, the other goes up by a directly proportional amount.  

0.5: Moderate positive correlation. There's a tendency for the variables to move together in the same direction, but it's not a super tight relationship.  

0.0: No correlation. There's no relationship between the variables. Changes in one don't tell you anything about changes in the other.  

-0.5: Moderate negative correlation. There's a tendency for the variables to move in opposite directions.  

-1.0: Perfect negative correlation. When one variable goes up, the other goes down by a directly proportional amount.




"""

# Scatter plot of Catagories vs. Views
plt.figure(figsize=(8, 6))
# Convert 'Categories' column to strings explicitly
plt.scatter(data['Catagories'].astype(str), data['Views'], color='green')
plt.title('Catagories vs. Views')
plt.xlabel('Catagories')
plt.ylabel('Views(Billions)')
plt.show()

# Calculate the correlation matrix, EXCLUDING non-numerical columns
correlation_matrix = data.select_dtypes(include=['number']).corr()

# Visualize the correlation matrix as a heatmap
import seaborn as sns
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()