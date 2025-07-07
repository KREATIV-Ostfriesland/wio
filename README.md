# WebImageOptimizer (WIO)

WebImageOptimizer (WIO) ist ein einfaches, aber leistungsstarkes Python-Tool zur Optimierung von Bildern für Webseiten. Es liest Bilder aus einem angegebenen Ordner, optimiert sie durch Komprimierung und speichert sie in einem gewünschten Format.

## Funktionen

- **Automatische Bildoptimierung** für Webnutzung (JPG, PNG, WEBP)
- **Umbenennen der Bilder** mit konfigurierbarer Nummerierung
- **Anpassbare Kompression & Qualität**
- **Bildgröße anpassbar (maximale Breite oder Höhe wählbar)**
- **Einfache Konfiguration über `config.ini`**

## Installation

### Voraussetzungen

WIO benötigt Python 3 und die `Pillow`-Bibliothek. Installiere die Abhängigkeiten mit:

```bash
pip install pillow
```

## Nutzung

Das Skript wird über die Kommandozeile ausgeführt:

```bash
python wio.py <input_folder> <output_folder> <logo-file.png>
```

Beispiel:

```bash
python wio.py ./input ./output ./logo.png
```

- `<input_folder>`: Ordner mit den Originalbildern
- `<output_folder>`: Ordner, in den optimierte Bilder gespeichert werden
- `<logo-file.png>`: Logo, welches in das Bild eingearbeitet wird (Postion wird in der Confi.ini gesetzt)

## Konfiguration (`config.ini`)


WIO verwendet eine `config.ini`, um Einstellungen anzupassen:

```ini
[settings]
rename = true  # Bilder umbenennen (true/false)
prefix = "imagename"  # Präfix für neue Namen
start_number = 1  # Startnummer für Umbenennung
numbering_digits = 3  # Anzahl der Stellen für die Nummerierung (z. B. 001, 01, 1)
format = "webp"  # Ausgabeformat: jpg, png oder webp
quality = 80  # Qualitätsstufe (1-100)
max_width = 1920  # Maximale Breite (0 = keine Änderung)
max_height = 1080  # Maximale Höhe (0 = keine Änderung)
# Position des Logos im Bild (top-left, top-right, bottom-left, bottom-right)
logo_position = bottom-right
```

## Unterstützte Formate

WIO kann folgende Bildformate als Input verarbeiten:

- `.jpg`, `.jpeg`
- `.png`
- `.webp`

Die optimierten Bilder können in einem der folgenden Formate gespeichert werden:

- **JPG** (gut für Fotos, hohe Kompression)
- **PNG** (verlustfrei, für transparente Bilder)
- **WEBP** (modernes Format mit hoher Effizienz)

## Beispielausgabe

```
WebImageOptimizer (WIO) v1.0 - Optimierung gestartet...
✅ Gespeichert: ./output/001-imagename.webp
✅ Gespeichert: ./output/002-imagename.webp
🎉 Optimierung abgeschlossen!
```

## Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**.

## Autor

Entwickelt von KREATIV-Ostfriesland 🚀

