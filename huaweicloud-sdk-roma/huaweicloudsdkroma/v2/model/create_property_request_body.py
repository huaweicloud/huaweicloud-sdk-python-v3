# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePropertyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'property_name': 'str',
        'description': 'str',
        'data_type': 'str',
        'required': 'int',
        'min': 'str',
        'max': 'str',
        'step': 'str',
        'max_length': 'int',
        'unit': 'str',
        'enum_list': 'str',
        'enum_dict': 'object',
        'method': 'str'
    }

    attribute_map = {
        'property_name': 'property_name',
        'description': 'description',
        'data_type': 'data_type',
        'required': 'required',
        'min': 'min',
        'max': 'max',
        'step': 'step',
        'max_length': 'max_length',
        'unit': 'unit',
        'enum_list': 'enum_list',
        'enum_dict': 'enum_dict',
        'method': 'method'
    }

    def __init__(self, property_name=None, description=None, data_type=None, required=None, min=None, max=None, step=None, max_length=None, unit=None, enum_list=None, enum_dict=None, method=None):
        r"""CreatePropertyRequestBody

        The model defined in huaweicloud sdk

        :param property_name: 属性名称，首位必须为字母，支持大小写字母，数字，中划线及下划线，长度2-50
        :type property_name: str
        :param description: 属性描述，长度0-200
        :type description: str
        :param data_type: 属性数据类型，枚举值大小写敏感；number格式为数字，范围±1.0 x 10^-28 to ±7.9228 x 10^28；sting为字符串；integer为整数；datetime为时间，格式为yyyyMMddTHHmmss；json为自定义json格式
        :type data_type: str
        :param required: 是否必填 0-非必填 1-必填
        :type required: int
        :param min: 最小值，当data_type为integer或number时必填
        :type min: str
        :param max: 最大值，当data_type为integer或number时必填
        :type max: str
        :param step: 步长，当data_type为integer或number时必填
        :type step: str
        :param max_length: 字符串最大长度，当data_type为string, datetime, json时必填，自动向下取整
        :type max_length: int
        :param unit: 属性单位
        :type unit: str
        :param enum_list: string的枚举值数组，使用逗号分隔
        :type enum_list: str
        :param enum_dict: 当数据类型为boolean枚举值时填写json格式数据，形如\&quot;enum_dict\&quot;:{\&quot;0\&quot;:\&quot;xxx\&quot;,\&quot;1\&quot;:\&quot;xxx\&quot;}
        :type enum_dict: object
        :param method: 访问模式（兼容20.0，R属性可读，W属性可写，E属性可执行）
        :type method: str
        """
        
        

        self._property_name = None
        self._description = None
        self._data_type = None
        self._required = None
        self._min = None
        self._max = None
        self._step = None
        self._max_length = None
        self._unit = None
        self._enum_list = None
        self._enum_dict = None
        self._method = None
        self.discriminator = None

        self.property_name = property_name
        if description is not None:
            self.description = description
        self.data_type = data_type
        self.required = required
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if step is not None:
            self.step = step
        if max_length is not None:
            self.max_length = max_length
        if unit is not None:
            self.unit = unit
        if enum_list is not None:
            self.enum_list = enum_list
        if enum_dict is not None:
            self.enum_dict = enum_dict
        if method is not None:
            self.method = method

    @property
    def property_name(self):
        r"""Gets the property_name of this CreatePropertyRequestBody.

        属性名称，首位必须为字母，支持大小写字母，数字，中划线及下划线，长度2-50

        :return: The property_name of this CreatePropertyRequestBody.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        r"""Sets the property_name of this CreatePropertyRequestBody.

        属性名称，首位必须为字母，支持大小写字母，数字，中划线及下划线，长度2-50

        :param property_name: The property_name of this CreatePropertyRequestBody.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def description(self):
        r"""Gets the description of this CreatePropertyRequestBody.

        属性描述，长度0-200

        :return: The description of this CreatePropertyRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePropertyRequestBody.

        属性描述，长度0-200

        :param description: The description of this CreatePropertyRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def data_type(self):
        r"""Gets the data_type of this CreatePropertyRequestBody.

        属性数据类型，枚举值大小写敏感；number格式为数字，范围±1.0 x 10^-28 to ±7.9228 x 10^28；sting为字符串；integer为整数；datetime为时间，格式为yyyyMMddTHHmmss；json为自定义json格式

        :return: The data_type of this CreatePropertyRequestBody.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        r"""Sets the data_type of this CreatePropertyRequestBody.

        属性数据类型，枚举值大小写敏感；number格式为数字，范围±1.0 x 10^-28 to ±7.9228 x 10^28；sting为字符串；integer为整数；datetime为时间，格式为yyyyMMddTHHmmss；json为自定义json格式

        :param data_type: The data_type of this CreatePropertyRequestBody.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def required(self):
        r"""Gets the required of this CreatePropertyRequestBody.

        是否必填 0-非必填 1-必填

        :return: The required of this CreatePropertyRequestBody.
        :rtype: int
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this CreatePropertyRequestBody.

        是否必填 0-非必填 1-必填

        :param required: The required of this CreatePropertyRequestBody.
        :type required: int
        """
        self._required = required

    @property
    def min(self):
        r"""Gets the min of this CreatePropertyRequestBody.

        最小值，当data_type为integer或number时必填

        :return: The min of this CreatePropertyRequestBody.
        :rtype: str
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this CreatePropertyRequestBody.

        最小值，当data_type为integer或number时必填

        :param min: The min of this CreatePropertyRequestBody.
        :type min: str
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this CreatePropertyRequestBody.

        最大值，当data_type为integer或number时必填

        :return: The max of this CreatePropertyRequestBody.
        :rtype: str
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this CreatePropertyRequestBody.

        最大值，当data_type为integer或number时必填

        :param max: The max of this CreatePropertyRequestBody.
        :type max: str
        """
        self._max = max

    @property
    def step(self):
        r"""Gets the step of this CreatePropertyRequestBody.

        步长，当data_type为integer或number时必填

        :return: The step of this CreatePropertyRequestBody.
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        r"""Sets the step of this CreatePropertyRequestBody.

        步长，当data_type为integer或number时必填

        :param step: The step of this CreatePropertyRequestBody.
        :type step: str
        """
        self._step = step

    @property
    def max_length(self):
        r"""Gets the max_length of this CreatePropertyRequestBody.

        字符串最大长度，当data_type为string, datetime, json时必填，自动向下取整

        :return: The max_length of this CreatePropertyRequestBody.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        r"""Sets the max_length of this CreatePropertyRequestBody.

        字符串最大长度，当data_type为string, datetime, json时必填，自动向下取整

        :param max_length: The max_length of this CreatePropertyRequestBody.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def unit(self):
        r"""Gets the unit of this CreatePropertyRequestBody.

        属性单位

        :return: The unit of this CreatePropertyRequestBody.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this CreatePropertyRequestBody.

        属性单位

        :param unit: The unit of this CreatePropertyRequestBody.
        :type unit: str
        """
        self._unit = unit

    @property
    def enum_list(self):
        r"""Gets the enum_list of this CreatePropertyRequestBody.

        string的枚举值数组，使用逗号分隔

        :return: The enum_list of this CreatePropertyRequestBody.
        :rtype: str
        """
        return self._enum_list

    @enum_list.setter
    def enum_list(self, enum_list):
        r"""Sets the enum_list of this CreatePropertyRequestBody.

        string的枚举值数组，使用逗号分隔

        :param enum_list: The enum_list of this CreatePropertyRequestBody.
        :type enum_list: str
        """
        self._enum_list = enum_list

    @property
    def enum_dict(self):
        r"""Gets the enum_dict of this CreatePropertyRequestBody.

        当数据类型为boolean枚举值时填写json格式数据，形如\"enum_dict\":{\"0\":\"xxx\",\"1\":\"xxx\"}

        :return: The enum_dict of this CreatePropertyRequestBody.
        :rtype: object
        """
        return self._enum_dict

    @enum_dict.setter
    def enum_dict(self, enum_dict):
        r"""Sets the enum_dict of this CreatePropertyRequestBody.

        当数据类型为boolean枚举值时填写json格式数据，形如\"enum_dict\":{\"0\":\"xxx\",\"1\":\"xxx\"}

        :param enum_dict: The enum_dict of this CreatePropertyRequestBody.
        :type enum_dict: object
        """
        self._enum_dict = enum_dict

    @property
    def method(self):
        r"""Gets the method of this CreatePropertyRequestBody.

        访问模式（兼容20.0，R属性可读，W属性可写，E属性可执行）

        :return: The method of this CreatePropertyRequestBody.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        r"""Sets the method of this CreatePropertyRequestBody.

        访问模式（兼容20.0，R属性可读，W属性可写，E属性可执行）

        :param method: The method of this CreatePropertyRequestBody.
        :type method: str
        """
        self._method = method

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
        if not isinstance(other, CreatePropertyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
