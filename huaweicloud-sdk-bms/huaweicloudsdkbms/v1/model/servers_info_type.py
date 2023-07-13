# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServersInfoType:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'servers': 'list[ServersList]'
    }

    attribute_map = {
        'type': 'type',
        'servers': 'servers'
    }

    def __init__(self, type=None, servers=None):
        """ServersInfoType

        The model defined in huaweicloud sdk

        :param type: 重启类型：SOFT：普通重启（不生效）。HARD：强制重启（默认）。
        :type type: str
        :param servers: 裸金属服务器ID列表，详情请参见表3 servers字段数据结构说明。
        :type servers: list[:class:`huaweicloudsdkbms.v1.ServersList`]
        """
        
        

        self._type = None
        self._servers = None
        self.discriminator = None

        self.type = type
        self.servers = servers

    @property
    def type(self):
        """Gets the type of this ServersInfoType.

        重启类型：SOFT：普通重启（不生效）。HARD：强制重启（默认）。

        :return: The type of this ServersInfoType.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ServersInfoType.

        重启类型：SOFT：普通重启（不生效）。HARD：强制重启（默认）。

        :param type: The type of this ServersInfoType.
        :type type: str
        """
        self._type = type

    @property
    def servers(self):
        """Gets the servers of this ServersInfoType.

        裸金属服务器ID列表，详情请参见表3 servers字段数据结构说明。

        :return: The servers of this ServersInfoType.
        :rtype: list[:class:`huaweicloudsdkbms.v1.ServersList`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this ServersInfoType.

        裸金属服务器ID列表，详情请参见表3 servers字段数据结构说明。

        :param servers: The servers of this ServersInfoType.
        :type servers: list[:class:`huaweicloudsdkbms.v1.ServersList`]
        """
        self._servers = servers

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
        if not isinstance(other, ServersInfoType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
