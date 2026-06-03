#===========================================================
# APP NAME HERE
# By YOUR NAME HERE
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Welcome page
#-----------------------------------------------------------
@app.get("/")
def show_welcome():
    return render_template("pages/welcome.jinja")


#-----------------------------------------------------------
# Creature list page - Show all the creatures
#-----------------------------------------------------------
@app.get("/creatures")
def show_all_creatures():
    with connect_db() as db:
        # Get the creatures to show
        sql = """
            SELECT id, species, name
            FROM creatures
        """
        params = ()
        creatures = db.execute(sql, params).fetchall()
        
        # Get the species for the drop-down in search
        sql = """
            SELECT DISTINCT species
            FROM creatures
            ORDER BY species ASC
        """
        params = ()
        species_rows = db.execute(sql, params).fetchall()
        # Turn into flat list
        species_list = [species['species'] for species in species_rows]

        return render_template("pages/creature_list.jinja", creatures=creatures, species_list=species_list)


#-----------------------------------------------------------
# Search the creatures
#-----------------------------------------------------------
@app.get("/search")
def process_search():
    search_term = request.args.get('q', '')          # fixed: args not arg
    search_match = f"%{search_term}%"
    species_term = request.args.get('species', '')   # fixed: args not arg
    
    with connect_db() as db:
        # Build query depending on whether species filter is active
        if species_term and species_term != 'all':
            sql = """
                SELECT id, species, name
                FROM creatures
                WHERE (name LIKE ? OR species LIKE ?)
                AND species = ?
            """
            params = (search_match, search_match, species_term)
        else:
            sql = """
                SELECT id, species, name
                FROM creatures
                WHERE name LIKE ? OR species LIKE ?
            """
            params = (search_match, search_match)

        creatures = db.execute(sql, params).fetchall()

        sql = """
            SELECT DISTINCT species
            FROM creatures
            ORDER BY species ASC
        """
        species_rows = db.execute(sql, ()).fetchall()
        species_list = [species['species'] for species in species_rows]

    return render_template(
        "pages/creature_list.jinja",
        creatures=creatures,
        species_list=species_list,
        search_term=search_term,
        species_term=species_term
    )

#-----------------------------------------------------------
# Help page - Show some help
#-----------------------------------------------------------
@app.get("/help")
def show_help():

    flash("Flash test message")
    flash("Flash test message with a longer bit of text")
    flash("Success test message", "success")
    flash("Error test message", "error")

    return render_template("pages/help.jinja")


#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

