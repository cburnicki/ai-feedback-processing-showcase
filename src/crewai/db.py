from tinydb import TinyDB


def _get_db(name: str) -> TinyDB:
    return TinyDB(f"data/db/{name}.json")


tasks_db = _get_db("tasks")
feedback_db = _get_db("feedback")
escalations_db = _get_db("escalations")

def truncate_all_data():
    tasks_db.truncate()
    feedback_db.truncate()
    escalations_db.truncate()