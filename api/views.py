import json
import os
from django.http import JsonResponse
from django.conf import settings

# Helper function to load json
def load_json(filename):
    file_path = os.path.join(settings.BASE_DIR, 'data', filename)
    with open(file_path, 'r',encoding='utf-8'
) as f:
        return json.load(f)

def blog_view(request):
    data = load_json('blog.json')
    return JsonResponse(data,safe=False)

def experience_view(request):
    data = load_json('exprience.json')
    return JsonResponse(data,safe=False)

def skills_view(request):
    data = load_json('skills.json')
    return JsonResponse(data,safe=False)

def projects_view(request):
    data = load_json('projects.json')
    return JsonResponse(data,safe=False)

def certifications_view(request):
    data = load_json('certificate.json')
    return JsonResponse(data,safe=False)

def education_view(request):
    data = load_json('education.json')
    return JsonResponse(data,safe=False)

