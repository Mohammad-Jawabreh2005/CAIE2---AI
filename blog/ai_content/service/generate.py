import logging

from .utils import generate_ai_content, validate_title

logger = logging.getLogger(__name__)

def _bulit_generate_prompt(title: str, tone: str | None) -> str:
    prompt = f"Write a short blog post about {title} "
    if tone:
        prompt += f"write in a \n {tone}"

    prompt += "keep the total output under 500 characters"
    return prompt

def _generate_post(title: str, tone: str | None = None) -> dict:

    cleaned_title = validate_title(title,min_length=5)

    prompt = _bulit_generate_prompt(cleaned_title, tone)

    try:
        cleand_content= generate_ai_content(prompt)
    except Exception:
        logger.error(f"Failled to generatr {cleaned_title}")
        raise

    if len(cleand_content) > 500:
        cleaned_content = cleand_content[:500]
    return{
        "title": cleaned_title,
        "content": cleaned_content,
        "length": len(cleaned_content)
    }    