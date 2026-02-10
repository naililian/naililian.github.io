"""Example module for MkDocs API reference.

This module contains sample functions documented with docstrings so that
mkdocstrings can render them on the site.
"""

__all__ = ["function_name"]

def function_name(arg1: int, arg2: str) -> bool:
    """One-line summary of what the function does.

    Longer description if needed. Mention assumptions, units,
    or edge cases here.

    Args:
        arg1: What arg1 represents.
        arg2: What arg2 represents.

    Returns:
        What the function returns.

    Raises:
        ValueError: When invalid input is provided.
    """
    print("hola")