from index import Index
import os

path_str = '.'
path_list = []
File_index = Index()
def bfs(upper_path,upper_path_list):
	for i in os.listdir(upper_path):
		new_path = upper_path+'/'+i
		new_path_list = upper_path_list + [i]
		File_index.register(new_path_list,None)
		if os.path.isdir(new_path):
			bfs(new_path,new_path_list)
	return 

bfs(path_str,path_list)

print(File_index.tree())