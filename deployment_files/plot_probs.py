import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd

def plot_solution(outputs):
  probabilities = {}
  for i in range(len(outputs[0])):
    if outputs[0][i].item() < 0:
      if i == 0:
        probabilities["Alligator Cracking"] = 0
      elif i == 1:
        probabilities["Good Condition"] = 0
      elif i == 2:
        probabilities["Longitudinal Cracking"] = 0
      elif i == 3:
        probabilities["Pothole"] = 0
    else:
      if i == 0:
        probabilities["Alligator Cracking"] = outputs[0][i].item()
      elif i == 1:
        probabilities["Good Condition"] = outputs[0][i].item()
      elif i == 2:
        probabilities["Longitudinal Cracking"] = outputs[0][i].item()
      elif i == 3:
        probabilities["Pothole"] = outputs[0][i].item()
  
  df = pd.DataFrame.from_dict(probabilities, orient='index')
  df.rename(columns = {0:"Probability"}, inplace=True)
  df.loc[:, "Condition"] = df.index

  fig = px.bar(df, 
               y = "Condition", 
               x="Probability", 
               orientation='h',
               title = 'Probability of Condition')
  fig.update_traces(marker_color = '#1B848E')
  return fig