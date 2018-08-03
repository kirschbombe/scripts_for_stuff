# If using Python 2, use `raw_input` for variable on rows 5 and 7. If using Python 3, change to `input`
# The script will automatically generate a new file named `output.tsv`, just enter the path to the directory where you would like to save the new file.

import re , codecs

file = raw_input('Enter file path: ')
file = file.replace(" ","")
output_file = raw_input('Enter output path: ')
output_file = output_file.replace(" ","")

# with open(file, encoding='utf-8') as f:
# data = f.read().decode('utf8', 'ignore')

f = open(file, 'r')
total_text = f.read()

#f=open('CISALL.txt','r')
#total_text=f.read()
total_text=total_text.replace('\n',' ')
## total_text=re.replace('\s*',' ')
print(total_text[:100])
f.close()

reported=re.findall("Reported\:.*?(?:(?!Location\:).)*",total_text)
location=re.findall("Location\:.*?(?:(?!Report #\:).)*",total_text)
incident=re.findall("Incident\:.*?(?:(?!Summary\:).)*",total_text)
summary=re.findall("Summary\:.*?(?:(?!Reported\:).)*",total_text)

reported = [i.replace('\t','') for i in reported ]
location = [i.replace('\t','') for i in location ]
incident = [i.replace('\t','') for i in incident ]
summary = [i.replace('\t','') for i in summary ]

f = open((output_file) + '/output.tsv','w')

for combo in zip(reported,location,incident,summary):
    out_line='\t'.join(combo)
    f.write(out_line+'\n')
f.close()
