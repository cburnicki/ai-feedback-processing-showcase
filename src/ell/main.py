import json
from pprint import pprint

from db import truncate_all_data
from task import process_message


def main():
    truncate_all_data()
    
    with open('data/example-feedback-data.json', 'r') as file:
        feedback_data = json.load(file)

    for item in feedback_data:
        print("######## PROCESSING NEXT FEEDBACK MESSAGE ########")
        result = process_message(item["message"], item["user_id"])
        print(result.text)
        if result.tool_calls:
            # This is done so that we can pass the tool calls to the language model
            result_message = result.call_tools_and_collect_as_message()
            print(result_message)


if __name__ == "__main__":
    main()
