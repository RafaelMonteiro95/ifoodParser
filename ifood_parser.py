import sys
import re
import os

#parsing stuff
with open('tmp.txt', 'w+', encoding='utf8') as fout:
    with open(sys.argv[1], encoding='utf8') as fin:
        for line in fin:
        	#if i found an item, search for its price
            item = re.search('.*<input id="des.*value="(.*)" value=""/', line)
            if item:
                nextLine = next(fin);
                value = re.search('.*value="(.*)" value=""/>', nextLine)
                #sometimes it's right at the next line
                if float(value.group(1)) > 0:
                	print("{}	R${}0".format(item.group(1), value.group(1)),file=fout);
                #sometimes life sucks and you have to keep reading until you find something
                else:
                	while True:
	               		nextLine = next(fin);
	               		value = re.search('R\$ (.*)', nextLine)
	               		if value:
	               			print("{}	R${}".format(item.group(1), re.sub(',','.',value.group(1))), file=fout);
	               			break;

#fix bad encoding. Fuck you, regex
#but regex is very useful btw
with open(re.sub('\..*','.out',sys.argv[1]), 'w+') as fout:
    with open('tmp.txt', 'r', encoding='utf8') as fin:
        for line in fin:
            line = line.replace("&Aacute;", "Á")
            line = line.replace("&aacute;", "á")
            line = line.replace("&Oacute;", "Ó")
            line = line.replace("&oacute;", "ó")
            line = line.replace("&Uacute;", "Ú")
            line = line.replace("&uacute;", "ú")
            line = line.replace("&atilde;", "ã")
            line = line.replace("&Agrave;", "À")
            line = line.replace("&agrave;", "à")
            line = line.replace("&amp;", "&")

            print(line,end='',file=fout);
    os.remove('tmp.txt')