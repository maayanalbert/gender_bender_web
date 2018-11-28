# Gender Bender for web
This is a website that flips text so that all male character become female and all female characters become male. At a high level, it does so by switching out all of the male pronouns and names for female pronouns and names and vice versa. The live site can be found at: https://nameless-shelf-22750.herokuapp.com/

### Context
This is the second iteration of a project concieved in a hybrid art and computer science class that involved genderbending classic novels. The original prompt was to create a book consisting of generative text. The results can be seen here:http://cmuems.com/2018/60212f/yalbert/11/16/yalbert-book/

The the original project occcured over a week long assignment. This second iteration involved improving the genderbending algorithm, reorganizing the code, and formatting it for the web. This was done over a couple of days.

### Frameworks
Django, Heroku, Bootstrap

### Files of Interest
Many of the files in this repository are a part of the basic Django framework. The interesting ones are:
- gender_bender_web/genderbender/templates/genderbender/index.html (frontend)
- gender_bender_web/genderbender/views.py (backend)
- gender_bender_web/genderbender/genderBender.py (genderbending algorithm)
- gender_bender_web/genderbender/nameDictMaker.py (genderbending algorithm)
- gender_bender_web/genderbender/pronounDictMaker.py (genderbending algorithm)

# How it works
I used find and replace algorithm that basically found all of the gendered pronouns and names and replaced them with the opposit gender. Although this method doesn't work perfectly (ML would probably be the best way to yeild completely accurare results) it produces beleivable results.

Major considerations I had when building this were efficiency (because I was potentially processing long strings) and how to acheive beleivable names. 

## Steps
There are four primary stages to this genderbending algorithm, 1) parsing the text 2) compiling a dictionary of pronouns mapped to their opposite gendered equivalents 3) compiling a dictionary of names mapped to their opposite gendered equivalents and 4) replacing all of the existing names and pronouns based on the aforementioned dictionaries.

### 1) Parsing the text
If we were to just use the raw text in its original format (a string), replacing the words in the text would be extremely costly because one would have to rewrite the entire string for each word replacement. Therefore, I created a custom stringsplit function that clumps all words together and isolated all non-letters (eg: ["Harry", ",", " ", "the", " ", "wizard"]). This made replacements much less costly and made it easier to search for names in order to compile the name dictionary.

Relevant files: 
- gender_bender_web/genderbender/genderBender.py

### 2) Compiling pronoun dictionary (eg dict = {his:her, man:woman, Mr.:Mrs.})
This step was pretty straightforward. I simply read in a txt file containing matching pronouns and compiling a dictionary. A consideration when adding pronouns to the dictionary was making sure I had all iterations of the word (uppercase, lowercase, plural, etc). 

Relevant files: 
- gender_bender_web/genderbender/pronounDictMaker.py; 
- gender_bender_web/genderbender/pronoun_corpus/pronouns.txt

### 3) Compiling name dictionary (eg dict = {Olive:Oliver, Hermione:Hermon, Mary:Marcus})
This was the most challenging part of the project. I struggled to find a decent corpus of names until I came acccross records from the US Social Security Administristration that contained the 10000 most popular baby names arranged in order of populary since 1880 (https://www.ssa.gov/oact/babynames/limits.html).

To find name replacements, I first iterated through the word array described above and picked out any word that appeared in the name file for the year the book was written. For each name found, I went through all of the opposite gendered names and used Levenshtein's distance algorithms to create a shortlist of names that were similar to the original. I then picked the most popular name from the shortlist and mapped it to the original name.

To speed up this process, I partitioned the names from the corpus into subdictionaries based first letter (eg. A={Amy, Amanda, Ada}, B={Bernadine, Becky}, etc). Therefore, in order to find the opposite gendered equivalent, I only had to look through the names with the same letter as the original instead of all of them.

Relevant files: 
- gender_bender_web/genderbender/nameDictMaker.py; 
- gender_bender_web/genderbender/name_corpus/*

### 4) Replacing words
This part was also quite straightforward. I simply iterated through the word array and if a word showed up as a key in either dictionary, I mapped it to its corresponding value.

Relevant files:
- gender_bender_web/genderbender/genderBender.py


# What I liked about this project
From a technical standpoint, I liked how there wasn't allways a clear answer for how best to solve the problems that arose. Most of this was self driven, so I had to figure out where I was going to get my data and how I wanted to structure it on my own. I found the process of solving these problems and seeing the results of my work very rewarding.

From a social standpoint, I like how this project raises awareness about gender expectations. Reading through the genderbent novels, I found certain characters strange before realizing that it was because their genders had been switched. I think it's interesting to consider why we think certain behavior is normal for a man yet strange for a woman and vice versa.

# Next steps
If I were to work on this project more, I'd like to continue testing and improving the genderbending algorithm and website. In addition, I'd like to explore creating a browser plugin that genderbends all of the text on a given website. 
