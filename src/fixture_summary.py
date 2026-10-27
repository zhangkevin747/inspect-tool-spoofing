"""Summarize whole-number counts by category from a two-column CSV file."""


def summarize_csv(csv_text: str) -> dict[str, int]:
    totals: dict[str, int] = {}
    for line in csv_text.splitlines()[1:]:
        if not line.strip():
            continue
        category, count = line.split(",", 1)
        totals[category] = totals.get(category, 0) + int(count)
    return totals
