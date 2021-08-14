# Recommendations
Book/Website recommendation

## Change recommendations :
Every information is stored in the reco.json file, which has the following structure :
```
+-- "books"
| +-- categorie of book (like "maths", "computer science", ...)
| | + 
| | | +-- "title" : 
| | | +-- "author" :
| | | +-- "year" :
| | | +-- "trad" (if there is any):
| | | | +-- language (like "french")
| | | | | +-- "year" :
| | | | | +-- "title" :
| | | | ...
| | ...
+-- "websites"
```

## Change the rendered files :
You can change the way index.html and recommendations.tex (and add other files) are made through the affich.languinv file as explained in the repository [compil_perso](https://github.com/UlysseDurand/compil_perso).

## Compile :
Just run ```make```, it will create the files (like index.html and recommendations.tex) and then it will compile the .tex files in .pdf.
