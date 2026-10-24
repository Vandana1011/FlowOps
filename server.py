
from fastmcp import FastMCP
from datetime import datetime, timezone

mcp = FastMCP("FlowOps")

tasks = {}
next_task_number = 1

def get_current_time():
    return datetime.now(timezone.utc).isoformat()

@mcp.tool()
def create_task(title: str, description: str = "") -> dict:
    global next_task_number
    task_id = next_task_number
    tasks[task_id] = {
        "id": task_id,
        "title": title,
        "description": description,
        "status": "pending",
        "created_at": get_current_time()
    }
    next_task_number += 1
    return tasks[task_id]

@mcp.tool()
def list_tasks() -> list:
    return list(tasks.values())

@mcp.tool()
def get_task(task_id: int) -> dict:
    if task_id not in tasks:
        return {"error": "Task not found"}
    return tasks[task_id]

@mcp.tool()
def update_task_status(task_id: int, status: str) -> dict:
    if task_id not in tasks:
        return {"error": "Task not found"}
    if status not in ["pending", "in_progress", "completed"]:
        return {"error": "Invalid status"}
    tasks[task_id]["status"] = status
    return tasks[task_id]

@mcp.tool()
def delete_task(task_id: int) -> dict:
    if task_id not in tasks:
        return {"error": "Task not found"}
    return {"deleted": tasks.pop(task_id)}

@mcp.tool()
def search_tasks(keyword: str) -> list:
    keyword = keyword.lower().strip()
    return [
        task for task in tasks.values()
        if keyword in task["title"].lower()
        or keyword in task["description"].lower()
    ]

@mcp.tool()
def set_task_priority(task_id: int, priority: str) -> dict:
    if task_id not in tasks:
        return {"error": "Task not found"}
    if priority not in ["low", "medium", "high"]:
        return {"error": "Invalid priority"}
    tasks[task_id]["priority"] = priority
    return tasks[task_id]

@mcp.tool()
def set_task_deadline(task_id: int, deadline: str) -> dict:
    if task_id not in tasks:
        return {"error": "Task not found"}
    try:
        parsed = datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        return {"error": "Use YYYY-MM-DD format"}
    tasks[task_id]["deadline"] = parsed.strftime("%Y-%m-%d")
    return tasks[task_id]

if __name__ == "__main__":
    mcp.run()
