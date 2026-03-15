import json
import os
from pathlib import Path

# project root
ROOT_DIR = Path(__file__).resolve().parent.parent

INPUT_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "cleaned_data"

OUTPUT_DIR.mkdir(exist_ok=True)


def extract_target(pos_candidates):
    """Extract relevant element information."""
    if not pos_candidates:
        return None

    elem = pos_candidates[0]

    return {
        "tag": elem.get("tag"),
        "attributes": elem.get("attributes"),
        "backend_node_id": elem.get("backend_node_id")
    }


def clean_action(action):

    operation = action.get("operation", {})

    return {
        "action_type": operation.get("op"),
        "value": operation.get("value"),
        "target_element": extract_target(action.get("pos_candidates", []))
    }


def clean_instance(instance):

    cleaned = {
        "task": instance.get("confirmed_task"),
        "website": instance.get("website"),
        "actions": []
    }

    for action in instance.get("actions", []):
        cleaned["actions"].append(clean_action(action))

    return cleaned


def process_file(input_path, output_path):

    with open(input_path) as f:
        data = json.load(f)

    cleaned_data = [clean_instance(x) for x in data]

    with open(output_path, "w") as f:
        json.dump(cleaned_data, f, indent=2)


def main():

    input_file = INPUT_DIR / "train_0.json"
    output_file = OUTPUT_DIR / "train_0_cleaned.json"

    print("Input:", input_file)
    print("Output:", output_file)

    process_file(input_file, output_file)

    print("Finished cleaning.")


if __name__ == "__main__":
    main()