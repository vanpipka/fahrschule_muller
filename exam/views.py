import json
from django.http import JsonResponse, HttpResponse 
from django.shortcuts import render, redirect
import services.exam_manager as exam_manager


def class_b(request):

    exam_id = request.GET.get('type_id')
    
    if request.method == "POST":
        try:
            answers = json.loads(request.body).get("answers")
        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON"}, status=400)
        
        questions = exam_manager.get_questions_by_ids([x[0] for x in answers])
        request.session['json_data'] = json.dumps(exam_manager.check_exam_answers(questions, answers), default=str)
        return JsonResponse({"redirect_url": "results/"})
    
    else:
        dataset = exam_manager.get_random_questions(exam_id)   
        
        if len(dataset) == 0:
            return HttpResponse(status=400) 
            
        return render(request, 'app/pages/exam.html', context={'dataset': dataset})


def exam_result(request):
    
    json_data = request.session.pop('json_data', '')
    questions = []
    
    try:
        questions = json.loads(json_data)
    except json.JSONDecodeError:
        redirect('500')
     
    data = exam_manager.convert_result_to_context(questions)
     
    return render(request, 'app/pages/exam_result.html', context={'dataset': data})