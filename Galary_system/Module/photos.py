import os

class Photos(object):
    def __init__(self):
        pass
    def get_all_photos(self,gallary_name):
        gallery_path=os.path.join("static/photos/",gallary_name)
        photos=[]
        try:
            for name in os.listdir(gallery_path):
                photos.append(name)
        except FileNotFoundError:
            print(f"Gallery '{gallary_name}' not found")
        return photos
    
    def delete_photo(self,gallery_name,photo_name):
        path_name=os.path.join("static/photos/",gallery_name,photo_name)
        if (os.path.exists(path_name)):
            if os.path.isfile(path_name):
                try:
                    os.remove(path_name)
                    return True
                except OSError as e:
                    print(f"Error deleting photos as {e}")
                    return False
            else:
                return False
        else:
            print(f"photos {photo_name} not found in gallery {gallery_name}")
            return False
        
a=Photos()
print(a.get_all_photos("buildings"))