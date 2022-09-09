# textbased-adventure-game-python
Welcome to my adventure-game-python-application Repository

I have included my python adventure game application along with a few other things to make it quick and easy foy you to set up a virtual machine
environment on your computer and be able to have access and play my python adventure game.

First you will need to have a couple dependencies installed on your computer which are: 
1. Vagrant (hashicorp) 
2. VirtualBox (Oracle Vm) or VMWare if you are using an M1 chip.

This repo includes: 
1. an app folder that contains the adventure game application and tests for the application code.
2. an env folder which contains a script.sh file that will provision the virtual machine to run the application.
3. a Vagrantfile that will configure and initialize the virtual machine.

Once you have those installed you can clone this repo to your computer in whatever file destination you decide.

Everything should be set up and ready for you to run a simple command to start your virtual machine.
Open up the terminal to the repo path and run the command: vagrant up
This will start up the virtual machine and the provisioning script.sh that is included should install and neccesary dependecies for your application to run.
Once the the vagrant up command is completed you can then run the command: vagrant ssh

This will SSH into the running Vagrant machine and give you access to a shell.
Then you will run the command: cd app
This will move into the app directory where the adventure game application lives.
Then you will run the command: python3 text_adventure.py

This final command will begin the apllication and the adventure game will initiate and then the fun begins.

