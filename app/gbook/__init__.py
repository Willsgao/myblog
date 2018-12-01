from flask import Blueprint

gbook = Blueprint('gbook',__name__)

from . import views