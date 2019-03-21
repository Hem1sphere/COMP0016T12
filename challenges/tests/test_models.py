from django.test import TestCase
from challenges.models import Challenge


class ChallengeModelTest(TestCase):
    # @classmethod
    # def setUpTestData(cls):
    #     Challenge.objects.create(title="Test Challenge", brief="Test Challenge Brief")

    def test_string_representation(self):
        challenge = Challenge(title="Test Challenge")
        self.assertEquals(str(challenge), "Challenge: Test hallenge")

    # def test_get_absolute_url(self):
    #     challenge = Challenge.objects.get(id=1)
    #     self.assertEquals(challenge.get_absolute_url(), '/challenge/1/')
