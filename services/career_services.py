from parsers.career_goal_response import CareerGoalResponse

def choose_career_path(goal: str):

    if goal == "company":
        return CareerGoalResponse(
            next_step="company_analysis",
            message="Great! Let's research your target company.",
            required_input="company_name",
            prompt="Enter your target company name."
        )
    return CareerGoalResponse(
        next_step="learning_roadmap",
        message="Great! Let's build your personalized learning roadmap.",
        required_input=None,
        prompt=None
    )
    