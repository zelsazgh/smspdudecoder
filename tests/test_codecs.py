# coding: utf-8
# Copyright (c) Qotto, 2018-2019
# Open-source software, see LICENSE file for details

import unittest

from smspdu.codecs import GSM

class GSMEncodingTestCase(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(GSM.encode('hello'), 'E8329BFD06')
        self.assertEqual(GSM.decode('E8329BFD06'), 'hello')

    def test_8chars(self):
        self.assertEqual(GSM.encode('12345678'), '31D98C56B3DD70')
        self.assertEqual(GSM.decode('31D98C56B3DD70'), '12345678')

    def test_extended(self):
        self.assertEqual(GSM.encode('[10€]'), '1B5E0CB6296F7C')
        self.assertEqual(GSM.decode('1B5E0CB6296F7C'), '[10€]')

    def test_empty(self):
        self.assertEqual(GSM.encode(''), GSM.decode(''), '')

    def test_long(self):
        DATA_DECODED = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        )
        DATA_ENCODED = (
            "CCB7BCDC06A5E1F37A1B447EB3DF72D03C4D0785DB653A0B347EBBE7E531BD4CAFCB4161"
            "721A9E9E8FD3EE33A8CC4ED359A079990C22BF41E5747DDE7E9341F4721BFE9683D2EE71"
            "9A9C26D7DD74509D0E6287C56F791954A683C86FF65B5E06B5C36777181466A7E3F5B00B"
        )
        self.assertEqual(GSM.encode(DATA_DECODED), DATA_ENCODED)
        self.assertEqual(GSM.decode(DATA_ENCODED), DATA_DECODED)
