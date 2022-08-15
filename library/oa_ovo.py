#!/usr/bin/python

DOCUMENTATION = '''
---
module: github_repo
short_description: Manage your repos on Github
'''

EXAMPLES = '''
- name: restart ovo agent
  oa_ovo:
    action: restart
  register: result

- name: kill the ovo agent 
  oa_ovo:
    action: kill
  register: result
'''

from ansible.module_utils.basic import *
import requests

api_url = "https://api.github.com"


def oa_restart(data):

    api_key = data['github_auth_key']

    del data['state']
    del data['github_auth_key']

    headers = {
        "Authorization": "token {}" . format(api_key)
    }
    url = "{}{}" . format(api_url, '/user/repos')
    result = requests.post(url, json.dumps(data), headers=headers)

    if result.status_code == 201:
        return False, True, result.json()
    if result.status_code == 422:
        return False, False, result.json()

    # default: something went wrong
    meta = {"status": result.status_code, 'response': result.json()}
    return True, False, meta




def main():

    fields = {
        "action": {
            "default": "none",
            "choices": ['start', 'stop', 'kill', 'restart'],
            "type": 'str'
        },
    }

    choice_map = {
        "start": oa_start,
        "stop": oa_stop,
        "kill": oa_kill,
        "restart": oa_restart,
    }

    module = AnsibleModule(argument_spec=fields)
    is_error, has_changed, result = choice_map.get(
        module.params['action'])(module.params)

    if not is_error:
        module.exit_json(changed=has_changed, meta=result)
    else:
        module.fail_json(msg="Error while executing action", meta=result)


if __name__ == '__main__':
    main()