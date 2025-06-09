import justpy as jp
import pandas as pd
from datetime import datetime
from pytz import utc
my_chart_def = """
{
   chart: {
        type: 'spline',
        
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x} km: {point.y}°C'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [
            [0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]
        ]

    }]
}
"""
def app():
    dane= pd.read_csv("reviews_courses.csv", parse_dates=["Timestamp"])
    dane["Month"]=dane["Timestamp"].dt.strftime('%Y-%m')
    month_avg=dane.groupby(dane["Month"]).mean(numeric_only=True)
    x=month_avg.index
    y=month_avg['Rating']

    wp=jp.QuasarPage()
    h1=jp.QDiv(
        a=wp, text="Analiza ocen kursów", classes="text-center text-h4"
    )
    p1=jp.QDiv(
        a=wp, text="Poszczególne wykresy z analiza ocen kursów", classes="text-h4 text-left"
    )
    highCharts=jp.HighCharts(
        a=wp, options=my_chart_def
    )
    highCharts.options.title.text="Srednia ocen kursow wg DNIA"
    highCharts.options.subtitle.text="Dane z pliku CSV"
    list_1=[1,2,3]
    list_2=[12,1,20]
    highCharts.options.xAxis.categories=list(x)
    highCharts.options.series[0].data=list(y)
    return wp



jp.justpy(app)