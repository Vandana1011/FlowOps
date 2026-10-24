# FlowOps — AI Workflow Automation Server

A Python-based task workflow management server built with FastMCP.

## Features
- Create, list, retrieve, update, and delete tasks
- Search tasks by keyword
- Set task priorities and deadlines
- Track task status
- Export task data to CSV
- JSON backup and restore in the notebook
- Task reports, activity logs, and visualizations in the notebook
- Automated tests

## Technology Stack
- Python 3.12
- FastMCP
- Pandas
- Matplotlib
- JSON and CSV

## Installation
Install dependencies:
```bash
pip install -r requirements.txt
```

## Run the MCP Server
```bash
python server.py
```

## Testing
Six automated checks passed in the current notebook test run.
They cover task creation, listing, searching, status updates, priorities, and deadlines.

## Important Note
The current server stores tasks in memory. Server tasks are not automatically
saved after the server process stops.

## Future Improvements
- Persistent database storage
- Authentication and access control
- LLM-powered task planning
- Multi-agent workflow coordination

## Author
Vandana Vajji
