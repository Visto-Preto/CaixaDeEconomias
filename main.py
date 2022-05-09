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

def v_conta():

    ver()
    def del_car(x):
        x = str(x).replace('(', '')
        x = str(x).replace(',', '')
        x = str(x).replace(')', '')
        if x == 'None':
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
    ultO = '+'
    ultC = ' R$ 10,00'
    os.system('cls')
    menu = '''
{}==============================================
             {}CAIXA DE ECONOMIAS           
{}==============================================
{}----------------------------------------------
{}DATA: {}{}                {}HORA: {}{}
{}----------------------------------------------
{}Ult. Movimento:{} [{}{}{}] {}{}
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
                                magenta, yellow, cls, red, ultO, cls, green, ((26 - len(ultC)) * ' ' + ultC), magenta,                  
                                yellow, green, ((30 - len(conta)) * ' ' + conta), magenta, green, blue, cls, yellow, blue,
                                cls, yellow, blue, cls, yellow, blue, cls, yellow, green, cls)
    print(menu)
    rsp = str(input('{}Entre com o numero da opção:\n\n{}~/{}Terminal{} $ '.format(blue, green, yellow, cls)))
   
    if rsp == '00':
        os.system('cls')
    else:
        main()
        
if __name__ == ('__main__'):
    main()
