import json
from dataclasses import asdict
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.core.cache import cache

from server.accessibility.extractor import extract_accessibility_info, extract_all_images, get_image_by_id, tag_image_with_alt_text


class MetadataView(View):
    def get(self, request, pdf_id):
        temp_path = cache.get(f"pdf_temp_path_{pdf_id}")
        if not temp_path:
            return JsonResponse({"error": "PDF not found"}, status=404)
        
        pdf_filename = temp_path.split("/")[-1].rsplit("_", 1)[0]
        
        result = extract_accessibility_info(temp_path, pdf_filename)
        result_dict = asdict(result)
        
        images = extract_all_images(temp_path)
        result_dict['actual_image_count'] = len(images)
        
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
    
    def post(self, request, pdf_id, image_id):
        import traceback
        
        temp_path = cache.get(f"pdf_temp_path_{pdf_id}")
        if not temp_path:
            return JsonResponse({"error": "PDF not found"}, status=404)
        
        try:
            data = json.loads(request.body)
            alt_text = data.get('alt_text')
            
            if not alt_text:
                return JsonResponse({"error": "alt_text is required"}, status=400)
            
            print(f"[DEBUG] Attempting to tag image {image_id} in {temp_path} with alt text: {alt_text}")
            
            success = tag_image_with_alt_text(temp_path, image_id, alt_text)
            
            if success:
                print(f"[DEBUG] Successfully tagged image {image_id}")
                return JsonResponse({"success": True, "message": "Image tagged successfully"})
            else:
                print(f"[DEBUG] Failed to tag image {image_id}")
                return JsonResponse({"error": "Failed to tag image - function returned False"}, status=500)
                
        except json.JSONDecodeError as e:
            error_msg = f"Invalid JSON: {str(e)}"
            print(f"[ERROR] {error_msg}")
            return JsonResponse({"error": error_msg}, status=400)
        except Exception as e:
            error_msg = f"{type(e).__name__}: {str(e)}"
            traceback_str = traceback.format_exc()
            print(f"[ERROR] Exception in POST handler: {error_msg}")
            print(f"[ERROR] Traceback:\n{traceback_str}")
            return JsonResponse({"error": error_msg, "traceback": traceback_str}, status=500)
        