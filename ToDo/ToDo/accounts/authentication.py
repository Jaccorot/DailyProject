import requests
import sys
from accounts.models import ListUser

class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        data = {'assertion': assertion, 'audience': 'localhost'}
        print 'sending to mozilla', data
        resp = requests.post('https://verifier.login.persona.org/verify', data=data)
        print 'got', resp.content

        if resp.ok:
            verification_data = resp.json()

            if verification_data['status'] == 'okay':
                email = verification_data['email']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.objects.create(email=email)

    def get_user(self, email):
        return ListUser.objects.get(email=email)
