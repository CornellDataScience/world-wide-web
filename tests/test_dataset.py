import json

DATA_PATH = "WWW/data/processed/train_0_cleaned.json"


def load_data():
    with open(DATA_PATH, "r") as f:
        return json.load(f)


# 1. Basic integrity
def test_no_null_entries():
    data = load_data()
    for sample in data:
        assert sample is not None


# 2. Required fields (based on real data)
def test_required_fields():
    data = load_data()
    for sample in data:
        assert "actions" in sample
        assert "website" in sample


# 3. Actions should not be empty
def test_actions_not_empty():
    data = load_data()
    for sample in data:
        assert len(sample["actions"]) > 0


# 4. Actions have correct structure
def test_actions_have_structure():
    data = load_data()

    for sample in data:
        for action in sample["actions"]:
            assert isinstance(action, dict)
            assert "action_type" in action


# 5. Action types are valid
def test_action_types_valid():
    data = load_data()

    valid_types = ["CLICK", "TYPE", "SELECT"]

    for sample in data:
        for action in sample["actions"]:
            assert action["action_type"] in valid_types


# 6. Actions contain some target info
def test_action_has_target_info():
    data = load_data()

    for sample in data:
        for action in sample["actions"]:
            # allow flexible naming depending on dataset
            assert any(
                key in action for key in ["target_element", "target", "element"]
            )

# 7. State transition / sequence consistency
def test_action_sequence_consistency():
    data = load_data()

    for sample in data:
        actions = sample["actions"]

        # must have at least one action
        assert len(actions) > 0

        # no repeated identical consecutive actions
        for i in range(1, len(actions)):
            assert actions[i] != actions[i - 1]


# 8. Action progression validity
def test_action_progression():
    data = load_data()

    for sample in data:
        actions = sample["actions"]

        for action in actions:
            assert "action_type" in action
            assert len(action.keys()) > 1