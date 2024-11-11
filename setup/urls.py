from django.contrib import admin
from django.urls import path
from apititanic.views import SummaryView,SurvivalRateView,AverageSurvivalRateView,CleanDataView,CorrelationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/summary/',SummaryView.as_view()),
    path('api/survival_rate/',SurvivalRateView.as_view()),
    path('api/grouped/<str:column>/',AverageSurvivalRateView.as_view()),
    path('api/clean_data/',CleanDataView.as_view()),
    path('api/correlation/',CorrelationView.as_view())
]
