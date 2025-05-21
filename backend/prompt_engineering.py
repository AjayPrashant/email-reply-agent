def build_prompt(email_text: str, tone: str, length: str) -> str:
    return f"""
You are an email assistant. Reply to the email below using a {tone.lower()} tone and keep it {length.lower()}.

Email:
\"\"\"
{email_text}
\"\"\"

Guidelines:
- Keep the reply clear and appropriate for the tone and length.
- Do not repeat the original email or include unnecessary details.
- Sign off appropriately if the email requires a closing.

Your reply:
"""
