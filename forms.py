from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField, IntegerField, DecimalField, BooleanField, SelectField, RadioField, DateField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange, Optional, Regexp, URL

# Basic Name Form
class NamerForm(FlaskForm):
    name = StringField("What's Your Name?", validators=[DataRequired(), Length(min=2, max=50, message="2-50 chars lang boss")])
    submit = SubmitField("Submit")

# COMPLETE ORDER FORM - Demo ng lahat
class OrderForm(FlaskForm):
    # StringField examples
    customer_name = StringField("Customer Name", validators=[
        DataRequired(message="Lagay mo name mo boss"),
        Length(min=3, max=50),
        Regexp('^[A-Za-z ]*$', message="Letters lang allowed")
    ])
    
    email = EmailField("Email Address", validators=[
        DataRequired(),
        Email(message="Ayusin mo email mo boss")
    ])

    # SelectField - Dropdown
    ulam = SelectField("Anong Ulam?", choices=[
        ('', 'Pili ka ng ulam'),
        ('adobo', 'Adobo - ₱120'),
        ('bulalo', 'Bulalo - ₱250'),
        ('tinola', 'Tinola - ₱180'),
        ('cabagan', 'Cabagan - ₱150')
    ], validators=[DataRequired()])

    # IntegerField - Buong number
    quantity = IntegerField("Quantity (pcs)", validators=[
        DataRequired(),
        NumberRange(min=1, max=20, message="1 to 20 pcs lang allowed")
    ])

    # DecimalField - Ito yung hinahanap mo - may point
    price = DecimalField("Price per Item (₱)", places=2, rounding=None, validators=[
        DataRequired(),
        NumberRange(min=0.01, max=10000, message="Price must be between 0.01 and 10000")
    ])

    # DecimalField with calculation example - Total
    discount = DecimalField("Discount (%)", places=2, default=0, validators=[
        Optional(),
        NumberRange(min=0, max=100, message="0-100% lang discount")
    ])

    # RadioField
    payment_method = RadioField("Payment Method", choices=[
        ('gcash', 'GCash'),
        ('cod', 'Cash on Delivery'),
        ('card', 'Credit Card')
    ], validators=[DataRequired()])

    # DateField
    delivery_date = DateField("Delivery Date", format='%Y-%m-%d', validators=[Optional()])

    # BooleanField
    agree_terms = BooleanField("I agree to Terms & Conditions", validators=[DataRequired(message="Need mo mag agree")])

    # Password example with EqualTo validator
    # password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    # confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message="Dapat same ng password")])

    submit = SubmitField("Place Order")

# Contact Form
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2, max=50)])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    website = StringField("Website (optional)", validators=[Optional(), URL(message="Dapat valid URL: https://...")])
    message = TextAreaField("Your Favorite Ulam & Message", validators=[DataRequired(), Length(min=10, message="At least 10 chars")])
    submit = SubmitField("Send Message")