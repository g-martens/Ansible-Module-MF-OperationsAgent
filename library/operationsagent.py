#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from pickletools import TAKEN_FROM_ARGUMENT4U
# needed to execute commands on linux
from subprocess import run
import os
import sys

__metaclass__ = type



DOCUMENTATION = r'''
---
module: operationsagent

short_description: With this module, you can execute some commands from te Microfocus Operations Agent

description: This is my longer description explaining my test module.

options:
    process:
        description: With process, you can specify with tool you want to use
        required: true
        type: str
    action:
        description: with action, you can specify which action you want to execute with process
        required: true
        type: str

author:
    - Guido Martens (@g-martens)
'''

EXAMPLES = r'''
# Start the OVO process from the Operations Agent
- name: start the ovo process
  operationsagent:
    process: ovo
    action: start

# Start the opcagt process from the Operations Agent
- name: start the opcagt process
  operationsagent:
    process: ovo
    action: start

'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    #Declare default Vars and put them on False
    oa_ovo = False
    oa_opcagt = False
    oa_ovcert = False
    oa_ovconfchg = False

    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        process=dict(type='str', required=True),
        action=dict(type='str', required=True,)
    )

    # seed the result dict in the object
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        module.exit_json(**result)


    # Verifiy wich process is wanted, and put variable to true
    if module.params['process'].lower() == 'ovo' :
        oa_ovo = True
    if module.params['process'].lower() == 'opcagt' :
        oa_opcagt = True
    if module.params['process'].lower() == 'ovcert' :
        oa_ovcert = True
    if module.params['process'].lower() == 'ovconfchg' :
        oa_ovconfchg = True
    # input validation for the process option
    if not oa_ovo and not oa_opcagt and not oa_ovcert and not oa_ovconfchg:
        module.fail_json(msg='Bad input - valid inputs are: opcagt, ovo, ovcert, ovconfchg', **result)



    # Actions for the process ovo
    if oa_ovo:
        action = module.params['action']

        if action == 'start':
            command = "/opt/OV/bin/ovc -start"
            exit = os.system(command)

            #Result output
            if exit != 0:
                result['message'] = "Could not start OVO"
                result['Executed command'] = command
                result['Exit code'] = exit
                module.fail_json(msg='Could not execute command: exit code is not 0', **result)
            else:
                result['changed'] = True
                result['message'] = "OVO is started"
                result['Executed command'] = command
                result['Exit code'] = exit

        elif action == 'stop':
            command = "/opt/OV/bin/ovc -stop"
            exit = os.system(command)

            #Result output
            if exit != 0:
                result['message'] = "Could not stop OVO"
                result['Executed command'] = command
                result['Exit code'] = exit
                module.fail_json(msg='Could not execute command: exit code is  not 0', **result)
            else:
                result['changed'] = True
                result['message'] = "OVO is stopped"
                result['Executed command'] = command
                result['Exit code'] = exit

        elif action == 'restart':
            command = "/opt/OV/bin/ovc -restart"
            exit = os.system(command)

            #Result output
            if exit != 0:
                result['message'] = "Could not restart OVO"
                result['Executed command'] = command
                result['Exit code'] = exit
                module.fail_json(msg='Could not execute command: exit code is not 0', **result)
            else:
                result['changed'] = True
                result['message'] = "OVO is restarted"
                result['Executed command'] = command
                result['Exit code'] = exit


        elif action == 'kill' :
            command = "/opt/OV/bin/ovc -kill"
            exit = os.system(command)

            #Result output
            if exit != 0:
                result['message'] = "Could not kill OVO"
                result['Executed command'] = command
                result['Exit code'] = exit
                module.fail_json(msg='Could not execute command: exit code is not 0', **result)
            else:
                result['changed'] = True
                result['message'] = "OVO is killed"
                result['Executed command'] = command
                result['Exit code'] = exit

        elif action == 'status' :
            module.fail_json(msg='not yet inplementated', **result)


        else:
            module.fail_json(msg='Bad input - valid inputs for OVO are: start, stop, restart, kill, status,', **result)


    #  Actions for the process opcagt
    if oa_opcagt:
        module.fail_json(msg='opcagt is not yet inplementated', **result)

    # Actions for the process ovcert
    if oa_ovcert:
        module.fail_json(msg='opcagt is not yet inplementated', **result)

    #Actions for the process ovconfchg
    if oa_ovconfchg:
        module.fail_json(msg='opcagt is not yet inplementated', **result)


    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()