def simplify(filename):
	with open(filename) as file:
		text = file.read()

	lines = text.split('\n')
	clean_lines = []
	for line in lines:
		if 'class' in line and '#' in line:
			website = line[:line.find('#')]
			class_names = line[line.find('"') + 1 : line.find(']') - 1].split()
			for name in class_names:
				clean_lines.append(website + '##.' + name)
		else:
			clean_lines.append(line)

	clean_lines.sort()
	
	with open(filename, "w") as file:
		file.write('\n'.join(clean_lines))


simplify('block-list.txt')