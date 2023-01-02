# flask_webapp_boilerplate
Boilerplate code and file structure for webapp developement in python and flask.  Don't use this unless you know me for now.  Its not ready for the wider world yet.  Taking PRs to clean up code primarily.  I would love PRs to make the HTML look nicer.  I will consider PRs for additional features.

Presently provisions an admin, signin and sign up page which function, and demonstrate flask's HTML and python injection syntax.

The hello world page is simply there to demonstrate blue printing in the most stripped back form

### Warnings
This app is distributed with a secret key defiend in webapp.py.  This is to make it easy to launch and play with the webapp.  Change this before going live with your project

### Skeleton css
The provided module use skeleton css as a base, with a tiny bit of custom css to demonstrate writing your own css (named my_style.css)

## Download dependancies with requirements.txt
```
python3 -m pip -r requirements.txt
```

## To launch webapp
launch debug server on local with 
```
flask --app webapp --debug run
```

# Items requiring further development
1. Clean up static, moving blueprint static under each blueprint
2. Add additional comments for new python users
3. Disambiguate any variables or files with identical names
4. Move some unorganized functions to utils or move under blueprint utils (or neither or both)
5. Finish the sign-in sign-up blueprint
