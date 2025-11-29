// Mock API that randomly succeeds or fails for testing retry logic.

function mockApiCall(successRate = 0.3) {
  // successRate float between 0 and 1; default 30% success
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (Math.random() < successRate) {
        resolve({ ok: true, data: { message: "mock success", ts: Date.now() } });
      } else {
        reject(new Error("mock failure"));
      }
    }, 200); // 200ms simulated latency
  });
}

module.exports = { mockApiCall };
