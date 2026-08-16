# Windows Setup for Environment and App

Sa Windows iba syntax, hindi export. Wala dapat space sa = pag nag se-set ka.

1. Kung gamit mo ay Command Prompt (`CMD`) - yung default na black na window

```cmd
set FLASK_APP=hello.py
set FLASK_ENV=development
flask run
```
**Important Note:**
Sa bago na version ng Flask (2.3+), deprecated na yung FLASK_ENV. Ganto na dapat:

```cmd
set FLASK_APP=hello.py
set FLASK_DEBUG=1
flask run
```

**Sa PowerShell:**
```cmd
$env:FLASK_APP="hello.py"
$env:FLASK_DEBUG="1"
flask run
```
Mas madali na way para di ka paulit-ulit mag set, lagay mo na lang to sa code mo mismo:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

Tapos run mo lang as:

```code
python hello.py
```
or sa **Powershell**:

```powershell
flask --app hello run --debug
```

---

# Flask / Jinja2 - Complete List of Filters

> Lahat ng built-in filters na pwede mo gamitin sa `{{ variable | filter }}`

## Syntax
```jinja
{{ variable | filter_name }}
{{ "hello world" | upper }} -> HELLO WORLD
{{ "HELLO WORLD" | lower }} -> hello world
{{ my_list | length }}
{{ price | round(2) }}
```

---

## A. String / Text Filters

| Filter | Example | Result |
| :--- | :--- | :--- |
| `lower` | `{{ "HELLO" | lower }}` | `hello` |
| `upper` | `{{ "hello" | upper }}` | `HELLO` |
| `capitalize` | `{{ "hello world" | capitalize }}` | `Hello world` |
| `title` | `{{ "hello world" | title }}` | `Hello World` |
| `trim` | `{{ "  hello  " | trim }}` | `hello` |
| `center(width=80)` | `{{ "hi" | center(10) }}` | `     hi     ` |
| `replace(old, new, count)` | `{{ "Hello World" | replace("Hello", "Hi") }}` | `Hi World` |
| `truncate(length=255, killwords=False, end='...')` | `{{ "foo bar baz qux" | truncate(9) }}` | `foo ...` |
| `striptags` | `{{ "<p>hello</p>" | striptags }}` | `hello` |
| `wordcount` | `{{ "hello world" | wordcount }}` | `2` |
| `wordwrap(width=79)` | `{{ long_text | wordwrap(50) }}` | Wrapped text |
| `indent(width=4, first=False)` | `{{ text | indent(2, true) }}` | Indented |

## B. Number Filters

| Filter | Example | Result |
| :--- | :--- | :--- |
| `abs` | `{{ -5 | abs }}` | `5` |
| `int(default=0, base=10)` | `{{ "5" | int }}` | `5` |
| `float(default=0.0)` | `{{ "3.14" | float }}` | `3.14` |
| `round(precision=0, method='common')` | `{{ 42.55 | round }}` | `43.0` |
| `round` ceil/floor | `{{ 42.55 | round(1, 'floor') }}` | `42.5` |
| `sum(attribute=None, start=0)` | `{{ [1,2,3] | sum }}` | `6` |
| `filesizeformat(binary=False)` | `{{ 1024 | filesizeformat }}` | `1.0 kB` |

## C. List / Dict / Sequence Filters

