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

## Task 2 - Async Data Fetcher with Retry

### Overview
A JavaScript function that implements robust API calling with automatic retry logic for handling temporary failures. This is essential for building resilient applications that can gracefully handle network issues and server unavailability.

### Features
- **Automatic Retry Logic**: Automatically retries failed API calls up to a configurable maximum
- **Configurable Delay**: Waits between retries to avoid overwhelming the server
- **Error Handling**: Provides clear error messages after all retries are exhausted
- **Async/Await**: Uses modern JavaScript asynchronous patterns for clean, readable code
- **Mock API Included**: Comes with a simulated API for testing retry behavior

### Implementation Details

**Key Components:**
- `fetchWithRetry(apiFn, options)`: Main function that handles the retry logic
- `mockApiCall(successRate)`: Simulated API that randomly succeeds/fails for testing
- `sleep(ms)`: Utility function for introducing delays between retries

**Core Logic:**
```javascript
async function fetchWithRetry(apiFn, options = {}) {
  const maxRetries = options.maxRetries ?? 3;
  const delayMs = options.delayMs ?? 1000;

  let attempt = 0;
  while (true) {
    try {
      attempt++;
      const result = await apiFn();
      return result; // Success - return immediately
    } catch (err) {
      if (attempt > maxRetries) {
        throw new Error(`All ${maxRetries} retries failed. Last error: ${err.message}`);
      }
      await sleep(delayMs); // Wait before retrying
    }
  }
}
```
**Usage Example:**
```javascript
const { fetchWithRetry } = require('./fetchWithRetry');
const { mockApiCall } = require('./mockApi');

// Using with mock API (30% success rate)
(async () => {
  try {
    const result = await fetchWithRetry(
      () => mockApiCall(0.3), 
      { maxRetries: 5, delayMs: 1000 }
    );
    console.log('Success:', result);
  } catch (error) {
    console.error('Failed after all retries:', error.message);
  }
})();
```
## Running the Code

**Prerequisites:**
- Node.js 14+
- No external dependencies required

**Command Line:**
```bash
cd task_2_async_fetcher
node fetchWithRetry.js
```

## Design Decisions & Trade-offs

- **Infinite Loop Pattern**: Implemented `while (true)` with clear break conditions for straightforward retry logic and easy-to-follow control flow
- **Configurable Options**: Designed with customizable retry count and delay parameters to accommodate different use cases and failure scenarios
- **Immediate Return on Success**: Returns successfully immediately upon first successful attempt to minimize response latency and resource usage
- **Progressive Backoff Consideration**: Evaluated exponential backoff but chose fixed delay for implementation simplicity while maintaining effectiveness

## Edge Cases Handled

- Complete failure across all retry attempts with comprehensive error reporting
- Immediate success scenarios to ensure optimal performance when systems are healthy
- Diverse API failure modes including network timeouts, server errors, and connection issues
- Configurable success probability for thorough testing and simulation of real-world conditions

## Real-World Applications

- **HTTP API Calls**: Enhancing fetch/axios requests with automatic retry mechanisms for improved reliability
- **Database Operations**: Retrying queries during temporary database connection issues or replication lag
- **File System Operations**: Handling transient errors during file reads/writes under high system load
- **Third-Party Service Integration**: Managing rate limits, temporary outages, and service degradation in external APIs

This implementation establishes a robust foundation for building resilient distributed systems capable of gracefully handling the inherent unpredictability of network-based communications and inter-service dependencies.
