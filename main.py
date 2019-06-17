import csv

domain_tree = {} # this dictionary will bear the tree structure 

with open('gouv.fr.csv') as csv_file: # reading CSV and inserting into dictionary
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0: # leaving CSV header out
            x = row[0]
            url = x.split('.')[::-1] # e.g. "www.gouv.fr" => ["fr", "gouv", "www"]
            dict_pointer = domain_tree

            while(url): # inserting the URL's domain levels as nested dicts within domain_tree
            	if not(url[0] in dict_pointer.keys()):
            		dict_pointer[url[0]] = {}
            	dict_pointer = dict_pointer[url[0]] # moving the pointer one level deeper
            	url.pop(0)

            dict_pointer["__node__"] = x # once at URL's tip, writing the full URL at an arbitrary "__node__" key

        line_count += 1

def recDrawTree(dict, original_depth): # recursively prints tree represented by dict, with memory of depth level
	keys = list(dict)
	keys.sort()

	for k in keys:
		if k == "__node__":
			line = " "*original_depth + "-- " + dict["__node__"]
			print(line)
			with open("output.txt", "a+") as output:
				output.write(line + '\n')
		else:
			recDrawTree(dict[k], original_depth+1)

open("output.txt", "w").close()
recDrawTree(domain_tree, 0)