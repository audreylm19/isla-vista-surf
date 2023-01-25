from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, CustomJS, Div
from bokeh.plotting import figure
from bokeh.embed import components
from bokeh.layouts import row

# Create the bar chart
bar_source = ColumnDataSource(data=dict(x=[1, 2, 3, 4, 5], y=[4, 5, 6, 2, 8]))
bar = figure(title="Bar Chart", x_range=(0, 6), y_range=(0, 10))
bar.vbar(x='x', top='y', width=0.9, source=bar_source)

# Create the 5 prepared plots
plot_1 = figure(title="Plot 1", x_range=(0, 10), y_range=(0, 10))
plot_2 = figure(title="Plot 2", x_range=(0, 10), y_range=(0, 10))
plot_3 = figure(title="Plot 3", x_range=(0, 10), y_range=(0, 10))
plot_4 = figure(title="Plot 4", x_range=(0, 10), y_range=(0, 10))
plot_5 = figure(title="Plot 5", x_range=(0, 10), y_range=(0, 10))

# Create a container to hold the plots
container = Div(width=500, height=500)

# Embed the 5 prepared plots
plot_1_html = components(plot_1)
plot_2_html = components(plot_2)
plot_3_html = components(plot_3)
plot_4_html = components(plot_4)
plot_5_html = components(plot_5)

# Add a custom JavaScript callback to the bar chart
bar.js_on_event(events.Tap, CustomJS(args=dict(bar_source=bar_source, container=container), code="""
    var data = bar_source.data;
    var inds = cb_data.index['1d'].indices;
    var x = data['x'][inds];

    // Show the corresponding plot based on the selected bar
    switch (x) {
        case 1:
            container.text = plot_1_html;
            break;
        case 2:
            container.text = plot_2_html;
            break;
        case 3:
            container.text = plot_3_html;
            break;
        case 4:
            container.text = plot_4_html;
            break;
        case 5:
            container.text = plot_5_html;
            break;
        default:
            container.text = '<div id="default"></div>';
    }
"""))

# Show the bar chart and the plots container
show(row(bar, container))
