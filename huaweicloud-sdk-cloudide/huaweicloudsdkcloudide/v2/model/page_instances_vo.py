# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageInstancesVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'empty': 'bool',
        'items': 'list[InstancesVO]',
        'items_before': 'int',
        'size': 'int',
        'total_items_count': 'int'
    }

    attribute_map = {
        'empty': 'empty',
        'items': 'items',
        'items_before': 'items_before',
        'size': 'size',
        'total_items_count': 'total_items_count'
    }

    def __init__(self, empty=None, items=None, items_before=None, size=None, total_items_count=None):
        r"""PageInstancesVO

        The model defined in huaweicloud sdk

        :param empty: 是否为空
        :type empty: bool
        :param items: 列表详情
        :type items: list[:class:`huaweicloudsdkcloudide.v2.InstancesVO`]
        :param items_before: 偏移量，表示从此偏移量开始查询
        :type items_before: int
        :param size: 每页显示的条目数量
        :type size: int
        :param total_items_count: 总数
        :type total_items_count: int
        """
        
        

        self._empty = None
        self._items = None
        self._items_before = None
        self._size = None
        self._total_items_count = None
        self.discriminator = None

        if empty is not None:
            self.empty = empty
        if items is not None:
            self.items = items
        if items_before is not None:
            self.items_before = items_before
        if size is not None:
            self.size = size
        if total_items_count is not None:
            self.total_items_count = total_items_count

    @property
    def empty(self):
        r"""Gets the empty of this PageInstancesVO.

        是否为空

        :return: The empty of this PageInstancesVO.
        :rtype: bool
        """
        return self._empty

    @empty.setter
    def empty(self, empty):
        r"""Sets the empty of this PageInstancesVO.

        是否为空

        :param empty: The empty of this PageInstancesVO.
        :type empty: bool
        """
        self._empty = empty

    @property
    def items(self):
        r"""Gets the items of this PageInstancesVO.

        列表详情

        :return: The items of this PageInstancesVO.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.InstancesVO`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this PageInstancesVO.

        列表详情

        :param items: The items of this PageInstancesVO.
        :type items: list[:class:`huaweicloudsdkcloudide.v2.InstancesVO`]
        """
        self._items = items

    @property
    def items_before(self):
        r"""Gets the items_before of this PageInstancesVO.

        偏移量，表示从此偏移量开始查询

        :return: The items_before of this PageInstancesVO.
        :rtype: int
        """
        return self._items_before

    @items_before.setter
    def items_before(self, items_before):
        r"""Sets the items_before of this PageInstancesVO.

        偏移量，表示从此偏移量开始查询

        :param items_before: The items_before of this PageInstancesVO.
        :type items_before: int
        """
        self._items_before = items_before

    @property
    def size(self):
        r"""Gets the size of this PageInstancesVO.

        每页显示的条目数量

        :return: The size of this PageInstancesVO.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this PageInstancesVO.

        每页显示的条目数量

        :param size: The size of this PageInstancesVO.
        :type size: int
        """
        self._size = size

    @property
    def total_items_count(self):
        r"""Gets the total_items_count of this PageInstancesVO.

        总数

        :return: The total_items_count of this PageInstancesVO.
        :rtype: int
        """
        return self._total_items_count

    @total_items_count.setter
    def total_items_count(self, total_items_count):
        r"""Sets the total_items_count of this PageInstancesVO.

        总数

        :param total_items_count: The total_items_count of this PageInstancesVO.
        :type total_items_count: int
        """
        self._total_items_count = total_items_count

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
        if not isinstance(other, PageInstancesVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
