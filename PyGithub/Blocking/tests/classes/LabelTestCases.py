# -*- coding: utf-8 -*-

# Copyright 2013-2014 Vincent Jacques <vincent@vincent-jacques.net>

from PyGithub.Blocking.tests.Framework import *


class LabelAttributes(TestCase):
    @Enterprise("electra")
    def test(self):
        l = self.g.get_repo(("electra", "mutable")).get_label("bug")
        self.assertEqual(l.color, "fc2929")
        self.assertEqual(l.name, "bug")


class LabelEdit(TestCase):
    @Enterprise("electra")
    def testName(self):
        l = self.g.get_repo(("electra", "mutable")).get_label("bug")
        self.assertEqual(l.name, "bug")
        l.edit(name="feature")
        self.assertEqual(l.name, "feature")
        l.edit(name="bug")
        self.assertEqual(l.name, "bug")

    @Enterprise("electra")
    def testColor(self):
        l = self.g.get_repo(("electra", "mutable")).get_label("bug")
        self.assertEqual(l.color, "fc2929")
        l.edit(color="aabbcc")
        self.assertEqual(l.color, "aabbcc")
        l.edit(color="fc2929")
        self.assertEqual(l.color, "fc2929")


class LabelDelete(TestCase):
    @Enterprise("electra")
    def test(self):
        l = self.g.get_repo(("electra", "mutable")).create_label("ephemeral", "FF0000")
        self.assertEqual(l.color, "FF0000")
        l.delete()