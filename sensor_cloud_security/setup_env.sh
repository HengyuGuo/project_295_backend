#!/bin/bash
script_dir="$( cd "$( dirname "${BASH_SOURCE[0]}")" && pwd )"
cd ${script_dir}

function setup_homebrew {
    which -s brew
    if [[ $? != 0 ]] ; then
        echo "installing brew"
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi
    echo "updating brew"
    brew update
}

function check_brew_pkg {
    echo "checking package $1 exists"
    if brew ls --version $1 > /dev/null ; then
        echo "package $1 exists"
    else
        echo "installing $1"
        brew install $1
    fi
}

function install_virtual_env {
#    python3_path=$(brew info python3 | grep Cellar | awk '{print $1}')
#    python3_path+="/bin/python3"
#    echo "python 3 path: ${python3_path}"
    echo "check if pip is installed"
    which -s pip
    if [[ $? != 0 ]] ; then
        echo "ERROR: please run: sudo easy_install pip"
        echo "and rerun the setup script again"
        exit 1
    fi
    which -s virtualenv
    if [[ $? != 0 ]] ; then
        echo "installing virtualenv"
        pip install virtualenv
    fi
#    virtualenv venv -p ${python3_path}
    virtualenv venv
    printf "\n\n"
    echo "now you have to install the package inside virtualenv"
    echo "type in the following:"
    echo "source venv/bin/activate"
    echo "pip install -r requirements.txt"
    echo "after that your environment is good to go!!"
    echo "to exit virtualenv simply type: deactivate"
}
setup_homebrew
check_brew_pkg mysql
#check_brew_pkg python3
install_virtual_env


