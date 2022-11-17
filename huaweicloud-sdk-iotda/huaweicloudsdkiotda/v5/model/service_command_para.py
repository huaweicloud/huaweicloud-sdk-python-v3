# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServiceCommandPara:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'para_name': 'str',
        'data_type': 'str',
        'required': 'bool',
        'enum_list': 'list[str]',
        'min': 'str',
        'max': 'str',
        'max_length': 'int',
        'step': 'float',
        'unit': 'str',
        'description': 'str'
    }

    attribute_map = {
        'para_name': 'para_name',
        'data_type': 'data_type',
        'required': 'required',
        'enum_list': 'enum_list',
        'min': 'min',
        'max': 'max',
        'max_length': 'max_length',
        'step': 'step',
        'unit': 'unit',
        'description': 'description'
    }

    def __init__(self, para_name=None, data_type=None, required=None, enum_list=None, min=None, max=None, max_length=None, step=None, unit=None, description=None):
        """ServiceCommandPara

        The model defined in huaweicloud sdk

        :param para_name: **参数说明**：参数的名称。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?&#39;#().,&amp;%@!-等字符的组合。
        :type para_name: str
        :param data_type: **参数说明**：参数的数据类型。 **取值范围**：int，long，decimal，string，DateTime，jsonObject，enum，boolean，string list。
        :type data_type: str
        :param required: **参数说明**：参数是否必选。默认为false。
        :type required: bool
        :param enum_list: **参数说明**：参数的枚举值列表。
        :type enum_list: list[str]
        :param min: **参数说明**：参数的最小值。 **取值范围**：长度1-16。
        :type min: str
        :param max: **参数说明**：参数的最大值。 **取值范围**：长度1-16。
        :type max: str
        :param max_length: **参数说明**：参数的最大长度。
        :type max_length: int
        :param step: **参数说明**：参数的步长。
        :type step: float
        :param unit: **参数说明**：参数的单位。 **取值范围**：长度不超过16。
        :type unit: str
        :param description: **参数说明**：参数的描述。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?&#39;#().,;&amp;%@!- ，、：；。/等字符的组合。
        :type description: str
        """
        
        

        self._para_name = None
        self._data_type = None
        self._required = None
        self._enum_list = None
        self._min = None
        self._max = None
        self._max_length = None
        self._step = None
        self._unit = None
        self._description = None
        self.discriminator = None

        self.para_name = para_name
        self.data_type = data_type
        if required is not None:
            self.required = required
        if enum_list is not None:
            self.enum_list = enum_list
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if max_length is not None:
            self.max_length = max_length
        if step is not None:
            self.step = step
        if unit is not None:
            self.unit = unit
        if description is not None:
            self.description = description

    @property
    def para_name(self):
        """Gets the para_name of this ServiceCommandPara.

        **参数说明**：参数的名称。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :return: The para_name of this ServiceCommandPara.
        :rtype: str
        """
        return self._para_name

    @para_name.setter
    def para_name(self, para_name):
        """Sets the para_name of this ServiceCommandPara.

        **参数说明**：参数的名称。 **取值范围**：长度不超过32，只允许中文、字母、数字、以及_?'#().,&%@!-等字符的组合。

        :param para_name: The para_name of this ServiceCommandPara.
        :type para_name: str
        """
        self._para_name = para_name

    @property
    def data_type(self):
        """Gets the data_type of this ServiceCommandPara.

        **参数说明**：参数的数据类型。 **取值范围**：int，long，decimal，string，DateTime，jsonObject，enum，boolean，string list。

        :return: The data_type of this ServiceCommandPara.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ServiceCommandPara.

        **参数说明**：参数的数据类型。 **取值范围**：int，long，decimal，string，DateTime，jsonObject，enum，boolean，string list。

        :param data_type: The data_type of this ServiceCommandPara.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def required(self):
        """Gets the required of this ServiceCommandPara.

        **参数说明**：参数是否必选。默认为false。

        :return: The required of this ServiceCommandPara.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ServiceCommandPara.

        **参数说明**：参数是否必选。默认为false。

        :param required: The required of this ServiceCommandPara.
        :type required: bool
        """
        self._required = required

    @property
    def enum_list(self):
        """Gets the enum_list of this ServiceCommandPara.

        **参数说明**：参数的枚举值列表。

        :return: The enum_list of this ServiceCommandPara.
        :rtype: list[str]
        """
        return self._enum_list

    @enum_list.setter
    def enum_list(self, enum_list):
        """Sets the enum_list of this ServiceCommandPara.

        **参数说明**：参数的枚举值列表。

        :param enum_list: The enum_list of this ServiceCommandPara.
        :type enum_list: list[str]
        """
        self._enum_list = enum_list

    @property
    def min(self):
        """Gets the min of this ServiceCommandPara.

        **参数说明**：参数的最小值。 **取值范围**：长度1-16。

        :return: The min of this ServiceCommandPara.
        :rtype: str
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ServiceCommandPara.

        **参数说明**：参数的最小值。 **取值范围**：长度1-16。

        :param min: The min of this ServiceCommandPara.
        :type min: str
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this ServiceCommandPara.

        **参数说明**：参数的最大值。 **取值范围**：长度1-16。

        :return: The max of this ServiceCommandPara.
        :rtype: str
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ServiceCommandPara.

        **参数说明**：参数的最大值。 **取值范围**：长度1-16。

        :param max: The max of this ServiceCommandPara.
        :type max: str
        """
        self._max = max

    @property
    def max_length(self):
        """Gets the max_length of this ServiceCommandPara.

        **参数说明**：参数的最大长度。

        :return: The max_length of this ServiceCommandPara.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this ServiceCommandPara.

        **参数说明**：参数的最大长度。

        :param max_length: The max_length of this ServiceCommandPara.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def step(self):
        """Gets the step of this ServiceCommandPara.

        **参数说明**：参数的步长。

        :return: The step of this ServiceCommandPara.
        :rtype: float
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this ServiceCommandPara.

        **参数说明**：参数的步长。

        :param step: The step of this ServiceCommandPara.
        :type step: float
        """
        self._step = step

    @property
    def unit(self):
        """Gets the unit of this ServiceCommandPara.

        **参数说明**：参数的单位。 **取值范围**：长度不超过16。

        :return: The unit of this ServiceCommandPara.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ServiceCommandPara.

        **参数说明**：参数的单位。 **取值范围**：长度不超过16。

        :param unit: The unit of this ServiceCommandPara.
        :type unit: str
        """
        self._unit = unit

    @property
    def description(self):
        """Gets the description of this ServiceCommandPara.

        **参数说明**：参数的描述。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?'#().,;&%@!- ，、：；。/等字符的组合。

        :return: The description of this ServiceCommandPara.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ServiceCommandPara.

        **参数说明**：参数的描述。 **取值范围**：长度不超过128，只允许中文、字母、数字、空白字符、以及_?'#().,;&%@!- ，、：；。/等字符的组合。

        :param description: The description of this ServiceCommandPara.
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
        if not isinstance(other, ServiceCommandPara):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