| Filter | Example | Description |
| :--- | :--- | :--- |
| `first` | `{{ [1,2,3] | first }}` | Unang item |
| `last` | `{{ [1,2,3] | last }}` | Huling item |
| `length / count` | `{{ [1,2,3] | length }}` | Bilang ng items |
| `reverse` | `{{ [1,2,3] | reverse | list }}` | Baliktad |
| `sort(reverse=False, attribute=None)` | `{{ [3,1,2] | sort }}` | I-sort |
| `random` | `{{ [1,2,3] | random }}` | Random item |
| `list` | `{{ "abc" | list }}` | Gawing list `['a','b','c']` |
| `batch(n, fill_with)` | `{% for row in items | batch(3) %}` | I-batch per n |
| `slice(n, fill_with)` | `{% for col in items | slice(3) %}` | I-slice into columns |
| `join(d='', attribute=None)` | `{{ [1,2,3] | join('|') }}` | `1|2|3` |
| `groupby(attribute)` | `{% for g in persons | groupby('gender') %}` | I-group |
| `dictsort(case_sensitive, by='key')` | `{% for k,v in mydict | dictsort %}` | I-sort dict |
| `map(attribute='name')` | `{{ users | map(attribute='username') | join(', ') }}` | Kunin lang field |
| `select('odd')` | `{{ numbers | select('odd') }}` | Filter |
| `reject('odd')` | `{{ numbers | reject('odd') }}` | Reject |
| `selectattr('is_active')` | `{{ users | selectattr('is_active') }}` | Filter by attr |
| `rejectattr('is_active')` | `{{ users | rejectattr('is_active') }}` | Reject by attr |

## D. HTML / Escape / Format Filters

| Filter | Example | Description |
| :--- | :--- | :--- |
| `escape / e` | `{{ "<div>" | e }}` | Gawing `&lt;div&gt;` |
| `forceescape` | `{{ text | forceescape }}` | Double escape |
| `safe` | `{{ "<b>hi</b>" | safe }}` | Wag i-escape, render as HTML |
| `format` | `{{ "%s - %s" | format("A", "B") }}` | String format |
| `urlencode` | `{{ "a b" | urlencode }}` | `a%20b` |
| `urlize(trim, nofollow, target)` | `{{ "http://google.com" | urlize }}` | Gawing clickable link |
| `xmlattr(autospace=True)` | `{{ {'class':'my_list'} | xmlattr }}` | ` class="my_list"` |
| `tojson` | `{{ data | tojson }}` | Gawing JSON for JS |
| `string` | `{{ 123 | string }}` | Gawing string |

## E. Other / Utility Filters

| Filter | Example | Description |
| :--- | :--- | :--- |
| `default(value, boolean=False) / d` | `{{ my_var | default('wala') }}` | Default pag undefined |
| `attr(name)` | `{{ foo | attr("bar") }}` | Kunin attribute |
| `pprint(verbose=False)` | `{{ my_dict | pprint }}` | Pretty print for debug |

---

## Most Used in Real Projects

```jinja
{# CASE CONVERSION #}
{{ name | upper }}
{{ name | lower }}
{{ name | title }}
{{ name | capitalize }}

{# SAFETY #}
{{ user_input | escape }}
{{ html_content | safe }}

{# LIST HANDLING #}
{% for user in users | sort(attribute='name') %}
  {{ user.name | upper }} - {{ user.email | lower }}
{% endfor %}

{# TRUNCATE & JOIN #}
{{ description | truncate(100) }}
{{ tags | join(', ') }}

{# DEFAULT & JSON #}
{{ username | default('Guest') }}
<script>var data = {{ users | tojson }};</script>
```

## Bonus: Chaining Filters

```jinja
{{ "  HELLO WORLD  " | trim | lower | title }} -> Hello World
{{ [1,2,3,4] | reverse | first }} -> 4
{{ users | map(attribute='name') | join(', ') | upper }}
```

Source: Jinja2 Official Docs - List of Builtin Filters

---

# Flask - Custom Error Pages (404 & 500)

## 1. Folder Structure

```
flask-lessons/
├── hello.py
└── templates/
    ├── index.html
    ├── user.html
    ├── 404.html   <- Page Not Found
    └── 500.html   <- Server Error
```

## 2. Create templates/404.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>404 Not Found</title>
</head>
<body>
    <center>
        <h1>404 Error</h1>
        <h2>Page Not Found - Naligaw ka boss!</h2>
        <p>Yung hinahanap mong page wala dito.</p>
        <a href="/">Bumalik sa Home</a>
    </center>
</body>
</html>
```

## 3. Create templates/500.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>500 Internal Server Error</title>
</head>
<body>
    <center>
        <h1>500 Internal Server Error</h1>
        <h2>May nasira sa server!</h2>
        <p>Try mo ulit mamaya.</p>
        <a href="/">Bumalik sa Home</a>
    </center>
</body>
</html>
```

