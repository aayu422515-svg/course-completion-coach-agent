def validate_inputs(course_name, hours_per_week, deadline, goal):
    if not course_name.strip():
        raise ValueError("Course name is required.")

    if hours_per_week <= 0 or hours_per_week > 40:
        raise ValueError("Hours per week must be between 1 and 40.")

    if not deadline.strip():
        raise ValueError("Deadline is required.")

    if not goal.strip():
        raise ValueError("Goal is required.")


def build_planning_prompt(course_name, hours_per_week, deadline, goal):
    return f"""
You are a Course Completion Coach Agent.

Create a realistic study plan.

Course: {course_name}
Hours available per week: {hours_per_week}
Deadline: {deadline}
Goal: {goal}

Requirements:
- Create a week-by-week study plan.
- Include milestones.
- Include final submission checklist.
- Keep recommendations realistic.
- Do not ask for sensitive personal information.
"""
