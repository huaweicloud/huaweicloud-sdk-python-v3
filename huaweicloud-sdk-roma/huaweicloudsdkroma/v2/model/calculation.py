# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Calculation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'never_connected': 'int',
        'online': 'int',
        'offline': 'int'
    }

    attribute_map = {
        'never_connected': 'never_connected',
        'online': 'online',
        'offline': 'offline'
    }

    def __init__(self, never_connected=None, online=None, offline=None):
        """Calculation

        The model defined in huaweicloud sdk

        :param never_connected: 从未连接过的设备数量
        :type never_connected: int
        :param online: 在线设备数量
        :type online: int
        :param offline: 离线设备数量
        :type offline: int
        """
        
        

        self._never_connected = None
        self._online = None
        self._offline = None
        self.discriminator = None

        if never_connected is not None:
            self.never_connected = never_connected
        if online is not None:
            self.online = online
        if offline is not None:
            self.offline = offline

    @property
    def never_connected(self):
        """Gets the never_connected of this Calculation.

        从未连接过的设备数量

        :return: The never_connected of this Calculation.
        :rtype: int
        """
        return self._never_connected

    @never_connected.setter
    def never_connected(self, never_connected):
        """Sets the never_connected of this Calculation.

        从未连接过的设备数量

        :param never_connected: The never_connected of this Calculation.
        :type never_connected: int
        """
        self._never_connected = never_connected

    @property
    def online(self):
        """Gets the online of this Calculation.

        在线设备数量

        :return: The online of this Calculation.
        :rtype: int
        """
        return self._online

    @online.setter
    def online(self, online):
        """Sets the online of this Calculation.

        在线设备数量

        :param online: The online of this Calculation.
        :type online: int
        """
        self._online = online

    @property
    def offline(self):
        """Gets the offline of this Calculation.

        离线设备数量

        :return: The offline of this Calculation.
        :rtype: int
        """
        return self._offline

    @offline.setter
    def offline(self, offline):
        """Sets the offline of this Calculation.

        离线设备数量

        :param offline: The offline of this Calculation.
        :type offline: int
        """
        self._offline = offline

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
        if not isinstance(other, Calculation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
