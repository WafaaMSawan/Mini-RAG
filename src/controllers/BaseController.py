from helpers.config import get_settings, Settings
import os

class BaseController:
   
   def __init__(self):
     self.app_settings = get_settings()
     self.base_dir = os.path.dirname(os.path.dirname(__file__))
     self.files_dir = os.path.join(
        self.base_dir,
        "assets/files"
     )
     # anthor solution maybe run on all OS or NOT
     #self.file_dir = self.base_dir + "/" + "assets/files"

    