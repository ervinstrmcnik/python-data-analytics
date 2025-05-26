import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y, label="sin(x)")
ax.set_title("Middle-click twice: mark points, measure Δx and Δy")

click_points = []
lines = []
texts = []


def on_mouse(event):
    global click_points, lines, texts

    if event.button == 2 and event.inaxes:  # Middle click
        # Store point
        click_points.append((event.xdata, event.ydata))

        # Draw a persistent red dot
        ax.plot(event.xdata, event.ydata, "ro")
        fig.canvas.draw_idle()

        # If two points clicked, draw Δx and Δy
        if len(click_points) == 2:
            (x1, y1), (x2, y2) = click_points
            dx = x2 - x1
            dy = y2 - y1

            # Draw Δx and Δy dashed lines
            hl = Line2D([x1, x2], [y1, y1], color="blue", linestyle="--")
            vl = Line2D([x2, x2], [y1, y2], color="green", linestyle="--")
            ax.add_line(hl)
            ax.add_line(vl)
            lines.extend([hl, vl])

            # Display Δx and Δy labels
            text_dx = ax.text((x1 + x2) / 2, y1, f"Δx = {dx:.2f}", color="blue", fontsize=10, ha="center", va="bottom")
            text_dy = ax.text(x2, (y1 + y2) / 2, f"Δy = {dy:.2f}", color="green", fontsize=10, ha="left", va="center")
            texts.extend([text_dx, text_dy])

            fig.canvas.draw_idle()

            # Reset for next measurement pair
            click_points = []


# Connect the middle-click handler
fig.canvas.mpl_connect("button_press_event", on_mouse)

plt.show()
