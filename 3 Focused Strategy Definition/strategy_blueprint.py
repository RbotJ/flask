from flask import Blueprint, request, render_template, redirect, url_for
from .strategy_manager import StrategyManager

strategy_blueprint = Blueprint('strategy', __name__)
strategy_manager = StrategyManager()

@strategy_blueprint.route('/strategy/new', methods=['GET', 'POST'])
def add_strategy():
    if request.method == 'POST':
        # Handle the form submission for a new strategy
        strategy_data = request.form
        strategy_manager.create_strategy(strategy_data)
        return redirect(url_for('strategy.list_strategies'))
    return render_template('strategy/new_strategy.html')

@strategy_blueprint.route('/strategies')
def list_strategies():
    # Code to list all strategies
    pass

# Additional routes as needed
