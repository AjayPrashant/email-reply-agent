import re

def clean_email_text(raw_email: str) -> str:
    # Remove quoted replies (common formats)
    patterns = [
        r"On\s.*wrote:",  # e.g. On Jan 1, Alice wrote:
        r"From:\s.*",      # lines that start with From:
        r"Sent:\s.*",      # Sent: Tuesday, etc.
        r"To:\s.*",        # To: Bob
        r"Subject:\s.*",   # Subject: Meeting
        r">.*",            # Lines starting with >
    ]
    
    for pattern in patterns:
        raw_email = re.sub(pattern, "", raw_email, flags=re.IGNORECASE)
    
    return raw_email.strip()
