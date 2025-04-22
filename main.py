# ethics_sandbox/main.py

import json
from datetime import datetime
from ethics_engine import evaluate_scenario
from model_bridge import get_model_response
from ui_terminal import display_result

# Load scenario from JSON file
def load_scenarios(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Save log entry to file
def log_response(scenario_id, question, response):
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "scenario_id": scenario_id,
        "question": question,
        "response": response
    }
    with open("logs/response_log.jsonl", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")


def run_sandbox():
    scenarios = load_scenarios("scenarios/scenario_bank.json")
    for s in scenarios:
        print("\n--- Running Scenario:", s["id"], "---")
        response = get_model_response(s["prompt"])
        moral_eval = evaluate_scenario(s, response)
        display_result(s["prompt"], response, moral_eval)
        log_response(s["id"], s["prompt"], response)


if __name__ == "__main__":
    run_sandbox()
