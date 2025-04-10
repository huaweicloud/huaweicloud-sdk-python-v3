# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstancesSessionStatisticsRespondBodyTopSourceIps:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'client_ip': 'str',
        'connection_count': 'int'
    }

    attribute_map = {
        'client_ip': 'client_ip',
        'connection_count': 'connection_count'
    }

    def __init__(self, client_ip=None, connection_count=None):
        r"""ListInstancesSessionStatisticsRespondBodyTopSourceIps

        The model defined in huaweicloud sdk

        :param client_ip: 客户端ip地址。
        :type client_ip: str
        :param connection_count: 客户端连接数。
        :type connection_count: int
        """
        
        

        self._client_ip = None
        self._connection_count = None
        self.discriminator = None

        if client_ip is not None:
            self.client_ip = client_ip
        if connection_count is not None:
            self.connection_count = connection_count

    @property
    def client_ip(self):
        r"""Gets the client_ip of this ListInstancesSessionStatisticsRespondBodyTopSourceIps.

        客户端ip地址。

        :return: The client_ip of this ListInstancesSessionStatisticsRespondBodyTopSourceIps.
        :rtype: str
        """
        return self._client_ip

    @client_ip.setter
    def client_ip(self, client_ip):
        r"""Sets the client_ip of this ListInstancesSessionStatisticsRespondBodyTopSourceIps.

        客户端ip地址。

        :param client_ip: The client_ip of this ListInstancesSessionStatisticsRespondBodyTopSourceIps.
        :type client_ip: str
        """
        self._client_ip = client_ip

    @property
    def connection_count(self):
        r"""Gets the connection_count of this ListInstancesSessionStatisticsRespondBodyTopSourceIps.

        客户端连接数。

        :return: The connection_count of this ListInstancesSessionStatisticsRespondBodyTopSourceIps.
        :rtype: int
        """
        return self._connection_count

    @connection_count.setter
    def connection_count(self, connection_count):
        r"""Sets the connection_count of this ListInstancesSessionStatisticsRespondBodyTopSourceIps.

        客户端连接数。

        :param connection_count: The connection_count of this ListInstancesSessionStatisticsRespondBodyTopSourceIps.
        :type connection_count: int
        """
        self._connection_count = connection_count

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
        if not isinstance(other, ListInstancesSessionStatisticsRespondBodyTopSourceIps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
