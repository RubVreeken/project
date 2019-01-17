from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import mkdtemp
import aiohttp, requests
import urllib.request
import json
from pytrivia import Category, Diffculty, Type, Trivia

my_api = Trivia(True)
response = my_api.request(1, Category.Books, Diffculty.Hard, Type.Multiple_Choice)
print(response)





