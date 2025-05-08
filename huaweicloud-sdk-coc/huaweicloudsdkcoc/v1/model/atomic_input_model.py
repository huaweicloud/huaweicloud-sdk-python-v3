# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AtomicInputModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param_key': 'str',
        'param_name_zh': 'str',
        'param_name_en': 'str',
        'required': 'bool',
        'param_type': 'str',
        'min': 'int',
        'max': 'int',
        'min_len': 'int',
        'max_len': 'int',
        'pattern': 'str'
    }

    attribute_map = {
        'param_key': 'param_key',
        'param_name_zh': 'param_name_zh',
        'param_name_en': 'param_name_en',
        'required': 'required',
        'param_type': 'param_type',
        'min': 'min',
        'max': 'max',
        'min_len': 'min_len',
        'max_len': 'max_len',
        'pattern': 'pattern'
    }

    def __init__(self, param_key=None, param_name_zh=None, param_name_en=None, required=None, param_type=None, min=None, max=None, min_len=None, max_len=None, pattern=None):
        r"""AtomicInputModel

        The model defined in huaweicloud sdk

        :param param_key: 参数变量名，执行时原子能力内引用
        :type param_key: str
        :param param_name_zh: 参数中文名，下拉展示时使用
        :type param_name_zh: str
        :param param_name_en: 参数英文名，下拉展示时使用
        :type param_name_en: str
        :param required: 是否必填
        :type required: bool
        :param param_type: 参数类型：常量/字典
        :type param_type: str
        :param min: 最小值
        :type min: int
        :param max: 最大值
        :type max: int
        :param min_len: 长度最小值
        :type min_len: int
        :param max_len: 长度最大值
        :type max_len: int
        :param pattern: 正则限制表达式
        :type pattern: str
        """
        
        

        self._param_key = None
        self._param_name_zh = None
        self._param_name_en = None
        self._required = None
        self._param_type = None
        self._min = None
        self._max = None
        self._min_len = None
        self._max_len = None
        self._pattern = None
        self.discriminator = None

        if param_key is not None:
            self.param_key = param_key
        if param_name_zh is not None:
            self.param_name_zh = param_name_zh
        if param_name_en is not None:
            self.param_name_en = param_name_en
        if required is not None:
            self.required = required
        if param_type is not None:
            self.param_type = param_type
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if min_len is not None:
            self.min_len = min_len
        if max_len is not None:
            self.max_len = max_len
        if pattern is not None:
            self.pattern = pattern

    @property
    def param_key(self):
        r"""Gets the param_key of this AtomicInputModel.

        参数变量名，执行时原子能力内引用

        :return: The param_key of this AtomicInputModel.
        :rtype: str
        """
        return self._param_key

    @param_key.setter
    def param_key(self, param_key):
        r"""Sets the param_key of this AtomicInputModel.

        参数变量名，执行时原子能力内引用

        :param param_key: The param_key of this AtomicInputModel.
        :type param_key: str
        """
        self._param_key = param_key

    @property
    def param_name_zh(self):
        r"""Gets the param_name_zh of this AtomicInputModel.

        参数中文名，下拉展示时使用

        :return: The param_name_zh of this AtomicInputModel.
        :rtype: str
        """
        return self._param_name_zh

    @param_name_zh.setter
    def param_name_zh(self, param_name_zh):
        r"""Sets the param_name_zh of this AtomicInputModel.

        参数中文名，下拉展示时使用

        :param param_name_zh: The param_name_zh of this AtomicInputModel.
        :type param_name_zh: str
        """
        self._param_name_zh = param_name_zh

    @property
    def param_name_en(self):
        r"""Gets the param_name_en of this AtomicInputModel.

        参数英文名，下拉展示时使用

        :return: The param_name_en of this AtomicInputModel.
        :rtype: str
        """
        return self._param_name_en

    @param_name_en.setter
    def param_name_en(self, param_name_en):
        r"""Sets the param_name_en of this AtomicInputModel.

        参数英文名，下拉展示时使用

        :param param_name_en: The param_name_en of this AtomicInputModel.
        :type param_name_en: str
        """
        self._param_name_en = param_name_en

    @property
    def required(self):
        r"""Gets the required of this AtomicInputModel.

        是否必填

        :return: The required of this AtomicInputModel.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this AtomicInputModel.

        是否必填

        :param required: The required of this AtomicInputModel.
        :type required: bool
        """
        self._required = required

    @property
    def param_type(self):
        r"""Gets the param_type of this AtomicInputModel.

        参数类型：常量/字典

        :return: The param_type of this AtomicInputModel.
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        r"""Sets the param_type of this AtomicInputModel.

        参数类型：常量/字典

        :param param_type: The param_type of this AtomicInputModel.
        :type param_type: str
        """
        self._param_type = param_type

    @property
    def min(self):
        r"""Gets the min of this AtomicInputModel.

        最小值

        :return: The min of this AtomicInputModel.
        :rtype: int
        """
        return self._min

    @min.setter
    def min(self, min):
        r"""Sets the min of this AtomicInputModel.

        最小值

        :param min: The min of this AtomicInputModel.
        :type min: int
        """
        self._min = min

    @property
    def max(self):
        r"""Gets the max of this AtomicInputModel.

        最大值

        :return: The max of this AtomicInputModel.
        :rtype: int
        """
        return self._max

    @max.setter
    def max(self, max):
        r"""Sets the max of this AtomicInputModel.

        最大值

        :param max: The max of this AtomicInputModel.
        :type max: int
        """
        self._max = max

    @property
    def min_len(self):
        r"""Gets the min_len of this AtomicInputModel.

        长度最小值

        :return: The min_len of this AtomicInputModel.
        :rtype: int
        """
        return self._min_len

    @min_len.setter
    def min_len(self, min_len):
        r"""Sets the min_len of this AtomicInputModel.

        长度最小值

        :param min_len: The min_len of this AtomicInputModel.
        :type min_len: int
        """
        self._min_len = min_len

    @property
    def max_len(self):
        r"""Gets the max_len of this AtomicInputModel.

        长度最大值

        :return: The max_len of this AtomicInputModel.
        :rtype: int
        """
        return self._max_len

    @max_len.setter
    def max_len(self, max_len):
        r"""Sets the max_len of this AtomicInputModel.

        长度最大值

        :param max_len: The max_len of this AtomicInputModel.
        :type max_len: int
        """
        self._max_len = max_len

    @property
    def pattern(self):
        r"""Gets the pattern of this AtomicInputModel.

        正则限制表达式

        :return: The pattern of this AtomicInputModel.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        r"""Sets the pattern of this AtomicInputModel.

        正则限制表达式

        :param pattern: The pattern of this AtomicInputModel.
        :type pattern: str
        """
        self._pattern = pattern

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
        if not isinstance(other, AtomicInputModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
