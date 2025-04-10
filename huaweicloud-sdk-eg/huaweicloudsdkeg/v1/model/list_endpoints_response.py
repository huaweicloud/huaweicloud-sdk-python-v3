# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointsResponse(SdkResponse):

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
        'items': 'list[EndpointInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'total': 'total',
        'size': 'size',
        'items': 'items',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, total=None, size=None, items=None, x_request_id=None):
        r"""ListEndpointsResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param size: 本页数量
        :type size: int
        :param items: 对象列表
        :type items: list[:class:`huaweicloudsdkeg.v1.EndpointInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ListEndpointsResponse, self).__init__()

        self._total = None
        self._size = None
        self._items = None
        self._x_request_id = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if items is not None:
            self.items = items
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def total(self):
        r"""Gets the total of this ListEndpointsResponse.

        总数

        :return: The total of this ListEndpointsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListEndpointsResponse.

        总数

        :param total: The total of this ListEndpointsResponse.
        :type total: int
        """
        self._total = total

    @property
    def size(self):
        r"""Gets the size of this ListEndpointsResponse.

        本页数量

        :return: The size of this ListEndpointsResponse.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this ListEndpointsResponse.

        本页数量

        :param size: The size of this ListEndpointsResponse.
        :type size: int
        """
        self._size = size

    @property
    def items(self):
        r"""Gets the items of this ListEndpointsResponse.

        对象列表

        :return: The items of this ListEndpointsResponse.
        :rtype: list[:class:`huaweicloudsdkeg.v1.EndpointInfo`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListEndpointsResponse.

        对象列表

        :param items: The items of this ListEndpointsResponse.
        :type items: list[:class:`huaweicloudsdkeg.v1.EndpointInfo`]
        """
        self._items = items

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListEndpointsResponse.

        :return: The x_request_id of this ListEndpointsResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListEndpointsResponse.

        :param x_request_id: The x_request_id of this ListEndpointsResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ListEndpointsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
