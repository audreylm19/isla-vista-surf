from bokeh.models.callbacks import CustomJS
from bokeh.plotting import figure
from bokeh.io import show

callback = CustomJS(code="""
// the event that triggered the callback is cb_obj:
// The event type determines the relevant attributes
console.log('Tap event occurred at x-position: ' + cb_obj.x)
""")

p = figure()
# execute a callback whenever the plot canvas is tapped
p.js_on_event('tap', callback)

show(p)