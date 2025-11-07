from dataclasses import asdict
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache

from server.accessibility.extractor import extract_accessibility_info, extract_all_images, get_image_by_id


class MetadataView(View):
    def get(self, request, pdf_id):
        temp_path = cache.get(f"pdf_temp_path_{pdf_id}")
        if not temp_path:
            return JsonResponse({"error": "PDF not found"}, status=404)
        
        pdf_filename = temp_path.split("/")[-1].rsplit("_", 1)[0]
        
        result = extract_accessibility_info(temp_path, pdf_filename)
        result_dict = asdict(result)
        
        return JsonResponse(result_dict, safe=False, json_dumps_params={'default': str})


class ImageListView(View):
    def get(self, request, pdf_id):
        temp_path = cache.get(f"pdf_temp_path_{pdf_id}")
        if not temp_path:
            return JsonResponse({"error": "PDF not found"}, status=404)
        
        images = extract_all_images(temp_path)
        
        image_list = []
        for img in images:
            image_list.append({
                'id': img['id'],
                'page_number': img['page_number'],
                'width': img['width'],
                'height': img['height'],
                'format': img['format']
            })
        
        return JsonResponse({'images': image_list})


class ImageDetailView(View):
    def get(self, request, pdf_id, image_id):
        temp_path = cache.get(f"pdf_temp_path_{pdf_id}")
        if not temp_path:
            return JsonResponse({"error": "PDF not found"}, status=404)
        
        image = get_image_by_id(temp_path, image_id)
        
        if not image:
            return JsonResponse({"error": "Image not found"}, status=404)
        
        response = HttpResponse(image['data'], content_type='image/png')
        return response
        