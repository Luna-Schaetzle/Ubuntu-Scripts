#!/bin/bash

# Name der virtuellen Umgebung
VENV_NAME="venv"

# Verzeichnis der virtuellen Umgebung
VENV_DIR="./$VENV_NAME"

# Überprüfen, ob die venv existiert
if [ ! -d "$VENV_DIR" ]; then
    echo "Virtuelle Umgebung existiert nicht. Bitte führe zuerst create_venv.sh aus."
    exit 1
fi

# Aktivieren der virtuellen Umgebung
source "$VENV_DIR/bin/activate"

# Skriptname, das ausgeführt werden soll
SCRIPT_NAME="$1"

# Überprüfen, ob ein Skriptname angegeben wurde
if [ -z "$SCRIPT_NAME" ]; then
    echo "Bitte gib den Namen des Skripts an, das ausgeführt werden soll."
    exit 1
fi

# Ausführen des angegebenen Skripts
python "$SCRIPT_NAME"

# Deaktivieren der virtuellen Umgebung
deactivate

echo "Skript $SCRIPT_NAME wurde ausgeführt und die virtuelle Umgebung wurde deaktiviert."
