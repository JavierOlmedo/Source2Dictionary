#!/bin/bash

echo "       INSTALLATION SCRIPT      ";
echo "     https://hackpuntes.com     ";

function installDebian () {
    sudo apt-get update;
}

function installFedora () {
    sudo yum -y install git python-pip;
}

function install () {
    case "$(uname -a)" in
        *Debian*|*Ubuntu*)
            installDebian;
            ;;
        *Fedora*)
            installFedora;
            ;;
        *Darwin*)
            installOSX;
            ;;
        *)
            echo "Unable to detect operating system that is compatible with S2D...";
            ;;
    esac
    echo "";
    echo "Installation Complete";
}

install;