## 4. Update hello.py

```python
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

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

# ===============================
# CUSTOM ERROR PAGES
# ===============================

# Invalid URL - 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error - 500
@app.errorhandler(500)
def internal_error(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)
```

## 5. How to Test

1. Run your app:
   ```powershell
   flask --app hello run --debug
   ```

2. For 404: Go to any invalid URL
   ```
   http://127.0.0.1:5000/asdasd
   http://127.0.0.1:5000/walangganito
   ```

3. For 500: You need to set `debug=False` first, or create a test route that causes error:
   ```python
   @app.route("/error")
   def error_test():
       return 1 / 0  # This will trigger 500
   ```

## 6. Bonus - More Error Codes

You can add more if you want:

```python
@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

@app.errorhandler(401)
def unauthorized(e):
    return render_template("401.html"), 401
```

| Code | Meaning |
| :--- | :--- |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Page Not Found |
| 500 | Internal Server Error |

## Notes
- Return format is always: `return render_template("xxx.html"), CODE`
- Don't forget the `, 404` or `, 500` at the end
- When `debug=True`, Flask shows debugger instead of your 500.html. Set to `False` to see custom 500 page

---

# Flask - Bootstrap Navbar with Search (Personalized)

> Final version: Personalized branding + working search bar like sa screenshot mo.

## 1. New Files Needed

```
templates/
├── base.html      <- UPDATE - may search na
├── index.html
├── user.html
├── search.html    <- NEW FILE
├── 400.html
├── 401.html
├── 403.html
├── 404.html
└── 500.html
```

## 2. Update `hello.py` - Lagyan ng Search Logic

```python
from flask import Flask, render_template, abort, request

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['PROPAGATE_EXCEPTIONS'] = False

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

# --- NEW: SEARCH FUNCTION ---
@app.route("/search", methods=["POST"])
def search():
    searched = request.form.get('searched')
    
    # Para ma-search lahat ng food mo
    all_items = ["Adobo", "Cabagan", "Bulalo", "Sayote", "Manok", "Sibuyas", "Bawang", "Chili Leave", "Tanglad", "Pepperoni", "Cheese", "Mushroom", "Pineapple", "Ham"]

    results = []
    if searched:
        # i-lower lahat para case-insensitive
        for item in all_items:
            if searched.lower() in item.lower():
                results.append(item)

    return render_template("search.html", searched=searched, results=results)

# --- ERROR HANDLERS ---
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

if __name__ == "__main__":
    app.run(debug=True)
```

## 3. NEW FILE: `templates/search.html`

```html
{% extends 'base.html' %}

{% block content %}
    <br/>
    <h2>You Searched For: <em>{{ searched }}</em></h2>
    <br/>

    {% if results %}
        <p>Found {{ results | length }} result(s):</p>
        <ul class="list-group">
            {% for item in results %}
                <li class="list-group-item">{{ item }}</li>
            {% endfor %}
        </ul>
    {% else %}
        <p>Sorry, no results found for <strong>{{ searched }}</strong>...</p>
        <p>Try searching for: Adobo, Sayote, Cheese, etc.</p>
    {% endif %}

    <br/>
    <a href="{{ url_for('index') }}" class="btn btn-dark">Back to Home</a>
{% endblock %}
```

## 4. UPDATE `templates/base.html` - Personalized + Search Bar

Ito yung pinaka importante. Ginawa ko nang `Mancao's Kitchen` yung brand at nilagyan ng search na katulad sa screenshot mo.

```html
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Mancao's Kitchen - Edmon</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        /* Para maging katulad nung screenshot mo */
        .search-box {
            background-color: #2b3035;
            border: 1px solid #495057;
            color: white;
        }
        .search-box::placeholder { color: #adb5bd; }
        .btn-search {
            border: 1px solid #198754;
            color: #198754;
        }
        .btn-search:hover {
            background-color: #198754;
            color: white;
        }
    </style>
  </head>
  <body>
    <!-- NAVBAR - PERSONALIZED -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <a class="navbar-brand fw-bold" href="{{ url_for('index') }}">🍲 Mancao's Kitchen</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link" href="{{ url_for('index') }}">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="{{ url_for('user', name='Edmon') }}">Profile</a>
            </li>
          </ul>
          <!-- SEARCH FORM - TULAD NG SCREENSHOT MO -->
          <form method="POST" action="{{ url_for('search') }}" class="d-flex" role="search">
            <input class="form-control me-2 search-box" type="search" placeholder="Search" aria-label="Search" name="searched">
            <button class="btn btn-search" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>

    <div class="container mt-4">
        {% block content %}
        {% endblock %}
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  </body>
</html>
```

