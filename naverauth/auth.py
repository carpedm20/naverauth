# -*- coding: utf-8 -*-

"""
naverdic.auth
~~~~~~~~~~~~~

This module provides an authentication for NAVER account.
"""

from curses.ascii import isprint

import requests

def auth(account, password):
    r = requests.get("http://static.nid.naver.com/enclogin/keys.nhn")
    key, name, n, e = r.text.split(',')

    pub_key = RSA.PublicKey(int(n,16), int(e,16))

    secret = key + chr(len(account)) + account + chr(len(password)) + password
    secret = ''.join([i if 32 < ord(i) < 128 else '' for i in secret])

    enc_key = RSA.encrypt(secret, pub_key)

    data = {'enctp' : '1',
            'encpw' : enc_key,
            'encnm' : name,
            'svctype' : '0',
            'url' : 'http://naver.com/',
            'enc_url' : 'http%3A%2F%2Fwww.naver.com%2F',
            'smart_level' : '-1',
    }

    r = requests.post("https://nid.naver.com/nidlogin.login",
                      data = data,
                      headers = headers)

    return r
