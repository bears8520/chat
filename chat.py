import os

def main():
	chatall = 'chatin.txt'
	chatconvert = []
	if os.path.isfile(chatall):
		print('有找到檔案')
		lines = readchat(chatall)
		lines = convert(lines)
		writefile('chatout.txt', lines)
	else:
		print('無清單檔案')

def readchat(chatall):
	lines = []
	with open(chatall, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
		return lines

def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == '楊鎮宇':
			person = '楊鎮宇'
			continue
		elif line == 'Lu':
			person = 'Lu'
			continue
		if person:
			new.append(person + ': ' + line)
	return new

def writefile(filename,lines):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')


main()