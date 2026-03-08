"""Lightweight filters for flight-data record lists."""

def by_field(records: list[dict], field: str, value) -> list[dict]:
    """Return records where records[field] == value."""
    return [r for r in records if r.get(field) == value]

def time_range(records: list[dict], t_field: str,
               t_start: float, t_end: float) -> list[dict]:
    """Return records whose t_field falls within [t_start, t_end]."""
    return [r for r in records
            if t_start <= float(r[t_field]) <= t_end]

def drop_nulls(records: list[dict], fields: list[str]) -> list[dict]:
    """Drop records that have None/empty string in any of the given fields."""
    return [r for r in records
            if all(r.get(f) not in (None, '') for f in fields)]
