import pathlib
import json


def main():
    images = pathlib.Path().glob("*.png")

    vn_name_map = {
        "adastra": "Adastra",
        "bth": "Beyond The Harbor",
        "echo": "Echo",
        "fbi": "Fueled By Insanity",
        "flw": "Four Letter Word",
        "pervader": "Pervader",
        "repeat": "Repeat",
        "ta": "Tennis Ace",
        "tsr": "The Smoke Room",
    }

    husbandos = []

    for file in images:
        filename = str(file)[:-4]

        game, character = filename.split("_")

        husbandos.append(
            {
                "name": character.capitalize(),
                "sourceVisualNovel": vn_name_map[game],
                "image": f"img/{file}",
            }
        )

    with open("aaa_husbando_database.json", "w") as f:
        json.dump(husbandos, f, indent=4)




if __name__ == "__main__":
    main()
