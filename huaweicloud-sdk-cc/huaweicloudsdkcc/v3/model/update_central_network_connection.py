# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCentralNetworkConnection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bandwidth_type': 'BandwidthTypeEnum',
        'global_connection_bandwidth_id': 'str',
        'bandwidth_size': 'int'
    }

    attribute_map = {
        'bandwidth_type': 'bandwidth_type',
        'global_connection_bandwidth_id': 'global_connection_bandwidth_id',
        'bandwidth_size': 'bandwidth_size'
    }

    def __init__(self, bandwidth_type=None, global_connection_bandwidth_id=None, bandwidth_size=None):
        """UpdateCentralNetworkConnection

        The model defined in huaweicloud sdk

        :param bandwidth_type: 
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        :param global_connection_bandwidth_id: 资源ID标识符。
        :type global_connection_bandwidth_id: str
        :param bandwidth_size: 带宽值定义，单位Mbps。
        :type bandwidth_size: int
        """
        
        

        self._bandwidth_type = None
        self._global_connection_bandwidth_id = None
        self._bandwidth_size = None
        self.discriminator = None

        self.bandwidth_type = bandwidth_type
        if global_connection_bandwidth_id is not None:
            self.global_connection_bandwidth_id = global_connection_bandwidth_id
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size

    @property
    def bandwidth_type(self):
        """Gets the bandwidth_type of this UpdateCentralNetworkConnection.

        :return: The bandwidth_type of this UpdateCentralNetworkConnection.
        :rtype: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        return self._bandwidth_type

    @bandwidth_type.setter
    def bandwidth_type(self, bandwidth_type):
        """Sets the bandwidth_type of this UpdateCentralNetworkConnection.

        :param bandwidth_type: The bandwidth_type of this UpdateCentralNetworkConnection.
        :type bandwidth_type: :class:`huaweicloudsdkcc.v3.BandwidthTypeEnum`
        """
        self._bandwidth_type = bandwidth_type

    @property
    def global_connection_bandwidth_id(self):
        """Gets the global_connection_bandwidth_id of this UpdateCentralNetworkConnection.

        资源ID标识符。

        :return: The global_connection_bandwidth_id of this UpdateCentralNetworkConnection.
        :rtype: str
        """
        return self._global_connection_bandwidth_id

    @global_connection_bandwidth_id.setter
    def global_connection_bandwidth_id(self, global_connection_bandwidth_id):
        """Sets the global_connection_bandwidth_id of this UpdateCentralNetworkConnection.

        资源ID标识符。

        :param global_connection_bandwidth_id: The global_connection_bandwidth_id of this UpdateCentralNetworkConnection.
        :type global_connection_bandwidth_id: str
        """
        self._global_connection_bandwidth_id = global_connection_bandwidth_id

    @property
    def bandwidth_size(self):
        """Gets the bandwidth_size of this UpdateCentralNetworkConnection.

        带宽值定义，单位Mbps。

        :return: The bandwidth_size of this UpdateCentralNetworkConnection.
        :rtype: int
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        """Sets the bandwidth_size of this UpdateCentralNetworkConnection.

        带宽值定义，单位Mbps。

        :param bandwidth_size: The bandwidth_size of this UpdateCentralNetworkConnection.
        :type bandwidth_size: int
        """
        self._bandwidth_size = bandwidth_size

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
        if not isinstance(other, UpdateCentralNetworkConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
