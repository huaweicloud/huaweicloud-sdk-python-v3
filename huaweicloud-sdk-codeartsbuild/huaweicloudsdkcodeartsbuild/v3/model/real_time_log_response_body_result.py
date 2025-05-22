# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RealTimeLogResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'has_more_data': 'bool',
        'offset': 'int',
        'content': 'str',
        'current_offset': 'int'
    }

    attribute_map = {
        'has_more_data': 'has_more_data',
        'offset': 'offset',
        'content': 'content',
        'current_offset': 'current_offset'
    }

    def __init__(self, has_more_data=None, offset=None, content=None, current_offset=None):
        r"""RealTimeLogResponseBodyResult

        The model defined in huaweicloud sdk

        :param has_more_data: 是否还有剩余日志标识
        :type has_more_data: bool
        :param offset: 偏移量，可用于下一次请求
        :type offset: int
        :param content: 返回日志内容，可能会空，请再次请求
        :type content: str
        :param current_offset: 当前请求偏移量
        :type current_offset: int
        """
        
        

        self._has_more_data = None
        self._offset = None
        self._content = None
        self._current_offset = None
        self.discriminator = None

        if has_more_data is not None:
            self.has_more_data = has_more_data
        if offset is not None:
            self.offset = offset
        if content is not None:
            self.content = content
        if current_offset is not None:
            self.current_offset = current_offset

    @property
    def has_more_data(self):
        r"""Gets the has_more_data of this RealTimeLogResponseBodyResult.

        是否还有剩余日志标识

        :return: The has_more_data of this RealTimeLogResponseBodyResult.
        :rtype: bool
        """
        return self._has_more_data

    @has_more_data.setter
    def has_more_data(self, has_more_data):
        r"""Sets the has_more_data of this RealTimeLogResponseBodyResult.

        是否还有剩余日志标识

        :param has_more_data: The has_more_data of this RealTimeLogResponseBodyResult.
        :type has_more_data: bool
        """
        self._has_more_data = has_more_data

    @property
    def offset(self):
        r"""Gets the offset of this RealTimeLogResponseBodyResult.

        偏移量，可用于下一次请求

        :return: The offset of this RealTimeLogResponseBodyResult.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this RealTimeLogResponseBodyResult.

        偏移量，可用于下一次请求

        :param offset: The offset of this RealTimeLogResponseBodyResult.
        :type offset: int
        """
        self._offset = offset

    @property
    def content(self):
        r"""Gets the content of this RealTimeLogResponseBodyResult.

        返回日志内容，可能会空，请再次请求

        :return: The content of this RealTimeLogResponseBodyResult.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this RealTimeLogResponseBodyResult.

        返回日志内容，可能会空，请再次请求

        :param content: The content of this RealTimeLogResponseBodyResult.
        :type content: str
        """
        self._content = content

    @property
    def current_offset(self):
        r"""Gets the current_offset of this RealTimeLogResponseBodyResult.

        当前请求偏移量

        :return: The current_offset of this RealTimeLogResponseBodyResult.
        :rtype: int
        """
        return self._current_offset

    @current_offset.setter
    def current_offset(self, current_offset):
        r"""Sets the current_offset of this RealTimeLogResponseBodyResult.

        当前请求偏移量

        :param current_offset: The current_offset of this RealTimeLogResponseBodyResult.
        :type current_offset: int
        """
        self._current_offset = current_offset

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
        if not isinstance(other, RealTimeLogResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
