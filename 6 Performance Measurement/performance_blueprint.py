from flask import Blueprint

performance_bp = Blueprint('performance', __name__)

from . import routes  # Importing routes after blueprint initialization to avoid circular dependencies
