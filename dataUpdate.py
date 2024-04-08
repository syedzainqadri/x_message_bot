import json

# Load your existing JSON data
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Save the updated JSON data
def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Load responses from a text file
def load_responses(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

# Update the JSON data
def update_json_contents(json_data, responses):
    for i, user_data in enumerate(json_data):
        user_data["content"] = responses[i % len(responses)]

# Main function
def main():
    json_file_path = 'modifiedData.json'  # Replace with your JSON file path
    responses_file_path = 'newData.txt'  # Path to your responses text file
    json_data = load_json(json_file_path)
    responses = load_responses(responses_file_path)
    update_json_contents(json_data, responses)
    save_json(json_data, 'updateData.json')  # File path to save the updated JSON

if __name__ == "__main__":
    main()
