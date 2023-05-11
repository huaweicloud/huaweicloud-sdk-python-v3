# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateClientNetworkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_network_ranges': 'list[str]'
    }

    attribute_map = {
        'client_network_ranges': 'client_network_ranges'
    }

    def __init__(self, client_network_ranges=None):
        """UpdateClientNetworkRequestBody

        The model defined in huaweicloud sdk

        :param client_network_ranges: 客户端所在网段。  - 跨网段访问配置只有在客户端与副本集实例部署在不同网段的情况下才需要配置，例如访问副本集的客户端所在网段为192.168.0.0/16，副本集所在的网段为172.16.0.0/24，则需要添加跨网段配置192.168.0.0/16才能正常访问。  - 例如配置的源端网段为192.168.0.0/xx，则xx的输入值必须在8到32之间。  - 源端ECS连接实例的前提是与实例节点网络通信正常，如果网络不通，可以参考对等连接进行相关配置。
        :type client_network_ranges: list[str]
        """
        
        

        self._client_network_ranges = None
        self.discriminator = None

        self.client_network_ranges = client_network_ranges

    @property
    def client_network_ranges(self):
        """Gets the client_network_ranges of this UpdateClientNetworkRequestBody.

        客户端所在网段。  - 跨网段访问配置只有在客户端与副本集实例部署在不同网段的情况下才需要配置，例如访问副本集的客户端所在网段为192.168.0.0/16，副本集所在的网段为172.16.0.0/24，则需要添加跨网段配置192.168.0.0/16才能正常访问。  - 例如配置的源端网段为192.168.0.0/xx，则xx的输入值必须在8到32之间。  - 源端ECS连接实例的前提是与实例节点网络通信正常，如果网络不通，可以参考对等连接进行相关配置。

        :return: The client_network_ranges of this UpdateClientNetworkRequestBody.
        :rtype: list[str]
        """
        return self._client_network_ranges

    @client_network_ranges.setter
    def client_network_ranges(self, client_network_ranges):
        """Sets the client_network_ranges of this UpdateClientNetworkRequestBody.

        客户端所在网段。  - 跨网段访问配置只有在客户端与副本集实例部署在不同网段的情况下才需要配置，例如访问副本集的客户端所在网段为192.168.0.0/16，副本集所在的网段为172.16.0.0/24，则需要添加跨网段配置192.168.0.0/16才能正常访问。  - 例如配置的源端网段为192.168.0.0/xx，则xx的输入值必须在8到32之间。  - 源端ECS连接实例的前提是与实例节点网络通信正常，如果网络不通，可以参考对等连接进行相关配置。

        :param client_network_ranges: The client_network_ranges of this UpdateClientNetworkRequestBody.
        :type client_network_ranges: list[str]
        """
        self._client_network_ranges = client_network_ranges

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
        if not isinstance(other, UpdateClientNetworkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
