from datetime import datetime, timedelta

def calculate_priority(task):
    days_left = (task.deadline - datetime.now().date()).days
    urgency = max(0, 10 - days_left)  # closer deadline = higher urgency
    difficulty_weight = task.difficulty
    importance_weight = task.hours // 2
    return urgency + difficulty_weight + importance_weight

def generate_schedule(tasks, daily_hours):
    # Sort tasks by priority
    sorted_tasks = sorted(tasks, key=lambda t: calculate_priority(t), reverse=True)

    schedule = {}
    current_day = datetime.now().date()

    for task in sorted_tasks:
        hours_remaining = task.hours
        while hours_remaining > 0:
            if current_day not in schedule:
                schedule[current_day] = []
            available = daily_hours - sum([h['hours'] for h in schedule[current_day]])
            if available > 0:
                allocated = min(available, hours_remaining)
                schedule[current_day].append({
                    'task': task,
                    'hours': allocated
                })
                hours_remaining -= allocated
            else:
                current_day += timedelta(days=1)

    return schedule
