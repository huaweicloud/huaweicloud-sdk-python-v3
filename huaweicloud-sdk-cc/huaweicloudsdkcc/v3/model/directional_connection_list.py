# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DirectionalConnectionList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'directional_connections': 'list[DirectionalConnection]'
    }

    attribute_map = {
        'directional_connections': 'directional_connections'
    }

    def __init__(self, directional_connections=None):
        r"""DirectionalConnectionList

        The model defined in huaweicloud sdk

        :param directional_connections: 有向连接列表。
        :type directional_connections: list[:class:`huaweicloudsdkcc.v3.DirectionalConnection`]
        """
        
        

        self._directional_connections = None
        self.discriminator = None

        self.directional_connections = directional_connections

    @property
    def directional_connections(self):
        r"""Gets the directional_connections of this DirectionalConnectionList.

        有向连接列表。

        :return: The directional_connections of this DirectionalConnectionList.
        :rtype: list[:class:`huaweicloudsdkcc.v3.DirectionalConnection`]
        """
        return self._directional_connections

    @directional_connections.setter
    def directional_connections(self, directional_connections):
        r"""Sets the directional_connections of this DirectionalConnectionList.

        有向连接列表。

        :param directional_connections: The directional_connections of this DirectionalConnectionList.
        :type directional_connections: list[:class:`huaweicloudsdkcc.v3.DirectionalConnection`]
        """
        self._directional_connections = directional_connections

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
        if not isinstance(other, DirectionalConnectionList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
