# -*- coding: utf-8 -*-
# Stalker a Production Asset Management System
# Copyright (C) 2009-2016 Erkan Ozgur Yilmaz
#
# This file is part of Stalker.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation;
# version 2.1 of the License.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

import unittest

from stalker import Role


class RoleTestCase(unittest.TestCase):
    """testing the Role class
    """

    def setUp(self):
        """set the test up
        """
        # the role class does not have anything to test
        pass

    def test_role_class_generic(self):
        """testing of creation of a Role instance
        """
        r = Role(name='Lead')
        self.assertTrue(isinstance(r, Role))
        self.assertEqual(r.name, 'Lead')
