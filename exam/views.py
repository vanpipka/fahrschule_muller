import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from services.exam_manager import get_questions_by_category, check_exam_answers, convert_result_to_context


def class_b(request):

    exam_id = request.GET.get('type_id')
    
    if request.method == "POST":
        try:
            answers = json.loads(request.body).get("answers")
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)

        questions = get_questions_by_category(exam_id)
        request.session['json_data'] = json.dumps(check_exam_answers(questions, answers), default=str)
        return JsonResponse({"redirect_url": "results/"})
    
    else:
        dataset = get_questions_by_category(exam_id)   
        
        if len(dataset) == 0:
            redirect("500") 
            
        return render(request, 'app/pages/exam.html', context={'dataset': dataset})


def exam_result(request):
    
    json_data = request.session.pop('json_data', '')
    questions = []
    
    try:
        questions = json.loads(json_data)
    except json.JSONDecodeError:
        render(request, 'app/pages/500.html')
     
    return render(request, 'app/pages/exam_result.html', context={'dataset': convert_result_to_context(questions)})