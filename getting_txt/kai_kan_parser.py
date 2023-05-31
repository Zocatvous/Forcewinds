import os
import regex as re
import pprint as pprint
import json


def objectify_techniques(tech_l):
	big_obj = []

	#map tech to t_obj
	i = 0
	for tech in tech_l:
		t_obj = {
	"name":'',
	"cost":'',
	"type":'',
	"die_pool":'',
	"activation_time":'',
	"duration":'',
	"range":'',
	"prereq":'',
	"targets":'',
	"defense":'',
	"effect":'',
	"description":'',
	"style":'',
	"mins":'',
	"keywords":''
	}
		i+=1
		t_obj['name'] = tech[0]
		t_obj['id'] = i
		for line in tech:
			if re.search(r'cost\:',line, re.IGNORECASE):
				t_obj['cost'] = line
			if re.search(r'Mins\:', line, re.IGNORECASE):
				t_obj['mins'] = line
			if re.search(r'Type\:', line, re.IGNORECASE):
				t_obj['type'] = line
			if re.search(r'Prereq\:', line, re.IGNORECASE):
				t_obj['prereq'] = line
			if re.search(r'Duration\:', line, re.IGNORECASE):
				t_obj['duration'] = line
			if re.search(r'Targets\:', line, re.IGNORECASE):
				t_obj['targets'] = line
			if re.search(r'Activation', line, re.IGNORECASE):
				t_obj['activation_time'] = line
			# if re.search(r'Defense', line, re.IGNORECASE):
			# 	t_obj['defense'] = line
			if re.search(r'Keyword', line, re.IGNORECASE):
				t_obj['keywords'] = line
			if len(line) > 20:
				t_obj['description'] = line
		big_obj.append(t_obj)
		# pprint.pprint(big_obj)
		# input()
	return big_obj




def ingest_techniques(lines):
	#build a list of a lists that are blobs of all the data for a specific technique 
	final_line_list = []
	technique_line_boundary = 0
	technique_l = []
	boundary = True
	for i,line in enumerate(lines):
		#edge of a technique block - set boundary to true
		if re.search(r'(\n|\ufeff\n)',line):
			boundary = True
		#skip 
		if re.search(r'\n', line) and boundary is True:
			pass
		#detect a boundary of a technique block - set boundary to false
		if re.search(r'.', line) and boundary is True:
			boundary = False
			technique_l.append(line)
		#just finished the technique block - set boundary to true delete the tlist append the final_list
		if re.search(r'\n', line) and boundary is True and len(technique_l)>0:
			boundary = True
			final_line_list.append(technique_l)
			technique_l = []
	return final_line_list
		# print(f'Boundary:{boundary} - line is [{line}]')
		# print(technique_l)
		# print(f'{len(final_line_list)} techniques - {final_line_list}')
		# input('next?')
#make everything a string - we'll pull it all in and figure it out later

kai_kan_filestring = './files/KaiKan/'
files = os.listdir(kai_kan_filestring)





for file in files:
	with open(kai_kan_filestring+file) as f:
		lines = f.readlines()
		technique_list = ingest_techniques(lines)
		print(f'{len(technique_list)} techniques in {file}')
		#pprint.pprint(technique_list)
		input('Turn all that into objects?')
		result = objectify_techniques(technique_list)
		n = file.strip('.txt')
		with open(f'./files/json/{n}.json', 'w') as j:
			json.dump(result,j)


