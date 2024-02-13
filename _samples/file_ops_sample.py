#!/usr/bin/python3
import json


"""
This module saves and loads json files.

Communication with the importer and json files are
seperated for modularization purposes.
"""

# Communication with importer .py file(s)
# Main Functionality
class FileOps():
    
    @staticmethod
    def load_file(file_path:str):
        return _FileComm.load_file(file_path)
    
    @staticmethod
    def save_file(file_path:str, data:dict):
        _FileComm.save_file(file_path, data)


"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
The following class(es) are NOT MEANT to be
accessed OUTSIDE of THIS FILE.
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""

class _FileComm():

    @staticmethod
    def load_file(file_path:str):
            with open(file_path, 'r') as file:
                return json.load(file)
        
    @staticmethod
    def save_file(file_path:str, data:str):
            with open(file_path, 'w') as file:
                return json.dump(data, file)


if __name__=='__main__':
    stuff = {
        "bunnies": 16,
        "rabbits": 12,
        "fart": 1
        }
    FileOps.save_file('file.json', stuff)
    stuff2 = FileOps.load_file('file.json')
    print(stuff2)
