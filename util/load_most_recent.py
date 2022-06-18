import os
save_path = "./text/saves/"



#YIELD IS WIERD
# def load_most_recent_filestring(path):
# 	def all_files_under(path):
# 		for cur_path, dirs, files in os.walk(path):
# 			for f in files:
# 				yield os.path.join(cur_path,f)
# 	latest_file=max(all_files_under(path), key=os.path.getmtime)
# 	print(latest_file)
def load_most_recent_filestring():
	return max([f for f in os.scandir(save_path)], key=lambda x: x.stat().st_mtime).name

# if __name__=="__main__":
# 	latest_edited_file = max([f for f in os.scandir(save_path)], key=lambda x: x.stat().st_mtime).name
# 	print(latest_edited_file)