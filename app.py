from flask import Flask
from flask import flash, render_template, request, url_for, session, redirect

from auth import Auth
from recipes import Recipes

app = Flask(__name__)
app.secret_key = b'aj(>,m87hJn9+-alkjns*jkj90($'


@app.route("/login/", methods=["POST", "GET"])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    username = request.form.get('username', None)
    password = request.form.get('password', None)
    auth = Auth()
    if auth.login(username, password):
        return redirect(url_for('show_recipes'))

    flash('Could not log you in')
    return render_template('login.html')



@app.route("/sign-up/", methods=["POST", "GET"])
def sign_up():
    if request.method == 'GET':
        return render_template('sign-up.html')

    username = request.form.get('username', None)
    password = request.form.get('password', None)
    password2 = request.form.get('password2', None)

    auth = Auth()
    error = None

    if auth.has_user(username):
        error = 'There is already a user with that name'
    elif password != password2:
        error = 'Passwords must match'

    if error:
        flash(error)
        return redirect(url_for('sign_up'))

    auth.create_user(username, password)
    auth.login(username, password)
    return redirect(url_for('show_recipes'))


@app.route("/logout/")
def logout():
    auth = Auth()
    auth.logout()
    return redirect(url_for('show_recipes'))


@app.route("/")
@app.route("/recipes/")
def show_recipes():
    '''If logged in, show recipes for the current user.
    Otherwise, redirect to the Login page.'''
    auth = Auth()
    recipe = Recipes()

    if auth.is_logged_in():
        user_id = auth.get_current_user()['id']
        recipes = recipe.get_recipes(user_id)
        return render_template('recipes.html', recipes=recipes)
    return redirect(url_for('login'))


@app.route("/recipes/new/", methods=['GET', 'POST'])
def add_recipe():
    '''If request method is GET, load the 'add recipe' page.
    If request method is POST:
      1. Get all posted form data
      2. Get ID of currently logged-in user
      3. Call the relevant function of the Recipes class to add/create
         a new record in the recipes table. Pass in the relevant 
         information as arguments to the function.
      4. Redirect to the Recipes (listing) page.'''
    if request.method == 'GET':
        return render_template('add_recipe.html')
    auth = Auth()
    recipe = Recipes()

    data = {
    'name': request.form.get('name', None),
    'description': request.form.get('description', None),
    'ingredients': request.form.get('ingredients', None),
    'image': request.form.get('image', None)
    }

    user_id = auth.get_current_user()['id']
    recipe.add_recipe(data, user_id)
    return redirect(url_for('show_recipes'))


@app.route("/recipes/<int:recipe_id>/")
def show_recipe(recipe_id):
    '''Show the recipe that matches the given recipe ID.'''
    recipe = Recipes()
    this_recipe = recipe.get_recipe(recipe_id)
    return render_template('recipe.html', recipe=this_recipe)
