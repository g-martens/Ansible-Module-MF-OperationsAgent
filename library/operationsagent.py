#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
from pickletools import TAKEN_FROM_ARGUMENT4U
from subprocess import run # needed to execute commands on linux

__metaclass__ = type



DOCUMENTATION = r'''
---
module: operationsagent

short_description: This is my test module

# If this is part of a collection, you need to use semantic versioning,
# i.e. the version is of the form "2.5.0" and not "2.4".
version_added: "1.0.0"

description: This is my longer description explaining my test module.

options:
    name:
        description: This is the message to send to the test module.
        required: true
        type: str
    new:
        description:
            - Control to demo if the result of this module is changed or not.
            - Parameter description can be a list as well.
        required: false
        type: bool
# Specify this value according to your collection
# in format of namespace.collection.doc_fragment_name

author:
    - Guido Martens (@g-martens)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
original_message:
    description: The original name param that was passed in.
    type: str
    returned: always
    sample: 'hello world'
message:
    description: The output message that the test module generates.
    type: str
    returned: always
    sample: 'goodbye'
'''

from ansible.module_utils.basic import AnsibleModule


def run_module():
    oa_ovo = False
    oa_opcag = False
    oa_ovcert = False
    oa_ovconfchg = False

    # define available arguments/parameters a user can pass to the module
    module_args = dict(
        process=dict(type='str', required=True),
        action=dict(type='bool', required=False, default=False)
    )

    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
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

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)


    # Actions for the process ovo
    if oa_ovo:
        action = module.params['action']

        if action == 'start':
            tool = '/opt/OV/bin/ovo'
            p = run( [ tool, '-start' ])
            exit = p.returncode
            #Result output
            result['Executed tool'] = tool
            result['Used option'] = '-start'
            result['Exit code'] = exit
            if exit != 0:
                module.fail_json(msg='Exit code is not 0', **result)
            else:
                result['changed'] = True

        elif action == 'stop':
            tool = '/opt/OV/bin/ovo'
            p = run( [ tool, '-stop' ])
            exit = p.returncode
            #Result output
            result['Executed tool'] = tool
            result['Used option'] = '-stop'
            result['Exit code'] = exit
            if exit != 0:
                module.fail_json(msg='Exit code is not 0', **result)
            else:
                result['changed'] = True

        elif action == 'restart':
            tool = '/opt/OV/bin/ovo'
            p = run( [ tool, '-restart' ])
            exit = p.returncode
            #Result output
            result['Executed tool'] = tool
            result['Used option'] = '-restart'
            result['Exit code'] = exit
            if exit != 0:
                module.fail_json(msg='Exit code is not 0', **result)
            else:
                result['changed'] = True

        elif action == 'kill' :
            tool = '/opt/OV/bin/ovo'
            p = run( [ tool, '-kill' ])
            exit = p.returncode
            #Result output
            result['Executed tool'] = tool
            result['Used option'] = '-kill'
            result['Exit code'] = exit
            if exit != 0:
                module.fail_json(msg='Exit code is not 0', **result)
            else:
                result['changed'] = True

        else:
            module.fail_json(msg='Bad input - valid inputs for OVO are: start, stop, restart, kill', **result)


    #  Actions for the process opcagt
    if oa_opcagt:
        module.fail_json(msg='opcagt is not yet inplementated', **result)

    # Actions for the process ovcert
    if oa_ovcert:
        module.fail_json(msg='opcagt is not yet inplementated', **result)

    #Actions for the process ovconfchg
    if oa_ovconfchg:
        module.fail_json(msg='opcagt is not yet inplementated', **result)




    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'

    # use whatever logic you need to determine whether or not this module
    # made any modifications to your target
    if module.params['new']:
        result['changed'] = True

    # during the execution of the module, if there is an exception or a
    # conditional state that effectively causes a failure, run
    # AnsibleModule.fail_json() to pass in the message and the result
    if module.params['name'] == 'fail me':
        module.fail_json(msg='You requested this to fail', **result)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()