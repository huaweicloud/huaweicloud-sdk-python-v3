# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PagedInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'current_count': 'int',
        'next_marker': 'str',
        'previous_marker': 'str'
    }

    attribute_map = {
        'current_count': 'current_count',
        'next_marker': 'next_marker',
        'previous_marker': 'previous_marker'
    }

    def __init__(self, current_count=None, next_marker=None, previous_marker=None):
        """PagedInfo

        The model defined in huaweicloud sdk

        :param current_count: 本次返回的对象个数
        :type current_count: int
        :param next_marker: 下一页查询地址
        :type next_marker: str
        :param previous_marker: 上一页查询地址
        :type previous_marker: str
        """
        
        

        self._current_count = None
        self._next_marker = None
        self._previous_marker = None
        self.discriminator = None

        self.current_count = current_count
        self.next_marker = next_marker
        self.previous_marker = previous_marker

    @property
    def current_count(self):
        """Gets the current_count of this PagedInfo.

        本次返回的对象个数

        :return: The current_count of this PagedInfo.
        :rtype: int
        """
        return self._current_count

    @current_count.setter
    def current_count(self, current_count):
        """Sets the current_count of this PagedInfo.

        本次返回的对象个数

        :param current_count: The current_count of this PagedInfo.
        :type current_count: int
        """
        self._current_count = current_count

    @property
    def next_marker(self):
        """Gets the next_marker of this PagedInfo.

        下一页查询地址

        :return: The next_marker of this PagedInfo.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this PagedInfo.

        下一页查询地址

        :param next_marker: The next_marker of this PagedInfo.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def previous_marker(self):
        """Gets the previous_marker of this PagedInfo.

        上一页查询地址

        :return: The previous_marker of this PagedInfo.
        :rtype: str
        """
        return self._previous_marker

    @previous_marker.setter
    def previous_marker(self, previous_marker):
        """Sets the previous_marker of this PagedInfo.

        上一页查询地址

        :param previous_marker: The previous_marker of this PagedInfo.
        :type previous_marker: str
        """
        self._previous_marker = previous_marker

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
        if not isinstance(other, PagedInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
