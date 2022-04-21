# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRequestPropertyResponse(SdkResponse):

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
        'enum_list': 'str'
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
        'enum_list': 'enum_list'
    }

    def __init__(self, property_id=None, property_name=None, description=None, data_type=None, required=None, min=None, max=None, step=None, max_length=None, unit=None, enum_list=None):
        """ShowRequestPropertyResponse

        The model defined in huaweicloud sdk

        :param property_id: 属性ID
        :type property_id: int
        :param property_name: 属性名称，首位必须为字母，支持大小写字母，数字，中划线及下划线，长度2-50
        :type property_name: str
        :param description: 属性描述，长度0-200
        :type description: str
        :param data_type: 属性数据类型，枚举值大小写敏感；number格式为数字，范围±1.0 x 10^-28 to ±7.9228 x 10^28；sting为字符串；integer为整数；datetime为时间，格式为yyyyMMddTHHmmss；json为自定义json格式
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
        """
        
        super(ShowRequestPropertyResponse, self).__init__()

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

    @property
    def property_id(self):
        """Gets the property_id of this ShowRequestPropertyResponse.

        属性ID

        :return: The property_id of this ShowRequestPropertyResponse.
        :rtype: int
        """
        return self._property_id

    @property_id.setter
    def property_id(self, property_id):
        """Sets the property_id of this ShowRequestPropertyResponse.

        属性ID

        :param property_id: The property_id of this ShowRequestPropertyResponse.
        :type property_id: int
        """
        self._property_id = property_id

    @property
    def property_name(self):
        """Gets the property_name of this ShowRequestPropertyResponse.

        属性名称，首位必须为字母，支持大小写字母，数字，中划线及下划线，长度2-50

        :return: The property_name of this ShowRequestPropertyResponse.
        :rtype: str
        """
        return self._property_name

    @property_name.setter
    def property_name(self, property_name):
        """Sets the property_name of this ShowRequestPropertyResponse.

        属性名称，首位必须为字母，支持大小写字母，数字，中划线及下划线，长度2-50

        :param property_name: The property_name of this ShowRequestPropertyResponse.
        :type property_name: str
        """
        self._property_name = property_name

    @property
    def description(self):
        """Gets the description of this ShowRequestPropertyResponse.

        属性描述，长度0-200

        :return: The description of this ShowRequestPropertyResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowRequestPropertyResponse.

        属性描述，长度0-200

        :param description: The description of this ShowRequestPropertyResponse.
        :type description: str
        """
        self._description = description

    @property
    def data_type(self):
        """Gets the data_type of this ShowRequestPropertyResponse.

        属性数据类型，枚举值大小写敏感；number格式为数字，范围±1.0 x 10^-28 to ±7.9228 x 10^28；sting为字符串；integer为整数；datetime为时间，格式为yyyyMMddTHHmmss；json为自定义json格式

        :return: The data_type of this ShowRequestPropertyResponse.
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ShowRequestPropertyResponse.

        属性数据类型，枚举值大小写敏感；number格式为数字，范围±1.0 x 10^-28 to ±7.9228 x 10^28；sting为字符串；integer为整数；datetime为时间，格式为yyyyMMddTHHmmss；json为自定义json格式

        :param data_type: The data_type of this ShowRequestPropertyResponse.
        :type data_type: str
        """
        self._data_type = data_type

    @property
    def required(self):
        """Gets the required of this ShowRequestPropertyResponse.

        是否必填 0-非必填 1-必填

        :return: The required of this ShowRequestPropertyResponse.
        :rtype: int
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ShowRequestPropertyResponse.

        是否必填 0-非必填 1-必填

        :param required: The required of this ShowRequestPropertyResponse.
        :type required: int
        """
        self._required = required

    @property
    def min(self):
        """Gets the min of this ShowRequestPropertyResponse.

        最小值，当data_type为integer或number时有效

        :return: The min of this ShowRequestPropertyResponse.
        :rtype: str
        """
        return self._min

    @min.setter
    def min(self, min):
        """Sets the min of this ShowRequestPropertyResponse.

        最小值，当data_type为integer或number时有效

        :param min: The min of this ShowRequestPropertyResponse.
        :type min: str
        """
        self._min = min

    @property
    def max(self):
        """Gets the max of this ShowRequestPropertyResponse.

        最大值，当data_type为integer或number时有效

        :return: The max of this ShowRequestPropertyResponse.
        :rtype: str
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this ShowRequestPropertyResponse.

        最大值，当data_type为integer或number时有效

        :param max: The max of this ShowRequestPropertyResponse.
        :type max: str
        """
        self._max = max

    @property
    def step(self):
        """Gets the step of this ShowRequestPropertyResponse.

        步长，当data_type为integer或number时有效

        :return: The step of this ShowRequestPropertyResponse.
        :rtype: str
        """
        return self._step

    @step.setter
    def step(self, step):
        """Sets the step of this ShowRequestPropertyResponse.

        步长，当data_type为integer或number时有效

        :param step: The step of this ShowRequestPropertyResponse.
        :type step: str
        """
        self._step = step

    @property
    def max_length(self):
        """Gets the max_length of this ShowRequestPropertyResponse.

        字符串最大长度，当data_type为string, datetime, json时有效

        :return: The max_length of this ShowRequestPropertyResponse.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this ShowRequestPropertyResponse.

        字符串最大长度，当data_type为string, datetime, json时有效

        :param max_length: The max_length of this ShowRequestPropertyResponse.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def unit(self):
        """Gets the unit of this ShowRequestPropertyResponse.

        属性单位

        :return: The unit of this ShowRequestPropertyResponse.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ShowRequestPropertyResponse.

        属性单位

        :param unit: The unit of this ShowRequestPropertyResponse.
        :type unit: str
        """
        self._unit = unit

    @property
    def enum_list(self):
        """Gets the enum_list of this ShowRequestPropertyResponse.

        string的枚举值数组，使用逗号分隔

        :return: The enum_list of this ShowRequestPropertyResponse.
        :rtype: str
        """
        return self._enum_list

    @enum_list.setter
    def enum_list(self, enum_list):
        """Sets the enum_list of this ShowRequestPropertyResponse.

        string的枚举值数组，使用逗号分隔

        :param enum_list: The enum_list of this ShowRequestPropertyResponse.
        :type enum_list: str
        """
        self._enum_list = enum_list

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
        if not isinstance(other, ShowRequestPropertyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
