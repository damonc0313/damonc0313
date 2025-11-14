def normalize_scores(scores: list[float]) -> list[float]:
    total = sum(scores)
    if total == 0:
        return [0.0] * len(scores)
    return [score / total for score in scores]
