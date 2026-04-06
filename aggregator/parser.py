"""Parse common flight-data log formats into unified dicts."""
import csv
import json
from pathlib import Path

def parse_csv(path: str | Path) -> list[dict]:
    """Load a CSV flight log; first row is header."""
    with open(path, newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f))

def parse_json(path: str | Path) -> list[dict]:
    """Load a JSON array flight log."""
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, list):
        raise ValueError("Expected JSON array at root")
    return data

def load(path: str | Path) -> list[dict]:
    """Auto-detect format by extension and return records."""
    p = Path(path)
    if p.suffix.lower() == '.csv':
        return parse_csv(p)
    elif p.suffix.lower() == '.json':
        return parse_json(p)
    raise ValueError(f"Unsupported format: {p.suffix}")
