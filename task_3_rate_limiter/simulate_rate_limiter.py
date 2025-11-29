import time
from rate_limiter import RateLimiter

def simulate():
    rl = RateLimiter(limit=5, window_seconds=60)
    user = "user_123"
    results = []
    # make 10 rapid requests
    for i in range(10):
        allowed = rl.allow_request(user)
        ts = time.strftime("%H:%M:%S", time.localtime())
        print(f"[{i+1}] {ts} allowed={allowed} count_in_window={rl.get_request_count(user)}")
        results.append((i+1, allowed))
        # no sleep -> rapid
    print("---- Now waiting 61 seconds to observe auto-reset ----")
    time.sleep(61)
    print("After waiting:")
    allowed_after = rl.allow_request(user)
    print("allowed after window:", allowed_after)

if __name__ == "__main__":
    simulate()
