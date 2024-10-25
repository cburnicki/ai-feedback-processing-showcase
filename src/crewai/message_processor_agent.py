from tools import create_feedback_note_tool, create_ticket_tool, escalate_issue_tool

from crewai import Agent, Crew, Task


def create_message_processing_agent():
    return Agent(
        role="Customer Support Representative / Customer Service Agent",
        goal="Understand user feedback, decide what action to take and apply the tool to take the action.",
        backstory="You are an experienced customer support agent.",
        verbose=True,
        llm = 'ollama/llama3',
    )
    

def create_message_processing_task(agent: Agent):
    return Task(
        description=(
            """
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
            
            The user's user_id is: {user_id}
            
            This is the user's feedback:
            
            {feedback}
        """
        ),
        expected_output="Explain what action you took and why.",
        human_input=False,
        tools=[
            create_ticket_tool,
            create_feedback_note_tool,
            escalate_issue_tool
        ],
        agent=agent,
    )


def create_message_processor_crew():
    agent = create_message_processing_agent()
    task = create_message_processing_task(agent)
    return Crew(
        agents=[agent],
        tasks=[task],
    )

