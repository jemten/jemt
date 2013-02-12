import sys
import os
#import argparse


class repo_dir(object):
#The context manger. 
  def __init__(self, path):
    self.original_path = os.getcwd()
    #stores current dir
    self.path=(path) 
    #stores new path        
         
  def __enter__(self):
    os.chdir(self.path)
    #changes dir to path
    
  def __exit__(self, type, value, traceback):
    os.chdir(self.original_path)
    #return to original path
    
      
class CourseRepo(object):
  def __init__(self,lastname):
    self.lastname = lastname
    #stores lastname
    self.required = ['.git',
      'setup.py',
      'README.md',
      'scripts/getting_data.py',
      'scripts/check_repo.py',
      self.lastname+'/__init__.py',
      self.lastname+'/session3.py'
      ]   
      
  @property
  def surname(self):
    #sys.stderr.write('# Running property function ... \n')
    return self.lastname
    
  @surname.setter
  def surname(self, value):
  #changes lastname to valu 
    self.lastname = value
    self.required[-2] = self.lastname+'/__init__.py'
    self.required[-1] = self.lastname+'/session3.py'
        
  def check(self):
    #checks if the dir and files in self.required exists in current path
    check = 'PASS'
    print '\n'
    for directory in self.required:
      if not os.path.exists(directory):
        print directory ,"NOT IN:", os.getcwd() 
        check = 'FAIL'
    print check
    print '\n'  
    
      
        
       
    
    