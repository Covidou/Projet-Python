from datetime import datetime, timedelta
from django.views.generic import TemplateView
from django.shortcuts import render
from django.utils import timezone
from chartjs.views.lines import BaseLineChartView
from .models import City
from commerce.models import Product, Order

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
        days = []
        for i in range(7):
            days.append(timezone.now()-timedelta(days=i))
        return [day.strftime("%Y-%m-%d") for day in days]

    def get_providers(self):
        """Return names of datasets."""
        return [p.name for p in Product.objects.all()]

    def get_data(self):
        """Return 3 datasets to plot."""
        datasets = []
        for i in Product.objects.all():
            orders = i.order_set.all()
            product_dataset = []
            today = datetime.today()
            for j in range(7):
                day_orders = orders.filter(date__year=today.year,
                                           date__month=today.month,
                                           date__day=today.day-j)
                product_dataset.append(sum([o.quantity for o in day_orders]))
            datasets.append(product_dataset)

        return datasets

line_chart_json = LineChartJSONView.as_view()
