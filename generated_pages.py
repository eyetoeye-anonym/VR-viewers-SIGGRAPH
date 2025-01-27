import os

VIEWERS_DIR = "./viewers"
IMAGES_DIR = "./images"

OUTPUT_INDEX_HTML = "index.html"
OUTPUT_COMPARISON_HTML = "comparison.html"
OUTPUT_RESULTS_HTML = "results.html"

def parse_prompt(folder_name: str) -> str:
    """
    Removes known suffixes from folder_name to find the base name.
    For example:
      "a_classic_office_with_a_desk_and_a_chair_comparison_spatial"
      -> "a_classic_office_with_a_desk_and_a_chair"
    """
    known_suffixes = ["_comparison_spatial", "_comparison_temporal", "_ours"]
    for suffix in known_suffixes:
        if folder_name.endswith(suffix):
            return folder_name[: -len(suffix)]
    return folder_name

def generate_main_index():
    """
    Generates index.html with two buttons that link to comparison.html and results.html
    """
    html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <title>Main Page</title>
    <style>
        body {
            background: #f5f5f5;
            font-family: sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            margin-bottom: 2rem;
        }
        .button {
            background-color: #2E7D32;
            color: white;
            border: none;
            padding: 15px 30px;
            margin: 10px;
            font-size: 18px;
            border-radius: 8px;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        .button:hover {
            background-color: #1b5e20;
        }
    </style>
</head>
<body>
    <h1></h1>
    <button class="button" onclick="window.location.href='results.html'">View Our Results In VR!</button>
    <button class="button" onclick="window.location.href='comparison.html'">Comparison to Warp & Inpaint Baseline, in VR</button>
</body>
</html>
"""
    with open(OUTPUT_INDEX_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {OUTPUT_INDEX_HTML}")


def generate_comparison_page(comparison_folders):
    """
    Generates comparison.html. Displays thumbnails for each folder ending with '_comparison_spatial'.
    Clicking a thumbnail goes to the folder's index.html in ./viewers/<folder>/index.html.
    Thumbnails are looked up at images/<base_name>.png
    """
    cards = []
    for folder in comparison_folders:
        # The VR viewer index path
        viewer_path = os.path.join(VIEWERS_DIR, folder, "index.html").replace("\\", "/")

        # Parse the "prompt" by stripping off suffix
        prompt = parse_prompt(folder)
        # Look for a .png in the images folder
        thumb_path = os.path.join(IMAGES_DIR, f"{prompt}.png")
        if os.path.isfile(thumb_path):
            thumb_rel = thumb_path.replace("\\", "/")
        else:
            # fallback or placeholder
            thumb_rel = "https://via.placeholder.com/300x200?text=No+Thumbnail"

        cards.append(f"""
        <div class="card">
            <a href="{viewer_path}" target="_blank">
                <img src="{thumb_rel}" alt="{folder}" />
            </a>

        </div>
        """)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <title>Comparison View</title>
    <style>
        body {{
            background: #f5f5f5;
            font-family: sans-serif;
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .card {{
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            text-align: center;
            padding: 10px;
        }}
        .card img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto 10px;
        }}
        .back-button {{
            display: inline-block;
            margin-bottom: 20px;
            background-color: #666;
            color: #fff;
            padding: 10px 20px;
            border-radius: 6px;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <h1>Comparison: _comparison_spatial</h1>
    <a href="index.html" class="back-button">Back to Main</a>
    <div class="grid">
        {''.join(cards)}
    </div>
</body>
</html>
"""

    with open(OUTPUT_COMPARISON_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {OUTPUT_COMPARISON_HTML} with {len(comparison_folders)} entries.")


def generate_results_page(results_folders):
    """
    Generates results.html. Displays thumbnails for each folder ending with '_ours'.
    Clicking a thumbnail goes to the folder's index.html in ./viewers/<folder>/index.html.
    Thumbnails are looked up at images/<base_name>.png
    """
    cards = []
    for folder in results_folders:
        # The VR viewer index path
        viewer_path = os.path.join(VIEWERS_DIR, folder, "index.html").replace("\\", "/")

        # Parse the "prompt" by stripping off suffix
        prompt = parse_prompt(folder)
        # Look for a .png in the images folder
        thumb_path = os.path.join(IMAGES_DIR, f"{prompt}.png")
        if os.path.isfile(thumb_path):
            thumb_rel = thumb_path.replace("\\", "/")
        else:
            # fallback or placeholder
            thumb_rel = "https://via.placeholder.com/300x200?text=No+Thumbnail"

        cards.append(f"""
        <div class="card">
            <a href="{viewer_path}" target="_blank">
                <img src="{thumb_rel}" alt="{folder}" />
            </a>
        </div>
        """)

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8"/>
    <title>Results View</title>
    <style>
        body {{
            background: #f5f5f5;
            font-family: sans-serif;
            margin: 0;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
            margin-bottom: 20px;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .card {{
            background: #fff;
            border: 1px solid #ddd;
            border-radius: 8px;
            overflow: hidden;
            text-align: center;
            padding: 10px;
        }}
        .card img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 0 auto 10px;
        }}
        .back-button {{
            display: inline-block;
            margin-bottom: 20px;
            background-color: #666;
            color: #fff;
            padding: 10px 20px;
            border-radius: 6px;
            text-decoration: none;
        }}
    </style>
</head>
<body>
    <h1>Click the images to enter the VR viewrs.</h1>
    <a href="index.html" class="back-button">Back to Main</a>
    <div class="grid">
        {''.join(cards)}
    </div>
</body>
</html>
"""

    with open(OUTPUT_RESULTS_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated {OUTPUT_RESULTS_HTML} with {len(results_folders)} entries.")


def main():
    # Create lists to hold folder names matching specific patterns
    comparison_folders = []
    results_folders = []

    # Gather all subfolders in VIEWERS_DIR
    for item in os.listdir(VIEWERS_DIR):
        if item.startswith("."):
            # Skip hidden items like .DS_Store
            continue
        full_path = os.path.join(VIEWERS_DIR, item)
        if os.path.isdir(full_path):
            # Identify if folder name ends with "_comparison_spatial" or "_ours"
            if item.endswith("_comparison_spatial"):
                comparison_folders.append(item)
            elif item.endswith("_ours"):
                results_folders.append(item)

    # Sort them if desired
    comparison_folders.sort()
    results_folders.sort()

    # Generate the three pages
    generate_main_index()
    generate_comparison_page(comparison_folders)
    generate_results_page(results_folders)


if __name__ == "__main__":
    main()
