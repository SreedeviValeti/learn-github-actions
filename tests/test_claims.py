from src.claims import (
    calculate_patient_responsibility,
    is_claim_eligible,
    get_claim_status_label,
)


# --- calculate_patient_responsibility ---

def test_full_amount_goes_to_deductible():
    # Billed 500, deductible has 1000 remaining → patient pays full 500
    result = calculate_patient_responsibility(500, 1000, 0.20)
    assert result == 500.0


def test_partial_deductible_then_copay():
    # Billed 500, deductible has 200 remaining
    # 200 goes to deductible, 300 remaining × 20% copay = 60
    # Total patient pays: 200 + 60 = 260
    result = calculate_patient_responsibility(500, 200, 0.20)
    assert result == 260.0


def test_no_deductible_remaining_only_copay():
    # Deductible already met, patient pays 20% of 500 = 100
    result = calculate_patient_responsibility(500, 0, 0.20)
    assert result == 100.0


def test_zero_copay_after_deductible():
    # Plan covers 100% after deductible
    result = calculate_patient_responsibility(500, 0, 0.00)
    assert result == 0.0


# --- is_claim_eligible ---

def test_covered_claim_type():
    assert is_claim_eligible("medical", ["medical", "dental", "vision"]) is True


def test_uncovered_claim_type():
    assert is_claim_eligible("cosmetic", ["medical", "dental"]) is False


def test_empty_covered_list():
    assert is_claim_eligible("medical", []) is False


# --- get_claim_status_label ---

def test_approved_status():
    assert get_claim_status_label("A") == "Approved"


def test_denied_status():
    assert get_claim_status_label("D") == "Denied"


def test_unknown_status_code():
    assert get_claim_status_label("X") == "Unknown"
