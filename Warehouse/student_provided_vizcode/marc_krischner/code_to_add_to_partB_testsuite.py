#Code provided by Marc Krischner, with additions from: Steven Abbot,Dustin Jones, Brian McCormick
# Add the following code to the test_suite_partB.py file, probably at/near the top:

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import collections  as mc
plt.ion()

def render(state):
    margin = 1.
    wall_size = 1.0
    box_size = 0.2 * wall_size
    robo_size = 0.25 * wall_size
    fig, ax = plt.subplots(1)
    ax.set_aspect(aspect=1.0)

    plt.ylim(state.warehouse_limits['min_y'] - margin, margin)
    plt.xlim(-margin, state.warehouse_limits['max_x'] + margin)
    plt.axhline(y=0)
    plt.axhline(y=state.warehouse_limits['min_y'])
    plt.axvline(x=0)
    plt.axvline(x=state.warehouse_limits['max_x'])

    rect = patches.Rectangle((state.dropzone['min_x'], state.dropzone['min_y']), wall_size, wall_size, linewidth=1,
                             edgecolor='y', facecolor='y')
   


    plt.gca().add_patch(rect)


    for obs in state.obstacles:
        ox, oy = obs['min_x'], obs['min_y']
        rect = patches.Rectangle((ox, oy), wall_size, wall_size, linewidth=1, edgecolor='r', facecolor='r')
        plt.gca().add_patch(rect)

    for box in state.boxes:
        x, y = state.boxes[box]['min_x'], state.boxes[box]['min_y']
        rect = patches.Rectangle((x, y), box_size, box_size, linewidth=1, edgecolor='k', facecolor='k')
        plt.gca().add_patch(rect)
        plt.gca().text(x, y, str(box), color='white')

    robo_circle = plt.Circle((state.robot.x, state.robot.y), robo_size, color='g')
    plt.gca().add_artist(robo_circle)
    # Show bearing
    l0 = (state.robot.x, state.robot.y)
    l1 = (l0[0] + 0.5*np.cos(state.robot.bearing), l0[1] + 0.5*np.sin(state.robot.bearing))
    lines = [[l0, l1]]
    c = np.array([(0, 0, 1, 1)])
    lc = mc.LineCollection(lines, colors=c, linewidths=2)
    plt.gca().add_collection(lc)

    if state.box_held is not None:
        plt.gca().text(state.robot.x, state.robot.y, str(state.box_held), color='white')
    plt.show()
    plt.pause(0.5)
    plt.clf()





#Then, add a call to "render" right above the "state.update_according_to(action)" line later in the file as in this example:

render(state)
state.update_according_to(action)

