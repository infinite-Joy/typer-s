###############################################################################################################################
## This file contains the class for each key object and core funcitons for defining the datastructure used in thsi program   ##
## datastructure is a tree like structure in which the parent node will be the space key and each node will have 52 leaf     ##
## nodes. This 52 can be defined 26 captial letters and 26 small letters of english alphabet                                 ##
## The object creation function is accepting values from front end and creat the object which is storing in the              ##
## datastructure.                                                                                                            ##
##                                                   Author: hhsecond                                                        ##
##                                          Github: github.com/hhsecond/typer-s                                              ##
##                                                   date: 1/30/2016                                                         ##
###############################################################################################################################

import threading, time


dicti = {}
#trial_dict = {'a':{'b':{'c':{'d':{}}, 'e':{}}}} - Trial dictionary: datastructure will look like this if the words added are "abcd" and "abe"
dict_time_args = {0:[0.0, 0.0]}
dict_counter = {'Space':0}
counter = 0
key_list = []


class key:
	"""docstring for key - this class is for creating  object with 2 attributes which we are accounting for a key"""
	def __init__(self, name, hold, releasedn):
		#super(key, self).__init__() ------------------- what is this doing?
		self.hold = hold #hold time for a key : (key up time - key down time)
		self.releasedn = releasedn # duration between each key strokes: (previous key down time - current key down time)
		self.name = name #key name in character rather string format:  for readability


#function creates dictionary which will accept a word at a time as a list of characters
#dictionary = dicti, fetching the main dictionary if no dictionary specified in the function call
def dict_create(key_list, dictionary = dicti):
	#fetching each key and sending to the dict create function
	for key_val in key_list:
		dictionary = key_to_dict(key_val, dictionary) #returning dictionary recursively


def key_to_dict(key_val, dictionary):
	#function which is currently executing does not have other dictionary functions. kind of funcitonal programming
	for key in dictionary:
		if key.name == key_val.name:			
			key.hold = (key.hold + key_val.hold)/2

			#handling cases with releasedn value is zero
			if key.releasedn == 0.0:
				key.releasedn = key_val.releasedn
				return dictionary[key]
			elif key_val.releasedn == 0.0:
				return dictionary[key]				
			else:
				key.releasedn = (key.releasedn + key_val.releasedn)/2
				return dictionary[key]
	dictionary[key_val] = {}	
	return dictionary[key_val]



class objthread(threading.Thread):
	"""docstring for objthread - handling threads which is creating by each and every event from typer-s"""
	def __init__(self, event_name, event_window, event_time, event_status):
		threading.Thread.__init__(self)
		self.start()



		



#Sample codes starts here with test inputs and printing fucntion - can be used for debugging
def dict_print(dictionary):
	for key, value in dictionary.items():
		print(key.name, " : ", key.hold, " : ", key.releasedn)
		if value:
			dict_print(value)



