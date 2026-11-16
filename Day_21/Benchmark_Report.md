# Day 21 – API Performance Benchmark Report

## 1. Objective

The objective of this experiment was to compare synchronous and asynchronous API performance using FastAPI.

## 2. Testing Methodology

- Created a synchronous API using `def` and `time.sleep()`.
- Created an asynchronous API using `async def` and `await asyncio.sleep()`.
- Used HTTPX to send 50 concurrent requests to each API.
- Measured the total execution time using Python's `time.perf_counter()`.

## 3. Performance Comparison

| Metric | Synchronous API | Asynchronous API |
|---|---:|---:|
| Total Requests | 50 | 50 |
| Successful Requests | 50 | 50 |
| Failed Requests | 0 | 0 |
| Total Execution Time | 5.06 seconds | 3.11 seconds |

## 4. Performance Improvement

The execution-time reduction was calculated using:

Performance Improvement = ((Synchronous Time - Asynchronous Time) / Synchronous Time) × 100

= ((5.06 - 3.11) / 5.06) × 100

= **38.54%**

The asynchronous API completed the benchmark approximately 1.63 times faster.

## 5. Observations

- Both APIs successfully handled all 50 requests.
- The synchronous API processed requests with blocking operations.
- The asynchronous API used non-blocking `asyncio.sleep()`.
- Asynchronous programming allowed the API to handle multiple waiting requests more efficiently.
- The asynchronous API showed a lower total execution time in this experiment.

## 6. Conclusion

The experiment demonstrated that asynchronous programming can improve API performance when handling concurrent I/O-bound operations.

The asynchronous API reduced the observed total execution time by 38.54% compared with the synchronous API.

These results are specific to this test setup and workload. Actual performance improvements may vary depending on the application and server environment.