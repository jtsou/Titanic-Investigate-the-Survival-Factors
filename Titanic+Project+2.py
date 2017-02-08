
# coding: utf-8

# # Who is more likely to survive the tragedy of Titanic? 
# What factored in the survival rate of the passengers on Titanic?

# Here, I am going to explore if gender, wealth status, and age played a role in the Titanic as the movie Titanic suggested.

# In[2]:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
get_ipython().magic(u'matplotlib inline')


# In[3]:

#General Survival rate by Categories
titanic=pd.read_csv('titanic-data.csv')
titanic_Survived=titanic.groupby(['Survived'])
titanic_Survived.describe().dropna()


# DATA WRANGLING:
# Looking at the dataset, I noticed that there are some missing data from the dataset provided. My way to deal with the missing values is to just drop it. That way, I am able to calculate the data without messing with the original source.For example, the 'Age' column is missing some values, so what I did was that I simply omit that, since '0' means something for age.
# 
# More data wrangling below.

# In[4]:

# Create Pclass Label Column
titanic['Class'] = titanic.Pclass.map({1 : 'First Class', 2 : 'Second Class', 3 : 'Third Class'})
titanic.Class.head()


# In[5]:

# Create Survival Label Column
titanic['Survival'] = titanic.Survived.map({0 : 'Died', 1 : 'Survived'})
titanic.Survival.head()


# In[6]:

# Create Embarked Labels Column
titanic['Ports'] = titanic.Embarked.map({'C' : 'Cherbourg', 'Q' : 'Queenstown', 'S' : 'Southampton'})
titanic.Ports.head()


# The table above summarizes the general surivial rate by different categories.

# The table below separates "Survived" into two groups. 0 indicated those who did not survive while 1 indicate those who survived. Now I am going to isolate each data group.

# In[7]:

#female vs male in survival rate in different categories
titanic_Survived=titanic.groupby(['Survived','Sex'])
titanic_Survived.describe().dropna()


# In[8]:

#Visualization of initial understanding of data
sns.set(style="ticks", color_codes=True)
sns.pairplot(titanic.dropna())
sns.plt.show()


# In[9]:

#Female and male that survived in general
survived=titanic.groupby('Sex')['Survived']
survived.mean()


# The number of female survived is significantly higher than male survived. Gender plays a role in survival rate. As suggested in the movie.

# Next, I am curious if age plays a factor; if so, old or young?

# In[11]:

#Age with missing value
sns.kdeplot(titanic.loc[(titanic['Survived']==0),'Age'], label = 'Died',cut=0)
sns.kdeplot(titanic.loc[(titanic['Survived']==1),'Age'], label = 'Survived',cut=0)
plt.xlabel("AGE")
plt.ylabel("DENSITY ESTIMATION OF SURVIVAL")
plt.title("AGE VS SURVIVAL")
plt.show()


# The graph and data suggest that the younger the age, the more likely for them to survive.

# In[10]:

#Find the correlation between variables


# In[11]:

titanic['Fare'].corr(titanic['Survived'])


# The correlation above shows that there is a weak link between fare and those who survived.

# In[12]:

titanic['SibSp'].corr(titanic['Survived'])


# The correlation above sugguest that even though there is a negative correltion between passenger with siblings and those who survived, the link is very weak.

# In[13]:

titanic['Parch'].corr(titanic['Survived'])


# The correlation above sugguest that there is a weak correlation between passenger with parents and those who survived.

# Now I would like to measure wealth based on class.

# In[14]:

Pclass=titanic.groupby(['Pclass'])["Survived"].mean()
Pclass


# More wealthy people were able to survive than the less wealthy. Now I wonder if there are any confounding variable such that there are more people in 1st class than the rest? and that there are more women than men in first class, since more women survived than men in general.

# In[15]:

titanic.groupby('Pclass')['Sex'].value_counts()


# In[16]:

sns.barplot(x="Sex", y="Survived", hue="Pclass", data=titanic)


# The data above shows that more poeple are in 3rd class than the rest. 

# In[17]:

hassib=titanic.groupby('SibSp')['Survived'].mean()
hassib


# In[18]:

sns.barplot(x="SibSp", y="Survived", hue="Sex", data=titanic)


# The data and graph above and below indicate that people with less siblings tend to have a higher survival rate. And out those those, siblings, females have higher survival rate.

# In[19]:

pas_sib=titanic.groupby('SibSp')['Survived'].mean()
pas_sib.plot(kind='bar')
plt.xlabel('Passenger with Siblings')
plt.ylabel('Probability of Survival')
plt.title('Survived vs Passenger with Siblings')
plt.show()


# In[20]:

parch=titanic.groupby('Parch')['Survived'].mean()
parch.plot(kind='bar')
plt.xlabel('PARENTS WITH CHILDREN')
plt.ylabel('PROBABILITY OF SURVIVAL')
plt.title('SURVIVAL VS PARENTS WITH CHILDREN')


# According to the plot and data analysis above, passengers with parents/children, the less children the parents have, the more likely they are able to survive.

# Conclusion: 
# 
# The analysis above indiciates that factors such as age and gender plays a role in survival rate. I am quite surprised to see that just because you paid a higher fare, it does not mean you get a better chance in surviving the tragedy, However, if we see wealth in a different perspective; that is, in class, then the higher the class the more likely you are able to survive. Now, we take into confounding factor into the analysis, even the less wealthy is in the majority, less of them sirvied than the wealthy.
# 
# It seems that at life and death, wealthy still has access to higher survival rate; on top of this, you have advantage if you are young and female. 
# 
# One thing to note is that there is limitation to the dataset. There are missing data, and we do not know for sure that these are all the passengers we have. In addition, it would be really helpful if the data include where were the passengers at on the ship at the time when the ship crashed. This way, we can know if the location of each passenger dramatically increase their survival rate.
