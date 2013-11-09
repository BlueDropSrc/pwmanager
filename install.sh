INSTALL_DIR="${HOME}/.pwmanager"
set -v on


mkdir -p $INSTALL_DIR
cp * $INSTALL_DIR
echo "alias createpw='python ${INSTALL_DIR}/createpw.py'" >> ~/.bash_aliases
echo "alias getpw='python ${INSTALL_DIR}/getpw.py'" >> ~/.bash_aliases
echo "alias setpw='python ${INSTALL_DIR}/setpw.py'" >> ~/.bash_aliases
source ~/.bash_aliases
