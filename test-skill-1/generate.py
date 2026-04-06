skill = """
---
name: test-skill-1
description: announces itself when executed
---

to know what version of the skill is being tested, execute the following command in the terminal:

```bash
python -c 'print("test-skill-1: announce")'
```
"""


async def handler(request: dict) -> dict:
    req = request or {}
    text = req.get("text") or ""
    return {
        "text": skill,
        "echo": text,
        "moduleVersion": "0.0.1",
    }
