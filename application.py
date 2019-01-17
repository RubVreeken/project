from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp

import urllib.request
import json



data = json.loads(urllib.request.urlopen("http://jservice.io/api/categories?count=1000").read())
lijst = []
for dict in data:
    lijst.append(dict['id'])

print(lijst)





