# Extracting scipt from the other python file

from Time_storage_obj_entering_leaving import df

from bokeh.plotting import figure
from bokeh.io import output_file, show
#from bokeh.models import HoverTool

p = figure(x_axis_type = 'datetime', height = 100, width = 500, title = "Motion Graph")

p.yaxis.minor_tick_line_color = None
#p.ygrid[0].ticker.desired_num_ticks = 1

#hover = HoverTool(tooltips= [("Start: "," ")])

q = p.quad(left = df["Start"], right = df["End"], bottom =0, top=1, color = "green")
output_file("Graph1.html")
show(p)
