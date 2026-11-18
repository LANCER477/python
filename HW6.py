import json
import os
from datetime import datetime

LOG_FILENAME = "runs.json"


def read_launch_history(filename: str) -> list[dict]:
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            return []
    except (OSError, json.JSONDecodeError):
        return []


def save_launch_history(filename: str, history: list[dict]) -> bool:
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4, ensure_ascii=False)
        return True
    except OSError:
        return False


def main():
    history = read_launch_history(LOG_FILENAME)

    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_run = {
        "id": len(history) + 1,
        "timestamp": now_str
    }
    history.append(current_run)

    save_launch_history(LOG_FILENAME, history)

    for run in history:
        print(f"{run['id']} {run['timestamp']}")


if __name__ == "__main__":
    main()
