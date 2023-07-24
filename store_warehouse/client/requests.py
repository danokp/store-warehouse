import requests

def synchronize_databases(http_method, url, token, data):
    '''Send request to connected client to synchronize databases.'''

    http_method_dict = {
        'put': requests.put,
        'post': requests.post,
    }

    headers = {'Authorization': f'Token {token}'}
    return http_method_dict[http_method](url, headers=headers, data=data)
