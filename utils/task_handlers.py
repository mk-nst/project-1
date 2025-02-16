from datetime import datetime
from utils.file_utils import read_file, write_file

def count_wednesdays(input_path: str, output_path: str):
    dates = read_file(input_path).splitlines()
    wednesdays = [date for date in dates if datetime.strptime(date, "%Y-%m-%d").weekday() == 2]
    write_file(output_path, str(len(wednesdays)))

task_handlers = {
    "count_wednesdays": count_wednesdays,
    # Add other tasks here
}

def handle_task(task: str):
    # Parse the task description and call the appropriate handler
    if "count" in task and "wednesdays" in task:
        count_wednesdays("/data/dates.txt", "/data/dates-wednesdays.txt")
    # Add other conditions for other tasks