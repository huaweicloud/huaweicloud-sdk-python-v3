# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotKeysInfoResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'command': 'str',
        'qps': 'int',
        'db_id': 'int'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'command': 'command',
        'qps': 'qps',
        'db_id': 'db_id'
    }

    def __init__(self, name=None, type=None, command=None, qps=None, db_id=None):
        r"""HotKeysInfoResponseBody

        The model defined in huaweicloud sdk

        :param name: 热Key名。
        :type name: str
        :param type: 热Key类型。
        :type type: str
        :param command: 热Key命令。
        :type command: str
        :param qps: 热Key QPS。
        :type qps: int
        :param db_id: 热key所在的DB。
        :type db_id: int
        """
        
        

        self._name = None
        self._type = None
        self._command = None
        self._qps = None
        self._db_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if command is not None:
            self.command = command
        if qps is not None:
            self.qps = qps
        if db_id is not None:
            self.db_id = db_id

    @property
    def name(self):
        r"""Gets the name of this HotKeysInfoResponseBody.

        热Key名。

        :return: The name of this HotKeysInfoResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this HotKeysInfoResponseBody.

        热Key名。

        :param name: The name of this HotKeysInfoResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this HotKeysInfoResponseBody.

        热Key类型。

        :return: The type of this HotKeysInfoResponseBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this HotKeysInfoResponseBody.

        热Key类型。

        :param type: The type of this HotKeysInfoResponseBody.
        :type type: str
        """
        self._type = type

    @property
    def command(self):
        r"""Gets the command of this HotKeysInfoResponseBody.

        热Key命令。

        :return: The command of this HotKeysInfoResponseBody.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        r"""Sets the command of this HotKeysInfoResponseBody.

        热Key命令。

        :param command: The command of this HotKeysInfoResponseBody.
        :type command: str
        """
        self._command = command

    @property
    def qps(self):
        r"""Gets the qps of this HotKeysInfoResponseBody.

        热Key QPS。

        :return: The qps of this HotKeysInfoResponseBody.
        :rtype: int
        """
        return self._qps

    @qps.setter
    def qps(self, qps):
        r"""Sets the qps of this HotKeysInfoResponseBody.

        热Key QPS。

        :param qps: The qps of this HotKeysInfoResponseBody.
        :type qps: int
        """
        self._qps = qps

    @property
    def db_id(self):
        r"""Gets the db_id of this HotKeysInfoResponseBody.

        热key所在的DB。

        :return: The db_id of this HotKeysInfoResponseBody.
        :rtype: int
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this HotKeysInfoResponseBody.

        热key所在的DB。

        :param db_id: The db_id of this HotKeysInfoResponseBody.
        :type db_id: int
        """
        self._db_id = db_id

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
        if not isinstance(other, HotKeysInfoResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
