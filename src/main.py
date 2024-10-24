import json

from db import truncate_all_data
from message_processor_agent import create_message_processor_crew

# litellm.set_verbose = True

def main():
    truncate_all_data()
    
    with open('data/example-feedback-data.json', 'r') as file:
        feedback_data = json.load(file)

    for item in feedback_data:
        print("######## PROCESSING NEXT FEEDBACK MESSAGE ########")
        # create a new crew instance for each feedback message
        crew = create_message_processor_crew()
        crew.kickoff(
            {"feedback": item["message"], "user_id": item["user_id"]},
        )


if __name__ == "__main__":
    main()
