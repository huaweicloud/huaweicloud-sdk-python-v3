# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyDedicatedStandbyNetworkParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'port': 'int',
        'availability_zone': 'list[str]'
    }

    attribute_map = {
        'address': 'address',
        'port': 'port',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, address=None, port=None, availability_zone=None):
        r"""ApplyDedicatedStandbyNetworkParam

        The model defined in huaweicloud sdk

        :param address: 租户指定的专线备用地址。
        :type address: str
        :param port: 租户指定的专线备用地址端口。
        :type port: int
        :param availability_zone: 开通服务资源使用的可用分区，默认随机使用2个可用区。
        :type availability_zone: list[str]
        """
        
        

        self._address = None
        self._port = None
        self._availability_zone = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if port is not None:
            self.port = port
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def address(self):
        r"""Gets the address of this ApplyDedicatedStandbyNetworkParam.

        租户指定的专线备用地址。

        :return: The address of this ApplyDedicatedStandbyNetworkParam.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this ApplyDedicatedStandbyNetworkParam.

        租户指定的专线备用地址。

        :param address: The address of this ApplyDedicatedStandbyNetworkParam.
        :type address: str
        """
        self._address = address

    @property
    def port(self):
        r"""Gets the port of this ApplyDedicatedStandbyNetworkParam.

        租户指定的专线备用地址端口。

        :return: The port of this ApplyDedicatedStandbyNetworkParam.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this ApplyDedicatedStandbyNetworkParam.

        租户指定的专线备用地址端口。

        :param port: The port of this ApplyDedicatedStandbyNetworkParam.
        :type port: int
        """
        self._port = port

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this ApplyDedicatedStandbyNetworkParam.

        开通服务资源使用的可用分区，默认随机使用2个可用区。

        :return: The availability_zone of this ApplyDedicatedStandbyNetworkParam.
        :rtype: list[str]
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this ApplyDedicatedStandbyNetworkParam.

        开通服务资源使用的可用分区，默认随机使用2个可用区。

        :param availability_zone: The availability_zone of this ApplyDedicatedStandbyNetworkParam.
        :type availability_zone: list[str]
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, ApplyDedicatedStandbyNetworkParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
