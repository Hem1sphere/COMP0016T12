from django.test import TestCase
from django.urls import reverse


class ChallengeViewTest(TestCase):
    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/challenges/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('challenges_main'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('challenges_main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'challenges/challenge_list.html')