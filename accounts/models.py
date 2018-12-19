# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class users1(models.Model):
	name=models.CharField(max_length=10, unique= True)
	password=models.CharField(max_length=10)
