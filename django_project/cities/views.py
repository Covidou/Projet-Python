from django.shortcuts import render
from .models import City
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView

def dataviz(request, commune):
    try :
        City.objects.get(name__iexact=commune)
        context = {
            'title': f'Dataviz de la commune {commune}',
        }
        return render(request, 'cities/dataviz.html', context=context)
    except Exception as ex:
        context = {
            'title': 'Commune incorrecte',
            'cities': City.objects.all(),
            'exception': ex
        }
        return render(request, 'cities/wrong_city.html', context=context)

class LineChartJSONView(BaseLineChartView):
    def get_labels(self):
        """Return 7 labels for the x-axis."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_data(self):
        """Return 3 datasets to plot."""

        return [[75, 44, 92, 11, 44, 95, 35],
                [41, 92, 18, 3, 73, 87, 92],
                [87, 21, 94, 3, 90, 13, 65]]

line_chart_json = LineChartJSONView.as_view()
