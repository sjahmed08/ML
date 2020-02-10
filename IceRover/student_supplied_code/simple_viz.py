
'''I made this super simple visualization method using matplotlib. It's not the prettiest but gets the job done. - Shrey Satpathy
 Just pass in the landmark coordinates and the coordinates of the path of the rover.'''

def create_plot(self, landmap, path):
    x_array = np.zeros(len(landmap))
    y_array = np.zeros(len(landmap))
    x_path = np.zeros(len(path))
    y_path = np.zeros(len(path))
    for i in range(len(landmap)):
        x_array[i] = landmap[i][1]
        y_array[i] = landmap[i][2]

    for i in range(len(path)):
        x_path[i] = path[i][0]
        y_path[i] = path[i][1]

    plt.scatter(x_array, y_array)
    plt.plot(x_path, y_path, '-ko')
    plt.show()

