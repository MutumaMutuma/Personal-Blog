from flask import Blueprint
main = Blueprint('main',__name__)
from . import views
# Here we import the blueprint class from flask to avoid circular dependancies