## 5. UPDATE other templates (para same branding)

**templates/index.html**
```html
{% extends 'base.html' %}
{% block content %}
    <h1>Welcome to Mancao's Kitchen!</h1>
    <h2>By the way, my name is {{ f_name | upper }}</h2>
    <p>{{ stff | safe }}</p>
    
    <p>My favorite foods are:</p>
    <ul>
        {% for food in fav_food %}
        <li>{{ food }}</li>
        {% endfor %}
    </ul>

    <p>The Topics of Pizza:</p>
    <ul>
        {% for topping in recipe %}
        <li>{{ topping }}</li>
        {% endfor %}
    </ul>

    <p>The ingredients of Tinola:</p>
    <ul>
        {% for ingredient in ingredients %}
        <li>{{ ingredient }}</li>
        {% endfor %}
    </ul>
{% endblock %}
```

**templates/user.html**
```html
{% extends 'base.html' %}
{% block content %}
    <h1>Hello {{ user_name | title }}!</h1>
    <p>Welcome to Mancao's Kitchen profile page.</p>
    <a href="{{ url_for('index') }}" class="btn btn-success">Back to Home</a>
{% endblock %}
```

**templates/404.html** (same for 400,401,403,500)
```html
{% extends 'base.html' %}
{% block content %}
    <center>
        <h1>404 Error</h1>
        <h2>Naligaw ka boss, wala sa menu yan!</h2>
        <p>Try mo mag-search sa taas.</p>
        <a href="{{ url_for('index') }}" class="btn btn-dark">Back to Kusina</a>
    </center>
{% endblock %}
```

## 6. How it works

1. `base.html` has `<form method="POST" action="{{ url_for('search') }}">`
2. Input has `name="searched"` - important!
3. Pag nag-search ka ng "Adobo", pupunta sa `/search` route
4. Sa `hello.py`, `request.form.get('searched')` kukunin yung tinype mo
5. I-filter nya lahat ng foods
6. Ipapakita sa `search.html`

## 7. Test

```powershell
flask --app hello run --debug
```

Try:
- Search: "Manok" -> lalabas Tinola ingredient
- Search: "Adobo" -> lalabas favorite food
- Search: "cheese" -> lalabas pizza topping

---

# Flask - Web Forms COMPLETE (All Fields & All Validators)

> 100% Complete version for Mancao's Kitchen - Kasama DecimalField, StringField at lahat ng validators.

## 0. Install

```powershell
pip install Flask Flask-WTF email_validator
```

## 1. Final Folder Structure

```
flask-lessons/
├── hello.py
├── forms.py
├── static/images/kitchen-wallpaper.png
└── templates/
    ├── base.html
    ├── index.html
    ├── order.html      <- NEW - para sa DecimalField demo
    ├── name.html
    └── ...
```

## 2. ALL WTForms Fields - Complete List

Ito yung kumpletong listahan na pwede mo gamitin:

| Field Type | Para saan | Example |
| :--- | :--- | :--- |
| `StringField` | Text input | Name, Ulam |
| `TextAreaField` | Malaking text | Message, Recipe |
| `EmailField` | Email | Email |
| `PasswordField` | Password | Password |
| `IntegerField` | Buong number | Quantity, Age |
| `DecimalField` | May decimal | Price - 99.99 |
| `FloatField` | Float number | Weight |
| `BooleanField` | Checkbox | Agree, Is Available? |
| `DateField` | Date | Birthday |
| `DateTimeField` | Date + Time | Order time |
| `SelectField` | Dropdown | Pili ng ulam |
| `SelectMultipleField` | Multi select | Toppings |
| `RadioField` | Radio button | Payment method |
| `FileField` | Upload | Food photo |
| `SubmitField` | Button | Submit |
| `HiddenField` | Hidden | ID |

