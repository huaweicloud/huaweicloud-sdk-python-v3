# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenTSDBMetric:

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
        'value': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, type=None, value=None):
        """OpenTSDBMetric

        The model defined in huaweicloud sdk

        :param type: - Constant表示metric为常量value的值。 - String表示metric为通道内用户数据对应JSON属性的取值，且该JOSN属性的取值为String。
        :type type: str
        :param value: 常量或通道内用户数据的JSON属性名称。  取值范围：1～32，只能包含英文字母、数字和点。
        :type value: str
        """
        
        

        self._type = None
        self._value = None
        self.discriminator = None

        self.type = type
        self.value = value

    @property
    def type(self):
        """Gets the type of this OpenTSDBMetric.

        - Constant表示metric为常量value的值。 - String表示metric为通道内用户数据对应JSON属性的取值，且该JOSN属性的取值为String。

        :return: The type of this OpenTSDBMetric.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OpenTSDBMetric.

        - Constant表示metric为常量value的值。 - String表示metric为通道内用户数据对应JSON属性的取值，且该JOSN属性的取值为String。

        :param type: The type of this OpenTSDBMetric.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this OpenTSDBMetric.

        常量或通道内用户数据的JSON属性名称。  取值范围：1～32，只能包含英文字母、数字和点。

        :return: The value of this OpenTSDBMetric.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OpenTSDBMetric.

        常量或通道内用户数据的JSON属性名称。  取值范围：1～32，只能包含英文字母、数字和点。

        :param value: The value of this OpenTSDBMetric.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, OpenTSDBMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
