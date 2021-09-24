import justpy as jp
from pandas.core.dtypes.common import classes

def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp, text="Analysis of Course Reviews", classes="text-h2 text-center text-weight-low" )
    p1=jp.QDiv(a=wp, text='These graphs represent course review analysis',classes='text-subtitle1')

    return wp

jp.justpy(app)