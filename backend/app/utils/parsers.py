import pandas as pd

def parse_none(value):
   """Return None if value is empty string, NaN, or null-like."""
   if pd.isna(value) or value == "":
      return None
   return value

def parse_bool(value):
    """Converts common truthy/falsy values to Python bool."""
    if isinstance(value, str):
        return value.strip().lower() in ("true", "1", "yes")
    return bool(value)

def parse_int_or_none(value):
    """Convert to int, or return None if not possible."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

