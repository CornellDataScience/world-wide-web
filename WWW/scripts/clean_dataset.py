import json
import os
from pathlib import Path

# Set up root and data directories
ROOT_DIR = Path(__file__).resolve().parent.parent
INPUT_DIR = ROOT_DIR / "data"
OUTPUT_DIR = ROOT_DIR / "data" / "processed"

# Create output directory if it doesn't exist
OUTPUT_DIR.mkdir(exist_ok=True)


def extract_target(pos_candidates):
    """Extract relevant element information from candidate elements."""
    # If no candidates exist, return None
    if not pos_candidates:
        return None

    # Take the first candidate element
    elem = pos_candidates[0]

    # Return only the relevant fields
    return {
        "tag": elem.get("tag"),
        "attributes": elem.get("attributes"),
        "backend_node_id": elem.get("backend_node_id")
    }


def clean_action(action):
    """Clean a single action by extracting useful fields."""
    operation = action.get("operation", {})

    # Extract the target element from candidates
    target = extract_target(action.get("pos_candidates", []))

    # Skip actions with no valid target
    if target is None:
        return None

    # Get the action type (e.g., click, type)
    action_type = operation.get("op")

    # Skip actions with no defined type
    if action_type is None:
        return None

    # Return cleaned action
    return {
        "action_type": action_type,
        "value": operation.get("value"),
        "target_element": target
    }


def clean_instance(instance):
    """Clean a full trajectory (task + actions)."""

    # Initialize cleaned structure
    cleaned = {
        "task": instance.get("confirmed_task"),
        "website": instance.get("website"),
        "actions": []
    }

    # Process each action in the trajectory
    for action in instance.get("actions", []):
        cleaned_action = clean_action(action)

        # Only keep valid actions
        if cleaned_action is not None:
            cleaned["actions"].append(cleaned_action)

    return cleaned


def process_file(input_path, output_path):
    """Load, clean, and save a dataset file."""

    # Load raw JSON data
    with open(input_path) as f:
        data = json.load(f)

    cleaned_data = []

    # Clean each instance in the dataset
    for instance in data:
        cleaned_instance = clean_instance(instance)

        # Remove empty trajectories (no valid actions)
        if cleaned_instance["actions"]:
            cleaned_data.append(cleaned_instance)

    # Save cleaned data to output file
    with open(output_path, "w") as f:
        json.dump(cleaned_data, f, indent=2)


def main():
    """Process all train files (train_0.json to train_10.json)."""

    # Loop through all dataset files
    for i in range(11):  
        input_file = INPUT_DIR / f"train_{i}.json"
        output_file = OUTPUT_DIR / f"train_{i}_cleaned.json"

        # Print progress for visibility
        print("Input:", input_file)
        print("Output:", output_file)

        process_file(input_file, output_file)

    print("Finished cleaning all files.")


if __name__ == "__main__":
    main()