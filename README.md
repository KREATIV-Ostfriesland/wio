# WebImageOptimizer (WIO)

WebImageOptimizer (WIO) ist ein einfaches, aber leistungsstarkes Python-Tool zur Optimierung von Bildern für Webseiten. Es liest Bilder aus einem angegebenen Ordner, optimiert sie durch Komprimierung und speichert sie in einem gewünschten Format.

## Funktionen

- **Automatische Bildoptimierung** für Webnutzung (JPG, PNG, WEBP)
- **Umbenennen der Bilder** mit konfigurierbarer Nummerierung
- **Anpassbare Kompression & Qualität**
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
python wio.py <input_folder> <output_folder>
```

Beispiel:

```bash
python wio.py ./input ./output
```

- `<input_folder>`: Ordner mit den Originalbildern
- `<output_folder>`: Ordner, in den optimierte Bilder gespeichert werden

## Konfiguration (`config.ini`)

WIO verwendet eine `config.ini`, um Einstellungen anzupassen:

```ini
[settings]
rename = true  # Bilder umbenennen (true/false)
prefix = "image_"  # Präfix für neue Namen
start_number = 1  # Startnummer für Umbenennung
numbering_digits = 3  # Anzahl der Stellen für die Nummerierung (z. B. 001, 01, 1)
format = "webp"  # Ausgabeformat: jpg, png oder webp
quality = 80  # Qualitätsstufe (1-100)
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
✅ Gespeichert: ./output/image_001.webp
✅ Gespeichert: ./output/image_002.webp
🎉 Optimierung abgeschlossen!
```

## Lizenz

Dieses Projekt steht unter der **MIT-Lizenz**.

## Autor

Entwickelt von KREATIV-Ostfriesland 🚀

