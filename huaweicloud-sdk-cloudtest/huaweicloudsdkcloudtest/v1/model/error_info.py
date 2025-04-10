# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'error_content': 'str',
        'error_index': 'str',
        'error_point': 'str',
        'high_light': 'bool'
    }

    attribute_map = {
        'error_content': 'error_content',
        'error_index': 'error_index',
        'error_point': 'error_point',
        'high_light': 'high_light'
    }

    def __init__(self, error_content=None, error_index=None, error_point=None, high_light=None):
        r"""ErrorInfo

        The model defined in huaweicloud sdk

        :param error_content: 错误内容的描述
        :type error_content: str
        :param error_index: 错误索引的描述
        :type error_index: str
        :param error_point: 错误点的描述
        :type error_point: str
        :param high_light: 是否高亮标识
        :type high_light: bool
        """
        
        

        self._error_content = None
        self._error_index = None
        self._error_point = None
        self._high_light = None
        self.discriminator = None

        if error_content is not None:
            self.error_content = error_content
        if error_index is not None:
            self.error_index = error_index
        if error_point is not None:
            self.error_point = error_point
        if high_light is not None:
            self.high_light = high_light

    @property
    def error_content(self):
        r"""Gets the error_content of this ErrorInfo.

        错误内容的描述

        :return: The error_content of this ErrorInfo.
        :rtype: str
        """
        return self._error_content

    @error_content.setter
    def error_content(self, error_content):
        r"""Sets the error_content of this ErrorInfo.

        错误内容的描述

        :param error_content: The error_content of this ErrorInfo.
        :type error_content: str
        """
        self._error_content = error_content

    @property
    def error_index(self):
        r"""Gets the error_index of this ErrorInfo.

        错误索引的描述

        :return: The error_index of this ErrorInfo.
        :rtype: str
        """
        return self._error_index

    @error_index.setter
    def error_index(self, error_index):
        r"""Sets the error_index of this ErrorInfo.

        错误索引的描述

        :param error_index: The error_index of this ErrorInfo.
        :type error_index: str
        """
        self._error_index = error_index

    @property
    def error_point(self):
        r"""Gets the error_point of this ErrorInfo.

        错误点的描述

        :return: The error_point of this ErrorInfo.
        :rtype: str
        """
        return self._error_point

    @error_point.setter
    def error_point(self, error_point):
        r"""Sets the error_point of this ErrorInfo.

        错误点的描述

        :param error_point: The error_point of this ErrorInfo.
        :type error_point: str
        """
        self._error_point = error_point

    @property
    def high_light(self):
        r"""Gets the high_light of this ErrorInfo.

        是否高亮标识

        :return: The high_light of this ErrorInfo.
        :rtype: bool
        """
        return self._high_light

    @high_light.setter
    def high_light(self, high_light):
        r"""Sets the high_light of this ErrorInfo.

        是否高亮标识

        :param high_light: The high_light of this ErrorInfo.
        :type high_light: bool
        """
        self._high_light = high_light

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
        if not isinstance(other, ErrorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
