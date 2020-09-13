import csv
with open('Prays-list_SZSK-2018_g.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for row in spamreader:
		print('<tr>')
		if row[1].isdigit() or ('.' in row[1] and all(i.isdigit() for i in row[1].split('.'))):
			print(f'  <td>{row[1]}</td>')
			print(f'  <td>{row[2]}</td>')
			print(f'  <td>{row[3].strip()}</td>')
			print(f'  <td>{row[6].replace("2","²").replace("3","³")}</td>')
		else:
			print('  <th colspan="4" class="w3-center w3-text-yellow">' + row[1].strip() + '</th>')
		print('</tr>')