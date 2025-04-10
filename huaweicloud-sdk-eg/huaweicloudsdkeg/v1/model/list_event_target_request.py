# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventTargetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'sort': 'str',
        'fuzzy_label': 'str',
        'support_types': 'list[str]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sort': 'sort',
        'fuzzy_label': 'fuzzy_label',
        'support_types': 'support_types'
    }

    def __init__(self, offset=None, limit=None, sort=None, fuzzy_label=None, support_types=None):
        r"""ListEventTargetRequest

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询，偏移量不能小于0
        :type offset: int
        :param limit: 每页显示的条目数量，不能小于1或大于1000
        :type limit: int
        :param sort: 指定查询排序
        :type sort: str
        :param fuzzy_label: 指定查询的事件目标标签，模糊匹配
        :type fuzzy_label: str
        :param support_types: 事件目标支持方式：事件订阅：SUBSCRIPTION、事件流：FLOW
        :type support_types: list[str]
        """
        
        

        self._offset = None
        self._limit = None
        self._sort = None
        self._fuzzy_label = None
        self._support_types = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort is not None:
            self.sort = sort
        if fuzzy_label is not None:
            self.fuzzy_label = fuzzy_label
        if support_types is not None:
            self.support_types = support_types

    @property
    def offset(self):
        r"""Gets the offset of this ListEventTargetRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :return: The offset of this ListEventTargetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEventTargetRequest.

        偏移量，表示从此偏移量开始查询，偏移量不能小于0

        :param offset: The offset of this ListEventTargetRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEventTargetRequest.

        每页显示的条目数量，不能小于1或大于1000

        :return: The limit of this ListEventTargetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEventTargetRequest.

        每页显示的条目数量，不能小于1或大于1000

        :param limit: The limit of this ListEventTargetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort(self):
        r"""Gets the sort of this ListEventTargetRequest.

        指定查询排序

        :return: The sort of this ListEventTargetRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this ListEventTargetRequest.

        指定查询排序

        :param sort: The sort of this ListEventTargetRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def fuzzy_label(self):
        r"""Gets the fuzzy_label of this ListEventTargetRequest.

        指定查询的事件目标标签，模糊匹配

        :return: The fuzzy_label of this ListEventTargetRequest.
        :rtype: str
        """
        return self._fuzzy_label

    @fuzzy_label.setter
    def fuzzy_label(self, fuzzy_label):
        r"""Sets the fuzzy_label of this ListEventTargetRequest.

        指定查询的事件目标标签，模糊匹配

        :param fuzzy_label: The fuzzy_label of this ListEventTargetRequest.
        :type fuzzy_label: str
        """
        self._fuzzy_label = fuzzy_label

    @property
    def support_types(self):
        r"""Gets the support_types of this ListEventTargetRequest.

        事件目标支持方式：事件订阅：SUBSCRIPTION、事件流：FLOW

        :return: The support_types of this ListEventTargetRequest.
        :rtype: list[str]
        """
        return self._support_types

    @support_types.setter
    def support_types(self, support_types):
        r"""Sets the support_types of this ListEventTargetRequest.

        事件目标支持方式：事件订阅：SUBSCRIPTION、事件流：FLOW

        :param support_types: The support_types of this ListEventTargetRequest.
        :type support_types: list[str]
        """
        self._support_types = support_types

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
        if not isinstance(other, ListEventTargetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
