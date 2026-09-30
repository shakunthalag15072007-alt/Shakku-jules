"""Module providing addition operations."""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    """Return the sum of two numbers."""
    return a + b
