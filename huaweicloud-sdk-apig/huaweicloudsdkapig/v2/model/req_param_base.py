# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqParamBase:


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
        'location': 'str',
        'default_value': 'str',
        'sample_value': 'str',
        'required': 'int',
        'valid_enable': 'int',
        'remark': 'str',
        'enumerations': 'str',
        'min_num': 'int',
        'max_num': 'int',
        'min_size': 'int',
        'max_size': 'int',
        'regular': 'str',
        'json_schema': 'str',
        'pass_through': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'location': 'location',
        'default_value': 'default_value',
        'sample_value': 'sample_value',
        'required': 'required',
        'valid_enable': 'valid_enable',
        'remark': 'remark',
        'enumerations': 'enumerations',
        'min_num': 'min_num',
        'max_num': 'max_num',
        'min_size': 'min_size',
        'max_size': 'max_size',
        'regular': 'regular',
        'json_schema': 'json_schema',
        'pass_through': 'pass_through'
    }

    def __init__(self, name=None, type=None, location=None, default_value=None, sample_value=None, required=None, valid_enable=None, remark=None, enumerations=None, min_num=None, max_num=None, min_size=None, max_size=None, regular=None, json_schema=None, pass_through=None):
        """ReqParamBase - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._type = None
        self._location = None
        self._default_value = None
        self._sample_value = None
        self._required = None
        self._valid_enable = None
        self._remark = None
        self._enumerations = None
        self._min_num = None
        self._max_num = None
        self._min_size = None
        self._max_size = None
        self._regular = None
        self._json_schema = None
        self._pass_through = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.location = location
        if default_value is not None:
            self.default_value = default_value
        if sample_value is not None:
            self.sample_value = sample_value
        if required is not None:
            self.required = required
        if valid_enable is not None:
            self.valid_enable = valid_enable
        if remark is not None:
            self.remark = remark
        if enumerations is not None:
            self.enumerations = enumerations
        if min_num is not None:
            self.min_num = min_num
        if max_num is not None:
            self.max_num = max_num
        if min_size is not None:
            self.min_size = min_size
        if max_size is not None:
            self.max_size = max_size
        if regular is not None:
            self.regular = regular
        if json_schema is not None:
            self.json_schema = json_schema
        if pass_through is not None:
            self.pass_through = pass_through

    @property
    def name(self):
        """Gets the name of this ReqParamBase.

        参数名称。 长度为1 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 

        :return: The name of this ReqParamBase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReqParamBase.

        参数名称。 长度为1 ~ 32位的字符串，字符串由英文字母、数字、中划线、下划线、英文句号组成，且只能以英文开头。 

        :param name: The name of this ReqParamBase.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ReqParamBase.

        参数类型

        :return: The type of this ReqParamBase.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ReqParamBase.

        参数类型

        :param type: The type of this ReqParamBase.
        :type: str
        """
        self._type = type

    @property
    def location(self):
        """Gets the location of this ReqParamBase.

        参数位置

        :return: The location of this ReqParamBase.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this ReqParamBase.

        参数位置

        :param location: The location of this ReqParamBase.
        :type: str
        """
        self._location = location

    @property
    def default_value(self):
        """Gets the default_value of this ReqParamBase.

        参数默认值

        :return: The default_value of this ReqParamBase.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ReqParamBase.

        参数默认值

        :param default_value: The default_value of this ReqParamBase.
        :type: str
        """
        self._default_value = default_value

    @property
    def sample_value(self):
        """Gets the sample_value of this ReqParamBase.

        参数示例值

        :return: The sample_value of this ReqParamBase.
        :rtype: str
        """
        return self._sample_value

    @sample_value.setter
    def sample_value(self, sample_value):
        """Sets the sample_value of this ReqParamBase.

        参数示例值

        :param sample_value: The sample_value of this ReqParamBase.
        :type: str
        """
        self._sample_value = sample_value

    @property
    def required(self):
        """Gets the required of this ReqParamBase.

        是否必须 - 1：是 - 2：否  location为PATH时，required默认为1，其他场景required默认为2

        :return: The required of this ReqParamBase.
        :rtype: int
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this ReqParamBase.

        是否必须 - 1：是 - 2：否  location为PATH时，required默认为1，其他场景required默认为2

        :param required: The required of this ReqParamBase.
        :type: int
        """
        self._required = required

    @property
    def valid_enable(self):
        """Gets the valid_enable of this ReqParamBase.

        是否开启校验 - 1：开启校验 - 2：不开启校验

        :return: The valid_enable of this ReqParamBase.
        :rtype: int
        """
        return self._valid_enable

    @valid_enable.setter
    def valid_enable(self, valid_enable):
        """Sets the valid_enable of this ReqParamBase.

        是否开启校验 - 1：开启校验 - 2：不开启校验

        :param valid_enable: The valid_enable of this ReqParamBase.
        :type: int
        """
        self._valid_enable = valid_enable

    @property
    def remark(self):
        """Gets the remark of this ReqParamBase.

        描述信息。长度不超过255个字符 > 中文字符必须为UTF-8或者unicode编码。

        :return: The remark of this ReqParamBase.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this ReqParamBase.

        描述信息。长度不超过255个字符 > 中文字符必须为UTF-8或者unicode编码。

        :param remark: The remark of this ReqParamBase.
        :type: str
        """
        self._remark = remark

    @property
    def enumerations(self):
        """Gets the enumerations of this ReqParamBase.

        参数枚举值

        :return: The enumerations of this ReqParamBase.
        :rtype: str
        """
        return self._enumerations

    @enumerations.setter
    def enumerations(self, enumerations):
        """Sets the enumerations of this ReqParamBase.

        参数枚举值

        :param enumerations: The enumerations of this ReqParamBase.
        :type: str
        """
        self._enumerations = enumerations

    @property
    def min_num(self):
        """Gets the min_num of this ReqParamBase.

        参数最小值  参数类型为NUMBER时有效

        :return: The min_num of this ReqParamBase.
        :rtype: int
        """
        return self._min_num

    @min_num.setter
    def min_num(self, min_num):
        """Sets the min_num of this ReqParamBase.

        参数最小值  参数类型为NUMBER时有效

        :param min_num: The min_num of this ReqParamBase.
        :type: int
        """
        self._min_num = min_num

    @property
    def max_num(self):
        """Gets the max_num of this ReqParamBase.

        参数最大值  参数类型为NUMBER时有效

        :return: The max_num of this ReqParamBase.
        :rtype: int
        """
        return self._max_num

    @max_num.setter
    def max_num(self, max_num):
        """Sets the max_num of this ReqParamBase.

        参数最大值  参数类型为NUMBER时有效

        :param max_num: The max_num of this ReqParamBase.
        :type: int
        """
        self._max_num = max_num

    @property
    def min_size(self):
        """Gets the min_size of this ReqParamBase.

        参数最小长度  参数类型为STRING时有效

        :return: The min_size of this ReqParamBase.
        :rtype: int
        """
        return self._min_size

    @min_size.setter
    def min_size(self, min_size):
        """Sets the min_size of this ReqParamBase.

        参数最小长度  参数类型为STRING时有效

        :param min_size: The min_size of this ReqParamBase.
        :type: int
        """
        self._min_size = min_size

    @property
    def max_size(self):
        """Gets the max_size of this ReqParamBase.

        参数最大长度  参数类型为STRING时有效

        :return: The max_size of this ReqParamBase.
        :rtype: int
        """
        return self._max_size

    @max_size.setter
    def max_size(self, max_size):
        """Sets the max_size of this ReqParamBase.

        参数最大长度  参数类型为STRING时有效

        :param max_size: The max_size of this ReqParamBase.
        :type: int
        """
        self._max_size = max_size

    @property
    def regular(self):
        """Gets the regular of this ReqParamBase.

        正则校验规则  暂不支持

        :return: The regular of this ReqParamBase.
        :rtype: str
        """
        return self._regular

    @regular.setter
    def regular(self, regular):
        """Sets the regular of this ReqParamBase.

        正则校验规则  暂不支持

        :param regular: The regular of this ReqParamBase.
        :type: str
        """
        self._regular = regular

    @property
    def json_schema(self):
        """Gets the json_schema of this ReqParamBase.

        JSON校验规则  暂不支持

        :return: The json_schema of this ReqParamBase.
        :rtype: str
        """
        return self._json_schema

    @json_schema.setter
    def json_schema(self, json_schema):
        """Sets the json_schema of this ReqParamBase.

        JSON校验规则  暂不支持

        :param json_schema: The json_schema of this ReqParamBase.
        :type: str
        """
        self._json_schema = json_schema

    @property
    def pass_through(self):
        """Gets the pass_through of this ReqParamBase.

        是否透传 - 1：是 - 2：否

        :return: The pass_through of this ReqParamBase.
        :rtype: str
        """
        return self._pass_through

    @pass_through.setter
    def pass_through(self, pass_through):
        """Sets the pass_through of this ReqParamBase.

        是否透传 - 1：是 - 2：否

        :param pass_through: The pass_through of this ReqParamBase.
        :type: str
        """
        self._pass_through = pass_through

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReqParamBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
