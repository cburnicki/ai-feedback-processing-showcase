from typing import Optional

from crewai_tools import tool

from db import escalations_db, feedback_db, tasks_db


@tool("Save Task Tool")
def create_task_tool(task_description: str, user_id: Optional[str] = None):
    """Create a task that will be reviewed and solved later by a team member"""
    tasks_db.insert({"task": task_description, "user_id": user_id})
    return "Task saved"


@tool("Escalate issue tool")
def escalate_issue_tool(issue_description: str, user_id: Optional[str] = None):
    """Immediately escalate an urgent issue to a human"""
    escalations_db.insert({"issue": issue_description, "user_id": user_id})
    return "A human has been informed!"


@tool("Create Feedback Note Tool")
def create_feedback_note_tool(feedback_description: str, user_id: Optional[str] = None):
    """Create a general feedback note for the team to review"""
    feedback_db.insert({"feedback": feedback_description, "user_id": user_id})
    return "Feedback note saved"
