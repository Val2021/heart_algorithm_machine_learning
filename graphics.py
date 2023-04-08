
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot  as plt
from data_processing import cholesterol_mean,data




data['Age'].value_counts().sort_index()

hist1 = px.histogram(data, x='Age', nbins=60)
hist1.update_layout(width=800, height=500, title_text='Age distribution')
hist1.show()

# Age

graph1 = sns.histplot(data, x="Age",bins=30, color='orange',kde=True,stat="count")
plt.show()

# Gender

sns.countplot(x='Sex', data=data)
plt.show()

# Chest Pain Type

sns.countplot(x='ChestPainType',data=data)
plt.show()

# Blood pressure

sns.histplot(data, x='RestingBP', bins=30,color='orange',kde=True,stat='count')
plt.show()

# Serum cholesterol

sns.histplot(cholesterol_mean(), x='Cholesterol', bins=30,color='orange',kde=True,stat='count')
plt.show()

# Fasting blood sugar

sns.countplot(x='FastingBS', data=data)
plt.show()

# Resting electrocardiogram

sns.countplot(x='RestingECG',data=data)
plt.show()

# Maximum heart rate

sns.histplot(data, x='MaxHR',bins=30,color='orange',kde=True,stat='count')
plt.show()

# Exercise-induced angina

execAn=px.pie(data,'ExerciseAngina')
execAn.show()

# Old peak - ST depression

sns.histplot(data, x='Oldpeak',bins=30,color='orange',kde=True,stat='count')
plt.show()

# Slope of the ST segment on the ECg

slopst=px.pie(data,'ST_Slope')
slopst.show()


# Heart Disease
# 0 = No heart disease
# 1 = heart disease

heartds=px.pie(data,'HeartDisease')
heartds.show()




