# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RedisDisabledCommandsDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_id': 'str',
        'key': 'str',
        'commands': 'list[str]'
    }

    attribute_map = {
        'db_id': 'db_id',
        'key': 'key',
        'commands': 'commands'
    }

    def __init__(self, db_id=None, key=None, commands=None):
        r"""RedisDisabledCommandsDetail

        The model defined in huaweicloud sdk

        :param db_id: key所在的DB。
        :type db_id: str
        :param key: key名。
        :type key: str
        :param commands: 命令列表。
        :type commands: list[str]
        """
        
        

        self._db_id = None
        self._key = None
        self._commands = None
        self.discriminator = None

        self.db_id = db_id
        self.key = key
        self.commands = commands

    @property
    def db_id(self):
        r"""Gets the db_id of this RedisDisabledCommandsDetail.

        key所在的DB。

        :return: The db_id of this RedisDisabledCommandsDetail.
        :rtype: str
        """
        return self._db_id

    @db_id.setter
    def db_id(self, db_id):
        r"""Sets the db_id of this RedisDisabledCommandsDetail.

        key所在的DB。

        :param db_id: The db_id of this RedisDisabledCommandsDetail.
        :type db_id: str
        """
        self._db_id = db_id

    @property
    def key(self):
        r"""Gets the key of this RedisDisabledCommandsDetail.

        key名。

        :return: The key of this RedisDisabledCommandsDetail.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        r"""Sets the key of this RedisDisabledCommandsDetail.

        key名。

        :param key: The key of this RedisDisabledCommandsDetail.
        :type key: str
        """
        self._key = key

    @property
    def commands(self):
        r"""Gets the commands of this RedisDisabledCommandsDetail.

        命令列表。

        :return: The commands of this RedisDisabledCommandsDetail.
        :rtype: list[str]
        """
        return self._commands

    @commands.setter
    def commands(self, commands):
        r"""Sets the commands of this RedisDisabledCommandsDetail.

        命令列表。

        :param commands: The commands of this RedisDisabledCommandsDetail.
        :type commands: list[str]
        """
        self._commands = commands

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
        if not isinstance(other, RedisDisabledCommandsDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
