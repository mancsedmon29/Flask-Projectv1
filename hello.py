from flask import Flask, render_template, request, flash, redirect, url_for, abort
from forms import NamerForm, ContactForm, OrderForm


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SECRET_KEY'] = "mancao-kitchen-secret-key"

@app.route("/")
def index():
    first_name = "Edmon"
    stuff = "This is <strong>STRONG</strong> Text"
    favorite_food = ["Adobo", "Cabagan", "Bulalo"]
    my_recipe = ["Sayote", "Manok", "Sibuyas", "Bawang", "Chili Leave", "Tanglad"]
    fav_pizza = ["Pepperoni", "Cheese", "Mushroom", "Pineapple", "Ham"]
    return render_template("index.html", 
                           f_name=first_name, 
                           stff=stuff, 
                           fav_food=favorite_food, 
                           recipe=fav_pizza, 
                           ingredients=my_recipe)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)

@app.route("/search", methods=["POST"])
def search():
    searched = request.form.get('searched')
    all_items = ["Adobo", "Cabagan", "Bulalo", "Sayote", "Manok", "Sibuyas", "Bawang", "Chili Leave", "Tanglad", "Pepperoni", "Cheese", "Mushroom", "Pineapple", "Ham"]
    results = [item for item in all_items if searched and searched.lower() in item.lower()] if searched else []
    return render_template("search.html", searched=searched, results=results)

@app.route("/name", methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!")  # <-- SIMPLE FLASH
    return render_template("name.html", name=name, form=form)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Thanks {form.name.data}! Na-receive namin message mo.", "success")  # <-- DAGDAG
        flash(f"We will reply to {form.email.data} soon!", "info")  # <-- DAGDAG PWEDENG 2 FLASH
    elif request.method == 'POST':
        flash("Please check your form, may kulang pa!", "danger")  # <-- PAG ERROR
    return render_template("contact.html", form=form)

@app.route("/order", methods=['GET', 'POST'])
def order():
    form = OrderForm()
    total = None
    if form.validate_on_submit():
        qty = form.quantity.data
        price = float(form.price.data)
        discount = float(form.discount.data or 0)
        subtotal = qty * price
        total = subtotal - (subtotal * discount / 100)
        
        if total > 1000:
            flash(f"Wow big order! ₱{total:.2f} - Free Softdrinks!", "success")  # <-- WITH CATEGORY
        else:
            flash(f"Order placed! Total: ₱{total:.2f}", "success")
    elif request.method == 'POST':
        flash("Order failed! Check mo yung form mo.", "danger")
        
    return render_template("order.html", form=form, total=total)

# --- ERROR HANDLERS - KUMPLETO NA DAPAT LAHAT ---
@app.errorhandler(400)
def bad_request(e):
    return render_template("400.html"), 400

@app.errorhandler(401)
def unauthorized(e):
    return render_template("401.html"), 401

@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template("500.html"), 500

@app.route('/test/<int:code>')
def test_error(code):
    abort(code)
    
# Demo Message:
# @app.route("/message-demo")
# def message_demo():
#     flash("Success! Green to", "success")
#     flash("Error! Red to", "danger")
#     flash("Warning! Yellow to", "warning")
#     flash("Info! Blue to", "info")
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)