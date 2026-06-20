# Course Completion Coach Agent

## Overview

Course Completion Coach Agent is a simple AI-inspired planning assistant designed to help learners complete online courses and capstone projects successfully.

The agent collects information about a course, available study hours, deadlines, and goals, then generates a structured completion plan.

## Problem

Many learners begin online courses but struggle to finish them because they lack a realistic study plan and accountability structure.

## Solution

This project provides a command-line agent that helps users:

* Create a study schedule
* Break large goals into smaller tasks
* Prepare for final submissions
* Stay organized throughout a course

## Features

* User input validation
* Study planning recommendations
* Security-focused design
* Command-line deployment

## Architecture

User → Course Completion Coach Agent → Planning Skill → Study Plan Output

## Files

* agent.py
* main.py
* skills/planner.py
* requirements.txt

## Setup

```bash
pip install -r requirements.txt
python main.py
```

## Security

* No personal information is stored
* No API keys are committed to the repository
* User input is validated

## Course Concepts Demonstrated

* Agent architecture
* Agent skills
* Security validation
* Deployability

## Author

Created as part of Kaggle's AI Agents: Intensive Vibe Coding Capstone Project.
