import uuid
import services.db_manager as db_manager
import services.const as const


def get_random_questions(theme_id):

    # first - get grundstoff questions
    question_dtos = []
    
    entities = db_manager.get_random_questions_by_theme(const.GRUND_STOFF_ID, 20)   
    for question in entities:
        question_dtos.append(question.to_question_dto())

    entities = db_manager.get_random_questions_by_theme(theme_id, 10)
    for question in entities:
        question_dtos.append(question.to_question_dto())    
    
    return question_dtos


def get_questions_by_ids(ids = None):

    if ids is None: ids = []

    return [question.to_question_dto() for question in db_manager.get_questions_by_ids(ids)]


# [['cf6867ec-cfa4-4367-91e0-f7864d15a3fc', [1, 2]]]
def check_exam_answers(questions, answers):
    
    answers_dict = {uuid.UUID(answer[0]): answer[1] for answer in answers}
    
    for question in questions:     
        question_answers = sorted(str(x) for x in answers_dict.get(question.get("id"), []))
        question["right"] = question["right_answers"] == ','.join(question_answers) 
    
    return questions 
    
    
# questions - result of check_exam_answers
def convert_result_to_context(questions):

    penalty_points = 0
    answers_dict = dict()
    
    for i in questions:
        thema = i.get("thema", {}).get("name", "")
        category = i.get("category", {}).get("name", "")
        
        if thema not in answers_dict.keys():
            answers_dict[thema] = {}

        themes_dict = answers_dict.get(thema)

        if category not in themes_dict.keys():
            themes_dict[category] = [0, []]

        category_data = themes_dict.get(category)
        category_data[0] += 1 if i.get("right", False) else 0
        category_data[1].append(i.get("right", False))

        penalty_points += 0 if i.get("right", False) else i.get("penalty_points", 0)

    return {
        'answers': answers_dict, 
        'result': {
                'penalty_points': penalty_points,
                'result_text': 'NICHT BESTANDEN' if penalty_points >= 10 else 'BESTANDEN',
            }
        }