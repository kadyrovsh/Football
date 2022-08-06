from django.shortcuts import render
from django.views import View
from footapp.models import Players, Clubs, Transfer, Mamlakat

class PlayersView(View):
    def get(self, request):
        data = {
            "oyinchilar":Players.objects.all(),
            "mamlakatlar": Mamlakat.objects.all()
                }
        return render(request, 'players.html', data)

class ClubsView(View):
    def get(self, request):
        data = {
            "clubs": Clubs.objects.all(),
            "mamlakatlar": Mamlakat.objects.all()
                }
        return render(request, "clubs.html", data)

class TransferView(View):
    def get(self, request):
        data = {
            "transfer": Transfer.objects.all(),
            "mamlakatlar": Mamlakat.objects.all()
        }
        return render(request, "transfer-archive.html", data)

class CountryClubsView(View):
    def get(self, request, pk):
        m = Mamlakat.objects.get(id=pk)
        data = {
            "clubs":Clubs.objects.filter(mamlakat=m),
            "countrys": Mamlakat.objects.all(),
            "m": m.nom.upper()
        }
        return render(request, "c_clubs.html", data)

class AboutView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all()}
        return render(request, "about.html", data)

class CountryView(View):
    def get(self, request, pk):
        c = Clubs.objects.get(id=pk)
        data = {
            "club":c,
            "mamlakatlar": Mamlakat.objects.all(),
            "players": Players.objects.filter(club=c)
        }
        return render(request, "country-clubs.html", data)

class CoursesView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all()}
        return render(request, "courses.html", data)

class IndexView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all()}
        return render(request, "index.html", data)

class LatestView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all(),
                "lat_tr": Transfer.objects.filter(season="22/23").order_by("-fee_real")}
        return render(request, "latest-transfers.html", data)

class StatsView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all()}
        return render(request, "stats.html", data)

class TryoutsView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all()}
        return render(request, "tryouts.html", data)

class UplayersView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all(),
                "players": Players.objects.all(),
                "uplayers": Players.objects.filter(yosh__lte=20)
                }
        return render(request, "U-20 players.html", data)

class T_RecordsView(View):
    def get(self, request):
        data = {
            "mamlakatlar": Mamlakat.objects.all(),
            "rec": Transfer.objects.filter(fee_real__gte=50).order_by("-fee_real"),
            "tr": Transfer.objects.all()
                }
        return render(request, "transfer-records.html", data)

class TrArchiveView(View):
    def get(self, request):
        data = {
            "mamlakatlar": Mamlakat.objects.all(),
        }
        return render(request, "transfer-archive.html", data)

class SeasonsView(View):
    def get(self, request, son):
        data = {
            "mamlakatlar": Mamlakat.objects.all(),
            "transfer": Transfer.objects.filter(season__startswith=son)
        }
        return render(request, "seasons.html", data)

# class Season17View(View):
#     def get(self, request, son):
#         data = {
#             "mamlakatlar": Mamlakat.objects.all(),
#             "transfer": Transfer.objects.filter(season__startswith="17")
#         }
#         return render(request, "seasons.html", data)

class Top_ExpenditureView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all()}
        return render(request, "top-50-clubs-by-expenditure-in-2021.html", data)

class Top_IncomeView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all()}
        return render(request, "top-50-clubs-by-income-in-2021.html", data)

class AccurateView(View):
    def get(self, request):
        data = {"mamlakatlar": Mamlakat.objects.all()}
        return render(request, "150-accurate-predictions.html", data)

