from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="incomes"),
    path('add-income', views.add_income, name="add-incomes"),
    path('edit-income/<int:id>', views.income_edit, name="income-edit"),
    path('income-delete/<int:id>', views.delete_income, name="income-delete"),



    path('export_csv', views.exportt_csv, name='exportt-csv'),


    path('income_category_summary_six', views.income_category_summary_six, name='income_category_summary'),
    path('income_category_summary_year', views.income_category_summary_year, name='income_category_summary'),
    path('income_category_summary_month', views.income_category_summary_month, name='income_category_summary'),
    path('income_category_summary_day', views.income_category_summary_day, name='income_category_summary'),

    path('Stats', views.stats_view, name='income-stats'),


]