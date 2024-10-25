from tools import create_feedback_note_tool, create_ticket_tool, escalate_issue_tool

import ell

system_message = """
            You are a Customer Service Agent.
            
            Your job is to understand user feedback, decide what action to take and apply the tool to take the action.

            Your task is:
            1. Read the user's feedback.
            2. Decide what action to take.
            3. Use the tools provided to take the action.
            
            These are the decisions you can make and their corresponding actions:
            1. If the user requires immediate help to prevent further damage, escalate the issue to a human.
            2. If the user is reporting on something that needs to be fixed or looked into at some point, create a task.
            3. If the user is providing general feedback, create a feedback note.
            4. If you think no action is required, you can ignore the feedback.
            
            You are done when you have taken the action.
        """

@ell.complex(model="gpt-4-turbo", tools=[create_ticket_tool, escalate_issue_tool, create_feedback_note_tool])
def process_message(message: str, user_id: str):
    return [
        ell.system(system_message),
        ell.user(f"User {user_id} sent the following message: {message}")
    ]