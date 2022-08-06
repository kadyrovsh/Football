from django.contrib import admin
from django.urls import path
from footapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('players/', PlayersView.as_view()),
    path('c_clubs/<int:pk>/', CountryClubsView.as_view()),
    path('clubs/', ClubsView.as_view()),
    path('transfer/', TransferView.as_view()),
    path('tr_archive/', TrArchiveView.as_view()),
    path('seasons/<str:son>/', SeasonsView.as_view()),
    path('about/', AboutView.as_view()),
    path('country/<int:pk>/', CountryView.as_view()),
    path('courses/', CoursesView.as_view()),
    path('latest/', LatestView.as_view()),
    path('stats/', StatsView.as_view()),
    path('tryouts/', TryoutsView.as_view()),
    path('Uplayers/', UplayersView.as_view()),
    path('tr_records/', T_RecordsView.as_view()),
    path('topclubsexpen/', Top_ExpenditureView.as_view()),
    path('topclubsincome/', Top_IncomeView.as_view()),
    path('accurate/', AccurateView.as_view()),
]
