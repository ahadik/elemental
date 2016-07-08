import csv

with open('elements.csv', 'rb') as csvfile:
	elementReader = csv.reader(csvfile, delimiter=',')
	header = elementReader.next()
	sassString = "$elements: (\n"
	for row in elementReader:
		sassString += '\t' + row[0].rstrip().lstrip()+' : (\n'
		index = 1
		for datum in row[1:-1]:
			sassString += '\t\t' + header[index] + ' : \'' + datum.lstrip().rstrip() + '\',\n'
			index += 1
		if len(row[-1]) < 6:
			row[-1] = '00'+row[-1]
		row[-1] = row[-1].replace('+', '')
		sassString = sassString + '\t\t' + header[-1] + ' : #' + row[-1] + '\n\t),\n'
	sassString = sassString[:-2] + '\n);'
	with open('out.txt', 'wb') as f:
		f.write(sassString)
