# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Pagination:

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
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'total': 'total',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, total=None, offset=None, limit=None):
        r"""Pagination

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param offset: 偏移量
        :type offset: int
        :param limit: 每页显示的条目
        :type limit: int
        """
        
        

        self._total = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def total(self):
        r"""Gets the total of this Pagination.

        总数

        :return: The total of this Pagination.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this Pagination.

        总数

        :param total: The total of this Pagination.
        :type total: int
        """
        self._total = total

    @property
    def offset(self):
        r"""Gets the offset of this Pagination.

        偏移量

        :return: The offset of this Pagination.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this Pagination.

        偏移量

        :param offset: The offset of this Pagination.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this Pagination.

        每页显示的条目

        :return: The limit of this Pagination.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this Pagination.

        每页显示的条目

        :param limit: The limit of this Pagination.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, Pagination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
