import csv

def parse_input(input_file):
	data_dict = dict()
	index = 1
	with open(input_file, "r") as fp:
		for line in fp:
			key = str(index)
			file_name, x, y, width, height = line.rstrip().split(',')
	    		data_dict[key] = {'file' :  file_name  ,\
	                      'x' : float(x),\
	                      'y' : float(y),\
	                      'width' : float(width),\
	                      'height' : float(height),\
	                  }
			index = index + 1
	return data_dict
