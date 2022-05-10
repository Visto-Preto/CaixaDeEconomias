#!/usr/bin/env python
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
        cur.execute('''INSERT INTO movimentacao VALUES('{}', '{}', '{}')'''.format(datetime.today().strftime('%d/%m/%Y'), 'abertura', '0.0'))
        con.commit()
        con.close()

def depositar():
    print('{}00{}]    {}Voltar{}'.format(blue,cls, yellow, cls))
    print('{}=============================================={}'.format(green, cls))
    print()
    try:
        rsp = float(input('{}Entre com o valor do depósito:\n\n{}~/{}Terminal{}/{}Deposito{} $ '.format(blue, green, yellow, green, yellow, cls)))
    except:
        rsp = None
        os.system('clear')
        main(depositar)
    if rsp == 0.0:
        os.system('clear')
        main(mainop)
    elif rsp == None:
        pass
    else:
        tp = 'deposito'
        data = datetime.today().strftime('%d/%m/%Y')
        movimentacao(data, tp, rsp)
        os.system('clear')
        main(depositar)



def sacar():
    print('{}00{}]    {}Voltar{}'.format(blue,cls, yellow, cls))
    print('{}=============================================={}'.format(green, cls))
    print()
    try:
        rsp = float(input('{}Entre com o valor do saque:\n\n{}~/{}Terminal{}/{}Saque{} $ '.format(blue, green, yellow, green, yellow, cls)))
    except:
        rsp = None
        os.system('clear')
        main(sacar)
    if rsp == 0.0:
        os.system('clear')
        main(mainop)
    elif rsp == None:
        pass
    else:
        tp = 'saque'
        data = datetime.today().strftime('%d/%m/%Y')
        movimentacao(data, tp, rsp)
        os.system('clear')
        main(sacar)

def extrato():
    print('{}----------------------------------------------{}'.format(magenta, cls))
    con = sqlite3.connect('settings/cde.db')
    cur = con.cursor()
    for row in cur.execute('''SELECT * FROM movimentacao'''):
        if len(row[1]) == 5:
            sp = '   '
        else:
            sp = ''
        print('{}{} {}{} {}{}{}'.format(cyan, row[0], red, row[1].capitalize() + sp, green, ((26 - len(rs.float_to_s(row[2]))) * ' ' + rs.float_to_s(row[2])  ), cls))
        print('{}----------------------------------------------{}'.format(magenta, cls))
    print('{}=============================================={}'.format(green, cls))
    print('{}00{}]    {}Voltar{}'.format(blue,cls, yellow, cls))
    print('{}=============================================={}'.format(green, cls))
    print()
    rsp = str(input('{}Entre com o número da opção:\n\n{}~/{}Terminal{}/{}Extrato{} $ '.format(blue, green, yellow, green, yellow, cls)))
    if rsp == '00':
        os.system('clear')
        main(mainop)
    else:
        os.system('clear')
        main(extrato)


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
    z = ult[0]
    con.commit()
    con.close()
    return x, y, z
        
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


def main(x):
    conta = rs.float_to_s(v_conta())
    ultC , ultO, dt = ultrow()
    ultC = rs.float_to_s(ultC)
    ultO = ultO.capitalize()
    if len(ultO) == 5:
        sp = '   '
    else:
        sp = ''
    os.system('clear')
    menu = '''
{}==============================================
             {}CAIXA DE ECONOMIAS           
{}==============================================
{}----------------------------------------------
{}DATA: {}{}                {}HORA: {}{}
{}----------------------------------------------
{}UltM: {}|{}{}{}| |{}{}{}|{} {}{}
{}----------------------------------------------

{}Valor em conta: {}{}

{}----------------------------------------------
{}=============================================={}'''.format( green, blue ,green, magenta, yellow, cyan, 
                                datetime.today().strftime('%d/%m/%Y'),
                                yellow, cyan, datetime.today().strftime('%H:%M:%S'),       
                                magenta, yellow , magenta, red, dt ,magenta, red, ultO, magenta, sp, green, ((16 - len(ultC)) * ' ' + ultC), magenta,                  
                                yellow, green, ((30 - len(conta)) * ' ' + conta), magenta, green, cls)
    print(menu)
    x()


def mainop():
 
    print('{}01{}]    {}Depositar'.format(blue,cls, yellow))
    print('{}02{}]    {}Sacar'.format(blue,cls, yellow))
    print('{}03{}]    {}Extrato'.format(blue,cls, yellow))
    print('{}00{}]    {}Sair'.format(blue,cls, yellow))
    print('{}=============================================={}'.format(green, cls))
    print()
    rsp = str(input('{}Entre com o numero da opção:\n\n{}~/{}Terminal{} $ '.format(blue, green, yellow, cls)))
   
    if rsp == '00':
        os.system('clear')
    elif rsp == '01':
        os.system('clear')
        main(depositar)
    elif rsp == '02':
        os.system('clear')
        main(sacar)
    elif rsp == '03':
        os.system('clear')
        main(extrato)
    else:
        main(mainop)
        
if __name__ == ('__main__'):
    main(mainop)
