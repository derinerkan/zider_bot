import http.client
import requests


class Bot:
    token = None
    KARINT_ID = -1001309568370

    def __init__(self):
        with open("token.txt", 'r') as f:
            self.token = f.read()

    def query(self, queryname, contents=None):
        resp = requests.get(url='https://api.telegram.org' + '/bot' + self.token + '/' + queryname, params=contents)
        return resp.json()

    def get_updates(self, offset=None, limit=None, timeout=None, allowed_updates=None):
        options = dict()
        if offset is not None:
            options['offset'] = offset
        if limit is not None:
            options['limit'] = limit
        if timeout is not None:
            options['timeout'] = timeout
        if allowed_updates is not None:
            options['allowed_updates'] = allowed_updates
        queryname = 'getUpdates'
        resp = requests.get(url='https://api.telegram.org' + '/bot' + self.token + '/' + queryname, params=options)
        return resp.json()

    def get_fresh_updates(self, limit=None, timeout=None, allowed_updates=None):
        with open('last_update.txt', 'r') as f:
            num = f.read()
        if len(num) > 0:
            num = int(num)
            updates = self.get_updates(offset=num + 1, limit=limit, timeout=timeout, allowed_updates=allowed_updates)
        else:
            updates = self.get_updates(limit=limit, timeout=timeout, allowed_updates=allowed_updates)
        print(updates)
        if len(updates['result']) == 0:
            return updates
        else:
            newnum = updates['result'][-1]['update_id']
            with open('last_update.txt', 'w') as f:
                f.write(str(newnum))
            return updates

    def send_message(self, id, text):
        resp = self.query('sendMessage', {'chat_id': id, 'text': text})
        return resp
