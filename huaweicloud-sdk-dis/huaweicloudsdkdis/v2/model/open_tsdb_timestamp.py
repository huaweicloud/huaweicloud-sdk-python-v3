# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenTSDBTimestamp:

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
        'value': 'str',
        'format': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'format': 'format'
    }

    def __init__(self, type=None, value=None, format=None):
        """OpenTSDBTimestamp

        The model defined in huaweicloud sdk

        :param type: - Timestamp类型表示通道内用户数据对应JSON属性的取值为Timestamp类型，不需要进行数据格式转换就可以生成OpenTSDB的timestamp。 - String类型表示通道内用户数据对应JSON属性的取值为Date格式，需要进行数据格式转换才能生成OpenTSDB的timestamp。
        :type type: str
        :param value: 通道内用户数据的JSON属性名称。  取值范围：1～32，只能包含英文字母、数字和下划线。
        :type value: str
        :param format: “type”为“String”类型时必选。表示通道内用户数据对应JSON属性的取值为Date格式，需要根据format字段进行数据格式转换生成OpenTSDB的timestamp。  取值范围：  - yyyy/MM/dd HH:mm:ss - MM/dd/yyyy HH:mm:ss - dd/MM/yyyy HH:mm:ss - yyyy-MM-dd HH:mm:ss - MM-dd-yyyy HH:mm:ss - dd-MM-yyyy HH:mm:ss
        :type format: str
        """
        
        

        self._type = None
        self._value = None
        self._format = None
        self.discriminator = None

        self.type = type
        self.value = value
        self.format = format

    @property
    def type(self):
        """Gets the type of this OpenTSDBTimestamp.

        - Timestamp类型表示通道内用户数据对应JSON属性的取值为Timestamp类型，不需要进行数据格式转换就可以生成OpenTSDB的timestamp。 - String类型表示通道内用户数据对应JSON属性的取值为Date格式，需要进行数据格式转换才能生成OpenTSDB的timestamp。

        :return: The type of this OpenTSDBTimestamp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OpenTSDBTimestamp.

        - Timestamp类型表示通道内用户数据对应JSON属性的取值为Timestamp类型，不需要进行数据格式转换就可以生成OpenTSDB的timestamp。 - String类型表示通道内用户数据对应JSON属性的取值为Date格式，需要进行数据格式转换才能生成OpenTSDB的timestamp。

        :param type: The type of this OpenTSDBTimestamp.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this OpenTSDBTimestamp.

        通道内用户数据的JSON属性名称。  取值范围：1～32，只能包含英文字母、数字和下划线。

        :return: The value of this OpenTSDBTimestamp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OpenTSDBTimestamp.

        通道内用户数据的JSON属性名称。  取值范围：1～32，只能包含英文字母、数字和下划线。

        :param value: The value of this OpenTSDBTimestamp.
        :type value: str
        """
        self._value = value

    @property
    def format(self):
        """Gets the format of this OpenTSDBTimestamp.

        “type”为“String”类型时必选。表示通道内用户数据对应JSON属性的取值为Date格式，需要根据format字段进行数据格式转换生成OpenTSDB的timestamp。  取值范围：  - yyyy/MM/dd HH:mm:ss - MM/dd/yyyy HH:mm:ss - dd/MM/yyyy HH:mm:ss - yyyy-MM-dd HH:mm:ss - MM-dd-yyyy HH:mm:ss - dd-MM-yyyy HH:mm:ss

        :return: The format of this OpenTSDBTimestamp.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this OpenTSDBTimestamp.

        “type”为“String”类型时必选。表示通道内用户数据对应JSON属性的取值为Date格式，需要根据format字段进行数据格式转换生成OpenTSDB的timestamp。  取值范围：  - yyyy/MM/dd HH:mm:ss - MM/dd/yyyy HH:mm:ss - dd/MM/yyyy HH:mm:ss - yyyy-MM-dd HH:mm:ss - MM-dd-yyyy HH:mm:ss - dd-MM-yyyy HH:mm:ss

        :param format: The format of this OpenTSDBTimestamp.
        :type format: str
        """
        self._format = format

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
        if not isinstance(other, OpenTSDBTimestamp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
