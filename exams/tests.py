from django.test import TestCase


# Create your tests here.
class ExamsTest(TestCase):
    def test_exam_service_online(self):
        """
        Tests that the exam service is listening
        and ready to service requests
        """

        res = self.client.get("/exams/")

        self.assertEqual(res.status_code, 200)
