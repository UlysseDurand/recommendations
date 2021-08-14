import json
data = json.loads(open("reco.json").read())
print("")

def printbook(e):
    print("\\subsubsection{"+e["title"]+"}")
    print("\\textit{By "+e["author"]+"}\\\\\\\\")
    print("First published in "+e["year"])
print("")
print("\\documentclass{article}")
print("")
print("\\begin{document}")
print("    \\section{Books}")
print("")

for key,value in data["books"].items():
    print("\\subsection{"+key+"}")
    for e in value:
        printbook(e)
print("")
print("\\end{document}")
print("")