## 3. ALL Validators - Complete List

| Validator | Ano ginagawa | Example |
| :--- | :--- | :--- |
| `DataRequired()` | Required, di pwede blank | `StringField(..., validators=[DataRequired()])` |
| `InputRequired()` | Same as DataRequired pero mas strict | `InputRequired()` |
| `Length(min, max)` | Haba ng text | `Length(min=3, max=50, message="...")` |
| `Email()` | Valid email dapat | `Email(message="Invalid email")` |
| `EqualTo('field')` | Dapat same sa ibang field | `EqualTo('password')` for confirm password |
| `NumberRange(min, max)` | Range ng number - Gamit sa DecimalField | `NumberRange(min=0, max=1000)` |
| `Regexp()` | Regex pattern | `Regexp('^[A-Za-z]*$')` |
| `URL()` | Dapat valid URL | `URL()` |
| `AnyOf([list])` | Dapat nasa list | `AnyOf(['Adobo','Bulalo'])` |
| `NoneOf([list])` | Bawal nasa list | `NoneOf(['badword'])` |
| `Optional()` | Pwede blank | `Optional()` |
| `ReadOnly()` | Read only | `ReadOnly()` |
| `Disabled()` | Disabled | `Disabled()` |

## 4. NEW `forms.py` - COMPLETE VERSION

Ito na kumpleto with DecimalField, StringField, IntegerField, etc. + lahat ng validators

```python
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
```

## 5. UPDATE `hello.py` - Add Order Route

```python
from flask import Flask, render_template, abort, request, flash
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
        flash("Form Submitted Successfully!")
    return render_template("name.html", name=name, form=form)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash(f"Thanks {form.name.data}! Na-receive namin message mo.")
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
        discount_amount = subtotal * (discount / 100)
        total = subtotal - discount_amount
        
        flash(f"Order placed! {form.customer_name.data} - {qty}x {form.ulam.data} | Total: ₱{total:.2f}")

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

if __name__ == "__main__":
    app.run(debug=True)
```

## 6. `templates/base.html` - Add Order Link

Update mo navbar mo:

```html
<ul class="navbar-nav me-auto mb-2 mb-lg-0">
  <li class="nav-item"><a class="nav-link" href="{{ url_for('index') }}">Home</a></li>
  <li class="nav-item"><a class="nav-link" href="{{ url_for('user', name='Edmon') }}">Profile</a></li>
  <li class="nav-item"><a class="nav-link" href="{{ url_for('name') }}">Name Form</a></li>
  <li class="nav-item"><a class="nav-link" href="{{ url_for('contact') }}">Contact</a></li>
  <li class="nav-item"><a class="nav-link" href="{{ url_for('order') }}">Order 🍲</a></li>
</ul>
```

## 7. NEW `templates/order.html` - Demo ng DecimalField

Ito yung pinaka importante - makikita mo DecimalField in action.

