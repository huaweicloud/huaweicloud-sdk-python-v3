# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueDetailCustomField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'custom_field': 'str',
        'field_name': 'str',
        'value': 'str',
        'field_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'custom_field': 'custom_field',
        'field_name': 'field_name',
        'value': 'value',
        'field_type': 'field_type',
        'description': 'description'
    }

    def __init__(self, custom_field=None, field_name=None, value=None, field_type=None, description=None):
        r"""IssueDetailCustomField

        The model defined in huaweicloud sdk

        :param custom_field: 自定义字段
        :type custom_field: str
        :param field_name: 自定义字段名称
        :type field_name: str
        :param value: 自定义属性对应的值，多个值以英文逗号区分开
        :type value: str
        :param field_type: 自定义字段类型， textArea 多行文本，text 单行文本，select 下拉框，number 数字，time_date 日期，checkbox 多选框，radio 单选框
        :type field_type: str
        :param description: 自定义字段描述
        :type description: str
        """
        
        

        self._custom_field = None
        self._field_name = None
        self._value = None
        self._field_type = None
        self._description = None
        self.discriminator = None

        if custom_field is not None:
            self.custom_field = custom_field
        if field_name is not None:
            self.field_name = field_name
        if value is not None:
            self.value = value
        if field_type is not None:
            self.field_type = field_type
        if description is not None:
            self.description = description

    @property
    def custom_field(self):
        r"""Gets the custom_field of this IssueDetailCustomField.

        自定义字段

        :return: The custom_field of this IssueDetailCustomField.
        :rtype: str
        """
        return self._custom_field

    @custom_field.setter
    def custom_field(self, custom_field):
        r"""Sets the custom_field of this IssueDetailCustomField.

        自定义字段

        :param custom_field: The custom_field of this IssueDetailCustomField.
        :type custom_field: str
        """
        self._custom_field = custom_field

    @property
    def field_name(self):
        r"""Gets the field_name of this IssueDetailCustomField.

        自定义字段名称

        :return: The field_name of this IssueDetailCustomField.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this IssueDetailCustomField.

        自定义字段名称

        :param field_name: The field_name of this IssueDetailCustomField.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def value(self):
        r"""Gets the value of this IssueDetailCustomField.

        自定义属性对应的值，多个值以英文逗号区分开

        :return: The value of this IssueDetailCustomField.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this IssueDetailCustomField.

        自定义属性对应的值，多个值以英文逗号区分开

        :param value: The value of this IssueDetailCustomField.
        :type value: str
        """
        self._value = value

    @property
    def field_type(self):
        r"""Gets the field_type of this IssueDetailCustomField.

        自定义字段类型， textArea 多行文本，text 单行文本，select 下拉框，number 数字，time_date 日期，checkbox 多选框，radio 单选框

        :return: The field_type of this IssueDetailCustomField.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this IssueDetailCustomField.

        自定义字段类型， textArea 多行文本，text 单行文本，select 下拉框，number 数字，time_date 日期，checkbox 多选框，radio 单选框

        :param field_type: The field_type of this IssueDetailCustomField.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def description(self):
        r"""Gets the description of this IssueDetailCustomField.

        自定义字段描述

        :return: The description of this IssueDetailCustomField.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this IssueDetailCustomField.

        自定义字段描述

        :param description: The description of this IssueDetailCustomField.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, IssueDetailCustomField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
