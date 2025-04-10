# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MetaData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'start': 'str',
        'total': 'int'
    }

    attribute_map = {
        'count': 'count',
        'start': 'start',
        'total': 'total'
    }

    def __init__(self, count=None, start=None, total=None):
        r"""MetaData

        The model defined in huaweicloud sdk

        :param count: 当前返回结果条数。
        :type count: int
        :param start: 下一个开始的标记，用于分页，null表示无更多数据。
        :type start: str
        :param total: 总条数。
        :type total: int
        """
        
        

        self._count = None
        self._start = None
        self._total = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if start is not None:
            self.start = start
        if total is not None:
            self.total = total

    @property
    def count(self):
        r"""Gets the count of this MetaData.

        当前返回结果条数。

        :return: The count of this MetaData.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this MetaData.

        当前返回结果条数。

        :param count: The count of this MetaData.
        :type count: int
        """
        self._count = count

    @property
    def start(self):
        r"""Gets the start of this MetaData.

        下一个开始的标记，用于分页，null表示无更多数据。

        :return: The start of this MetaData.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        r"""Sets the start of this MetaData.

        下一个开始的标记，用于分页，null表示无更多数据。

        :param start: The start of this MetaData.
        :type start: str
        """
        self._start = start

    @property
    def total(self):
        r"""Gets the total of this MetaData.

        总条数。

        :return: The total of this MetaData.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this MetaData.

        总条数。

        :param total: The total of this MetaData.
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
        if not isinstance(other, MetaData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
