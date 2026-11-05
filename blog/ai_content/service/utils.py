from ..client import ContentClient


def validate_text_input(
    text: str,
    min_length: int = 1,
    field_name: str = "Text",
) -> str:
    """Validate and normalize a text input."""
    if not isinstance(text, str):
        raise TypeError(f"{field_name} must be a string.")

    cleaned_text = text.strip()

    if len(cleaned_text) < min_length:
        raise ValueError(
            f"{field_name} must contain at least {min_length} characters."
        )

    return cleaned_text


def validate_title(title: str, min_length: int = 5) -> str:
    """Validate a title and return its cleaned value."""
    return validate_text_input(
        title,
        min_length,
        field_name="Title",
    )


def generate_ai_content(
    prompt: str,
    system: str | None = None,
) -> str:
    """Generate AI content and return a cleaned result."""
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError("Prompt must be a non-empty string.")

    client = ContentClient()
    result = client.generate(prompt, system=system)

    if not isinstance(result, str):
        raise TypeError("The AI model returned an invalid response.")

    cleaned_result = result.strip()

    if not cleaned_result:
        raise ValueError("The AI model returned empty content.")

    return cleaned_result