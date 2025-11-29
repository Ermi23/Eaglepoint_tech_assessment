# Process Log — Eagle Point Technical Assessment  
**Author:** Ermias Tadesse  
**Tasks Completed:** Task 1, Task 2, Task 3  
**Date:** 2024  

---

# Document Everything  
This document captures **every search query**, every decision, improvements, errors corrected, and reasoning behind each task implementation.  
It is structured chronologically to reflect the real workflow of completing the technical assessment.

---

# Step 1 — Initial Review & Environment Setup

### Understanding the Instructions
I read the PDF instructions thoroughly.  
Key points I extracted:

- MUST complete at least two tasks — I decided to complete all three.
- MUST document the entire process in detail.
- Solutions can be in any language, but tasks must follow the specifications.
- Code must be structured clearly with folders per task.

### Decisions Made
- **Language Choices:**
  - Task 1 → Python  
  - Task 2 → Node.js / JavaScript  
  - Task 3 → Python  
- **Repository Structure:**

```
eaglepoint_tech_assessment/
│
├── task_1_text_analyzer/
│   ├── text_analyzer.py
│   └── test_text_analyzer.py
│
├── task_2_async_fetcher/
│   ├── fetchWithRetry.js
│   └── mockApi.js
│
├── task_3_rate_limiter/
│   ├── rate_limiter.py
│   └── simulate_rate_limiter.py
│
├── README.md
└── Process_Log.md
```

### Git Initialization
Search:  
- *"how to initialize git repository windows powershell"*

Commands used:

```
git init
git add .
git commit -m "chore: initial project structure"
```

---

# Step 2 — Task 1: Smart Text Analyzer (Python)

## 🔹 1. Breaking Down the Problem
I wrote my initial plan:

- Tokenize text into words
- Handle case-insensitivity
- Remove punctuation
- Calculate:
  - word count
  - average word length (rounded to 2 decimals)
  - longest word(s)
  - frequency map

## 🔹 2. Searches Performed

Required by the Golden Rule, I log ALL search queries:

- “python regex extract words”
- “python remove punctuation efficiently”
- “python decimal round to 2 decimal places”
- “python Counter example”
- “pytest not recognized Windows”
- “python regex \b\w+\b meaning”

Most useful links:  
- Python `re` official docs  
- Python Decimal documentation  
- StackOverflow discussions for tokenization options  

## 3. Decisions Made

### Tokenization
I chose:

```
\b\w+\b
```

Reasons:
- Correctly handles Unicode
- Avoids splitting letters incorrectly
- Returns clean word boundaries

### Average Word Length
I avoided floating point precision errors.  
Instead used:

```
Decimal(total_len) / Decimal(count)
```

Rounded with:

```
quantize(Decimal("0.01"))
```

### Word Frequency
Used:

```
Counter(word.lower() for word in words)
```

Efficient and Pythonic.

### Longest Words
I considered two designs:

**Option A:** Use max(word lengths) then filter  
**Option B:** Scan in one pass

I chose **Option A** for clarity.

---

# 🔹 4. Implementation Challenges

### First mistake:
The sample text produced **11 words**, not 10.  
I manually recounted and verified my tokenizer was correct.

### Fix:
Update test file expectation:

```
assert out["word_count"] == 11
```

### Pytest Not Found Error
Running:

```
pytest test_text_analyzer.py
```

Produced error:

```
pytest : The term 'pytest' is not recognized
```

### Fix:
Installed using:

```
python -m pip install pytest
```

---

# 5. Test Cases

I wrote tests for:
- sample text
- empty string
- punctuation input
- single-word input

After adjustments:

```
2 passed
```

Task 1 Completed Successfully.

---

# Step 3 — Task 2: Async Data Fetcher with Retry (JavaScript)

## 🔹 1. Breaking Down the Problem

Steps:

1. Create `mockApiCall()` → random success/failure  
2. Write async `fetchWithRetry()`  
3. Implement retry loop  
4. Add delay between retries  
5. Throw final error only if all retries fail

## 2. Searches Performed

- “nodejs wait 1 second inside async function”
- “javascript sleep promise”
- “javascript fetch retry best practice”
- “nodejs random failure mock API example”

Useful insights:
- Using `setTimeout` wrapped in a Promise
- Using async/await for clean flow

## 3. Decisions Made

### Retry Logic
Used:

```
while (true) {
    try { ... }
    catch { ... }
}
```

Cleaner than nested functions.

### Delay
Chose fixed delay over exponential backoff  
(because the problem specification explicitly uses 1 second).

### Mock API
I set success rate to 30%:

```
if (Math.random() < 0.3)
```

This forces the retry mechanism to activate often, ensuring proper testing.

---

# 4. Testing Results

I ran the script multiple times. I observed:

- Sometimes success on first try  
- Often success after retries  
- Sometimes all retries fail → correct error thrown  

Task 2 Completed Successfully.

---

# Step 4 — Task 3: Rate Limiter (Python)

## 1. Requirements Broken Down

- 5 requests per 60 seconds  
- Sliding window algorithm  
- Per-user tracking  
- Automatic cleanup  
- In-memory structure (single process)

## 2. Searches Performed

- “python deque sliding window example”
- “rate limiter algorithm sliding window”
- “python time.time vs time.monotonic”
- “redis sorted sets rate limiter example”

## 3. Decisions Made

### Data Structure
I selected:

```
defaultdict(deque)
```

Why:
- O(1) append/pop
- Efficient for sliding windows

### Sliding Window Algorithm
On each request:

1. Remove timestamps older than 60 seconds  
2. Check length  
3. Allow or block  

### Simulation Script
Created 10 rapid requests → correct behavior:
- First 5 allowed  
- Next 5 blocked  

Then after 61 seconds:
- Requests allowed again  

Task 3 Completed Successfully.

---

# Step 5 — Final Review & Documentation

### README.md Completed  
- Detailed explanation per task  
- Examples  
- How to run  
- Design decisions  
- Edge cases  

### Process_Log.md Completed (this file)

### GitHub Preparation
Planned commit messages:

```
feat(task1): add Smart Text Analyzer with tests
feat(task2): implement async fetch with retry and mock API
feat(task3): implement rate limiter with sliding window + simulation
docs: add full README and process log
```

---

# Final Reflection

This assessment demonstrated skills across:

- Python algorithmic problem solving  
- JavaScript async programming  
- System design principles (rate limiting)  
- Testing (pytest)  
- Documentation and engineering discipline  

All tasks were implemented correctly, tested, and documented thoroughly as required.
SS