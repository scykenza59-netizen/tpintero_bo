def rate_note(note: int) -> str:
    if note < 10:
        return "unsuccessful"
    if 10 < note < 13:
        return "good"
    if note == 13:
        return "very good"
    if 14 <= note < 15:
        return "veryVery good"

    if note == 16:
        return "exelent"
    return "acceptable"