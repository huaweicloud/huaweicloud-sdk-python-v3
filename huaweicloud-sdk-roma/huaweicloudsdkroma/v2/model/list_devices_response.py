# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevicesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'size': 'int',
        'connect_address': 'str',
        'ssl_connect_address': 'str',
        'ipv6_connect_address': 'str',
        'ipv6_ssl_connect_address': 'str',
        'items': 'list[Device]'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'connect_address': 'connect_address',
        'ssl_connect_address': 'ssl_connect_address',
        'ipv6_connect_address': 'ipv6_connect_address',
        'ipv6_ssl_connect_address': 'ipv6_ssl_connect_address',
        'items': 'items'
    }

    def __init__(self, total=None, size=None, connect_address=None, ssl_connect_address=None, ipv6_connect_address=None, ipv6_ssl_connect_address=None, items=None):
        r"""ListDevicesResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param size: 本次返回数量
        :type size: int
        :param connect_address: 设备接入地址
        :type connect_address: str
        :param ssl_connect_address: 设备接入SSL地址
        :type ssl_connect_address: str
        :param ipv6_connect_address: 设备接入IPV6地址
        :type ipv6_connect_address: str
        :param ipv6_ssl_connect_address: 设备接入IPV6 SSL地址
        :type ipv6_ssl_connect_address: str
        :param items: 设备ID列表
        :type items: list[:class:`huaweicloudsdkroma.v2.Device`]
        """
        
        super(ListDevicesResponse, self).__init__()

        self._total = None
        self._size = None
        self._connect_address = None
        self._ssl_connect_address = None
        self._ipv6_connect_address = None
        self._ipv6_ssl_connect_address = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if connect_address is not None:
            self.connect_address = connect_address
        if ssl_connect_address is not None:
            self.ssl_connect_address = ssl_connect_address
        if ipv6_connect_address is not None:
            self.ipv6_connect_address = ipv6_connect_address
        if ipv6_ssl_connect_address is not None:
            self.ipv6_ssl_connect_address = ipv6_ssl_connect_address
        if items is not None:
            self.items = items

    @property
    def total(self):
        r"""Gets the total of this ListDevicesResponse.

        总数

        :return: The total of this ListDevicesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDevicesResponse.

        总数

        :param total: The total of this ListDevicesResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ListDevicesResponse.

        本次返回数量

        :return: The size of this ListDevicesResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListDevicesResponse.

        本次返回数量

        :param size: The size of this ListDevicesResponse.
        :type size: int
        """
        self._size = size

    @property
    def connect_address(self):
        r"""Gets the connect_address of this ListDevicesResponse.

        设备接入地址

        :return: The connect_address of this ListDevicesResponse.
        :rtype: str
        """
        return self._connect_address

    @connect_address.setter
    def connect_address(self, connect_address):
        r"""Sets the connect_address of this ListDevicesResponse.

        设备接入地址

        :param connect_address: The connect_address of this ListDevicesResponse.
        :type connect_address: str
        """
        self._connect_address = connect_address

    @property
    def ssl_connect_address(self):
        r"""Gets the ssl_connect_address of this ListDevicesResponse.

        设备接入SSL地址

        :return: The ssl_connect_address of this ListDevicesResponse.
        :rtype: str
        """
        return self._ssl_connect_address

    @ssl_connect_address.setter
    def ssl_connect_address(self, ssl_connect_address):
        r"""Sets the ssl_connect_address of this ListDevicesResponse.

        设备接入SSL地址

        :param ssl_connect_address: The ssl_connect_address of this ListDevicesResponse.
        :type ssl_connect_address: str
        """
        self._ssl_connect_address = ssl_connect_address

    @property
    def ipv6_connect_address(self):
        r"""Gets the ipv6_connect_address of this ListDevicesResponse.

        设备接入IPV6地址

        :return: The ipv6_connect_address of this ListDevicesResponse.
        :rtype: str
        """
        return self._ipv6_connect_address

    @ipv6_connect_address.setter
    def ipv6_connect_address(self, ipv6_connect_address):
        r"""Sets the ipv6_connect_address of this ListDevicesResponse.

        设备接入IPV6地址

        :param ipv6_connect_address: The ipv6_connect_address of this ListDevicesResponse.
        :type ipv6_connect_address: str
        """
        self._ipv6_connect_address = ipv6_connect_address

    @property
    def ipv6_ssl_connect_address(self):
        r"""Gets the ipv6_ssl_connect_address of this ListDevicesResponse.

        设备接入IPV6 SSL地址

        :return: The ipv6_ssl_connect_address of this ListDevicesResponse.
        :rtype: str
        """
        return self._ipv6_ssl_connect_address

    @ipv6_ssl_connect_address.setter
    def ipv6_ssl_connect_address(self, ipv6_ssl_connect_address):
        r"""Sets the ipv6_ssl_connect_address of this ListDevicesResponse.

        设备接入IPV6 SSL地址

        :param ipv6_ssl_connect_address: The ipv6_ssl_connect_address of this ListDevicesResponse.
        :type ipv6_ssl_connect_address: str
        """
        self._ipv6_ssl_connect_address = ipv6_ssl_connect_address

    @property
    def items(self):
        r"""Gets the items of this ListDevicesResponse.

        设备ID列表

        :return: The items of this ListDevicesResponse.
        :rtype: list[:class:`huaweicloudsdkroma.v2.Device`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListDevicesResponse.

        设备ID列表

        :param items: The items of this ListDevicesResponse.
        :type items: list[:class:`huaweicloudsdkroma.v2.Device`]
        """
        self._items = items

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
        if not isinstance(other, ListDevicesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
