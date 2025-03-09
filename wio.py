import os
import sys
import configparser
from PIL import Image

# Programmname und Version
PROGRAM_NAME = "WebImageOptimizer (WIO)"
VERSION = "1.0"

def load_config(config_path="config.ini"):
    config = configparser.ConfigParser()
    config.read(config_path)

    settings = config["settings"]
    rename = settings.getboolean("rename", fallback=True)
    prefix = settings.get("prefix", fallback="image_")
    start_number = settings.getint("start_number", fallback=1)
    numbering_digits = settings.getint("numbering_digits", fallback=3)  # Anzahl der Ziffern für die Nummerierung
    img_format = settings.get("format", fallback="webp").lower()
    quality = settings.getint("quality", fallback=80)

    return rename, prefix, start_number, numbering_digits, img_format, quality

def optimize_images(input_folder, output_folder, config_path="config.ini"):
    print(f"{PROGRAM_NAME} v{VERSION} - Optimierung gestartet...")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    rename, prefix, start_number, numbering_digits, img_format, quality = load_config(config_path)

    supported_formats = (".jpg", ".jpeg", ".png", ".webp")
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_formats)]
    files.sort()  # Sortiert die Dateien, um eine konsistente Reihenfolge zu haben

    if not files:
        print("❌ Keine Bilder zum Optimieren gefunden.")
        return

    count = start_number

    for file in files:
        input_path = os.path.join(input_folder, file)
        with Image.open(input_path) as img:
            img = img.convert("RGB")  # RGB-Modus für Web-Bilder

            number_str = str(count).zfill(numbering_digits)  # Führende Nullen je nach Einstellung
            new_filename = f"{number_str}-{prefix}.{img_format}" if rename else f"{number_str}-{os.path.splitext(file)[0]}.{img_format}"
            output_path = os.path.join(output_folder, new_filename)

            img.save(output_path, format=img_format.upper(), quality=quality)
            print(f"✅ Gespeichert: {output_path}")

            count += 1

    print("🎉 Optimierung abgeschlossen!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"{PROGRAM_NAME} v{VERSION}")
        print("❌ Falsche Nutzung!")
        print("Verwendung: python wio.py <input_folder> <output_folder>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]

    optimize_images(input_folder, output_folder)
