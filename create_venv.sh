#!/bin/bash

# Name der virtuellen Umgebung
VENV_NAME="venv"

# Verzeichnis, in dem die venv erstellt wird
VENV_DIR="./$VENV_NAME"

# Erstellen der virtuellen Umgebung, wenn sie nicht existiert
if [ ! -d "$VENV_DIR" ]; then
    echo "Erstelle virtuelle Umgebung..."
    python3 -m venv "$VENV_DIR"
    echo "Virtuelle Umgebung erstellt: $VENV_DIR"
else
    echo "Virtuelle Umgebung existiert bereits: $VENV_DIR"
fi

# Aktivieren der virtuellen Umgebung
source "$VENV_DIR/bin/activate"

# Installiere benötigte Pakete (füge hier deine Pakete hinzu)
pip install -r requirements.txt

echo "Virtuelle Umgebung aktiviert. Du kannst jetzt deine Skripte ausführen."
