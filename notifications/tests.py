from json import loads
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile


# Create your tests here.
class NotificationsTest(TestCase):
    def test_notification_service_online(self):
        """
        Tests that the notification service is listening
        and ready to service requests
        """

        _res = self.client.get("/notifications/")

        self.assertEqual(_res.status_code, 200)

    def test_notification_service_empty(self):
        """
        Tests that the notification service is empty on init
        """

        _res = self.client.get("/notifications/")
        self.assertEqual(_res.content, b"[]")

    def test_notification_service_add(self):
        """
        Tests adding notifications to the DB
        """
        _form_data = {
            "contents": "Notification test",
            "file": SimpleUploadedFile("simple_file", b"this is a test file"),
            "validity": 1,
            "notification_link": "https://example.com/notification",
        }

        _res = self.client.post("/notifications/", _form_data, format="multipart")
        self.assertEqual(_res.status_code, 200)

    def test_notification_service_read(self):
        """
        Tests that a notification can be added and be read back
        """
        _form_data = {
            "contents": "Notification test",
            "file": SimpleUploadedFile("simple_file", b"this is a test file"),
            "validity": 1,
            "notification_link": "https://example.com/notification",
        }

        # Test adding to the DB
        _res = self.client.post("/notifications/", _form_data, format="multipart")
        self.assertEqual(_res.status_code, 200)

        # Test reading from the DB
        _res = self.client.get("/notifications/")
        self.assertNotEqual(_res.content, b"[]")

        # Decoding the contents from server request
        _content_str = _res.content.decode(
            "utf-8"
        )  # Convert bytes to stringcontent_list
        _content_list = loads(_content_str)

        self.assertNotEqual(_content_list, [])
