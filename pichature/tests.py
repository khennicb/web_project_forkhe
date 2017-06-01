from django.test import TestCase
from django.utils import timezone

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from django.contrib.auth.models import User

from .models import Chatroom, Message


class MessageMethodTests(TestCase):
    
    def test_formatted_timestamp(self):
        
        user = User.objects.create_user('test', 'test@test.fr', 'test')
        self.assertIsNotNone(user)
        user.save()
        
        room = Chatroom(name='test',label='test')
        self.assertIsNotNone(room)
        room.save()
        
        now = timezone.now()
        
        msg = Message(chatroom=room, user=user, timestamp=now)
        self.assertIsNotNone(msg)
        msg.save()
        
        self.assertEqual(now.strftime('%b %-d %-I:%M %p'), msg.formatted_timestamp)


class AccountTestCase(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(AccountTestCase, self).setUp()
        
    def tearDown(self):
        self.selenium.quit()
        super(AccountTestCase, self).tearDown()
        
    def test_signUp(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get('https://web-project-forkhe-fishkiller.c9users.io/signup/')
        #find the form element
        email = selenium.find_element_by_id('email')
        login = selenium.find_element_by_id('login')
        password = selenium.find_element_by_id('pass')
        
        submit = selenium.find_element_by_name('signUp')
        
        #Fill the form with data
        email.send_keys('testSelenium@test.fr')
        login.send_keys('Moi')
        password.send_keys('123456')
        
        #submitting the form
        submit.send_keys(Keys.RETURN)
        
        #check the returned result