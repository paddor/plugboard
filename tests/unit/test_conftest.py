"""Unit tests for the shared pytest configuration."""

import asyncio

import uvloop


async def test_tests_run_on_uvloop() -> None:
    """Tests should run on a uvloop event loop, supplied by the loop factory hook."""
    assert isinstance(asyncio.get_running_loop(), uvloop.Loop)
