import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.path as mplPath
matplotlib.use("TkAgg")

fig, ax = plt.subplots(1,1)

# 4. Visualization with matplotlib
class IndexTracker(object):
    def __init__(self, ax, X):
        self.ax = ax
        ax.set_title('Scroll to Navigate through the DICOM Image Slices')

        self.X = X
        rows, cols, self.slices = X.shape
        self.ind = self.slices//2

        self.im = ax.imshow(self.X[:, :, self.ind])
        self.update()

    def onscroll(self, event):
        print("%s %s" % (event.button, event.step))
        if event.button == 'up':
            self.ind = (self.ind + 1) % self.slices
        else:
            self.ind = (self.ind - 1) % self.slices
        self.update()

    def update(self):
        self.im.set_data(self.X[:, :, self.ind])
        ax.set_ylabel('Slice Number: %s' % self.ind)
        self.im.axes.figure.canvas.draw()

def dicomviewer(plot, name):
    y = np.dstack(plot)
    tracker = IndexTracker(ax, y)
    fig.canvas.set_window_title(name)
    fig.canvas.mpl_connect('scroll_event', tracker.onscroll)
    plt.show()
