def proposal_status(score):
    if score >= 80:
        return "Approved"
    return "Needs Review"


if __name__ == "__main__":
    print("AI Proposal Assistant Demo")
    print(proposal_status(85))