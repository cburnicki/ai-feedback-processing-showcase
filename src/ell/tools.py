from typing import Optional

from db import escalations_db, feedback_db, tasks_db

import ell


@ell.tool()
def create_ticket_tool(ticket_description: str, user_id: Optional[str] = None):
    """Create a ticket in the ticket system that will be reviewed and solved later by a team member"""
    tasks_db.insert({"task": ticket_description, "user_id": user_id})
    return "Task saved"


@ell.tool()
def escalate_issue_tool(issue_description: str, user_id: Optional[str] = None):
    """Immediately escalate an urgent issue to a human"""
    escalations_db.insert({"issue": issue_description, "user_id": user_id})
    return "A human has been informed!"


@ell.tool()
def create_feedback_note_tool(feedback_description: str, user_id: Optional[str] = None):
    """Create a general feedback note for the team to review"""
    feedback_db.insert({"feedback": feedback_description, "user_id": user_id})
    return "Feedback note saved"
