import os

def main():
	chatall = 'linechatin.txt'
	chatconvert = []
	if os.path.isfile(chatall):
		print('有找到檔案')
		lines = readchat(chatall)
		lines = convert(lines)
		#writefile('linechatin.txt', lines)
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
	m_wd = 0
	k_wd = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		for m in s[2:]:
			if s[1] == '盟':
				m_wd += len(m)
			elif s[1] == '康':
				k_wd += len(m)
	print('盟說了' , m_wd , '個字')
	print('康說了' , k_wd , '個字')
	return new

def writefile(filename,lines):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')


main()