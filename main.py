#!/usr/bin/env python

def simplify(filename):
	with open(filename) as file:
		lines = file.read().split('\n')

	clean_lines = []
	for line in lines:
		if 'class' in line and '#' in line:
			website = line[:line.find('#')]
			class_names = line[line.find('"') + 1 : line.find(']') - 1].split()
			for name in class_names:
				clean_lines.append(website + '##.' + name)
		else:
			clean_lines.append(line)

	with open(filename, "w") as file:
		adblock_header = clean_lines[:8]
		websites = sorted(set(clean_lines[8:]))
		file.write('\n'.join(adblock_header + websites))


simplify('block-list.txt')
