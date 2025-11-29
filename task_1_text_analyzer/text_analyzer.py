"""
Smart Text Analyzer
Inputs: string
Outputs: dict with:
    - word_count (int)
    - average_word_length (float rounded to 2 decimals)
    - longest_words (list of strings, lowercase)
    - word_frequency (dict lowercase -> int)
"""

import re
from collections import Counter
from decimal import Decimal, ROUND_HALF_UP

WORD_RE = re.compile(r"\b\w+\b", flags=re.UNICODE)

def tokenize(text: str):
    """Return list of word tokens (strings) from text. Keeps alphanumerics/underscore."""
    if not text:
        return []
    return WORD_RE.findall(text)

def analyze_text(text: str):
    words = tokenize(text)
    if not words:
        return {
            "word_count": 0,
            "average_word_length": 0.0,
            "longest_words": [],
            "word_frequency": {}
        }

    # lengths for average
    lengths = [len(w) for w in words]
    total_len = sum(lengths)
    count = len(words)

    # average with Decimal and round to 2 decimals
    avg = (Decimal(total_len) / Decimal(count)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

    # word frequency (case-insensitive)
    lower_words = [w.lower() for w in words]
    freq = Counter(lower_words)

    # longest words (case-insensitive unique list)
    max_len = max(lengths)
    longest = sorted(list({w.lower() for w in words if len(w) == max_len}))

    return {
        "word_count": count,
        "average_word_length": float(avg),
        "longest_words": longest,
        "word_frequency": dict(freq)
    }

# Test the function directly
if __name__ == "__main__":
    sample = "The quick brown fox jumps over the lazy dog the fox"
    out = analyze_text(sample)
    import json
    print(json.dumps(out, indent=2))
    
    # Also print key metrics for verification
    print(f"\nWord count: {out['word_count']}")
    print(f"Average word length: {out['average_word_length']}")
    print(f"Longest words: {out['longest_words']}")
    print(f"Frequency of 'the': {out['word_frequency'].get('the', 0)}")
    print(f"Frequency of 'fox': {out['word_frequency'].get('fox', 0)}")