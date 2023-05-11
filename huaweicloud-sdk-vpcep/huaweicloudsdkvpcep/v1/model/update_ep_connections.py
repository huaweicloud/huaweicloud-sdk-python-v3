# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEpConnections:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'connections': 'list[ConnectionsDesc]'
    }

    attribute_map = {
        'connections': 'connections'
    }

    def __init__(self, connections=None):
        """UpdateEpConnections

        The model defined in huaweicloud sdk

        :param connections: 连接管理描述字段列表
        :type connections: list[:class:`huaweicloudsdkvpcep.v1.ConnectionsDesc`]
        """
        
        

        self._connections = None
        self.discriminator = None

        self.connections = connections

    @property
    def connections(self):
        """Gets the connections of this UpdateEpConnections.

        连接管理描述字段列表

        :return: The connections of this UpdateEpConnections.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.ConnectionsDesc`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this UpdateEpConnections.

        连接管理描述字段列表

        :param connections: The connections of this UpdateEpConnections.
        :type connections: list[:class:`huaweicloudsdkvpcep.v1.ConnectionsDesc`]
        """
        self._connections = connections

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
        if not isinstance(other, UpdateEpConnections):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
