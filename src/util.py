import numpy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import animation


def animateAStar(map, path, closedList, start, end):
    palettes = {
        'map':          numpy.array( [  [1.0, 1.0, 1.0],        # index 0 =     Not in use
                                        [1.0, 1.0, 1.0],        # index 1 =     paths       = white
                                        [0.7, 0.7, 0.7],        # index 2 =     obstacle1   = light gray
                                        [0.5, 0.5, 0.5],        # index 3 =     obstacle2   = dark gray
                                        [0.2, 0.2, 0.2],        # index 4 =     obstacle3   = darker gray
                                        [0.0, 0.0, 0.0] ] ),    # index -1 =    walls       = black

        'path':         numpy.array( [  [1.0, 0.6, 0.2],        # search = orange
                                        [0.0, 0.5, 1.0] ] ),    # path = blue
        'start':        numpy.array( [  1.0, 0.0, 0.0 ] ),      # start = red
        'end':          numpy.array( [  0.0, 0.6, 0.0 ] ),      # end = green

    }

    def CreateImage(array, palette_name):
        return palettes[palette_name][array.astype(int)] # get colour based on value in array

    def animate_maze(map):
        image = CreateImage(map, 'map') # Init map using custom colour palette.
        fig = plt.figure(figsize=(6, 8)) # Figure size

        black = mpatches.Patch(color='black', label='Wall')
        white = mpatches.Patch(color='white', label='Path')
        orange = mpatches.Patch(color='orange', label='Closed node')
        green = mpatches.Patch(color='green', label='Goal')
        red = mpatches.Patch(color='red', label='Start')
        blue = mpatches.Patch(color='blue', label='Shortest path')
        gray = mpatches.Patch(color='gray', label='Obstacles (darker => higher cost)')


        plt.legend(bbox_to_anchor=(0., 1.05, 1., .105), loc='upper left', ncol=2, handles=[black, gray, orange, green, red, blue])

        plt.xticks([]), plt.yticks([]) # Remove axes
        imgplot = plt.imshow(image, interpolation='nearest') # Plot image

        def CreateFrame(frame):
            if frame<50:
                None
            elif frame<len(closedList)+50:
                image[closedList[frame-50]] = palettes['path'][0] # Draw search array
            elif frame<len(closedList)+len(path)+50:
                image[path[-((frame-50)-len(closedList)+1)]] = palettes['path'][1] # Draw path array
            else:
                None
            image[start] = palettes['start'] # Draw start position
            image[end] = palettes['end'] # Draw end position
            imgplot.set_data(image)
            return imgplot

        anim = animation.FuncAnimation(fig, CreateFrame, len(closedList)+len(path)+100, interval=20, repeat=False) # Call new frame
        # anim.save('SamfundetTraversert.gif', writer='PillowWriter') # Save animation
        plt.show()

    arrayMap = numpy.array(map)
    animate_maze(arrayMap)