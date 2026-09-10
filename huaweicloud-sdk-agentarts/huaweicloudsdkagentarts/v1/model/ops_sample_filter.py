# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsSampleFilter:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'field': 'str',
        'operator': 'str',
        'label_name': 'str',
        'value': 'object'
    }

    attribute_map = {
        'field': 'field',
        'operator': 'operator',
        'label_name': 'label_name',
        'value': 'value'
    }

    def __init__(self, field=None, operator=None, label_name=None, value=None):
        r"""OpsSampleFilter

        The model defined in huaweicloud sdk

        :param field: **参数解释：** 过滤名，指定要过滤的字段名称。  **约束限制：** 不涉及  **取值范围：** Duration,Label,Input,Output  **默认取值：** 无。
        :type field: str
        :param operator: **参数解释：** 操作符。  **约束限制：** 对不同的field类型，支持不同的操作符。 Duration：greater_than：大于等于，less_than：小于等于 Input：like：包含，not_like：不包含 Output：like：包含，not_like：不包含 Label：greater_than：大于等于，less_than：小于等于，like：包含，not_like：不包含，in：属于，not_in：不属于   **取值范围：** like：包含，not_like：不包含，equals：等于，empty：为空，not_empty：不为空，greater_than：大于等于，less_than：小于等于，in：属于，not_in：不属于  **默认取值：** 无。
        :type operator: str
        :param label_name: **参数解释：** 标签名。  **约束限制：** 当field为Label时必填。field为其他值时无意义。  **取值范围：**   **默认取值：** 无。
        :type label_name: str
        :param value: **参数解释：** 筛选的值。  **约束限制：** 值类型取决于操作符字段（operator）： 字符串(string)、数字(number)、布尔(boolean)或字符串数组(array)。  greater_than，less_than：数字(number) like，not_like：字符串(string) equals：数字(number) 或 字符串(string) empty，not_empty：不传递该字段 in，not_in：字符串数组(array)  **取值范围：** - 字符串：长度0-64个字符。 - 数字：整数或浮点数。 - 布尔：true或false。 - 数组：长度0-20，每个元素长度0-64个字符的字符串。  **默认取值：** 无。
        :type value: object
        """
        
        

        self._field = None
        self._operator = None
        self._label_name = None
        self._value = None
        self.discriminator = None

        self.field = field
        self.operator = operator
        if label_name is not None:
            self.label_name = label_name
        if value is not None:
            self.value = value

    @property
    def field(self):
        r"""Gets the field of this OpsSampleFilter.

        **参数解释：** 过滤名，指定要过滤的字段名称。  **约束限制：** 不涉及  **取值范围：** Duration,Label,Input,Output  **默认取值：** 无。

        :return: The field of this OpsSampleFilter.
        :rtype: str
        """
        return self._field

    @field.setter
    def field(self, field):
        r"""Sets the field of this OpsSampleFilter.

        **参数解释：** 过滤名，指定要过滤的字段名称。  **约束限制：** 不涉及  **取值范围：** Duration,Label,Input,Output  **默认取值：** 无。

        :param field: The field of this OpsSampleFilter.
        :type field: str
        """
        self._field = field

    @property
    def operator(self):
        r"""Gets the operator of this OpsSampleFilter.

        **参数解释：** 操作符。  **约束限制：** 对不同的field类型，支持不同的操作符。 Duration：greater_than：大于等于，less_than：小于等于 Input：like：包含，not_like：不包含 Output：like：包含，not_like：不包含 Label：greater_than：大于等于，less_than：小于等于，like：包含，not_like：不包含，in：属于，not_in：不属于   **取值范围：** like：包含，not_like：不包含，equals：等于，empty：为空，not_empty：不为空，greater_than：大于等于，less_than：小于等于，in：属于，not_in：不属于  **默认取值：** 无。

        :return: The operator of this OpsSampleFilter.
        :rtype: str
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        r"""Sets the operator of this OpsSampleFilter.

        **参数解释：** 操作符。  **约束限制：** 对不同的field类型，支持不同的操作符。 Duration：greater_than：大于等于，less_than：小于等于 Input：like：包含，not_like：不包含 Output：like：包含，not_like：不包含 Label：greater_than：大于等于，less_than：小于等于，like：包含，not_like：不包含，in：属于，not_in：不属于   **取值范围：** like：包含，not_like：不包含，equals：等于，empty：为空，not_empty：不为空，greater_than：大于等于，less_than：小于等于，in：属于，not_in：不属于  **默认取值：** 无。

        :param operator: The operator of this OpsSampleFilter.
        :type operator: str
        """
        self._operator = operator

    @property
    def label_name(self):
        r"""Gets the label_name of this OpsSampleFilter.

        **参数解释：** 标签名。  **约束限制：** 当field为Label时必填。field为其他值时无意义。  **取值范围：**   **默认取值：** 无。

        :return: The label_name of this OpsSampleFilter.
        :rtype: str
        """
        return self._label_name

    @label_name.setter
    def label_name(self, label_name):
        r"""Sets the label_name of this OpsSampleFilter.

        **参数解释：** 标签名。  **约束限制：** 当field为Label时必填。field为其他值时无意义。  **取值范围：**   **默认取值：** 无。

        :param label_name: The label_name of this OpsSampleFilter.
        :type label_name: str
        """
        self._label_name = label_name

    @property
    def value(self):
        r"""Gets the value of this OpsSampleFilter.

        **参数解释：** 筛选的值。  **约束限制：** 值类型取决于操作符字段（operator）： 字符串(string)、数字(number)、布尔(boolean)或字符串数组(array)。  greater_than，less_than：数字(number) like，not_like：字符串(string) equals：数字(number) 或 字符串(string) empty，not_empty：不传递该字段 in，not_in：字符串数组(array)  **取值范围：** - 字符串：长度0-64个字符。 - 数字：整数或浮点数。 - 布尔：true或false。 - 数组：长度0-20，每个元素长度0-64个字符的字符串。  **默认取值：** 无。

        :return: The value of this OpsSampleFilter.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this OpsSampleFilter.

        **参数解释：** 筛选的值。  **约束限制：** 值类型取决于操作符字段（operator）： 字符串(string)、数字(number)、布尔(boolean)或字符串数组(array)。  greater_than，less_than：数字(number) like，not_like：字符串(string) equals：数字(number) 或 字符串(string) empty，not_empty：不传递该字段 in，not_in：字符串数组(array)  **取值范围：** - 字符串：长度0-64个字符。 - 数字：整数或浮点数。 - 布尔：true或false。 - 数组：长度0-20，每个元素长度0-64个字符的字符串。  **默认取值：** 无。

        :param value: The value of this OpsSampleFilter.
        :type value: object
        """
        self._value = value

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
        if not isinstance(other, OpsSampleFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
