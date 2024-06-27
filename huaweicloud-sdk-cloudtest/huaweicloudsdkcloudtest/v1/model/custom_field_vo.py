# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomFieldVo:

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
        'custom_field_param': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'custom_field_param': 'custom_field_param',
        'user_name': 'user_name'
    }

    def __init__(self, type=None, value=None, custom_field_param=None, user_name=None):
        """CustomFieldVo

        The model defined in huaweicloud sdk

        :param type: 字段类型（单行文本text、多行文本textArea、单选框radio、多选框checkBox、日期date、数字number、单选用户user）
        :type type: str
        :param value: 测试用例自定义字段值
        :type value: str
        :param custom_field_param: 项目用例自定义字段入参或者返回参数名称
        :type custom_field_param: str
        :param user_name: user类型测试用例自定义字段对应用户名，其它类型字段不返回
        :type user_name: str
        """
        
        

        self._type = None
        self._value = None
        self._custom_field_param = None
        self._user_name = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if custom_field_param is not None:
            self.custom_field_param = custom_field_param
        if user_name is not None:
            self.user_name = user_name

    @property
    def type(self):
        """Gets the type of this CustomFieldVo.

        字段类型（单行文本text、多行文本textArea、单选框radio、多选框checkBox、日期date、数字number、单选用户user）

        :return: The type of this CustomFieldVo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CustomFieldVo.

        字段类型（单行文本text、多行文本textArea、单选框radio、多选框checkBox、日期date、数字number、单选用户user）

        :param type: The type of this CustomFieldVo.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        """Gets the value of this CustomFieldVo.

        测试用例自定义字段值

        :return: The value of this CustomFieldVo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CustomFieldVo.

        测试用例自定义字段值

        :param value: The value of this CustomFieldVo.
        :type value: str
        """
        self._value = value

    @property
    def custom_field_param(self):
        """Gets the custom_field_param of this CustomFieldVo.

        项目用例自定义字段入参或者返回参数名称

        :return: The custom_field_param of this CustomFieldVo.
        :rtype: str
        """
        return self._custom_field_param

    @custom_field_param.setter
    def custom_field_param(self, custom_field_param):
        """Sets the custom_field_param of this CustomFieldVo.

        项目用例自定义字段入参或者返回参数名称

        :param custom_field_param: The custom_field_param of this CustomFieldVo.
        :type custom_field_param: str
        """
        self._custom_field_param = custom_field_param

    @property
    def user_name(self):
        """Gets the user_name of this CustomFieldVo.

        user类型测试用例自定义字段对应用户名，其它类型字段不返回

        :return: The user_name of this CustomFieldVo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CustomFieldVo.

        user类型测试用例自定义字段对应用户名，其它类型字段不返回

        :param user_name: The user_name of this CustomFieldVo.
        :type user_name: str
        """
        self._user_name = user_name

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
        if not isinstance(other, CustomFieldVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
