# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConversionsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'measure_type': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'measure_type': 'measure_type'
    }

    def __init__(self, x_language=None, measure_type=None):
        """ListConversionsRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._measure_type = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if measure_type is not None:
            self.measure_type = measure_type

    @property
    def x_language(self):
        """Gets the x_language of this ListConversionsRequest.

        |忽略大小写，默认 zh_CN：中文 en_US：英文|

        :return: The x_language of this ListConversionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListConversionsRequest.

        |忽略大小写，默认 zh_CN：中文 en_US：英文|

        :param x_language: The x_language of this ListConversionsRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def measure_type(self):
        """Gets the measure_type of this ListConversionsRequest.

        |参数名称：度量类型| |参数的约束及描述：|

        :return: The measure_type of this ListConversionsRequest.
        :rtype: int
        """
        return self._measure_type

    @measure_type.setter
    def measure_type(self, measure_type):
        """Sets the measure_type of this ListConversionsRequest.

        |参数名称：度量类型| |参数的约束及描述：|

        :param measure_type: The measure_type of this ListConversionsRequest.
        :type: int
        """
        self._measure_type = measure_type

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
        if not isinstance(other, ListConversionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
