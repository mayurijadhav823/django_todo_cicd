from django.http import JsonResponse


def ml_predict(request):
    return JsonResponse({
        "prediction": 0
    })