import os
import sys
import configparser
from PIL import Image

# Programmname und Version
PROGRAM_NAME = "WebImageOptimizer (WIO)"
VERSION = "1.3"

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
    logo_position = settings.get("logo_position", fallback="bottom-right")

    return rename, prefix, start_number, numbering_digits, img_format, quality, max_width, max_height, logo_position

def resize_image(img, max_width, max_height):
    original_width, original_height = img.size

    if (max_width == 0 or original_width <= max_width) and (max_height == 0 or original_height <= max_height):
        return img

    scale_w = max_width / original_width if max_width > 0 else float('inf')
    scale_h = max_height / original_height if max_height > 0 else float('inf')
    scale_factor = min(scale_w, scale_h)

    new_width = int(original_width * scale_factor)
    new_height = int(original_height * scale_factor)

    return img.resize((new_width, new_height), Image.LANCZOS)

def add_logo(base_image, logo_path, position):
    if not logo_path or not os.path.isfile(logo_path):
        print(f"⚠️ Logo-Datei nicht gefunden oder nicht angegeben: {logo_path}")
        return base_image

    try:
        logo = Image.open(logo_path).convert("RGBA")
    except Exception as e:
        print(f"⚠️ Fehler beim Laden des Logos: {e}")
        return base_image

    base_image = base_image.convert("RGBA")

    logo_width = int(base_image.width * 0.15)
    logo_ratio = logo_width / logo.width
    logo_height = int(logo.height * logo_ratio)
    logo = logo.resize((logo_width, logo_height), Image.LANCZOS)

    margin = 10
    if position == "top-left":
        x, y = margin, margin
    elif position == "top-right":
        x = base_image.width - logo.width - margin
        y = margin
    elif position == "bottom-left":
        x = margin
        y = base_image.height - logo.height - margin
    elif position == "bottom-right":
        x = base_image.width - logo.width - margin
        y = base_image.height - logo.height - margin
    else:
        print(f"⚠️ Ungültige logo_position '{position}', benutze 'bottom-right' als Fallback.")
        x = base_image.width - logo.width - margin
        y = base_image.height - logo.height - margin

    base_image.paste(logo, (x, y), logo)
    return base_image.convert("RGB")

def optimize_images(input_folder, output_folder, logo_path=None, config_path="config.ini"):
    print(f"{PROGRAM_NAME} v{VERSION} - Optimierung gestartet...")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    (
        rename,
        prefix,
        start_number,
        numbering_digits,
        img_format,
        quality,
        max_width,
        max_height,
        logo_position
    ) = load_config(config_path)

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
            img = img.convert("RGB")
            original_size = img.size
            img = resize_image(img, max_width, max_height)
            resized_size = img.size

            if logo_path:
                img = add_logo(img, logo_path, logo_position)

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
    if len(sys.argv) < 3 or len(sys.argv) > 4:
        print(f"{PROGRAM_NAME} v{VERSION}")
        print("❌ Falsche Nutzung!")
        print("Verwendung: python wio.py <input_folder> <output_folder> [logo_path]")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    logo_path = sys.argv[3] if len(sys.argv) == 4 else None

    optimize_images(input_folder, output_folder, logo_path)
