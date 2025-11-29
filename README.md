# Eagle Point Technical Assessment - Ermias Tadesse

This repo contains my solutions for the Eagle Point full-stack technical assessment:
- Task 1: Smart Text Analyzer (Python)
- Task 2: Async Data Fetcher with Retry (JavaScript / Node)
- Task 3: Rate Limiter (Python)

## Structure
See the folder layout in the repository root.

## Quick start

### Task 1 - Smart Text Analyzer

#### Overview
A Python function that analyzes text and returns comprehensive statistics including word count, average word length, longest words, and word frequency distribution.

#### Features
- **Word Count**: Accurate tokenization using regex to handle punctuation
- **Average Word Length**: Calculated with decimal precision and rounded to 2 decimal places
- **Longest Words**: Returns all words tied for longest length (case-insensitive)
- **Word Frequency**: Case-insensitive frequency counting using Python's Counter
- **Robust Tokenization**: Handles punctuation, whitespace, and edge cases gracefully

#### Implementation Details

**Key Components:**
- `tokenize(text)`: Uses regex pattern `\b\w+\b` with Unicode support to extract words
- `analyze_text(text)`: Main analysis function that computes all required metrics
- **Decimal Precision**: Uses Python's `Decimal` class for accurate average calculation
- **Case Handling**: All comparisons and frequency counts are case-insensitive

**Example Usage:**
```python
from text_analyzer import analyze_text

sample_text = "The quick brown fox jumps over the lazy dog the fox"
result = analyze_text(sample_text)

# Returns:
# {
#     "word_count": 11,
#     "average_word_length": 3.73,
#     "longest_words": ["brown", "jumps", "quick"],
#     "word_frequency": {
#         "the": 3, "quick": 1, "brown": 1, "fox": 2,
#         "jumps": 1, "over": 1, "lazy": 1, "dog": 1
#     }
# }
```

## Running the Code

**Prerequisites:**
- Python 3.6+
- No external dependencies required (uses only standard library)

**Command Line:**
```bash
cd task_1_text_analyzer
python text_analyzer.py
```

**Command Line:**
```bash
cd task_1_text_analyzer
pytest test_text_analyzer.py -v
```

## Design Decisions & Trade-offs

- **Tokenization Approach**: Used regex pattern matching instead of simple string splitting to properly handle punctuation and maintain word boundaries
- **Precision**: Implemented Decimal arithmetic for average calculations to prevent floating-point precision errors and ensure accurate rounding
- **Memory Efficiency**: Designed with linear memory usage; for extremely large texts, streaming processing could be implemented
- **Performance**: Achieved O(n) time complexity through single-pass processing and efficient data structures

## Edge Cases Handled

- Empty input strings
- Text containing only punctuation and special characters
- Single-word inputs
- Multiple consecutive spaces and irregular whitespace
- Unicode characters and international text support
- Mixed case handling for frequency analysis

## Note on Output Differences

The implementation returns 11 words for the sample text "The quick brown fox jumps over the lazy dog the fox" instead of the expected 10. This occurs because the tokenizer correctly identifies all three instances of "the" in the text (including the second "the" before "fox" at the end), demonstrating more accurate word boundary detection compared to the example output.