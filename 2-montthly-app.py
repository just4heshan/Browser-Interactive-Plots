from ssl import Options
import justpy as jp
from justpy.htmlcomponents import Option
from pandas.core.dtypes.common import classes
import pandas

data = pandas.read_csv("reviews.csv", parse_dates=["Timestamp"])
data["Month"]=data["Timestamp"].dt.strftime("%Y, %m")
month_average = data.groupby(["Month"]).mean()

chart_def="""
    {
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Rating by Month'
    },
    subtitle: {
        text: 'According to past two years records'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Month'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Average Rating'
        },
        
       
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Rating',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text='Anlisis of course reviews', classes='text-h2 text-center text-weight-low')
    p1 = jp.QDiv(a=wp, text='These graphs represent course review analysis',classes='text-subtitle1')
    hc = jp.HighCharts(a=wp, options=chart_def)

    hc.options.title.text = "Average Rating by Month"
    hc.options.xAxis.categories=list(month_average.index)
    hc.options.series[0].data=list( month_average["Rating"])
    return wp

jp.justpy(app)

    
    