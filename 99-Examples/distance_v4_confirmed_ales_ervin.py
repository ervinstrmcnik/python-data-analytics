import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Middle-click to measure; right-click to delete a group")

click_points = []
measurements = []  # List of dicts: {'dots': [...], 'lines': [...], 'texts': [...]}


def on_mouse(event):
    global click_points

    if event.button == 2 and event.inaxes:  # Middle click
        # Draw a red dot immediately
        dot = ax.plot(event.xdata, event.ydata, "ro")[0]

        if len(click_points) == 0:
            # First click: start a new group
            click_points.append((event.xdata, event.ydata))
            measurements.append({"dots": [dot], "lines": [], "texts": []})

        elif len(click_points) == 1:
            # Second click: complete the group
            x1, y1 = click_points[0]
            x2, y2 = event.xdata, event.ydata
            dx = x2 - x1
            dy = y2 - y1

            # Add second point
            measurements[-1]["dots"].append(dot)

            # Horizontal and vertical lines
            hl = Line2D([x1, x2], [y1, y1], color="blue", linestyle="--")
            vl = Line2D([x2, x2], [y1, y2], color="green", linestyle="--")
            ax.add_line(hl)
            ax.add_line(vl)
            measurements[-1]["lines"].extend([hl, vl])

            # Add text labels
            text_dx = ax.text((x1 + x2) / 2, y1, f"Δx = {dx:.2f}", color="blue", fontsize=10, ha="center", va="bottom")
            text_dy = ax.text(x2, (y1 + y2) / 2, f"Δy = {dy:.2f}", color="green", fontsize=10, ha="left", va="center")
            measurements[-1]["texts"].extend([text_dx, text_dy])

            fig.canvas.draw_idle()
            click_points.clear()

        fig.canvas.draw_idle()

    elif event.button == 3 and event.inaxes:  # Right-click
        for group in measurements:
            for artist in group["dots"] + group["lines"] + group["texts"]:
                if artist.contains(event)[0]:
                    # Remove everything in the group
                    for item in group["dots"] + group["lines"] + group["texts"]:
                        item.remove()
                    measurements.remove(group)
                    fig.canvas.draw_idle()
                    return  # Stop after first match


# Connect event
fig.canvas.mpl_connect("button_press_event", on_mouse)

plt.show()
