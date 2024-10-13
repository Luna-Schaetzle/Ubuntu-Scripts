import webuntis
import datetime
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Funktion, um den Stundenplan abzurufen
def fetch_timetable():
    try:
        # Verbindung zur WebUntis-Instanz herstellen
        session = webuntis.Session(
            username='YOUR_Username',  # Dein WebUntis-Benutzername
            password='YOUR_Password',  # Dein WebUntis-Passwort
            school='htl1-innsbruck',  # Name deiner Schule, wie in WebUntis (htl1-innsbruck per Default = HTL Anichstraße Innsbruck)
            server='neilo.webuntis.com',
            useragent='python_script'
        ).login()

        today = datetime.datetime.now()
        monday = today - datetime.timedelta(days=today.weekday())
        sunday = monday + datetime.timedelta(days=5)
        table = session.my_timetable(start=monday, end=sunday)

        formatted_timetable = format_timetable(table)

        # Textfeld leeren und neuen Stundenplan einfügen
        text_area.delete(1.0, tk.END)
        if formatted_timetable:
            for entry in formatted_timetable:
                text_area.insert(tk.END, entry + "\n")
        else:
            text_area.insert(tk.END, "Keine Einträge gefunden für diese Woche.")

        session.logout()
    except Exception as e:
        messagebox.showerror("Fehler", f"Ein Fehler ist aufgetreten: {e}")

# Funktion zur Formatierung der Ausgabe
def format_timetable(table):
    timetable = []
    last_date = None

    table = sorted(table, key=lambda period: period.start)

    for period in table:
        date = period.start.strftime("%Y-%m-%d")
        if date != last_date:
            timetable.append(f"\nNeuer Tag: {date}\n")
            last_date = date
        
        start_time = period.start.strftime("%H:%M")
        end_time = period.end.strftime("%H:%M")
        subject = period.subjects[0].name if period.subjects else "Unbekannt"
        room = period.rooms[0].name if period.rooms else "Unbekannt"
        activity_type = period.activityType if period.activityType else "Unbekannt"
        
        timetable.append(f"{start_time} - {end_time} | Fach: {subject}, Raum: {room}, Art: {activity_type}")
    
    return timetable

# Hauptfenster
root = tk.Tk()
root.title("Schulstundenplan")
root.geometry("1200x850")
root.configure(bg="#f0f0f0")

# Stil-Elemente
title_label = tk.Label(root, text="Mein Schulstundenplan", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Button zum Abrufen des Stundenplans
fetch_button = tk.Button(root, text="Stundenplan abrufen", command=fetch_timetable, bg="#4CAF50", fg="white", font=("Helvetica", 12))
fetch_button.pack(pady=10)

# Rahmen für das Textfeld
frame = tk.Frame(root, bg="#f0f0f0", bd=2, relief=tk.RAISED)
frame.pack(padx=10, pady=10)

# Textfeld zur Anzeige des Stundenplans
text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, width=70, height=20, font=("Helvetica", 25), bg="#ffffff", fg="#333333")
text_area.pack(padx=10, pady=10)

# Hauptloop
root.mainloop()
