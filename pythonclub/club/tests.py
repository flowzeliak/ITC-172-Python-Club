from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event 
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