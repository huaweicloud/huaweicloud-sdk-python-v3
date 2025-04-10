# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkitemCustomField:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_id': 'str',
        'field_name': 'str',
        'field_type': 'str',
        'field_option_source': 'str',
        'value': 'str'
    }

    attribute_map = {
        'field_id': 'field_id',
        'field_name': 'field_name',
        'field_type': 'field_type',
        'field_option_source': 'field_option_source',
        'value': 'value'
    }

    def __init__(self, field_id=None, field_name=None, field_type=None, field_option_source=None, value=None):
        r"""WorkitemCustomField

        The model defined in huaweicloud sdk

        :param field_id: 自定义字段id
        :type field_id: str
        :param field_name: 自定义字段名称
        :type field_name: str
        :param field_type: 自定义字段类型, \&quot;Date\&quot;,\&quot;Number\&quot;,\&quot;DateTime\&quot;, \&quot;MultiLineText\&quot;,\&quot;SingleLineText\&quot;, \&quot;Select\&quot;,  \&quot;Checkbox\&quot;
        :type field_type: str
        :param field_option_source: 自定义字段的选项源,CUSTOM，USER，DOMAIN，ITERATION，MODULE，TAG
        :type field_option_source: str
        :param value: 自定义字段值, (field_type为Date,Number,DateTime时,field_option_source为空，value值是数字的字符串)， (field_type为MultiLineText,SingleLineText时,field_option_source为空，value值是文本字符串)， (field_type为Select ,field_option_source为CUSTOM时，value值是文本字符串) (field_type为Select ,field_option_source为USER，DOMAIN，ITERATION，MODULE，TAG时，value值是Json格式{}), (field_type为Checkbox ,field_option_source为CUSTOM时，value值是字符串数组[\\\&quot;aaa\\\&quot;]), (field_type为\&quot;Checkbox\&quot; ,field_option_source为USER，DOMAIN，ITERATION，MODULE，TAG时，value值是Json的数组[{},{}])
        :type value: str
        """
        
        

        self._field_id = None
        self._field_name = None
        self._field_type = None
        self._field_option_source = None
        self._value = None
        self.discriminator = None

        if field_id is not None:
            self.field_id = field_id
        if field_name is not None:
            self.field_name = field_name
        if field_type is not None:
            self.field_type = field_type
        if field_option_source is not None:
            self.field_option_source = field_option_source
        if value is not None:
            self.value = value

    @property
    def field_id(self):
        r"""Gets the field_id of this WorkitemCustomField.

        自定义字段id

        :return: The field_id of this WorkitemCustomField.
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        r"""Sets the field_id of this WorkitemCustomField.

        自定义字段id

        :param field_id: The field_id of this WorkitemCustomField.
        :type field_id: str
        """
        self._field_id = field_id

    @property
    def field_name(self):
        r"""Gets the field_name of this WorkitemCustomField.

        自定义字段名称

        :return: The field_name of this WorkitemCustomField.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        r"""Sets the field_name of this WorkitemCustomField.

        自定义字段名称

        :param field_name: The field_name of this WorkitemCustomField.
        :type field_name: str
        """
        self._field_name = field_name

    @property
    def field_type(self):
        r"""Gets the field_type of this WorkitemCustomField.

        自定义字段类型, \"Date\",\"Number\",\"DateTime\", \"MultiLineText\",\"SingleLineText\", \"Select\",  \"Checkbox\"

        :return: The field_type of this WorkitemCustomField.
        :rtype: str
        """
        return self._field_type

    @field_type.setter
    def field_type(self, field_type):
        r"""Sets the field_type of this WorkitemCustomField.

        自定义字段类型, \"Date\",\"Number\",\"DateTime\", \"MultiLineText\",\"SingleLineText\", \"Select\",  \"Checkbox\"

        :param field_type: The field_type of this WorkitemCustomField.
        :type field_type: str
        """
        self._field_type = field_type

    @property
    def field_option_source(self):
        r"""Gets the field_option_source of this WorkitemCustomField.

        自定义字段的选项源,CUSTOM，USER，DOMAIN，ITERATION，MODULE，TAG

        :return: The field_option_source of this WorkitemCustomField.
        :rtype: str
        """
        return self._field_option_source

    @field_option_source.setter
    def field_option_source(self, field_option_source):
        r"""Sets the field_option_source of this WorkitemCustomField.

        自定义字段的选项源,CUSTOM，USER，DOMAIN，ITERATION，MODULE，TAG

        :param field_option_source: The field_option_source of this WorkitemCustomField.
        :type field_option_source: str
        """
        self._field_option_source = field_option_source

    @property
    def value(self):
        r"""Gets the value of this WorkitemCustomField.

        自定义字段值, (field_type为Date,Number,DateTime时,field_option_source为空，value值是数字的字符串)， (field_type为MultiLineText,SingleLineText时,field_option_source为空，value值是文本字符串)， (field_type为Select ,field_option_source为CUSTOM时，value值是文本字符串) (field_type为Select ,field_option_source为USER，DOMAIN，ITERATION，MODULE，TAG时，value值是Json格式{}), (field_type为Checkbox ,field_option_source为CUSTOM时，value值是字符串数组[\\\"aaa\\\"]), (field_type为\"Checkbox\" ,field_option_source为USER，DOMAIN，ITERATION，MODULE，TAG时，value值是Json的数组[{},{}])

        :return: The value of this WorkitemCustomField.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this WorkitemCustomField.

        自定义字段值, (field_type为Date,Number,DateTime时,field_option_source为空，value值是数字的字符串)， (field_type为MultiLineText,SingleLineText时,field_option_source为空，value值是文本字符串)， (field_type为Select ,field_option_source为CUSTOM时，value值是文本字符串) (field_type为Select ,field_option_source为USER，DOMAIN，ITERATION，MODULE，TAG时，value值是Json格式{}), (field_type为Checkbox ,field_option_source为CUSTOM时，value值是字符串数组[\\\"aaa\\\"]), (field_type为\"Checkbox\" ,field_option_source为USER，DOMAIN，ITERATION，MODULE，TAG时，value值是Json的数组[{},{}])

        :param value: The value of this WorkitemCustomField.
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
        if not isinstance(other, WorkitemCustomField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
