import os
import sys
sys.path.insert(1, os.getcwd())
import definition
class Gallery(object):
    def __init__(self):
        pass
    def get_all_gallery(self):
        try:
            gallaries=[]
            all_entries =os.listdir("static/photos/")
            for entry in all_entries:
                full_path=os.path.join("static/photos/",entry)
                if(os.path.isdir(full_path)):
                    gallaries.append(entry)
            return gallaries
        except FileNotFoundError:
            return []

    def add_gallery(self,name_gallary):
        path_name =os.path.join("static/photos/",name_gallary)
        if (not os.path.exists(path_name)):
            try:
                os.mkdir(path_name)
                return True
            except OSError as e:
                print(f"Error creating Directory {e}")
                return False
        else:
            return False
        
    def delete_gallery(self,name_gallary):
        path_name=os.path.join("static/photos/",name_gallary)
        if (os.path.exists(path_name)):
            try:
                os.rmdir(path_name)
                return True
            except OSError as e:
                print(f"Error in deleting diretory {e}")
                return False
        else:
            return False
        
    def rename_gallery(self,old_name,new_name):
        old_path=os.path.join("static/photos/",old_name)
        new_path=os.path.join("static/photos/",new_name)
        if (os.path.exists(old_path) and not os.path.exists(new_path)):
            try:
                os.rename(old_path,new_path)
                return True
            except OSError as e:
                print(f"Error in renaming {e}")
                return False
        else:
            return False

a=Gallery()
a.add_gallery("Birds")
a.delete_gallery("Birds")
print(a.get_all_gallery())