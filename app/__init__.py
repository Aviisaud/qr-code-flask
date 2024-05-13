from flask import Flask

app = Flask(__name__)

app.secret_key = '763ret4765_&345'

from app import views
