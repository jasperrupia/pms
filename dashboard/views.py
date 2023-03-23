from django.views import View
# from django.views.generic.edit import CreateView
from django.shortcuts import render
from medicine.models import Stock, Category
from userAuth.models import pmsUser
from sales.models import Records
from datetime import date
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Sum


@method_decorator(login_required, name='get')
class DashboardView(View):
    def get(self, request):
        user_count = pmsUser.objects.filter(work_for=request.user.work_for).count()
        category_count = Category.objects.filter(owner=request.user.work_for).count()
        stock_values = Stock.objects.filter(owner=request.user.work_for).order_by('-sold', '-date_modified')
        today = date.today().isoformat()
        exipired_count = stock_values.exclude(best_before__gt=today).count()
        out_of_stock_count = Stock.objects.filter(quantity=0, owner=request.user.work_for).count()

        to_graph_trans_date = []
        to_graph_day_sales = []
        graph_values = Records.objects.filter(owner=request.user.work_for).values('trans_date').annotate(day_sales = Sum('total_amount')).order_by('trans_date')
        for instance in graph_values[:7]:
            if date.today().strftime("%d/%m/%Y") == instance['trans_date'].strftime("%d/%m/%Y"):
                to_graph_trans_date.append('Today')
            else:
                to_graph_trans_date.append(instance['trans_date'].strftime("%d/%m/%Y"))
            to_graph_day_sales.append(instance['day_sales']) 
        varToPass = {
            'category_count': category_count,
            'stock_values': stock_values,
            'exipired_count': exipired_count,
            'out_of_stock_count': out_of_stock_count,
            'user_count': user_count,
            'to_graph_trans_date': to_graph_trans_date,
            'to_graph_day_sales': to_graph_day_sales
        }
        return render(request, 'advanced/index.html', varToPass)
        