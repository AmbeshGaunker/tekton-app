
from ..main import last_day_of_month
from datetime import date
import pytest

@pytest.mark.parametrize("testDate, expected", [ (date(2023, 2, 1), date(2023, 2, 28)), 
        (date(2023, 1, 15), date(2023, 1, 31)),  
        (date(2024, 2, 15), date(2024, 2, 29)),# Leap yr 
        (date(2024, 12, 10), date(2024, 12, 31)),
          ])       
def test_last_day_of_month(testDate,expected):
    assert last_day_of_month(testDate)== expected

def test_last_day_of_month_exceptions():
    with pytest.raises(ValueError) as execinfo:
        last_day_of_month(date(2023,2,30))
