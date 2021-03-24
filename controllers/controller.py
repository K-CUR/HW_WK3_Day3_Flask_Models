from app import app
from flask import render_template
from models.customer_orders import orders

# @app.route('/')
# def index():
#     return "Hello World"

@app.route('/orders')
def summary():
    return render_template('summary.html', title="Order Summary", orders=orders) 


@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', order=orders[int(index)]) 



