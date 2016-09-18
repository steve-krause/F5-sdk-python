import itertools

class HostsError(Exception):
    pass

class Hosts(list):
    """
    Class for creating a list of hosts (IP or DNS)
    """

    def __init__(self, filename):
        self._filename = filename
        try:
            f = open(self._filename)
            hostlist = f.read().splitlines()
            f.close()
        except IOError:
            raise HostsError("Unable to read file: " + self._filename)
        for host in hostlist:
            self.append(host)
        return
