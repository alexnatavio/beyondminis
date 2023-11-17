# About:
This third mini-project is an idempotent Ansible playbook that automates the installation and configuration of Docker on a Debian bookworm host. <br>
The files included are the Ansible playbook and inventory files, and a Vagrantfile used for testing. <br>
<br>

## Prerequisites:
* Vagrant installed <br>
* VirtualBox or other supported Vagrant provider installed <br>


change working directory to 03-AnsiblePlaybook <br>
`vagrant up` Creates the virtual machine defined in the Vagrantfile <br>
`vagrant ssh` Logs into the virtual machine <br>
`sudo apt update` to get latest package list <br>
`sudo apt install ansible` to install Ansible <br>
From the root directory `cd vagrant` to access the shared folder set by the Vagrantfile, this should contain the playbook and inventory <br>
`ansible-playbook -i inventory.ini docker-playbook.yml` to run the Playbook <br>
To ensure the playbook correctly handles repeat executions without unnecessary changes to the system state, the above step can be repeated to play the playbook and verify no unnecessary changes are made.  
another way to do this is with `ansible-playbook -i inventory.ini docker-playbook.yml --diff` after it has been ran once to confirm no changes would occur from repeated playbook executions. <br>






## Troubleshooting
Initially when I started the vm it set my working directory to `/home` and I had to `cd ..` to get to the root directory before I could `cd vagrant` for the correct shared folder location 
to access the playbook and inventory.  Hopefully it behaves itself otherwise `sudo find / -type d -name "vagrant"` will also help locate the shared folder that contains the required files to run the playbook.
