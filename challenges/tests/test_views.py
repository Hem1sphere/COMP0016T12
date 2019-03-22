from django.test import TestCase
from django.urls import reverse
from challenges.models import Challenge
from users.models import User, Clinician


class ChallengeListViewTest(TestCase):
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


class ChallengeDeleteViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user1 = User.objects.create_user(username='testuser1', password='hello123!', is_clinician=True)
        Clinician.objects.create(user=test_user1)
        test_user2 = User.objects.create_user(username='testuser2', password='hello123!')
        Clinician.objects.create(user=test_user2)

        # create challenge object using test_user1
        test_clinician = Clinician.objects.get(id=1)
        Challenge.objects.create(title="Test Challenge", brief="Test Challenge Brief", clinician=test_clinician)

    def test_view_url_exists_at_desired_location(self):
        self.client.login(username="testuser1", password="hello123!")
        response = self.client.get('/challenges/1/delete')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        self.client.login(username="testuser1", password="hello123!")
        print(reverse('challenges_delete', kwargs={"pk": 1}))
        response = self.client.get(reverse('challenges_delete', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.client.login(username="testuser1", password="hello123!")
        response = self.client.get(reverse('challenges_delete', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'challenges/challenge_confirm_delete.html')

    def test_view_is_403_forbidden_for_other_users(self):
        # log in using testuser2 who is not the creator of the challenge
        self.client.login(username="testuser2", password="hello123!")
        response = self.client.get(reverse('challenges_delete', kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 403)

    def test_view_deletes_challenge_when_posted_to(self):
        self.client.login(username="testuser1", password="hello123!")
        response = self.client.post(reverse("challenges_delete", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, 302)
        self.assertRaises(Challenge.DoesNotExist, Challenge.objects.get, id="1")
