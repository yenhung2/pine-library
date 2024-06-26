import datetime
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Question

class QuestionModelTests(TestCase):

	def test_was_published_recently_with_future_question(self):
		# django seearches for func. whose name begins with 'test'
		time = timezone.now()+datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_old_question(self):
		# django seearches for func. whose name begins with 'test'
		time = timezone.now()-datetime.timedelta(days=1, seconds=1)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), False)

	def test_was_published_recently_with_recent_question(self):
		# django seearches for func. whose name begins with 'test'
		time = timezone.now()-datetime.timedelta(hours=23, minutes=59, seconds=59)
		future_question = Question(pub_date=time)
		self.assertIs(future_question.was_published_recently(), True)





def create_question(question_text, days):
	time=timezone.now()+datetime.timedelta(days=days)
	return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionIndexViewTests(TestCase):
	def test_no_question(self):

		response=self.client.get(reverse('library:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, 'No polls are available.')
		self.assertQuerysetEqual(response.context['latest_question_list'],[])

	def test_past_question(self):
		create_question(question_text='Past question.', days=-30)
		response=self.client.get(reverse('library:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question.>'])

	def test_future_question(self):
		create_question(question_text='Future question.', days=30)
		response=self.client.get(reverse('library:index'))
		self.assertContains(response, 'No polls are available.')
		self.assertQuerysetEqual(response.context['latest_question_list'],[])

	def test_future_question_and_past_question(self):
		create_question(question_text='Future question.', days=30)
		create_question(question_text='Past question.', days=-30)
		response=self.client.get(reverse('library:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question.>'])

	def test_two_past_question(self):
		create_question(question_text='Past question 1.', days=-5)
		create_question(question_text='Past question 2.', days=-30)
		response=self.client.get(reverse('library:index'))
		self.assertQuerysetEqual(response.context['latest_question_list'],['<Question: Past question 1.>', '<Question: Past question 2.>'])





class QuestionDetailViewTest(TestCase):
	def test_future_question(self):
		future_question=create_question(question_text='Future question.', days=5)
		url = reverse('library:detail', args=(future_question.id,))
		response=self.client.get(url)
		self.assertEqual(response.status_code, 404)

	def test_past_question(self):
		past_question=create_question(question_text='Past question.', days=-5)
		url = reverse('library:detail', args=(past_question.id,))
		response=self.client.get(url)
		self.assertContains(response, past_question.question_text)
