import pytest
from note_rating import rate_note


def test_rate_12_is_good():
    assert rate_note(12) == "good"
