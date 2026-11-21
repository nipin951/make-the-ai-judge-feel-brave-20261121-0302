"""Make the AI judge feel brave — writes one short relaxing text to /output/entry.txt."""

import os

TEXT = (
    "The verdict can wait. Outside, the rain has stopped, and somewhere a "
    "kettle is coming off the boil. Nothing here needs you yet. Read slowly: "
    "the next word will still be here when you reach it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
