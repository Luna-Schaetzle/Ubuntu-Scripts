# My Ubuntu Skripts

Dieses Projekt bietet eine Sammlung von Python-Skripten, die verschiedene Funktionen bereitstellen, darunter das Abrufen des Stundenplans von WebUntis, die Wetterabfrage über wttr.in und eine GUI-basierte RPG-Würfelauswahl.

## Features
- **WebUntis-Stundenplan-Viewer**: Abrufen und Anzeigen des aktuellen Stundenplans.
- **Wetterabfrage**: Abfrage des aktuellen Wetters über wttr.in.
- **RPG-Dice-Roller**: GUI zum Rollen verschiedener Würfeltypen (d4, d6, d8, d10, d12, d20, d100).

## Prerequisites

- Python 3.x
- Internetverbindung (für die WebUntis- und Wetterabfrage)
- WebUntis-Zugangsdaten

## Setup

### 1. Repository klonen

```bash
git clone https://github.com/yourusername/WebUntis-Schedule-Viewer.git
cd WebUntis-Schedule-Viewer
```

### 2. Virtuelle Umgebung mit Bash-Skript erstellen

Nutze das bereitgestellte Bash-Skript, um eine virtuelle Umgebung zu erstellen und die Abhängigkeiten zu installieren.

```bash
bash create_venv.sh
```

Dieses Skript erstellt die virtuelle Umgebung und installiert alle benötigten Abhängigkeiten aus der `requirements.txt`.

### 3. WebUntis-Skript konfigurieren

Ersetze die folgenden Felder in der `webuntis_script.py` durch deine WebUntis-Anmeldedaten:

```python
session = webuntis.Session(
    username='your_username',
    password='your_password',
    school='your_school',
    server='your_server_url',
    useragent='python_script'
)
```

### 4. Skripte ausführen

Nutze das bereitgestellte Bash-Skript, um die Skripte auszuführen. und ersetze `<script_name>` durch den Namen des Skripts, das du ausführen möchtest.

```bash
bash run_scripts.sh <script_name>
```

**Beispiel:**

```bash
bash run_scripts.sh webuntis_day.py
```

## Abhängigkeiten

- `webuntis`: Bibliothek zum Abrufen von Stundenplänen über die WebUntis-API.
- `tkinter`: GUI-Bibliothek (in Python integriert).
- `requests`: Bibliothek für HTTP-Anfragen (für die Wetterabfrage).
- `datetime`: Bibliothek für Datums- und Zeitfunktionen.
- `PyQt5`: Bibliothek für die einbindung von Webseiten in eine GUI-Anwendung.

## Projektstruktur

```plaintext
WebUntis-Schedule-Viewer/
│
├── venv/                     # Virtuelle Umgebung
├── requirements.txt          # Abhängigkeiten
├── webuntis_day_terminal.py  # WebUntis-Stundenplan-Viewer für einen tag im Terminal
├── webuntis_day.py           # WebUntis-Stundenplan-Viewer für einen Tag mit GUI
├── webuntis_week_terminal.py # WebUntis-Stundenplan-Viewer für eine Woche im Terminal
├── webuntis_week.py          # WebUntis-Stundenplan-Viewer für eine Woche mit GUI
├── rpg_dice_roller.py        # GUI-Anwendung zum Würfeln
├── run_scripts.sh            # Bash-Skript zum Ausführen der Skripte
├── create_venv.sh            # Bash-Skript zum Einrichten der virtuellen Umgebung
├── README.md                 # Dieses Dokument
```

## License

Dieses Projekt ist unter der GNU GENERAL PUBLIC LICENSE lizenziert. Weitere Informationen findest du in der [LICENSE](LICENSE) Datei.

## Contributing

Beiträge sind willkommen! Wenn du Vorschläge oder Verbesserungen hast, öffne bitte ein Issue oder reiche einen Pull-Request ein.

## Contact

Bei Fragen oder Anregungen kannst du mich unter:
- E-Mail: [luna.schaetzle.website@gmail.com](mailto: luna.schaetzle.website@gmail.com]
- GitHub: [luna-schaetzle](https://github.com/Luna-Schaetzle)
- LinkedIn: [luna-schaetzle](https://www.linkedin.com/in/luna-schaetzle/)
- Meiner Website: [luna-schaetzle.xyz](https://luna-schaetzle.xyz)



