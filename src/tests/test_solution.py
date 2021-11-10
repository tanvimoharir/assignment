import pytest

from src.solution import getProbability


class TestFunctionality:
    # functional tests
    @pytest.mark.parametrize("n, probability", [(5, "14/29"), (10, "372/773")])
    def test_probability_basic_cases(self, n, probability):
        assert getProbability(n) == probability

    @pytest.mark.parametrize("n, probability", [(1, "1/2"), (2, "2/4"), (3, "4/8")])
    def test_probability_additional_cases(self, n, probability):
        assert getProbability(n) == probability

    @pytest.mark.parametrize("n", [0])
    def test_probability_for_invalid_input(self, n):
        assert (
            getProbability(n)
            == "Invalid input value, must be greater than or equal to 1"
        )

    @pytest.mark.parametrize("n", [-1, -2])
    def test_value_error(self, n):
        with pytest.raises(ValueError):
            getProbability(n)
