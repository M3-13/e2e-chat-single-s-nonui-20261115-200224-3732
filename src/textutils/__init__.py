"""textutils: small string helper functions, standard library only."""

from textutils.counting import word_count
from textutils.palindrome import is_palindrome
from textutils.reversal import reverse_words
from textutils.slug import slugify
from textutils.truncation import truncate

__all__ = ["is_palindrome", "reverse_words", "slugify", "truncate", "word_count"]
