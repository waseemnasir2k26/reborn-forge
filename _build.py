#!/usr/bin/env python
"""Shim to tools/_build.py — kept at root for backwards-compat. Use tools/_build.py."""
import runpy, pathlib
runpy.run_path(str(pathlib.Path(__file__).parent / "tools" / "_build.py"), run_name="__main__")
