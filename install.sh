#!/data/data/com.termux/files/usr/bin/bash

echo -e '\n\n'
echo -e '\033[1;31mInstalando dependências...\033[m'
echo -e '\n'
apt update
apt install -y python figlet termux-api git

pip install requests lolcat

clear
termux-vibrate -d 100
figlet CaixaEco | lolcat
echo -e '\n\n'
echo -e '\033[1;31mInstalando o Caixa de Economias...\033[m'
echo -e '\n'

git clone https://github.com/Visto-Preto/CaixaDeEconomias CaixaEco

cat CaixaEco/caixaeco > /data/data/com.termux/files/usr/bin/caixaeco
chmod 700 /data/data/com.termux/files/usr/bin/caixaeco
cp -R CaixaEco /data/data/com.termux/files/usr/share/
rm -rf CaixaEco

termux-vibrate -d 100
echo -e '\n\n'
echo -e 'Para iniciar o Caixa de Economias entre com o comando: \033[1;32mcaixaeco\033[m'
echo -e '\n\n\n'
