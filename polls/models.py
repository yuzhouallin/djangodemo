from __future__ import unicode_literals

from django.db import models
from mongoengine import *

class Poll(Document):
	name = StringField(required=True)
	choice = StringField(required=True)
