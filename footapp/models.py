from django.db import models

class Mamlakat(models.Model):
    nom = models.CharField(max_length=30)
    def __str__(self):
        return self.nom

class Clubs(models.Model):
    nom = models.CharField(max_length=120)
    president = models.CharField(max_length=120)
    coach = models.CharField(max_length=130)
    year = models.DateField()
    max_purchase = models.SmallIntegerField()
    max_sell = models.SmallIntegerField()
    mamlakat = models.ForeignKey(Mamlakat, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.nom

class Players(models.Model):
    ism = models.CharField(max_length=120)
    yosh  = models.SmallIntegerField()
    davlat = models.CharField(max_length=100)
    position  = models.CharField(max_length=120)
    transfer_real = models.SmallIntegerField(null=True)
    club = models.ForeignKey(Clubs , on_delete=models.CASCADE)
    def __str__(self):
        return self.ism


class Transfer(models.Model):
    player = models.ForeignKey(Players, on_delete=models.CASCADE, null=True)
    club_from = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name="from_cl")
    club_to = models.ForeignKey(Clubs, on_delete=models.CASCADE, related_name="to_cl")
    fee_pre = models.SmallIntegerField()
    fee_real = models.SmallIntegerField()
    season = models.CharField(max_length=200)
    def __str__(self):
        return self.player.ism





