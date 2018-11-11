from flask import Blueprint

release = Blueprint('release',__name__)

from . import views