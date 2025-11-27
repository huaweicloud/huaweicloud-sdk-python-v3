# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClusterGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'order_by': 'str',
        'order': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'order_by': 'order_by',
        'order': 'order'
    }

    def __init__(self, limit=None, offset=None, order_by=None, order=None):
        r"""ListClusterGroupRequest

        The model defined in huaweicloud sdk

        :param limit: 分页获取列表时，页的大小，默认为-1
        :type limit: int
        :param offset: 分页获取列表时，起始偏移量，默认为0
        :type offset: int
        :param order_by: 分页获取列表时，排序参数，支持 create_at 和 update_at
        :type order_by: str
        :param order: 分页获取列表时，排序方向，支持 desc 和 asc
        :type order: str
        """
        
        

        self._limit = None
        self._offset = None
        self._order_by = None
        self._order = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if order_by is not None:
            self.order_by = order_by
        if order is not None:
            self.order = order

    @property
    def limit(self):
        r"""Gets the limit of this ListClusterGroupRequest.

        分页获取列表时，页的大小，默认为-1

        :return: The limit of this ListClusterGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListClusterGroupRequest.

        分页获取列表时，页的大小，默认为-1

        :param limit: The limit of this ListClusterGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListClusterGroupRequest.

        分页获取列表时，起始偏移量，默认为0

        :return: The offset of this ListClusterGroupRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListClusterGroupRequest.

        分页获取列表时，起始偏移量，默认为0

        :param offset: The offset of this ListClusterGroupRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def order_by(self):
        r"""Gets the order_by of this ListClusterGroupRequest.

        分页获取列表时，排序参数，支持 create_at 和 update_at

        :return: The order_by of this ListClusterGroupRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListClusterGroupRequest.

        分页获取列表时，排序参数，支持 create_at 和 update_at

        :param order_by: The order_by of this ListClusterGroupRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def order(self):
        r"""Gets the order of this ListClusterGroupRequest.

        分页获取列表时，排序方向，支持 desc 和 asc

        :return: The order of this ListClusterGroupRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this ListClusterGroupRequest.

        分页获取列表时，排序方向，支持 desc 和 asc

        :param order: The order of this ListClusterGroupRequest.
        :type order: str
        """
        self._order = order

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListClusterGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
