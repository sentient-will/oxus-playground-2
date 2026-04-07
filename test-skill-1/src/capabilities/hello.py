"""Minimal entitled capability — consumed by minimal-py-consumer."""


async def handler(request: dict) -> dict:
    name = str(request.get("name") or "world")
    return {"message": f"Hello, {name}!"}