```html
{% extends 'base.html' %}

{% block content %}
<h1>Order Form - Mancao's Kitchen 🍲</h1>
<p>Demo ng StringField, IntegerField, DecimalField at lahat ng Validators</p>
<hr/>

{% if total is not none %}
<div class="alert alert-info">
    <h4>Computation:</h4>
    <p>Total Computed: <strong>₱{{ "%.2f"|format(total) }}</strong></p>
</div>
{% endif %}

<form method="POST" novalidate>
    {{ form.hidden_tag() }}

    <div class="row">
        <div class="col-md-6">
            {{ form.customer_name.label(class="form-label fw-bold") }}
            {{ form.customer_name(class="form-control") }}
            {% if form.customer_name.errors %}
                {% for error in form.customer_name.errors %}
                    <small class="text-danger">{{ error }}</small>
                {% endfor %}
            {% endif %}
        </div>
        <div class="col-md-6">
            {{ form.email.label(class="form-label fw-bold") }}
            {{ form.email(class="form-control") }}
            {% for error in form.email.errors %}
                <small class="text-danger">{{ error }}</small>
            {% endfor %}
        </div>
    </div>
    <br/>

    {{ form.ulam.label(class="form-label fw-bold") }}
    {{ form.ulam(class="form-select") }}
    <br/>

    <div class="row">
        <div class="col-md-4">
            {{ form.quantity.label(class="form-label fw-bold") }} <small>(IntegerField)</small>
            {{ form.quantity(class="form-control", placeholder="1-20") }}
            {% for error in form.quantity.errors %}
                <small class="text-danger">{{ error }}</small>
            {% endfor %}
        </div>
        <div class="col-md-4">
            {{ form.price.label(class="form-label fw-bold") }} <small>(DecimalField)</small>
            {{ form.price(class="form-control", placeholder="e.g. 120.50") }}
            {% for error in form.price.errors %}
                <small class="text-danger">{{ error }}</small>
            {% endfor %}
        </div>
        <div class="col-md-4">
            {{ form.discount.label(class="form-label fw-bold") }} <small>(DecimalField)</small>
            {{ form.discount(class="form-control", placeholder="e.g. 10.00") }}
            {% for error in form.discount.errors %}
                <small class="text-danger">{{ error }}</small>
            {% endfor %}
        </div>
    </div>
    <br/>

    {{ form.payment_method.label(class="form-label fw-bold") }}<br/>
    {% for subfield in form.payment_method %}
        <div class="form-check form-check-inline">
            {{ subfield(class="form-check-input") }}
            {{ subfield.label(class="form-check-label") }}
        </div>
    {% endfor %}
    <br/><br/>

    {{ form.delivery_date.label(class="form-label fw-bold") }}
    {{ form.delivery_date(class="form-control", type="date") }}
    <br/>

    <div class="form-check">
        {{ form.agree_terms(class="form-check-input") }}
        {{ form.agree_terms.label(class="form-check-label") }}
        {% for error in form.agree_terms.errors %}
            <br/><small class="text-danger">{{ error }}</small>
        {% endfor %}
    </div>
    <br/>

    {{ form.submit(class="btn btn-success btn-lg w-100") }}
</form>

<br/>
<div class="card">
    <div class="card-body">
        <h5>DecimalField Explained:</h5>
        <code>price = DecimalField("Price", places=2, validators=[NumberRange(min=0.01)])</code>
        <ul class="mt-2">
            <li><code>places=2</code> = 2 decimals lang: 120.50</li>
            <li><code>NumberRange</code> validator = pang limit ng value</li>
            <li>Gamit pag pera, price, discount, weight na may .XX</li>
            <li>IntegerField = walang point (1,2,3) | DecimalField = may point (1.25, 99.99)</li>
        </ul>
    </div>
</div>

{% endblock %}
```

## 8. How to Display Errors (Important!)

Sa lahat ng forms mo, ganito para lumabas error ng validator:

```html
{{ form.field_name(class="form-control") }}
{% if form.field_name.errors %}
    {% for error in form.field_name.errors %}
        <small class="text-danger">{{ error }}</small>
    {% endfor %}
{% endif %}
```

## 9. Run & Test

```powershell
flask --app hello run --debug
```

Test mo:
- http://127.0.0.1:5000/order
- Try: Quantity = 2, Price = 120.50, Discount = 10.00 -> Total = ₱216.90
- Try mag error: email na walang @, quantity na 100 (bawal), name na 1 letter lang

## Summary Cheat Sheet

```python
# StringField with complete validators
name = StringField("Name", validators=[
    DataRequired(),
    Length(min=2, max=50),
    Regexp('^[A-Za-z ]*$')
])

# DecimalField - FOR MONEY / PRICE
price = DecimalField("Price", places=2, validators=[
    DataRequired(),
    NumberRange(min=0.01, max=10000)
])

# IntegerField - FOR QUANTITY
qty = IntegerField("Qty", validators=[
    NumberRange(min=1, max=100)
])
```

Yan na 100% complete boss! Next lesson mo Database na para ma-save yang orders sa tunay na DB.

---

