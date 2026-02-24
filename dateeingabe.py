from datetime import datetime

# Aktuelles Datum holen (Hazırkı tarixi götürürük)
heute = datetime.now()

name = input("Wie heißt du? ")

# Eingabe von Jahr, Monat und Tag
geburtsjahr = int(input("Geburtsjahr (YYYY): "))
geburtsmonat = int(input("Geburtsmonat (1-12): "))
geburtstag = int(input("Geburtstag (1-31): "))

# Alter vorerst nur nach Jahr berechnen
alter = heute.year - geburtsjahr

# Überprüfen, ob der Geburtstag in diesem Jahr schon war
# Əgər cari ay/gün doğum ay/günündən kiçikdirsə, hələ ad günü olmayıb
if (heute.month, heute.day) < (geburtsmonat, geburtstag):
    alter = alter - 1

print(f"Hallo {name}! Du bist genau {alter} Jahre alt.")