# Selenium_playbook
Ansible Playbook to prepare an environment for Selenium testing and running a script in that environment

# Requirements
1. The slave machines should have python installed and open ssh
2. The host should be able to connect to the slaves via ssh
3. The host should have ansible installed

# Instructions
1. Install ansible
2. Change the Sel.yml vars to your environment`s specifications
3. Change the test.py file to run your test
4. Go to the folder where this project is and run: ansible-playbook sel.yml
