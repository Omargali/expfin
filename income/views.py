from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Income
from django.contrib import messages
from django.core.paginator import Paginator
from userpreferences.models import UserPreference
import datetime
import csv

# Create your views here.
# @login_required(login_url='/login')
def index(request):
     categories = Category.objects.all()
     incomes = Income.objects.filter(owner=request.user)

     try:
         currency = UserPreference.objects.get(user=request.user).currency
     except UserPreference.DoesNotExist:
         currency = 'USD'  # set a default currency

     paginator=Paginator(incomes, 10)
     page_number = request.GET.get('page')
     page_obj = Paginator.get_page(paginator, page_number)
     context = {
          'incomes': incomes,
          'page_obj':  page_obj,
          'currency': currency,
     }
     return render(request, 'income/index.html', context)

def add_income(request):
     categories = Category.objects.all()
     context = {
          'categories': categories,
          'values': request.POST
     }
     if request.method == 'GET':
          return render(request, 'income/add_income.html', context)

     if request.method == 'POST':
          amount = request.POST['amount']

          if not amount:
               messages.error(request, 'Amount is required')
               return render(request, 'income/add_income.html', context)
          desrciption = request.POST['description']
          date = request.POST['income_date']
          category = request.POST['category']

          Income.objects.create(owner=request.user, amount=amount, date=date, description=desrciption, category=category)
          messages.success(request, 'Income saved successfully')
          return redirect('incomes')


def income_edit(request, id):
     income = Income.objects.get(pk=id)
     categories = Category.objects.all()
     context = {
          'income': income,
          'values': income,
          'categories': categories
     }
     if request.method == 'GET':
          return render(request, 'income/edit-income.html', context)
     if request.method == 'POST':
          amount = request.POST['amount']

          if not amount:
               messages.error(request, 'Amount is required')
               return render(request, 'income/edit-income.html', context)
          desrciption = request.POST['description']
          date = request.POST['income_date']
          category = request.POST['category']


          income.owner = request.user
          income.amount = amount
          income.date = date
          income.category = category
          income.description = desrciption
          income.save()

          messages.success(request, 'Income updated successfully')
          return redirect('incomes')



def delete_income(request, id):
     income = Income.objects.get(pk=id)
     income.delete()
     messages.success(request, 'Income removed')
     return redirect('incomes')


def exportt_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=Incomes'+str(datetime.datetime.now())+'.csv'

    writer=csv.writer(response)
    writer.writerow(['Amount', 'Description', 'Category', 'Date'])

    incomes = Income.objects.filter(owner=request.user)
    for income in incomes:
        writer.writerow([income.amount, income.description, income.category, income.date])

    return response


def income_category_summary_six(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=30 * 6)
    incomes = Income.objects.filter(owner=request.user, date__gte=six_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(income):
        return income.category

    category_list = list(set(map(get_category, incomes)))

    def get_income_category_amount(category):
        amount = 0
        filtered_by_category = incomes.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in incomes:
        for y in category_list:
            finalrep[y] = get_income_category_amount(y)

    return JsonResponse({'income_category_data': finalrep}, safe=False)








def income_category_summary_month(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=30)
    incomes = Income.objects.filter(owner=request.user, date__gte=six_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(income):
        return income.category

    category_list = list(set(map(get_category, incomes)))

    def get_income_category_amount(category):
        amount = 0
        filtered_by_category = incomes.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in incomes:
        for y in category_list:
            finalrep[y] = get_income_category_amount(y)

    return JsonResponse({'income_category_data': finalrep}, safe=False)


def income_category_summary_day(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=1)
    incomes = Income.objects.filter(owner=request.user, date__gte=six_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(income):
        return income.category

    category_list = list(set(map(get_category, incomes)))

    def get_income_category_amount(category):
        amount = 0
        filtered_by_category = incomes.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in incomes:
        for y in category_list:
            finalrep[y] = get_income_category_amount(y)

    return JsonResponse({'income_category_data': finalrep}, safe=False)



def income_category_summary_year(request):
    todays_date = datetime.date.today()
    six_months_ago = todays_date - datetime.timedelta(days=365)
    incomes = Income.objects.filter(owner=request.user, date__gte=six_months_ago, date__lte=todays_date)
    finalrep = {}

    def get_category(income):
        return income.category

    category_list = list(set(map(get_category, incomes)))

    def get_income_category_amount(category):
        amount = 0
        filtered_by_category = incomes.filter(category=category)

        for item in filtered_by_category:
            amount += item.amount
        return amount

    for x in incomes:
        for y in category_list:
            finalrep[y] = get_income_category_amount(y)

    return JsonResponse({'income_category_data': finalrep}, safe=False)











def stats_view(request):
    return render(request, 'income/income-stats.html')