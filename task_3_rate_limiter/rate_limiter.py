"""
Simple sliding-window rate limiter (in-memory).
Limit: N requests per WINDOW seconds per user_id.

Use for single-process demos. For production/distributed, use Redis with sorted sets.
"""

import time
from collections import defaultdict, deque


class RateLimiter:
    def __init__(self, limit=5, window_seconds=60):
        self.limit = limit
        self.window = window_seconds
        # store per-user deque of timestamps (monotonic increasing)
        self.requests = defaultdict(deque)

    def allow_request(self, user_id):
        now = time.time()
        q = self.requests[user_id]

        # remove timestamps older than window
        cutoff = now - self.window
        while q and q[0] < cutoff:
            q.popleft()

        if len(q) >= self.limit:
            # rate-limited
            return False
        # allow and record
        q.append(now)
        return True

    def get_request_count(self, user_id):
        # returns current count in window
        now = time.time()
        cutoff = now - self.window
        q = self.requests[user_id]
        while q and q[0] < cutoff:
            q.popleft()
        return len(q)
