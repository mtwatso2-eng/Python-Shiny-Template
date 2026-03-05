from shiny import App, ui, render
import numpy as np
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.h2("Interactive Histogram"),
    ui.input_slider("n_bins", "Number of bins:", min=5, max=50, value=20),
    ui.output_plot("histogram")
)

def server(input, output, session):
    @output
    @render.plot
    def histogram():
        # Generate random data
        data = np.random.normal(0, 1, 1000)
        
        # Create histogram
        plt.figure(figsize=(8, 6))
        plt.hist(data, bins=input.n_bins(), color='skyblue', edgecolor='black')
        plt.title("Histogram of Random Numbers")
        plt.xlabel("Value")
        plt.ylabel("Frequency")
        return plt.gcf()

app = App(app_ui, server) 