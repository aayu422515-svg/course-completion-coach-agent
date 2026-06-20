from agent import CourseCompletionCoachAgent


def main():

    print("\nCourse Completion Coach Agent")
    print("-" * 40)

    course_name = input("Course Name: ")
    hours_per_week = int(
        input("Hours Available Per Week: ")
    )
    deadline = input("Deadline: ")
    goal = input("Goal: ")

    agent = CourseCompletionCoachAgent()

    plan = agent.create_plan(
        course_name,
        hours_per_week,
        deadline,
        goal
    )

    print("\nGenerated Plan")
    print("-" * 40)
    print(plan)


if __name__ == "__main__":
    main()
