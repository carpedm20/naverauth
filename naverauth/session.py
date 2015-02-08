# -*- coding: utf-8 -*-

"""
naverauth.session
~~~~~~~~~~~~~~~~~~~
This module provides a Dictionary object to send NAVER dictionary APIs.

"""
import requests
import rsa as RSA

def Session(object):
    """A session for NAVER login.

    Basic Usage::

        >>> import naverauth
        >>> naver = naverauth.Session("YOUR_ID", "YOUR_PASSWORD")
    """

    def __init__(self, account="", password=""):
        self.session = requests.Session()


    def get_keys(self):
        if not self.session:
            assert("NullException: self.session should not be null")

