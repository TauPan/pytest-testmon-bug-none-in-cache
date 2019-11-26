from io import StringIO
from django.core.management import call_command
from django.test import TestCase

# See https://docs.djangoproject.com/en/2.2/topics/testing/tools/#topics-testing-management-commands


class TestDoStuffCommand(TestCase):
    def test_output(self):
        out = StringIO()
        call_command('do_stuff', stdout=out)
        self.assertEqual('Done stuff.\n', out.getvalue())
