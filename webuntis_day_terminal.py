import webuntis
import datetime

# Verbindung zur WebUntis-Instanz herstellen
session = webuntis.Session(
    username='YOUR_Username',  # Dein WebUntis-Benutzername
    password='YOUR_Password',  # Dein WebUntis-Passwort
    school='htl1-innsbruck',  # Name deiner Schule, wie in WebUntis (htl1-innsbruck per Default = HTL Anichstraße Innsbruck)
    server='neilo.webuntis.com',  # Die URL von deinem WebUntis
    useragent='python_script'  # User-Agent für die Verbindung
).login()

# Holt das aktuelle Datum
today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)

# Stundenplan für heute und morgen abrufen
table = session.my_timetable(start=today, end=tomorrow)

# Funktion zur Formatierung der Ausgabe
def format_timetable(table):
    timetable = []

    # Sortieren nach Startzeit
    table = sorted(table, key=lambda period: period.start)

    for period in table:
        date = period.start.strftime("%Y-%m-%d")
        start_time = period.start.strftime("%H:%M")
        end_time = period.end.strftime("%H:%M")
        subject = period.subjects[0].name if period.subjects else "Unbekannt"
        room = period.rooms[0].name if period.rooms else "Unbekannt"
        activity_type = period.activityType if period.activityType else "Unbekannt"
        
        timetable.append(f"{date}: {start_time} - {end_time} | Fach: {subject}, Raum: {room}, Art: {activity_type}")
    
    return timetable

print("Stundenplan vom: ", today)

# Stundenplan formatieren und ausgeben
formatted_timetable = format_timetable(table)
if len(formatted_timetable) == 0:
    print("Keine Einträge gefunden für heute (Wochenende?)")
    exit()

# Geordneten Stundenplan ausgeben
for entry in formatted_timetable:
    print(entry)

# Logout nach der Abfrage
session.logout()
