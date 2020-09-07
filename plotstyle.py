import numpy as np 
from matplotlib import style
from matplotlib import pyplot as plt 

def setStyle(styleName='blackBlue0', colors=None, testPlot=False):
    # Matplotlib rc file parameters to customize
    rcParams=[
        'figure.facecolor', 'axes.facecolor',
        'axes.labelcolor', 'axes.edgecolor',
        'ytick.color', 'xtick.color',
        'text.color'
    ]

    # Predefined styles:
    #  name: [figure background, axes background, texts colors]
    styles = {
        'blackWhite0':['202225', '393e46', 'ffffff'],
        'blackBlue0':['202225', '393e46', '00adb5']
    }
    
    # Dictionary to be fill with the custom styles
    customStyle = {}

    # Checks for users new set
    if colors == None:
        colors = styles[styleName]
    
    # Fills the customStyle dictionary
    for i in range(0,len(rcParams)):
        customStyle[rcParams[i]] = colors[i] if i <=2 else colors[2]
    
    style.use(customStyle)

    # Plot for fast test
    if testPlot:
        x = np.arange(0,10, 0.1)
        fig = plt.figure() 
        ax = fig.add_subplot(111)
        ax.plot(x, np.sin(x), label="sin(x)")
        ax.plot(x, np.exp(0.1*x)*np.cos(x), label=r"$e^{0.1x}\cos x$")
        ax.set_title("this is a title")
        ax.set_xlabel("this is the x label")
        ax.set_ylabel("this is the y label")
        ax.legend()
