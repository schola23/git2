from django.db import models


# deklaracja statycznej listy wyboru do wykorzystania w klasie modelu
MONTHS = models.IntegerChoices('Miesiace', 'Styczeń Luty Marzec Kwiecień Maj Czerwiec Lipiec Sierpień Wrzesień Październik Listopad Grudzień')

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )

PLEC = (
    ('k', 'kobieta'),
    ('m', 'mężczyzna'),
    ('i', 'inne')
)


class Team(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    # Shift + Alt + strzałka góra/dół
    firstname = models.CharField(max_length=60, verbose_name="First Name")
    lastname = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default=SHIRT_SIZES[0][0])
    month_added = models.IntegerField(choices=MONTHS.choices, default=MONTHS.choices[0][0])
    team = models.ForeignKey(Team, null=True, blank=True, on_delete=models.SET_NULL, help_text='Choose your Team')

    def __str__(self):
        return self.firstname
    
     
    class Meta:
        verbose_name_plural = "People"


class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=50)
    opis = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Stanowiska"

    def __str__(self) -> str:
        return self.nazwa


class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)
    plec = models.CharField(max_length=1, choices=PLEC, default=PLEC[0][0])
    stanowisko = models.ForeignKey(Stanowisko, null=True, blank=True, on_delete=models.SET_DEFAULT, default=1)
    data_dodania = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Osoby"
