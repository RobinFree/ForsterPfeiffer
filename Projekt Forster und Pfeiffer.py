

import xml.etree.ElementTree as ET
import os

print("Aktuelles Arbeitsverzeichnis:", os.getcwd())

def xml_datei_einlesen(pfeiffer1):
    """Liest eine XML-Datei ein und gibt das Wurzelelement zurück."""
    try:
        baum = ET.parse(pfeiffer1)
        return baum.getroot()
    except FileNotFoundError:
        print(f"Fehler: Datei '{pfeiffer1}' nicht gefunden.")
    except ET.ParseError:
        print(f"Fehler: Datei '{pfeiffer1}' konnte nicht als XML geparst werden.")
    except Exception as e:
        print(f"Unerwarteter Fehler beim Einlesen von '{pfeiffer1}': {e}")
    return None

def extrahiere_titel(wurzel):
    """Extrahiert den Titel aus der XML-Datei."""
    try:
        titel_element = wurzel.find(".//title[@type='main']")
        return titel_element.text if titel_element is not None else None
    except Exception as e:
        print(f"Fehler beim Extrahieren des Titels: {e}")
        return None

def extrahiere_autor(wurzel):
    """Extrahiert den Autor aus der XML-Datei."""
    try:
        autor_element = wurzel.find(".//persName/surname")
        return autor_element.text if autor_element is not None else None
    except Exception as e:
        print(f"Fehler beim Extrahieren des Autors: {e}")
        return None

def verarbeite_datei(pfeiffer1, bezeichner):
    """Liest eine XML-Datei ein, extrahiert Titel und Autor und gibt sie aus."""
    wurzel = xml_datei_einlesen(pfeiffer1)
    if wurzel is not None:
        titel = extrahiere_titel(wurzel)
        autor = extrahiere_autor(wurzel)
        if titel and autor:
            print("=" * 80)
            print(f"Titel ({bezeichner}): {titel}")
            print(f"Autor ({bezeichner}): {autor}")
        else:
            print(f"Fehlende Informationen in der Datei '{bezeichner}'.")
    else:
        print(f"Verarbeitung von '{bezeichner}' fehlgeschlagen.")

# Beispielaufrufe
verarbeite_datei("C:/Users/alina/OneDrive/Dokumente/Uni Basel/2. Semester/(De-)Coding History/Projekt/forster1.xml", "Forster1")
verarbeite_datei("C:/Users/alina/OneDrive/Dokumente/Uni Basel/2. Semester/(De-)Coding History/Projekt/pfeiffer1.xml", "Pfeiffer1")




def extrahiere_titel(wurzel):
    """Extrahiert den Haupttitel aus der XML-Datei."""
    ns = {"tei": "http://www.tei-c.org/ns/1.0"}  # Namespace definieren
    try:
        titel_element = wurzel.find(".//tei:title[@type='main']", namespaces=ns)
        return titel_element.text if titel_element is not None else None
    except Exception as e:
        print(f"Fehler beim Extrahieren des Titels: {e}")
        return None


def extrahiere_autor(wurzel):
    """Extrahiert den Autor aus der XML-Datei."""
    ns = {"tei": "http://www.tei-c.org/ns/1.0"}
    try:
        vorname = wurzel.find(".//tei:author/tei:persName/tei:forename", namespaces=ns)
        nachname = wurzel.find(".//tei:author/tei:persName/tei:surname", namespaces=ns)
        if vorname is not None and nachname is not None:
            return f"{vorname.text} {nachname.text}"
        elif nachname is not None:
            return nachname.text
        else:
            return None
    except Exception as e:
        print(f"Fehler beim Extrahieren des Autors: {e}")
        return None



