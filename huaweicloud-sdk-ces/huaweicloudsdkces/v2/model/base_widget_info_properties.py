# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseWidgetInfoProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter': 'str',
        'top_n': 'int',
        'order': 'str'
    }

    attribute_map = {
        'filter': 'filter',
        'top_n': 'topN',
        'order': 'order'
    }

    def __init__(self, filter=None, top_n=None, order=None):
        """BaseWidgetInfoProperties

        The model defined in huaweicloud sdk

        :param filter: 聚合类型，目前只有TopN这一种类型
        :type filter: str
        :param top_n: Top值前N个
        :type top_n: int
        :param order: 排序字段，asc正序，desc倒序
        :type order: str
        """
        
        

        self._filter = None
        self._top_n = None
        self._order = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if top_n is not None:
            self.top_n = top_n
        if order is not None:
            self.order = order

    @property
    def filter(self):
        """Gets the filter of this BaseWidgetInfoProperties.

        聚合类型，目前只有TopN这一种类型

        :return: The filter of this BaseWidgetInfoProperties.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this BaseWidgetInfoProperties.

        聚合类型，目前只有TopN这一种类型

        :param filter: The filter of this BaseWidgetInfoProperties.
        :type filter: str
        """
        self._filter = filter

    @property
    def top_n(self):
        """Gets the top_n of this BaseWidgetInfoProperties.

        Top值前N个

        :return: The top_n of this BaseWidgetInfoProperties.
        :rtype: int
        """
        return self._top_n

    @top_n.setter
    def top_n(self, top_n):
        """Sets the top_n of this BaseWidgetInfoProperties.

        Top值前N个

        :param top_n: The top_n of this BaseWidgetInfoProperties.
        :type top_n: int
        """
        self._top_n = top_n

    @property
    def order(self):
        """Gets the order of this BaseWidgetInfoProperties.

        排序字段，asc正序，desc倒序

        :return: The order of this BaseWidgetInfoProperties.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this BaseWidgetInfoProperties.

        排序字段，asc正序，desc倒序

        :param order: The order of this BaseWidgetInfoProperties.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, BaseWidgetInfoProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
