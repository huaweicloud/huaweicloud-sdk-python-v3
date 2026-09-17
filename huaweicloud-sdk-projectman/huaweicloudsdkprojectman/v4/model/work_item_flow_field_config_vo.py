# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WorkItemFlowFieldConfigVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field_code': 'str',
        'value_type': 'str',
        'field_operation': 'str',
        'field_value': 'WorkItemFlowFieldValueVO',
        'required': 'bool',
        'field_range': 'WorkItemFlowFieldRangeVO'
    }

    attribute_map = {
        'field_code': 'field_code',
        'value_type': 'value_type',
        'field_operation': 'field_operation',
        'field_value': 'field_value',
        'required': 'required',
        'field_range': 'field_range'
    }

    def __init__(self, field_code=None, value_type=None, field_operation=None, field_value=None, required=None, field_range=None):
        r"""WorkItemFlowFieldConfigVO

        The model defined in huaweicloud sdk

        :param field_code: 字段编码
        :type field_code: str
        :param value_type: 字段值类型
        :type value_type: str
        :param field_operation: 字段操作类型
        :type field_operation: str
        :param field_value: 
        :type field_value: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowFieldValueVO`
        :param required: 是否必填
        :type required: bool
        :param field_range: 
        :type field_range: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowFieldRangeVO`
        """
        
        

        self._field_code = None
        self._value_type = None
        self._field_operation = None
        self._field_value = None
        self._required = None
        self._field_range = None
        self.discriminator = None

        if field_code is not None:
            self.field_code = field_code
        if value_type is not None:
            self.value_type = value_type
        if field_operation is not None:
            self.field_operation = field_operation
        if field_value is not None:
            self.field_value = field_value
        if required is not None:
            self.required = required
        if field_range is not None:
            self.field_range = field_range

    @property
    def field_code(self):
        r"""Gets the field_code of this WorkItemFlowFieldConfigVO.

        字段编码

        :return: The field_code of this WorkItemFlowFieldConfigVO.
        :rtype: str
        """
        return self._field_code

    @field_code.setter
    def field_code(self, field_code):
        r"""Sets the field_code of this WorkItemFlowFieldConfigVO.

        字段编码

        :param field_code: The field_code of this WorkItemFlowFieldConfigVO.
        :type field_code: str
        """
        self._field_code = field_code

    @property
    def value_type(self):
        r"""Gets the value_type of this WorkItemFlowFieldConfigVO.

        字段值类型

        :return: The value_type of this WorkItemFlowFieldConfigVO.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        r"""Sets the value_type of this WorkItemFlowFieldConfigVO.

        字段值类型

        :param value_type: The value_type of this WorkItemFlowFieldConfigVO.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def field_operation(self):
        r"""Gets the field_operation of this WorkItemFlowFieldConfigVO.

        字段操作类型

        :return: The field_operation of this WorkItemFlowFieldConfigVO.
        :rtype: str
        """
        return self._field_operation

    @field_operation.setter
    def field_operation(self, field_operation):
        r"""Sets the field_operation of this WorkItemFlowFieldConfigVO.

        字段操作类型

        :param field_operation: The field_operation of this WorkItemFlowFieldConfigVO.
        :type field_operation: str
        """
        self._field_operation = field_operation

    @property
    def field_value(self):
        r"""Gets the field_value of this WorkItemFlowFieldConfigVO.

        :return: The field_value of this WorkItemFlowFieldConfigVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowFieldValueVO`
        """
        return self._field_value

    @field_value.setter
    def field_value(self, field_value):
        r"""Sets the field_value of this WorkItemFlowFieldConfigVO.

        :param field_value: The field_value of this WorkItemFlowFieldConfigVO.
        :type field_value: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowFieldValueVO`
        """
        self._field_value = field_value

    @property
    def required(self):
        r"""Gets the required of this WorkItemFlowFieldConfigVO.

        是否必填

        :return: The required of this WorkItemFlowFieldConfigVO.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this WorkItemFlowFieldConfigVO.

        是否必填

        :param required: The required of this WorkItemFlowFieldConfigVO.
        :type required: bool
        """
        self._required = required

    @property
    def field_range(self):
        r"""Gets the field_range of this WorkItemFlowFieldConfigVO.

        :return: The field_range of this WorkItemFlowFieldConfigVO.
        :rtype: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowFieldRangeVO`
        """
        return self._field_range

    @field_range.setter
    def field_range(self, field_range):
        r"""Sets the field_range of this WorkItemFlowFieldConfigVO.

        :param field_range: The field_range of this WorkItemFlowFieldConfigVO.
        :type field_range: :class:`huaweicloudsdkprojectman.v4.WorkItemFlowFieldRangeVO`
        """
        self._field_range = field_range

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, WorkItemFlowFieldConfigVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