if __name__ == '__main__':
	
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:18:42.750011, 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:18:42.796885, 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:18:42.906262, 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:18:42.984389, 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:18:43.046889, 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:18:43.140638, 0)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', 2016-02-12 15:18:43.625020, 1)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', 2016-02-12 15:18:43.750022, 0)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', 2016-02-12 15:18:46.256002, 1)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', 2016-02-12 15:18:46.412238, 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:19:23.097165, 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:19:23.206544, 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:23.487794, 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:23.581547, 0)
	with threading.Lock():
		objthread('E', 'cmd.exe', 2016-02-12 15:19:23.909676, 1)
	with threading.Lock():
		objthread('E', 'cmd.exe', 2016-02-12 15:19:24.034676, 0)
	with threading.Lock():
		objthread('R', 'cmd.exe', 2016-02-12 15:19:24.378394, 1)
	with threading.Lock():
		objthread('R', 'cmd.exe', 2016-02-12 15:19:24.503375, 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:24.789287, 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:24.898725, 0)
	with threading.Lock():
		objthread('N', 'cmd.exe', 2016-02-12 15:19:25.242471, 1)
	with threading.Lock():
		objthread('N', 'cmd.exe', 2016-02-12 15:19:25.351853, 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:26.101857, 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:26.242483, 0)
	with threading.Lock():
		objthread('C', 'cmd.exe', 2016-02-12 15:19:26.554981, 1)
	with threading.Lock():
		objthread('C', 'cmd.exe', 2016-02-12 15:19:26.664366, 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:26.929992, 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:27.039367, 0)
	with threading.Lock():
		objthread('A', 'cmd.exe', 2016-02-12 15:19:27.304995, 1)
	with threading.Lock():
		objthread('A', 'cmd.exe', 2016-02-12 15:19:27.461247, 0)
	with threading.Lock():
		objthread('C', 'cmd.exe', 2016-02-12 15:19:27.762813, 1)
	with threading.Lock():
		objthread('C', 'cmd.exe', 2016-02-12 15:19:27.887822, 0)
	with threading.Lock():
		objthread('K', 'cmd.exe', 2016-02-12 15:19:28.200321, 1)
	with threading.Lock():
		objthread('K', 'cmd.exe', 2016-02-12 15:19:28.294072, 0)
	with threading.Lock():
		objthread('O', 'cmd.exe', 2016-02-12 15:19:28.633682, 1)
	with threading.Lock():
		objthread('O', 'cmd.exe', 2016-02-12 15:19:28.711867, 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:29.088536, 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:29.213588, 0)
	with threading.Lock():
		objthread('T', 'cmd.exe', 2016-02-12 15:19:29.541716, 1)
	with threading.Lock():
		objthread('T', 'cmd.exe', 2016-02-12 15:19:29.651093, 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:29.947974, 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:30.041725, 0)
	with threading.Lock():
		objthread('O', 'cmd.exe', 2016-02-12 15:19:30.494853, 1)
	with threading.Lock():
		objthread('O', 'cmd.exe', 2016-02-12 15:19:30.604230, 0)
	with threading.Lock():
		objthread('M', 'cmd.exe', 2016-02-12 15:19:30.901106, 1)
	with threading.Lock():
		objthread('M', 'cmd.exe', 2016-02-12 15:19:31.026116, 0)
	with threading.Lock():
		objthread('A', 'cmd.exe', 2016-02-12 15:19:31.244862, 1)
	with threading.Lock():
		objthread('A', 'cmd.exe', 2016-02-12 15:19:31.385489, 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:19:31.729243, 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:19:31.854251, 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:32.604252, 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:32.739848, 0)
	with threading.Lock():
		objthread('M', 'cmd.exe', 2016-02-12 15:19:33.083603, 1)
	with threading.Lock():
		objthread('M', 'cmd.exe', 2016-02-12 15:19:33.192990, 0)
	with threading.Lock():
		objthread('E', 'cmd.exe', 2016-02-12 15:19:33.489811, 1)
	with threading.Lock():
		objthread('E', 'cmd.exe', 2016-02-12 15:19:33.599234, 0)
	with threading.Lock():
		objthread('R', 'cmd.exe', 2016-02-12 15:19:33.880490, 1)
	with threading.Lock():
		objthread('R', 'cmd.exe', 2016-02-12 15:19:33.989865, 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:34.302369, 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:34.411746, 0)
	with threading.Lock():
		objthread('N', 'cmd.exe', 2016-02-12 15:19:34.692997, 1)
	with threading.Lock():
		objthread('N', 'cmd.exe', 2016-02-12 15:19:34.818009, 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:35.161753, 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:35.302380, 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:19:35.614884, 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:19:35.724260, 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:36.052389, 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:36.166664, 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:37.095054, 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:37.204428, 0)
	with threading.Lock():
		objthread('M', 'cmd.exe', 2016-02-12 15:19:37.548182, 1)
	with threading.Lock():
		objthread('M', 'cmd.exe', 2016-02-12 15:19:37.688808, 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:37.965571, 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:38.106200, 0)
	with threading.Lock():
		objthread('N', 'cmd.exe', 2016-02-12 15:19:38.403077, 1)
	with threading.Lock():
		objthread('N', 'cmd.exe', 2016-02-12 15:19:38.528082, 0)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:38.856179, 1)
	with threading.Lock():
		objthread('Space', 'cmd.exe', 2016-02-12 15:19:38.996834, 0)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:19:39.278092, 1)
	with threading.Lock():
		objthread('S', 'cmd.exe', 2016-02-12 15:19:39.371838, 0)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:39.715592, 1)
	with threading.Lock():
		objthread('H', 'cmd.exe', 2016-02-12 15:19:39.824968, 0)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:40.106221, 1)
	with threading.Lock():
		objthread('I', 'cmd.exe', 2016-02-12 15:19:40.215598, 0)
	with threading.Lock():
		objthread('N', 'cmd.exe', 2016-02-12 15:19:40.496851, 1)
	with threading.Lock():
		objthread('N', 'cmd.exe', 2016-02-12 15:19:40.606228, 0)
	with threading.Lock():
		objthread('J', 'cmd.exe', 2016-02-12 15:19:40.924614, 1)
	with threading.Lock():
		objthread('J', 'cmd.exe', 2016-02-12 15:19:41.018358, 0)
	with threading.Lock():
		objthread('O', 'cmd.exe', 2016-02-12 15:19:41.393364, 1)
	with threading.Lock():
		objthread('O', 'cmd.exe', 2016-02-12 15:19:41.502741, 0)
	with threading.Lock():
		objthread('Escape', 'cmd.exe', 2016-02-12 15:19:43.891825, 
	dict_print(dicti)
