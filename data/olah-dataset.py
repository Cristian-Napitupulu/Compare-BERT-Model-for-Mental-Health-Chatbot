import pandas as pd

# Load the Excel file
excel_file_path = (
    "./data/Test-Set-Mental-Health-with-Tags.xlsx"  # Replace with your Excel file path
)
df = pd.read_excel(excel_file_path)

# Convert the DataFrame to a dictionary
data = {"topics": []}

# Group the data by Topic
for topic, group in df.groupby("Topik"):
    topic_data = {"topic": topic, "answers": []}

    for tag, answer_group in group.groupby("Tag"):
        answer_data = {
            "tag": tag,
            "answer": answer_group["Jawaban"].iloc[0],
            "questions": answer_group["Pertanyaan"].tolist(),
        }
        topic_data["answers"].append(answer_data)

    data["topics"].append(topic_data)

# Convert the dictionary to JSON and save to a file
import json

json_file_path = (
    "./data/test-set-mental-health-with-tag.json"  # Replace with your desired output file path
)
with open(json_file_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Converted Excel data to JSON and saved to {json_file_path}")
