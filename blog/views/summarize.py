from django.http import JsonResponse
from django.views.decorators.http import require_POST
from ..ai_content.services.summarize import (
    PostNotFoundError,
    summarize_post,
)

@csrf_exempt
@require_POST
def summarize_post_view(request, post_id):
    """
    Handle HTTP requests for AI post summarization.
    """

    try:
        result = summarize_post(post_id)

    except PostNotFoundError as exc:
        return JsonResponse(
            {"error": str(exc)},
            status=404,
        )

    except ValueError as exc:
        return JsonResponse(
            {"error": str(exc)},
            status=400,
        )

    return JsonResponse(result, status=200)
