# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DiscardInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'count': 'int',
        'total_time': 'int'
    }

    attribute_map = {
        'type': 'type',
        'count': 'count',
        'total_time': 'totalTime'
    }

    def __init__(self, type=None, count=None, total_time=None):
        r"""DiscardInfo

        The model defined in huaweicloud sdk

        :param type: 类型。
        :type type: str
        :param count: 数量。
        :type count: int
        :param total_time: 总时间。
        :type total_time: int
        """
        
        

        self._type = None
        self._count = None
        self._total_time = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if count is not None:
            self.count = count
        if total_time is not None:
            self.total_time = total_time

    @property
    def type(self):
        r"""Gets the type of this DiscardInfo.

        类型。

        :return: The type of this DiscardInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DiscardInfo.

        类型。

        :param type: The type of this DiscardInfo.
        :type type: str
        """
        self._type = type

    @property
    def count(self):
        r"""Gets the count of this DiscardInfo.

        数量。

        :return: The count of this DiscardInfo.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this DiscardInfo.

        数量。

        :param count: The count of this DiscardInfo.
        :type count: int
        """
        self._count = count

    @property
    def total_time(self):
        r"""Gets the total_time of this DiscardInfo.

        总时间。

        :return: The total_time of this DiscardInfo.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time):
        r"""Sets the total_time of this DiscardInfo.

        总时间。

        :param total_time: The total_time of this DiscardInfo.
        :type total_time: int
        """
        self._total_time = total_time

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
        if not isinstance(other, DiscardInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
