from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event 
from .forms import MeetingForm, ResourceForm
from datetime import datetime
from django.urls import reverse

# Create your tests here.
class MeetingTest(TestCase):
    def test_stringOutput(self):
        meeting=Meeting(meetingtitle='Firing Meeting')
        self.assertEqual(str(meeting), meeting.meetingtitle)
    
    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')

class EventTest(TestCase):
    def test_stringOutput(self):
        event=Event(eventtitle='Big Party')
        self.assertEqual(str(event), event.eventtitle)
    
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')

class ResourceTest(TestCase):
    def test_stringOutput(self):
        resource=Resource(resourcename='Seattle-Central')
        self.assertEqual(str(resource), resource.resourcename)
    
    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class MinutesTest(TestCase):
    def test_strOutput(self):
        minutes=MeetingMinutes(minutestext='The meeting went well.')
        self.assertEqual(str(minutes), minutes.minutestext)
    
    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')

#testing a view
class TestIndex(TestCase):
    def test_view_url_accessible_by_name(self):
        response=self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response=self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'club/index.html')

class TestGetMeeting(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/club/getmeeting/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('getmeeting'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('getmeeting'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'club/meeting.html')

class New_Meeting_Form_Test(TestCase):

    def test_MeetingForm_is_valid(self):
        form = MeetingForm(data={'meetingtitle':"Business Meeting", 'meetingdate':"2019-02-22", 'meetingtime':"09:30:00", 'meetinglocation':"The Business Office", 'agenda':"Talkin' Business"})
        self.assertTrue(form.is_valid())


    def test_MeetingForm_invalid(self):
        form = MeetingForm(data={'productname': "Surface", 'techtype': "laptop", 'user': "steve", 'entrydate': "2018-12-17", 'productURL':"http:microsoft.com", 'productdescription':"lightweight laptop"})
        self.assertFalse(form.is_valid())
