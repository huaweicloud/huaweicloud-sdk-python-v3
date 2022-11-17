# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePropertyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'property_id': 'int',
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
        'enum_dict': 'PropertyDataEnum',
        'method': 'str'
    }

    attribute_map = {
        'property_id': 'property_id',
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

    def __init__(self, property_id=None, property_name=None, description=None, data_type=None, required=None, min=None, max=None, step=None, max_length=None, unit=None, enum_list=None, enum_dict=None, method=None):
        """UpdatePropertyResponse

        The model defined in huaweicloud sdk

        :param property_id: 属性ID
        :type property_id: int
        :param property_name: 属性名称，首位必须为字母，支持大小写字母，数字，中划线及下划线，长度2-50
        :type property_name: str
        :param description: 属性描述，长度0-200
        :type description: str
        :param data_type: 属性数据类型，boolean枚举值大小写敏感；number格式为数字，范围±1.0 x 10^-28 to ±7.9228 x 10^28；string为字符串；integer为整数；datetime为时间，格式为yyyyMMddTHHmmss；json为自定义json格式; array为数组类型
        :type data_type: str
        :param required: 是否必填 0-非必填 1-必填
        :type required: int
        :param min: 最小值，当data_type为integer或number时有效
        :type min: str
        :param max: 最大值，当data_type为integer或number时有效
        :type max: str
        :param step: 步长，当data_type为integer或number时有效
        :type step: str
        :param max_length: 字符串最大长度，当data_type为string, datetime, json时有效
        :type max_length: int
        :param unit: 属性单位
        :type unit: str
        :param enum_list: string的枚举值数组，使用逗号分隔
        :type enum_list: str
        :param enum_dict: 
        :type enum_dict: :class:`huaweicloudsdkroma.v2.PropertyDataEnum`
        :param method: 访问模式（兼容20.0，R属性可读，W属性可写，E属性可执行）
        :type method: str
        """
        
        super(UpdatePropertyResponse, self).__init__()

        self._property_id = None
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

        if property_id is not None:
            self.property_id = property_id
        if property_name is not None:
            self.property_name = property_name
        if description is not None:
            self.description = description
        if data_type is not None:
            self.data_type = data_type
        if required is not None:
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
    def property_id(self):
        """Gets the property_id of this UpdatePropertyResponse.

        属性ID

        :return: The property_id of this UpdatePropertyResponse.
        :rtype: int
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this UpdatePropertyResponse.

        属性ID

        :param property_id: The property_id of this UpdatePropertyResponse.
        :type property_id: int
        """
        self._property_id = property_id

    @property
    def property_name(self):
        """Gets the property_name of this UpdatePropertyResponse.

        属性名称，首位必须为字母，支持大小写字母，数字，中划线及下划线，长度2-50

        :return: The property_name of this UpdatePropertyResponse.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this UpdatePropertyResponse.

        属性名称，首位必须为字母，支持大小写字母，数字，中划线及下划线，长度2-50

        :param property_name: The property_name of this UpdatePropertyResponse.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def description(self):
        """Gets the description of this UpdatePropertyResponse.

        属性描述，长度0-200

        :return: The description of this UpdatePropertyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdatePropertyResponse.

        属性描述，长度0-200

        :param description: The description of this UpdatePropertyResponse.
        :type description: str
        """
        self._description = description

    @property
    def data_type(self):
        """Gets the data_type of this UpdatePropertyResponse.

        属性数据类型，boolean枚举值大小写敏感；number格式为数字，范围±1.0 x 10^-28 to ±7.9228 x 10^28；string为字符串；integer为整数；datetime为时间，格式为yyyyMMddTHHmmss；json为自定义json格式; array为数组类型

        :return: The data_type of this UpdatePropertyResponse.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this UpdatePropertyResponse.

        属性数据类型，boolean枚举值大小写敏感；number格式为数字，范围±1.0 x 10^-28 to ±7.9228 x 10^28；string为字符串；integer为整数；datetime为时间，格式为yyyyMMddTHHmmss；json为自定义json格式; array为数组类型

        :param data_type: The data_type of this UpdatePropertyResponse.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def required(self):
        """Gets the required of this UpdatePropertyResponse.

        是否必填 0-非必填 1-必填

        :return: The required of this UpdatePropertyResponse.
        :rtype: int
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this UpdatePropertyResponse.

        是否必填 0-非必填 1-必填

        :param required: The required of this UpdatePropertyResponse.
        :type required: int
        """
        self._required = required

    @property
    def min(self):
        """Gets the min of this UpdatePropertyResponse.

        最小值，当data_type为integer或number时有效

        :return: The min of this UpdatePropertyResponse.
        :rtype: str
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this UpdatePropertyResponse.

        最小值，当data_type为integer或number时有效

        :param min: The min of this UpdatePropertyResponse.
        :type min: str
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this UpdatePropertyResponse.

        最大值，当data_type为integer或number时有效

        :return: The max of this UpdatePropertyResponse.
        :rtype: str
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this UpdatePropertyResponse.

        最大值，当data_type为integer或number时有效

        :param max: The max of this UpdatePropertyResponse.
        :type max: str
        """
        self._max = max

    @property
    def step(self):
        """Gets the step of this UpdatePropertyResponse.

        步长，当data_type为integer或number时有效

        :return: The step of this UpdatePropertyResponse.
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this UpdatePropertyResponse.

        步长，当data_type为integer或number时有效

        :param step: The step of this UpdatePropertyResponse.
        :type step: str
        """
        self._step = step

    @property
    def max_length(self):
        """Gets the max_length of this UpdatePropertyResponse.

        字符串最大长度，当data_type为string, datetime, json时有效

        :return: The max_length of this UpdatePropertyResponse.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this UpdatePropertyResponse.

        字符串最大长度，当data_type为string, datetime, json时有效

        :param max_length: The max_length of this UpdatePropertyResponse.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def unit(self):
        """Gets the unit of this UpdatePropertyResponse.

        属性单位

        :return: The unit of this UpdatePropertyResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this UpdatePropertyResponse.

        属性单位

        :param unit: The unit of this UpdatePropertyResponse.
        :type unit: str
        """
        self._unit = unit

    @property
    def enum_list(self):
        """Gets the enum_list of this UpdatePropertyResponse.

        string的枚举值数组，使用逗号分隔

        :return: The enum_list of this UpdatePropertyResponse.
        :rtype: str
        """
        return self._enum_list

    @enum_list.setter
    def enum_list(self, enum_list):
        """Sets the enum_list of this UpdatePropertyResponse.

        string的枚举值数组，使用逗号分隔

        :param enum_list: The enum_list of this UpdatePropertyResponse.
        :type enum_list: str
        """
        self._enum_list = enum_list

    @property
    def enum_dict(self):
        """Gets the enum_dict of this UpdatePropertyResponse.

        :return: The enum_dict of this UpdatePropertyResponse.
        :rtype: :class:`huaweicloudsdkroma.v2.PropertyDataEnum`
        """
        return self._enum_dict

    @enum_dict.setter
    def enum_dict(self, enum_dict):
        """Sets the enum_dict of this UpdatePropertyResponse.

        :param enum_dict: The enum_dict of this UpdatePropertyResponse.
        :type enum_dict: :class:`huaweicloudsdkroma.v2.PropertyDataEnum`
        """
        self._enum_dict = enum_dict

    @property
    def method(self):
        """Gets the method of this UpdatePropertyResponse.

        访问模式（兼容20.0，R属性可读，W属性可写，E属性可执行）

        :return: The method of this UpdatePropertyResponse.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this UpdatePropertyResponse.

        访问模式（兼容20.0，R属性可读，W属性可写，E属性可执行）

        :param method: The method of this UpdatePropertyResponse.
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
        if not isinstance(other, UpdatePropertyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
