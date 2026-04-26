def calculate_patient_responsibility(amount_billed, deductible_remaining, copay_pct):
    """How much does the patient owe after insurance pays its share."""
    deductible_applied = min(amount_billed, deductible_remaining)
    remaining_after_deductible = amount_billed - deductible_applied
    copay = remaining_after_deductible * copay_pct
    return round(deductible_applied + copay, 2)


def is_claim_eligible(claim_type, covered_types):
    """Is this claim type covered under the patient's plan."""
    return claim_type in covered_types


def get_claim_status_label(status_code):
    """Convert internal status code to human-readable label."""
    labels = {
        "S": "Submitted",
        "R": "Under Review",
        "A": "Approved",
        "D": "Denied",
        "P": "Paid",
    }
    return labels.get(status_code, "Unknown")
