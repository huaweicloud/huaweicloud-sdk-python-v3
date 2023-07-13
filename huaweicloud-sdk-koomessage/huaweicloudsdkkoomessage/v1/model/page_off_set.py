# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageOffSet:

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
        'total': 'int'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total'
    }

    def __init__(self, offset=None, limit=None, total=None):
        """PageOffSet

        The model defined in huaweicloud sdk

        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0。
        :type offset: int
        :param limit: 每页显示的条目数量。
        :type limit: int
        :param total: 总量。
        :type total: int
        """
        
        

        self._offset = None
        self._limit = None
        self._total = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total

    @property
    def offset(self):
        """Gets the offset of this PageOffSet.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :return: The offset of this PageOffSet.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PageOffSet.

        偏移量，表示从此偏移量开始查询，offset大于等于0。

        :param offset: The offset of this PageOffSet.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this PageOffSet.

        每页显示的条目数量。

        :return: The limit of this PageOffSet.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this PageOffSet.

        每页显示的条目数量。

        :param limit: The limit of this PageOffSet.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        """Gets the total of this PageOffSet.

        总量。

        :return: The total of this PageOffSet.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PageOffSet.

        总量。

        :param total: The total of this PageOffSet.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, PageOffSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
