#coding: utf-8
__author__ = 'Visto-Preto'

import os, sqlite3
from datetime import datetime
from module.realsymbol import Real as rs

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
magenta = '\033[1;35m'
cyan = '\033[1;36m'
cls = '\033[m'


def ver():
    if os.path.isfile('settings/cde.db'):
        pass
    else:
        con = sqlite3.connect('settings/cde.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE movimentacao(Data date, TMov text, VMov real)''')
        con.commit()
        con.close()

def depositar():
    print('Funcao depositar')

def sacar():
    print('funcao sacar')

def extrato():
    print('funcao extrato')

def movimentacao(x,y,z):
    con = sqlite3.connect('settings/cde.db')
    cur = con.cursor()
    cur.execute('''INSERT INTO movimentacao VALUES('{}', '{}', '{}')'''.format(x, y, z))
    con.commit()
    con.close()

def ultrow():
    con = sqlite3.connect('settings/cde.db')
    cur = con.cursor()
    for row in cur.execute('''SELECT * FROM movimentacao'''):
        ult = row
    x = ult[2]
    y = ult[1]
    con.commit()
    con.close()
    return x, y
        
def v_conta():

    ver()
    def del_car(x):
        x = x[0]
        if x == None:
            x = 0.0
        else:
            x = float(x)
        return x
    con = sqlite3.connect('settings/cde.db')
    cur = con.cursor()
    for row in cur.execute('''SELECT SUM(VMov) FROM movimentacao WHERE TMov='deposito' '''):
        deposito = row
    deposito = del_car(deposito)
    for row in cur.execute('''SELECT SUM(VMov) FROM movimentacao WHERE TMov='saque' '''):
        saque = row
    saque = del_car(saque)
    con.commit()
    con.close()
    return (deposito - saque)

def main():
    conta = rs.float_to_s(v_conta())
    ultC , ultO = ultrow()
    ultC = rs.float_to_s(ultC)
    ultO = ultO.capitalize()
    if len(ultO) == 5:
        sp = '   '
    else:
        sp = ''
    os.system('cls')
    menu = '''
{}==============================================
             {}CAIXA DE ECONOMIAS           
{}==============================================
{}----------------------------------------------
{}DATA: {}{}                {}HORA: {}{}
{}----------------------------------------------
{}Ult. Movimento:{} [{}{}{}]{} {}{}
{}----------------------------------------------

{}Valor em conta: {}{}

{}----------------------------------------------
{}==============================================
{}01{}]    {}Depositar
{}02{}]    {}Sacar
{}03{}]    {}Extrato

{}00{}]    {}Sair{}
=============================================={}'''.format( green, blue ,green, magenta, yellow, cyan, 
                                datetime.today().strftime('%d/%m/%Y'),
                                yellow, cyan, datetime.today().strftime('%H:%M:%S'),       
                                magenta, yellow, cls, red, ultO, cls, sp, green, ((19 - len(ultC)) * ' ' + ultC), magenta,                  
                                yellow, green, ((30 - len(conta)) * ' ' + conta), magenta, green, blue, cls, yellow, blue,
                                cls, yellow, blue, cls, yellow, blue, cls, yellow, green, cls)
    print(menu)
    rsp = str(input('{}Entre com o numero da opção:\n\n{}~/{}Terminal{} $ '.format(blue, green, yellow, cls)))
   
    if rsp == '00':
        os.system('clear')
    elif rsp == '01':
        os.system('clear')
        depositar()
    elif rsp == '02':
        os.system('clear')
        sacar()
    elif rsp == '03':
        os.system('clear')
        extrato()
    else:
        main()
        
if __name__ == ('__main__'):
    main()
