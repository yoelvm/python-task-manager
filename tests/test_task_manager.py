import unittest

from task_manager import create_task, validate_due_date, validate_priority


class TestTaskManager(unittest.TestCase):

    def test_validate_priority_accepts_valid_priority(self):
        result = validate_priority("alta")
        self.assertEqual(result, "alta")

    def test_validate_priority_replaces_invalid_priority_with_media(self):
        result = validate_priority("urgente")
        self.assertEqual(result, "media")

    def test_validate_due_date_accepts_valid_date(self):
        result = validate_due_date("2026-08-01")
        self.assertEqual(result, "2026-08-01")

    def test_validate_due_date_replaces_invalid_date_with_sin_fecha(self):
        result = validate_due_date("01/08/2026")
        self.assertEqual(result, "Sin fecha")

    def test_validate_due_date_replaces_empty_date_with_sin_fecha(self):
        result = validate_due_date("")
        self.assertEqual(result, "Sin fecha")

    def test_create_task_returns_expected_dictionary(self):
        task = create_task("Estudiar Python", "alta", "2026-08-01")

        expected_task = {
            "title": "Estudiar Python",
            "completed": False,
            "priority": "alta",
            "due_date": "2026-08-01"
        }

        self.assertEqual(task, expected_task)


if __name__ == "__main__":
    unittest.main()