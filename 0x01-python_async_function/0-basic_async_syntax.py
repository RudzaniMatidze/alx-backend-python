#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument
named wait_random that waits for a random delay.
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random number of seconds."""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
