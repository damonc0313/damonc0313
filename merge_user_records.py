from typing import Any

def merge_user_records(primary: dict[str, Any],
                       secondary: dict[str, Any]) -> dict[str, Any]:
    result = secondary.copy()
    for key, value in primary.items():
        if value is not None:
            result[key] = value
    return result
