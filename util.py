import numpy
import matplotlib.pyplot as plt
from matplotlib import animation


def animateAStar(map, path, closedList, start=None, end=None):
    palettes = {
        'map':          numpy.array( [  [1.0, 1.0, 1.0],        # index 0 =     Not in use
                                        [1.0, 1.0, 1.0],        # index 1 =     paths       = white
                                        [0.7, 0.7, 0.7],        # index 2 =     obstacle1   = light gray
                                        [0.5, 0.5, 0.5],        # index 3 =     obstacle2   = dark gray
                                        [0.2, 0.2, 0.2],        # index 4 =     obstacle3   = darker gray
                                        [0.0, 0.0, 0.0] ] ),    # index -1 =    walls       = black

        'path':         numpy.array( [  [0.0, 1.0, 0.5],        # search = green
                                        [0.0, 0.0, 1.0] ] ),    # path = blue
    }

    def CreateImage(array, palette_name):
        return palettes[palette_name][array.astype(int)]

    def animate_maze(map):
        image = CreateImage(map, 'map')
        fig = plt.figure(figsize=(10, 10))
        plt.xticks([]), plt.yticks([])
        imgplot = plt.imshow(image, interpolation='nearest')

        def CreateFrame(frame):
            print(frame)
            if frame<len(closedList):
                image[closedList[frame]] = palettes['path'][0]
            else:
                image[path[-(frame-len(closedList)+1)]] = palettes['path'][1]
            imgplot.set_data(image)
            return imgplot

        anim = animation.FuncAnimation(fig, CreateFrame, len(closedList)+len(path), interval=10, repeat=False)
        # anim.save('myAnimatedMaze.mp4')
        plt.show()

    arrayMap = numpy.array(map)
    animate_maze(arrayMap)