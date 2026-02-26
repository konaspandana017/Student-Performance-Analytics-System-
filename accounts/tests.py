from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AccountsSmokeTests(TestCase):
	def test_login_page_loads(self):
		response = self.client.get(reverse("login"))
		self.assertEqual(response.status_code, 200)

	def test_signup_creates_user_and_redirects_to_login(self):
		response = self.client.post(
			reverse("signup"),
			{
				"username": "newstudent",
				"email": "newstudent@example.com",
				"role": "student",
				"password1": "StrongPass123!",
				"password2": "StrongPass123!",
			},
		)

		self.assertRedirects(response, reverse("login"))
		self.assertTrue(User.objects.filter(username="newstudent").exists())

	def test_role_redirect_for_teacher(self):
		teacher = User.objects.create_user(
			username="teacher1", password="StrongPass123!", is_staff=True
		)
		self.client.login(username="teacher1", password="StrongPass123!")

		response = self.client.get(reverse("role_redirect"))
		self.assertRedirects(response, reverse("teacher_dashboard"))

	def test_dashboard_requires_authentication(self):
		response = self.client.get(reverse("student_dashboard"))
		self.assertEqual(response.status_code, 302)
		self.assertIn(reverse("login"), response.url)

	def test_logout_redirects_to_login(self):
		User.objects.create_user(username="u1", password="StrongPass123!")
		self.client.login(username="u1", password="StrongPass123!")

		response = self.client.get(reverse("logout"))
		self.assertRedirects(response, reverse("login"))
