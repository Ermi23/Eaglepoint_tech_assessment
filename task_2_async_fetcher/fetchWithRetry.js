const { mockApiCall } = require("./mockApi");

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

/**
 * fetchWithRetry calls an async function (simulating fetch) and retries on failure.
 * @param {Function} apiFn - an async function that returns a Promise
 * @param {Object} options - { maxRetries: number, delayMs: number }
 */
async function fetchWithRetry(apiFn, options = {}) {
  const maxRetries = options.maxRetries ?? 3;
  const delayMs = options.delayMs ?? 1000;

  let attempt = 0;
  while (true) {
    try {
      attempt++;
      // call the provided api function (e.g., mockApiCall)
      const result = await apiFn();
      console.log(`Attempt ${attempt}: success`);
      return result;
    } catch (err) {
      console.warn(`Attempt ${attempt} failed: ${err.message}`);
      if (attempt > maxRetries) {
        throw new Error(`All ${maxRetries} retries failed. Last error: ${err.message}`);
      }
      console.log(`Waiting ${delayMs}ms before retrying...`);
      await sleep(delayMs);
    }
  }
}

// If run directly, demonstrate with the mock API
if (require.main === module) {
  (async () => {
    try {
      const res = await fetchWithRetry(() => mockApiCall(0.3), { maxRetries: 5, delayMs: 1000 });
      console.log("Final result:", res);
    } catch (err) {
      console.error("Final error:", err.message);
    }
  })();
}

module.exports = { fetchWithRetry, sleep };