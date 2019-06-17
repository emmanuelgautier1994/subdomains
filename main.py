# f = open("gouv.fr.txt", "r").read().splitlines()
import csv

domain_tree = {}

with open('gouv.fr.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            x = row[0]
            url = x.split('.')[::-1]
            dict_pointer = domain_tree

            while(url):
            	if not(url[0] in dict_pointer.keys()):
            		dict_pointer[url[0]] = {}
            	dict_pointer = dict_pointer[url[0]]
            	url.pop(0)

            dict_pointer["__node__"] = x

        line_count += 1

def recDrawTree(dict, original_depth):
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