import re

# Your resume data
my_resume = {
    "experience_years": 5,  # Total years of experience
}


def evaluate_job_fit(job_description, resume=my_resume, required_skill="Java"):
    # Function to extract the required experience years from the job description
    def extract_experience_years(description):
        # Regular expression to find patterns like "X years of experience"
        match = re.search(r'(\d+)\s*\+?\s*years?\s+of\s+experience', description, re.IGNORECASE)
        if match:
            return int(match.group(1))
        return 0  # Default to 0 if no match is found

    # Extract required experience years from the job description
    required_experience_years = extract_experience_years(job_description)

    # Check if the required skill (Java) is mentioned in the job description
    skill_match = bool(re.search(r'\b' + re.escape(required_skill) + r'\b', job_description, re.IGNORECASE))

    # Check the match between experience and required skill
    experience_match = resume["experience_years"] >= required_experience_years

    # Return True if both conditions are met, otherwise False
    return experience_match and skill_match


# Example Usage
job_description = """
Kforce has a client in Cincinnati, OH that is seeking a Level 2 Java Developer to join their team on a 6-month contract. This will be supporting the Collaborative Planning, Forecasting, and Replenishment team. Candidates can be remote, but EST is preferred.

Summary:
The  Developer is 2 years of experience responsible for leading the design, development, testing, debugging, maintaining, and documenting software components to which they are assigned. The Developer will be involved in the technical design process and completes estimates and work plans for design, development, implementation, and rollout tasks. The Developer also communicates with the appropriate teams to ensure that assignments are delivered with the highest quality and in accordance with standards. The Developer strives to continuously improve the software delivery processes and practices.
"""

# Check if the candidate is a good fit
# is_good_fit = evaluate_job_fit(job_description)
#
# # Display the result
# print(is_good_fit)
