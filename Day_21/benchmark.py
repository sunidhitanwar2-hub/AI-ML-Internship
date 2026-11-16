
import asyncio
import time
import httpx

TOTAL_REQUESTS = 50


async def benchmark_api():
    url = input("Enter API URL: ")
    api_name = input("Enter API name: ")

    start_time = time.perf_counter()

    async with httpx.AsyncClient(timeout=30) as client:
        tasks = [
            client.get(url)
            for _ in range(TOTAL_REQUESTS)
        ]

        responses = await asyncio.gather(*tasks)

    end_time = time.perf_counter()

    successful = sum(
        1 for response in responses
        if response.status_code == 200
    )

    total_time = end_time - start_time

    print("\n===== BENCHMARK RESULTS =====")
    print("API:", api_name)
    print("Successful requests:", successful)
    print("Total requests:", TOTAL_REQUESTS)
    print("Total execution time:", round(total_time, 2), "seconds")

    return total_time


if __name__ == "__main__":
    asyncio.run(benchmark_api())
