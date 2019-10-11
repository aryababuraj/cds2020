
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


dor = pd.read_csv("DOR.csv")


# In[4]:


df_12_13 = dor[dor['year']=='2012-13']
pdf_12_13 = df_12_13[df_12_13['Primary_Boys']!='NR']
pavg = pdf_12_13[pdf_12_13['State_UT']=='All India']
pdf_12_13 = pdf_12_13[pdf_12_13['State_UT']!='All India']


# In[37]:


styles =  plt.style.available
plt.figure(figsize=(6,5))
plt.style.use(styles[0])
plt.scatter(pdf_12_13['Primary_Girls'], pdf_12_13['Primary_Boys'],color='blue')
star=plt.scatter(pavg['Primary_Girls'], pavg['Primary_Boys'],color='red',marker='*',s=100)
plt.xlabel('$Primary\ Girls$',fontsize=18)
plt.ylabel('$Primary\ Boys$',fontsize=18)
plt.title(" ",fontsize=2,color='b')
plt.suptitle('$Drop-out\ rate\ in\ Primary\ School\ for\ Boys\ vs\ Girls\ (year:\ 2012-13)$',fontsize=16,color='b')
plt.subplots_adjust(top=0.9)
leg=plt.legend([star], ["All India"],frameon=True)
leg.get_frame().set_edgecolor('black')
plt.savefig('ScatterPlot.pdf',bbox_inches='tight')


# In[38]:


df = dor[dor['year']=='2012-13']
df = df[df['Primary_Total']!='NR']
df = df[df['Upper Primary_Total']!='NR']
df = df[df['Secondary _Total']!='NR']

styles =  plt.style.available
plt.figure(figsize=(6,5))
plt.style.use(styles[0])
plt.boxplot((pd.to_numeric(df['Primary_Total']),pd.to_numeric(df['Upper Primary_Total']),pd.to_numeric(df['Secondary _Total'])),labels=['Primary','Upper Primary','Secondary'])
plt.ylabel('$Drop-out\ rates$',fontsize=14)
plt.title(" ",fontsize=2,color='b')
plt.suptitle('$Total\ drop-out\ rate\ (year:\ 2012-13)$',fontsize=16,color='b')
plt.subplots_adjust(top=0.9)
plt.savefig('BoxPlot.pdf',bbox_inches='tight')


# In[39]:


df = dor[dor['year']=='2012-13']
df = df[df['Primary_Total']!='NR']
df = df[df['Upper Primary_Total']!='NR']
df = df[df['Secondary _Total']!='NR']

states = df['State_UT']
pgirls = df['Primary_Girls']
pboys = df['Primary_Boys']

ppos=range(0,len(states)*3,3)

styles =  plt.style.available
plt.figure(figsize=(14,5))
plt.style.use(styles[0])
p1=plt.bar(ppos,pboys,color='orange')
p2=plt.bar(ppos,pgirls,color='green')
plt.xticks(ppos,states,rotation='vertical')
plt.ylabel('$Drop-out\ rates$',fontsize=14)
plt.title(" ",fontsize=2,color='b')
plt.suptitle('$State-wise\ primary\ school\ drop-out\ rate\ (year:\ 2012-13)$',fontsize=16,color='b')
plt.subplots_adjust(top=0.9)
plt.legend((p1[0], p2[0]), ('Boys', 'Girls'))
plt.savefig('BarPlot.pdf',bbox_inches='tight')

