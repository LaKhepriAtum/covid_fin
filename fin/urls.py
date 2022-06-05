from . import views
from django.urls import include, path


app_name = 'fin'


urlpatterns = [
    path('chart/', views.chart, name= 'chart' ),
    path('plot/', views.plot, name= 'plot' ),
    path('code_DailyCovid/', views.code_DailyCovid, name= 'code_DailyCovid' ),
    path('code_totalCovid/', views.code_totalCovid, name= 'code_totalCovid' ),
    path('code_totalVaccine/', views.code_totalVaccine, name= 'code_totalVaccine' ),
    path('code_dailyVaccine/', views.code_dailyVaccine, name= 'code_dailyVaccine' ),
    path('DailyCovid/', views.DailyCovid, name= 'DailyCovid' ),
    path('TotalCovid/', views.TotalCovid, name= 'TotalCovid' ),
    path('DailyVaccine/', views.DailyVaccine, name= 'DailyVaccine' ),
    path('TotalVaccine/', views.TotalVaccine, name= 'TotalVaccine' ),
    path('codeDate/', views.codeDate, name= 'codeDate' ),
    path('covidspread/', views.covidspread, name= 'covidspread' ),
    path('aipredict/', views.aipredict, name= 'aipredict' ),
    path('periodselect/', views.periodselect, name= 'periodselect' ),
    path('periodselect_total/', views.periodselect_total, name= 'periodselect_total' ),
    path('ticker_search/', views.ticker_search, name= 'ticker_search' )
]