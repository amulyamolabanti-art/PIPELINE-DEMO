from app import proposal_status


def test_approved():
    assert proposal_status(85) == "Approved"


def test_needs_review():
    assert proposal_status(70) == "Needs Review"