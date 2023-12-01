# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenTSDBTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'value': 'value'
    }

    def __init__(self, name=None, type=None, value=None):
        """OpenTSDBTags

        The model defined in huaweicloud sdk

        :param name: 存储该通道数据的OpenTSDB数据的tag名称。  取值范围：1～32，只能包含英文字母、数字和下划线。
        :type name: str
        :param type: 通道内用户JSON数据对应JSON属性的类型名称。  取值范围：  - Bigint - Double - Boolean - Timestamp - String - Decimal
        :type type: str
        :param value: 常量或通道内用户数据的JSON属性名称。  取值范围：1～32，只能包含英文字母、数字和下划线。
        :type value: str
        """
        
        

        self._name = None
        self._type = None
        self._value = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.value = value

    @property
    def name(self):
        """Gets the name of this OpenTSDBTags.

        存储该通道数据的OpenTSDB数据的tag名称。  取值范围：1～32，只能包含英文字母、数字和下划线。

        :return: The name of this OpenTSDBTags.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OpenTSDBTags.

        存储该通道数据的OpenTSDB数据的tag名称。  取值范围：1～32，只能包含英文字母、数字和下划线。

        :param name: The name of this OpenTSDBTags.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this OpenTSDBTags.

        通道内用户JSON数据对应JSON属性的类型名称。  取值范围：  - Bigint - Double - Boolean - Timestamp - String - Decimal

        :return: The type of this OpenTSDBTags.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OpenTSDBTags.

        通道内用户JSON数据对应JSON属性的类型名称。  取值范围：  - Bigint - Double - Boolean - Timestamp - String - Decimal

        :param type: The type of this OpenTSDBTags.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this OpenTSDBTags.

        常量或通道内用户数据的JSON属性名称。  取值范围：1～32，只能包含英文字母、数字和下划线。

        :return: The value of this OpenTSDBTags.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OpenTSDBTags.

        常量或通道内用户数据的JSON属性名称。  取值范围：1～32，只能包含英文字母、数字和下划线。

        :param value: The value of this OpenTSDBTags.
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
        if not isinstance(other, OpenTSDBTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
