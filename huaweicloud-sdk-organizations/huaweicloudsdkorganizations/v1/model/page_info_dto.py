# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PageInfoDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'next_marker': 'str',
        'current_count': 'int'
    }

    attribute_map = {
        'next_marker': 'next_marker',
        'current_count': 'current_count'
    }

    def __init__(self, next_marker=None, current_count=None):
        """PageInfoDto

        The model defined in huaweicloud sdk

        :param next_marker: 如果存在，则表示可用的输出比当前响应中包含的输出多。在对操作的后续调用中，在标签请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null。
        :type next_marker: str
        :param current_count: 本页返回条目数量
        :type current_count: int
        """
        
        

        self._next_marker = None
        self._current_count = None
        self.discriminator = None

        self.next_marker = next_marker
        if current_count is not None:
            self.current_count = current_count

    @property
    def next_marker(self):
        """Gets the next_marker of this PageInfoDto.

        如果存在，则表示可用的输出比当前响应中包含的输出多。在对操作的后续调用中，在标签请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null。

        :return: The next_marker of this PageInfoDto.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this PageInfoDto.

        如果存在，则表示可用的输出比当前响应中包含的输出多。在对操作的后续调用中，在标签请求参数中使用此值，以获取输出的下一部分。您应该重复此操作，直到next_marker响应元素返回为null。

        :param next_marker: The next_marker of this PageInfoDto.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def current_count(self):
        """Gets the current_count of this PageInfoDto.

        本页返回条目数量

        :return: The current_count of this PageInfoDto.
        :rtype: int
        """
        return self._current_count

    @current_count.setter
    def current_count(self, current_count):
        """Sets the current_count of this PageInfoDto.

        本页返回条目数量

        :param current_count: The current_count of this PageInfoDto.
        :type current_count: int
        """
        self._current_count = current_count

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
        if not isinstance(other, PageInfoDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
