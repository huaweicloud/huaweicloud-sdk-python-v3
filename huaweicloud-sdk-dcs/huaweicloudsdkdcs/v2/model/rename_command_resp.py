# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RenameCommandResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command': 'str',
        'flushall': 'str',
        'flushdb': 'str',
        'hgetall': 'str',
        'keys': 'str',
        'hscan': 'str',
        'scan': 'str',
        'sscan': 'str',
        'zscan': 'str'
    }

    attribute_map = {
        'command': 'command',
        'flushall': 'flushall',
        'flushdb': 'flushdb',
        'hgetall': 'hgetall',
        'keys': 'keys',
        'hscan': 'hscan',
        'scan': 'scan',
        'sscan': 'sscan',
        'zscan': 'zscan'
    }

    def __init__(self, command=None, flushall=None, flushdb=None, hgetall=None, keys=None, hscan=None, scan=None, sscan=None, zscan=None):
        r"""RenameCommandResp

        The model defined in huaweicloud sdk

        :param command: 命令command
        :type command: str
        :param flushall: 命令flushall
        :type flushall: str
        :param flushdb: 命令flushdb
        :type flushdb: str
        :param hgetall: 命令hgetall
        :type hgetall: str
        :param keys: 命令keys
        :type keys: str
        :param hscan: 命令hscan
        :type hscan: str
        :param scan: 命令scan
        :type scan: str
        :param sscan: 命令sscan
        :type sscan: str
        :param zscan: 命令zscan
        :type zscan: str
        """
        
        

        self._command = None
        self._flushall = None
        self._flushdb = None
        self._hgetall = None
        self._keys = None
        self._hscan = None
        self._scan = None
        self._sscan = None
        self._zscan = None
        self.discriminator = None

        if command is not None:
            self.command = command
        if flushall is not None:
            self.flushall = flushall
        if flushdb is not None:
            self.flushdb = flushdb
        if hgetall is not None:
            self.hgetall = hgetall
        if keys is not None:
            self.keys = keys
        if hscan is not None:
            self.hscan = hscan
        if scan is not None:
            self.scan = scan
        if sscan is not None:
            self.sscan = sscan
        if zscan is not None:
            self.zscan = zscan

    @property
    def command(self):
        r"""Gets the command of this RenameCommandResp.

        命令command

        :return: The command of this RenameCommandResp.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this RenameCommandResp.

        命令command

        :param command: The command of this RenameCommandResp.
        :type command: str
        """
        self._command = command

    @property
    def flushall(self):
        r"""Gets the flushall of this RenameCommandResp.

        命令flushall

        :return: The flushall of this RenameCommandResp.
        :rtype: str
        """
        return self._flushall

    @flushall.setter
    def flushall(self, flushall):
        r"""Sets the flushall of this RenameCommandResp.

        命令flushall

        :param flushall: The flushall of this RenameCommandResp.
        :type flushall: str
        """
        self._flushall = flushall

    @property
    def flushdb(self):
        r"""Gets the flushdb of this RenameCommandResp.

        命令flushdb

        :return: The flushdb of this RenameCommandResp.
        :rtype: str
        """
        return self._flushdb

    @flushdb.setter
    def flushdb(self, flushdb):
        r"""Sets the flushdb of this RenameCommandResp.

        命令flushdb

        :param flushdb: The flushdb of this RenameCommandResp.
        :type flushdb: str
        """
        self._flushdb = flushdb

    @property
    def hgetall(self):
        r"""Gets the hgetall of this RenameCommandResp.

        命令hgetall

        :return: The hgetall of this RenameCommandResp.
        :rtype: str
        """
        return self._hgetall

    @hgetall.setter
    def hgetall(self, hgetall):
        r"""Sets the hgetall of this RenameCommandResp.

        命令hgetall

        :param hgetall: The hgetall of this RenameCommandResp.
        :type hgetall: str
        """
        self._hgetall = hgetall

    @property
    def keys(self):
        r"""Gets the keys of this RenameCommandResp.

        命令keys

        :return: The keys of this RenameCommandResp.
        :rtype: str
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        r"""Sets the keys of this RenameCommandResp.

        命令keys

        :param keys: The keys of this RenameCommandResp.
        :type keys: str
        """
        self._keys = keys

    @property
    def hscan(self):
        r"""Gets the hscan of this RenameCommandResp.

        命令hscan

        :return: The hscan of this RenameCommandResp.
        :rtype: str
        """
        return self._hscan

    @hscan.setter
    def hscan(self, hscan):
        r"""Sets the hscan of this RenameCommandResp.

        命令hscan

        :param hscan: The hscan of this RenameCommandResp.
        :type hscan: str
        """
        self._hscan = hscan

    @property
    def scan(self):
        r"""Gets the scan of this RenameCommandResp.

        命令scan

        :return: The scan of this RenameCommandResp.
        :rtype: str
        """
        return self._scan

    @scan.setter
    def scan(self, scan):
        r"""Sets the scan of this RenameCommandResp.

        命令scan

        :param scan: The scan of this RenameCommandResp.
        :type scan: str
        """
        self._scan = scan

    @property
    def sscan(self):
        r"""Gets the sscan of this RenameCommandResp.

        命令sscan

        :return: The sscan of this RenameCommandResp.
        :rtype: str
        """
        return self._sscan

    @sscan.setter
    def sscan(self, sscan):
        r"""Sets the sscan of this RenameCommandResp.

        命令sscan

        :param sscan: The sscan of this RenameCommandResp.
        :type sscan: str
        """
        self._sscan = sscan

    @property
    def zscan(self):
        r"""Gets the zscan of this RenameCommandResp.

        命令zscan

        :return: The zscan of this RenameCommandResp.
        :rtype: str
        """
        return self._zscan

    @zscan.setter
    def zscan(self, zscan):
        r"""Sets the zscan of this RenameCommandResp.

        命令zscan

        :param zscan: The zscan of this RenameCommandResp.
        :type zscan: str
        """
        self._zscan = zscan

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RenameCommandResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
