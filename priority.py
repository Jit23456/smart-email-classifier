def get_priority(text):
    text = text.lower()

    if "urgent" in text or "deadline" in text:
        return "High"
    elif "meeting" in text:
        return "Medium"
    else:
        return "Low"