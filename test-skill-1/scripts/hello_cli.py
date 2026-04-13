#!/usr/bin/env python3
"""CLI companion to the hello capability — run via `oxus skills run minimal-py-provider.hello-cli -- <name>`."""
import sys

name = sys.argv[1] if len(sys.argv) > 1 else "world"
print(f"Hello, {name}!")
