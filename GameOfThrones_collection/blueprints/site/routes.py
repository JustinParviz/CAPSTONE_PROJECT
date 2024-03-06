from flask import Blueprint, render_template 

#internal import 
from GameOfThrones_collection.helpers import get_character


#need to instantiate our Blueprint class
site = Blueprint('site', __name__, template_folder='site_templates' )


#use site object to create our routes
@site.route('/')
def character_collection():
    # characters = get_character()
    # # print(characters)
    # print(characters[0]["fullName"])

    # for i in characters:
    #     if i["fullName"] == search

    
    return render_template('character_collection.html') #looking inside our template_folder (site_templates) to find our character_collection.html file