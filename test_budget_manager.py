
import pytest
from budgeting_manager import name_budget, run_budget

def test_name_budget():
    assert name_budget("testing 1 2 3 ") == "testing_1_2_3.json"
    assert name_budget("    fun4 7") == "fun4_7.json"
    assert name_budget("pay  day") == "pay__day.json"

def test_run_budget():
    assert run_budget(100, {
      "car": {
            "Percentage": 40.0,
            "Account": "bank",
            "Current Balance": 0.0,
            "Time": "Wednesday Jul 24 05:05 PM"
      },
      "food": {
            "Percentage": 10.0,
            "Account": "piggy",
            "Current Balance": 10.0,
            "Time": "Wednesday Jul 24 05:06 PM"
      },
      "rent": {
            "Percentage": 50.0,
            "Account": "cash",
            "Current Balance": 100.0,
            "Time": "Wednesday Jul 24 05:06 PM"
      }
}) == {
      "car": {
            "Percentage": 40.0,
            "Account": "bank",
            "Current Balance": 40.0,
            "Time": "Wednesday Jul 24 05:05 PM"
      },
      "food": {
            "Percentage": 10.0,
            "Account": "piggy",
            "Current Balance": 20.0,
            "Time": "Wednesday Jul 24 05:06 PM"
      },
      "rent": {
            "Percentage": 50.0,
            "Account": "cash",
            "Current Balance": 150.0,
            "Time": "Wednesday Jul 24 05:06 PM"
      }
}
    assert run_budget(110, {
      "car": {
            "Percentage": 40.0,
            "Account": "bank",
            "Current Balance": 0.0,
            "Time": "Wednesday Jul 24 05:05 PM"
      },
      "food": {
            "Percentage": 10.0,
            "Account": "piggy",
            "Current Balance": 10.0,
            "Time": "Wednesday Jul 24 05:06 PM"
      },
      "rent": {
            "Percentage": 50.0,
            "Account": "cash",
            "Current Balance": 100.0,
            "Time": "Wednesday Jul 24 05:06 PM"
      }
}) == {
      "car": {
            "Percentage": 40.0,
            "Account": "bank",
            "Current Balance": 44.0,
            "Time": "Wednesday Jul 24 05:05 PM"
      },
      "food": {
            "Percentage": 10.0,
            "Account": "piggy",
            "Current Balance": 21.0,
            "Time": "Wednesday Jul 24 05:06 PM"
      },
      "rent": {
            "Percentage": 50.0,
            "Account": "cash",
            "Current Balance": 155.0,
            "Time": "Wednesday Jul 24 05:06 PM"
      }
}


pytest.main(["-v", "--tb=line", "-rN", __file__])