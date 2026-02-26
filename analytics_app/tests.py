from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class AnalyticsSmokeTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username="analyticsuser", password="StrongPass123!"
		)
		self.client.login(username="analyticsuser", password="StrongPass123!")

	def test_analytics_root_loads(self):
		response = self.client.get("/analytics/")
		self.assertEqual(response.status_code, 200)

	def test_performance_page_loads(self):
		response = self.client.get(reverse("performance"))
		self.assertEqual(response.status_code, 200)

	def test_reports_page_loads(self):
		response = self.client.get(reverse("reports"))
		self.assertEqual(response.status_code, 200)

	def test_suggestions_page_loads(self):
		response = self.client.get(reverse("suggestions"))
		self.assertEqual(response.status_code, 200)

	def test_admin_overview_page_loads(self):
		response = self.client.get(reverse("analytics_admin_overview"))
		self.assertEqual(response.status_code, 200)

	def test_admin_students_page_loads(self):
		response = self.client.get(reverse("analytics_admin_students"))
		self.assertEqual(response.status_code, 200)
