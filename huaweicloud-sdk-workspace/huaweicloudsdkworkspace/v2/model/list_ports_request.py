# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPortsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'marker': 'str',
        'limit': 'int',
        'ip_address': 'str',
        'subnet_id': 'str',
        'is_used': 'bool'
    }

    attribute_map = {
        'marker': 'marker',
        'limit': 'limit',
        'ip_address': 'ip_address',
        'subnet_id': 'subnet_id',
        'is_used': 'is_used'
    }

    def __init__(self, marker=None, limit=None, ip_address=None, subnet_id=None, is_used=None):
        r"""ListPortsRequest

        The model defined in huaweicloud sdk

        :param marker: 分页查询的起始资源ID。
        :type marker: str
        :param limit: 功能说明：每页返回的个数。取值范围：1~2000。默认值：2000。
        :type limit: int
        :param ip_address: ip地址。
        :type ip_address: str
        :param subnet_id: 子网ID。
        :type subnet_id: str
        :param is_used: 是否被使用。
        :type is_used: bool
        """
        
        

        self._marker = None
        self._limit = None
        self._ip_address = None
        self._subnet_id = None
        self._is_used = None
        self.discriminator = None

        if marker is not None:
            self.marker = marker
        if limit is not None:
            self.limit = limit
        if ip_address is not None:
            self.ip_address = ip_address
        if subnet_id is not None:
            self.subnet_id = subnet_id
        if is_used is not None:
            self.is_used = is_used

    @property
    def marker(self):
        r"""Gets the marker of this ListPortsRequest.

        分页查询的起始资源ID。

        :return: The marker of this ListPortsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPortsRequest.

        分页查询的起始资源ID。

        :param marker: The marker of this ListPortsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def limit(self):
        r"""Gets the limit of this ListPortsRequest.

        功能说明：每页返回的个数。取值范围：1~2000。默认值：2000。

        :return: The limit of this ListPortsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPortsRequest.

        功能说明：每页返回的个数。取值范围：1~2000。默认值：2000。

        :param limit: The limit of this ListPortsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ListPortsRequest.

        ip地址。

        :return: The ip_address of this ListPortsRequest.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ListPortsRequest.

        ip地址。

        :param ip_address: The ip_address of this ListPortsRequest.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ListPortsRequest.

        子网ID。

        :return: The subnet_id of this ListPortsRequest.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ListPortsRequest.

        子网ID。

        :param subnet_id: The subnet_id of this ListPortsRequest.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def is_used(self):
        r"""Gets the is_used of this ListPortsRequest.

        是否被使用。

        :return: The is_used of this ListPortsRequest.
        :rtype: bool
        """
        return self._is_used

    @is_used.setter
    def is_used(self, is_used):
        r"""Sets the is_used of this ListPortsRequest.

        是否被使用。

        :param is_used: The is_used of this ListPortsRequest.
        :type is_used: bool
        """
        self._is_used = is_used

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
        if not isinstance(other, ListPortsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
