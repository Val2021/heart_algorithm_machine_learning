import plotly.express as px

from main import data


age_outliers = px.box(data, y='Age')
age_outliers.show()

restingBP_outliers = px.box(data, y='RestingBP')
age_outliers.show()

mxhr_outliers = px.box(data, y='MaxHR')
mxhr_outliers.show()

chol_outliers = px.box(data, y='Cholesterol')
chol_outliers.show()