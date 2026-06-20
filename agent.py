from skills.planner import validate_inputs


class CourseCompletionCoachAgent:

    def create_plan(self, course_name, hours_per_week, deadline, goal):
        validate_inputs(course_name, hours_per_week, deadline, goal)

        return f"""
Course Completion Plan

Course: {course_name}
Hours per week: {hours_per_week}
Deadline: {deadline}
Goal: {goal}

Week 1:
- Review capstone requirements.
- Choose the Concierge Agents track.
- Build the basic agent code.
- Test the command-line demo.

Week 2:
- Improve README documentation.
- Add architecture diagram.
- Record a short demo video.
- Upload the video to YouTube.

Final Checklist:
- Public GitHub repository
- README with setup instructions
- Kaggle Writeup
- Cover image
- YouTube demo video
- Public project link

Security Notes:
- No API keys are stored in code.
- User input is validated.
- No personal data is saved.
"""
