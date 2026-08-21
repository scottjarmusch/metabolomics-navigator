#!/usr/bin/env python
"""Backward-compatible wrapper. Use validate_catalogue.py for new workflows."""
from validate_catalogue import main
if __name__ == '__main__':
    raise SystemExit(main())
