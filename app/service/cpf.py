import os 
from flask import current_app

class CPFCheckBlacklist(object):
    def __init__(self, cpf:str):
        self.cpf = self.clear(cpf)

        if self.cpf.isnumeric() and len(self.cpf) == 11:
            self.blacklist = self.get_blacklist()
        else:
            raise TypeError('This CPF is not valid.')

    def get_blacklist(self):
        '''
        Return blacklist with cpfs clean
        '''
        directory = os.path.join(current_app.config['BASEDIR'],'blacklist.txt')
        
        with open(directory, 'r') as file:
            blacklist = [self.clear(cpf) for cpf in file.readlines()]
        return blacklist

    def clear(self, cpf:str):
        '''
        Clearing CPF leaving only numbers
        '''
        return cpf.replace('.', '').replace('-', '').replace('\n', '')

    def check(self):
        '''
        Check cpf in blacklist, if so return True else False
        '''
        return self.cpf in self.blacklist
