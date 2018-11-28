# Gender Bender for web
This is a website that flips text so that all male character become female and all female characters become male. At a high level, it does so by switching out all of the male pronouns and names for female pronouns and names and vice versa. The live site can be found at: https://nameless-shelf-22750.herokuapp.com/

### Usage
Simply input a set of text press the genderbend button! Optionally, you can specify the year it was written in order to provide historically accurate names.

### Context
This is the second iteration of a project concieved in a hybrid art and computer science class that involved genderbending classic novels. The original prompt was to create a book consisting of generative text. The results can be seen here:http://cmuems.com/2018/60212f/yalbert/11/16/yalbert-book/

The the original project occcured over a week long assignment. This second iteration involved improving the genderbending algorithm, reorganizing the code, and formatting it for the web. This was done over a couple of days.

# Details

### Frameworks
The web app was build in Django and deployed using Heroku.

### Files of Interest
Many of the files in this repository are a part of the basic Django framework. The interesting ones are:

#### Frontend: 
- gender_bender_web/genderbender/templates/genderbender/index.html

#### Backend: 
- gender_bender_web/genderbender/views.py

#### Genderbending Algorithm:
- gender_bender_web/genderbender/genderBender.py 
- gender_bender_web/genderbender/nameDictMaker.py
- gender_bender_web/genderbender/pronounDictMaker.py

# How it works
There are three primary stages to this genderbending algorithm, 1) parsing the text 2) compiling the pronoun dictionary 3) compiling then name dictionary and 4) replacing all of the existing names and pronouns based on the aforementioned dictionaries.

### Parsing the text
Relevant files: gender_bender_web/genderbender/genderBender.py 
If we were to just use the raw text in its original format (a string) replacing the words in the text would be extremely costly because one would have to rewrite the entire string for each word replacement. Therefore, I created a custom stringsplit function that clumps all words together and isolated all non-letters (eg: ["Harry", ",", " ", "the", " ", "wizard"]). This made replacements much less costly and made it easier to search for names in order to compile the name dictionary.

### Compiling pronoun dictionary
Relevant files: gender_bender_web/genderbender/genderBender.py; gender_bender_web/genderbender/pronoun_corpus/pronouns.txt 


# Reflection
