# -*- coding: utf-8 -*-
from __future__ import absolute_import
# vim: set ai et ts=4 sw=4:

# This file is part of OpenHatch.
# Copyright (C) 2014 Elana Hashman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


# Imports {{{
import mysite.bugsets.views

from django.db import models

from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
# }}}


class BugSet(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse(mysite.bugsets.views.listview_index, kwargs={
            'pk': self.pk,
            'slug': slugify(self.name),
        })


class AnnotatedBug(models.Model):
    url = models.URLField(max_length=200, verbose_name='Bug URL')
    bugsets = models.ManyToManyField(BugSet)
