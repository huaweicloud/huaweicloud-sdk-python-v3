# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchReboot:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'servers': 'list[BaseId]',
        'type': 'str'
    }

    attribute_map = {
        'servers': 'servers',
        'type': 'type'
    }

    def __init__(self, servers=None, type=None):
        r"""BatchReboot

        The model defined in huaweicloud sdk

        :param servers: 待重启的边缘实例列表。
        :type servers: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        :param type: 重启类型：   - SOFT：普通重启。  - HARD：强制重启。  &gt; 重启必须指定重启类型。
        :type type: str
        """
        
        

        self._servers = None
        self._type = None
        self.discriminator = None

        if servers is not None:
            self.servers = servers
        if type is not None:
            self.type = type

    @property
    def servers(self):
        r"""Gets the servers of this BatchReboot.

        待重启的边缘实例列表。

        :return: The servers of this BatchReboot.
        :rtype: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        r"""Sets the servers of this BatchReboot.

        待重启的边缘实例列表。

        :param servers: The servers of this BatchReboot.
        :type servers: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        """
        self._servers = servers

    @property
    def type(self):
        r"""Gets the type of this BatchReboot.

        重启类型：   - SOFT：普通重启。  - HARD：强制重启。  > 重启必须指定重启类型。

        :return: The type of this BatchReboot.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BatchReboot.

        重启类型：   - SOFT：普通重启。  - HARD：强制重启。  > 重启必须指定重启类型。

        :param type: The type of this BatchReboot.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, BatchReboot):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
