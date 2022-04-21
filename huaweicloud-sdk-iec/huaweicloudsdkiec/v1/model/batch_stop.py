# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStop:

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
        """BatchStop

        The model defined in huaweicloud sdk

        :param servers: 待停止的边缘实例列表。
        :type servers: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        :param type: 关机类型，默认为SOFT。  取值范围： - SOFT：普通关机。 - HARD：强制关机。
        :type type: str
        """
        
        

        self._servers = None
        self._type = None
        self.discriminator = None

        self.servers = servers
        if type is not None:
            self.type = type

    @property
    def servers(self):
        """Gets the servers of this BatchStop.

        待停止的边缘实例列表。

        :return: The servers of this BatchStop.
        :rtype: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this BatchStop.

        待停止的边缘实例列表。

        :param servers: The servers of this BatchStop.
        :type servers: list[:class:`huaweicloudsdkiec.v1.BaseId`]
        """
        self._servers = servers

    @property
    def type(self):
        """Gets the type of this BatchStop.

        关机类型，默认为SOFT。  取值范围： - SOFT：普通关机。 - HARD：强制关机。

        :return: The type of this BatchStop.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchStop.

        关机类型，默认为SOFT。  取值范围： - SOFT：普通关机。 - HARD：强制关机。

        :param type: The type of this BatchStop.
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
        if not isinstance(other, BatchStop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
