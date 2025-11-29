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


## Task 3 - Rate Limiter

### Overview
A Python-based sliding window rate limiter that restricts API usage to a specified number of requests per time window per user. This implementation provides protection against API abuse and ensures fair resource distribution among users.

### Features
- **Sliding Window Algorithm**: Accurate time-based request tracking that automatically expires old requests
- **Per-User Limits**: Separate rate limiting for each user ID
- **Real-Time Enforcement**: Immediate request allowance/denial based on current window usage
- **Auto-Reset Mechanism**: Automatic cleanup of expired requests without manual intervention
- **In-Memory Storage**: Efficient deque-based storage suitable for single-process applications

### Implementation Details

**Key Components:**
- `RateLimiter(limit, window_seconds)`: Main class implementing the rate limiting logic
- `allow_request(user_id)`: Checks if a request should be allowed or denied
- `get_request_count(user_id)`: Returns current request count within the window

**Core Algorithm:**
```python
def allow_request(self, user_id):
    now = time.time()
    q = self.requests[user_id]
    
    # Remove timestamps older than window
    cutoff = now - self.window
    while q and q[0] < cutoff:
        q.popleft()
    
    if len(q) >= self.limit:
        return False  # Rate limited
    q.append(now)     # Allow and record
    return True
```
## Running the Code
```python
from rate_limiter import RateLimiter
import time

# Create rate limiter: 5 requests per 60 seconds
limiter = RateLimiter(limit=5, window_seconds=60)

# Simulate user requests
user_id = "user_123"
for i in range(10):
    allowed = limiter.allow_request(user_id)
    count = limiter.get_request_count(user_id)
    print(f"Request {i+1}: Allowed={allowed}, Count={count}")

# Demonstrate auto-reset after window
time.sleep(61)
print("After reset:", limiter.allow_request(user_id))
```

## Running the Code

**Prerequisites:**
- Python 3.6+
- No external dependencies required

**Command Line:**
```bash
cd task_3_rate_limiter
python rate_limiter.py
```

## Design Decisions & Trade-offs

- **Sliding Window vs Fixed Window**: Implemented sliding window algorithm for precise time-based limiting, providing more accurate request tracking compared to fixed window approaches that can allow bursts at window boundaries
- **In-Memory Storage**: Utilized Python's defaultdict and deque for efficient memory management and O(1) operations, optimized for single-process applications while maintaining simplicity
- **Automatic Cleanup**: Employed lazy cleanup strategy that removes expired timestamps only during request processing, balancing performance with accurate window maintenance
- **Monotonic Time Consideration**: Used time.time() for development simplicity while acknowledging time.monotonic() would be preferable for production systems to handle clock adjustments

## Edge Cases Handled

- Rapid burst requests that immediately exceed the rate limit threshold
- Requests occurring precisely at window boundary transitions
- Multiple users with completely independent rate limit counters
- New users with empty request history initialization
- Automatic expiration of timestamps without manual intervention
- Concurrent window transitions during high-frequency request patterns

## Real-World Applications

- **API Rate Limiting**: Protecting backend services and microservices from excessive request volumes and potential denial-of-service scenarios
- **User Action Throttling**: Preventing spam and abuse in chat systems, comment sections, and form submission interfaces
- **Payment Processing Security**: Limiting transaction attempts and card verification requests for fraud prevention
- **File Upload Management**: Controlling resource consumption and bandwidth usage in file handling and media processing systems
- **Third-Party Integration**: Managing API quotas and rate limits when integrating with external services and partner APIs

## Scalability Considerations

This implementation serves as a foundation for single-process environments. For distributed production systems, the same sliding window algorithm can be extended using Redis with sorted sets or other distributed data stores to maintain consistency across multiple application instances while preserving the accurate time-based limiting characteristics.