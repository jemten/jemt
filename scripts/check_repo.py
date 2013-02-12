import sys
import os
from jemt.session3 import *

directory=sys.argv[1]

with repo_dir(directory):
  surname=os.path.basename(directory)
  repo = CourseRepo(surname)
  repo.check()