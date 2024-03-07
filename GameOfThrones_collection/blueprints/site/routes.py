from flask import Blueprint, flash, redirect, render_template, request

#internal import 
from GameOfThrones_collection.helpers import get_character
from GameOfThrones_collection.models import Character, db
from GameOfThrones_collection.forms import CharacterForm


#need to instantiate the Blueprint class
site = Blueprint('site', __name__, template_folder='site_templates')


#use site object to create the routes
@site.route('/')
def character_collection():

    #need to query the database to grab all of the characters to display
    allcharacters = Character.query.all() #the same as SELECT * FROM characters, list of objects 


    #making a dictionary for the shop stats/info

    collection_stats = {
        'characters' : len(allcharacters), # this is how many total characters the user has
    }


                            #whats on left side is html, right side is whats in our route
    return render_template('character_collection.html', character_collection=allcharacters, stats=collection_stats) #looking inside the template_folder (site_templates) to find the character_collection.html file


@site.route('/character_collection/add', methods= ['GET', 'POST']) 
def add():                                       # *** CHANGED THIS FROM "CREATE" IN THE NOTION TO ADD ***

    #instantiate the characterform

    addform = CharacterForm()

    characters = get_character()
    # print(characters)
    # print(characters[0]["fullName"])

    if request.method == 'POST' and addform.validate_on_submit():
        #grab our data from our form
        full_name = addform.full_name.data.title()
        description = addform.description.data
         
        for i in characters:
            if i["fullName"] == full_name:
                first_name = i["firstName"]
                last_name = i["lastName"]
                title = i["title"]
                family = i["family"]
                image = i["imageUrl"]


        #instantiate that class as an object passing in our arguments to replace our parameters 
        
        character = Character(first_name, last_name, full_name, title, family, image, description)

        db.session.add(character) #adding our new instantiating object to our database
        db.session.commit()

        flash(f"You have successfully added character {full_name}", category='Success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect('/character_collection/add')
    

    return render_template('create.html', form=addform )


@site.route('/character_collection/update/<id>', methods=['GET', 'POST']) #<parameter> this is how pass parameters to our routes 
def update(id):

    #lets grab the specific character we want to update
    character = Character.query.get(id) #this should only ever bring back 1 item/object
    updateform = CharacterForm()

    if request.method == 'POST' and updateform.validate_on_submit():

        character.full_name = updateform.full_name.data 
        character.description = updateform.description.data 

        #commit our changes
        db.session.commit()

        flash(f"You have successfully updated character {character.full_name}", category='Success')
        return redirect('/')
    
    elif request.method == 'POST':
        flash("We were unable to process your request", category='warning')
        return redirect('/')
    
    return render_template('update.html', form=updateform, character=character )


@site.route('/character_collection/delete/<id>')
def delete(id):

    #query our database to find that object we want to delete
    character = Character.query.get(id)

    db.session.delete(character)
    db.session.commit()

    return redirect('/')



