class MissingUsername(Exception):
    pass

class MissingPassword(Exception):
    pass

class Credential(object):
    """
    Class for managing the credentials
    """

    def __init__(self, **kwargs):
        self._username = kwargs.pop('username', "")
        self._password = kwargs.pop('password', "")
        self._pwfile = kwargs.pop('pwfile',"")
        if kwargs:
            raise TypeError('Unexpected **kwargs: %r' % kwargs)

        f = open(self._pwfile)
        self._username = f.readline().strip('\n')
        self._password = f.readline().strip('\n')
        f.close()
        if self._username == "":
            raise MissingUsername
        if self._password == "":
            raise MissingPassword

    @property # username
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property # password
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @property # pwfile
    def pwfile(self):
        return self._pwfile

    @pwfile.setter
    def pwfile(self, filename):
        self._pwfile = filename