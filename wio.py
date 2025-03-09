import os
import sys
import configparser
from PIL import Image

# Programmname und Version
PROGRAM_NAME = "WebImageOptimizer (WIO)"
VERSION = "1.2"

def load_config(config_path="config.ini"):
    config = configparser.ConfigParser()
    config.read(config_path)

    settings = config["settings"]
    rename = settings.getboolean("rename", fallback=True)
    prefix = settings.get("prefix", fallback="imagename")
    start_number = settings.getint("start_number", fallback=1)
    numbering_digits = settings.getint("numbering_digits", fallback=3)
    img_format = settings.get("format", fallback="webp").strip('"').strip("'").lower()
    quality = settings.getint("quality", fallback=80)
    max_width = settings.getint("max_width", fallback=0)  # 0 bedeutet keine Änderung
    max_height = settings.getint("max_height", fallback=0)  # 0 bedeutet keine Änderung

    return rename, prefix, start_number, numbering_digits, img_format, quality, max_width, max_height

def resize_image(img, max_width, max_height):
    """Skaliert das Bild proportional, sodass es in die max. Breite/Höhe passt."""
    original_width, original_height = img.size

    # Kein Resizing notwendig
    if (max_width == 0 or original_width <= max_width) and (max_height == 0 or original_height <= max_height):
        return img

    # Berechnung des Skalierungsfaktors unter Beibehaltung des Seitenverhältnisses
    scale_w = max_width / original_width if max_width > 0 else float('inf')
    scale_h = max_height / original_height if max_height > 0 else float('inf')
    scale_factor = min(scale_w, scale_h)

    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    return img.resize((new_width, new_height), Image.LANCZOS)

def optimize_images(input_folder, output_folder, config_path="config.ini"):
    print(f"{PROGRAM_NAME} v{VERSION} - Optimierung gestartet...")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    rename, prefix, start_number, numbering_digits, img_format, quality, max_width, max_height = load_config(config_path)

    supported_formats = (".jpg", ".jpeg", ".png", ".webp")
    files = [f for f in os.listdir(input_folder) if f.lower().endswith(supported_formats)]
    files.sort()

    if not files:
        print("❌ Keine Bilder zum Optimieren gefunden.")
        return

    count = start_number

    for file in files:
        input_path = os.path.join(input_folder, file)
        with Image.open(input_path) as img:
            img = img.convert("RGB")  # RGB-Modus für Web-Bilder

            # Falls nötig, Bildgröße proportional anpassen
            original_size = img.size
            img = resize_image(img, max_width, max_height)
            resized_size = img.size

            # Nummerierung mit führenden Nullen
            number_str = str(count).zfill(numbering_digits)
            new_filename = f"{number_str}-{prefix}.{img_format}" if rename else f"{number_str}-{os.path.splitext(file)[0]}.{img_format}"
            output_path = os.path.join(output_folder, new_filename)

            img.save(output_path, format=img_format.upper(), quality=quality)

            if original_size != resized_size:
                print(f"✅ {new_filename} (Skaliert auf {resized_size[0]}x{resized_size[1]})")
            else:
                print(f"✅ {new_filename} (Originalgröße beibehalten)")

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
