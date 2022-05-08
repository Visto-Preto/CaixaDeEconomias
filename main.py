#coding: utf-8
__author__ = 'Visto-Preto'

import os
from datetime import datetime
from module.realsymbol import Real as rs

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
cls = '\033[m'

def main():
    conta = ' R$ 1.000,00'
    ultO = '+'
    ultC = ' R$ 10,00'
    os.system('cls')
    menu = '''
{}========================================
        {}CAIXA DE ECONOMIAS           
{}========================================
{}DATA: {}{}          {}HORA: {}{}
{}----------------------------------------
{}Ult. Movimento:{} [{}{}{}] {}{}
{}----------------------------------------

{}Valor em conta: {}{}

{}----------------------------------------
{}========================================
{}01{}]	{}Depositar
{}02{}]	{}Sacar
{}00{}]	{}Sair{}
========================================{}'''.format( green, blue, green, yellow, cyan, 
                                datetime.today().strftime('%d/%m/%Y'),
                                yellow, cyan, datetime.today().strftime('%H:%M:%S'),       
                                magenta, yellow, cls, red, ultO, cls, green, ((20 - len(ultC)) * ' ' + ultC), magenta,                  
                                yellow, green, ((24 - len(conta)) * ' ' + conta), magenta, green, blue, cls, yellow, blue,
                                cls, yellow, blue, cls, yellow, green, cls)
    print(menu)
    rsp = input('{}Entre com o numero da opção:{}\n\n'.format(blue, cls))

if __name__ == ('__main__'):
    main()