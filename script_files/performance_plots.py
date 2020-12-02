import pandas as import pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def get_plots(df):
    """creates plots of train vs val loss and train vs val accuracy
    INPUTS df, dataframe of training stats by epoch
    RETURNS None"""

    #plot for loss
    fig = go.Figure(layout=go.Layout(
        title="Loss by Training Epoch",
        xaxis = dict(
            title = "Training Epoch"
        ),
        yaxis=dict(
            title = "Loss"
        )
    ))
  fig.add_trace(go.Scatter(x=df["epoch"], y=df["training_loss"],
                    mode='lines',
                    name='training',
                    line_color = '#1B848E'))
  fig.add_trace(go.Scatter(x=df["epoch"], y=df["val_loss"],
                    mode='lines',
                    name='validation',
                    line_color = '#33B8B5'))

  fig.show()


  # plot for accuracy
  fig = go.Figure(layout=go.Layout(
        title="Accuracy by Training Epoch",
        xaxis = dict(
            title = "Training Epoch"
        ),
        yaxis=dict(
            title = "Accuracy"
        )
  ))
  fig.add_trace(go.Scatter(x=df["epoch"], y=df["training_acc"],
                    mode='lines',
                    name='training',
                    line_color = '#1B848E'))
  fig.add_trace(go.Scatter(x=df["epoch"], y=df["val_acc"],
                    mode='lines',
                    name='validation',
                    line_color = '#33B8B5'))

  fig.show()

  return
