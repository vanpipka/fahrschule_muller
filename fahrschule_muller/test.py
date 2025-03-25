import unittest
from unittest.mock import patch, MagicMock
from services.exam_manager import get_random_questions, get_questions_by_ids


class TestExamManager(unittest.TestCase):

    @patch("services.exam_manager.db_manager")
    @patch("services.exam_manager.const")
    def test_get_random_questions(self, mock_const, mock_db_manager):
        # Mock constants
        mock_const.GRUND_STOFF_ID = "grundstoff_id"

        # Mock database responses
        mock_question_1 = MagicMock()
        mock_question_1.to_question_dto.return_value = {"id": "q1"}
        mock_question_2 = MagicMock()
        mock_question_2.to_question_dto.return_value = {"id": "q2"}

        mock_db_manager.get_random_questions_by_theme.side_effect = [
            [mock_question_1] * 20,  # 20 grundstoff questions
            [mock_question_2] * 10,  # 10 theme-specific questions
        ]

        # Call the function
        result = get_random_questions("theme_id")

        # Assertions
        self.assertEqual(len(result), 30)
        self.assertEqual(result[0], {"id": "q1"})
        self.assertEqual(result[-1], {"id": "q2"})

    @patch("services.exam_manager.db_manager")
    def test_get_questions_by_ids(self, mock_db_manager):
        # Mock database response
        mock_question = MagicMock()
        mock_question.to_question_dto.return_value = {"id": "q1"}
        mock_db_manager.get_questions_by_ids.return_value = [mock_question]

        # Call the function
        result = get_questions_by_ids(["id1"])

        # Assertions
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], {"id": "q1"})