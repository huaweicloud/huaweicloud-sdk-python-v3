# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtendsParamV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tips': 'str',
        'required': 'int',
        'length': 'int',
        'language': 'str',
        'param_key': 'str',
        'param_name': 'str',
        'param_type': 'int',
        'param_desc': 'str',
        'default_value': 'str',
        'max_value': 'int',
        'min_value': 'int',
        'select_item': 'str',
        'is_show': 'int',
        'is_sensitive': 'int'
    }

    attribute_map = {
        'tips': 'tips',
        'required': 'required',
        'length': 'length',
        'language': 'language',
        'param_key': 'param_key',
        'param_name': 'param_name',
        'param_type': 'param_type',
        'param_desc': 'param_desc',
        'default_value': 'default_value',
        'max_value': 'max_value',
        'min_value': 'min_value',
        'select_item': 'select_item',
        'is_show': 'is_show',
        'is_sensitive': 'is_sensitive'
    }

    def __init__(self, tips=None, required=None, length=None, language=None, param_key=None, param_name=None, param_type=None, param_desc=None, default_value=None, max_value=None, min_value=None, select_item=None, is_show=None, is_sensitive=None):
        r"""ExtendsParamV2

        The model defined in huaweicloud sdk

        :param tips: 提示
        :type tips: str
        :param required: 是否必填
        :type required: int
        :param length: 限制长度
        :type length: int
        :param language: 语言
        :type language: str
        :param param_key: 参数标识
        :type param_key: str
        :param param_name: 参数名称
        :type param_name: str
        :param param_type: 参数类型
        :type param_type: int
        :param param_desc: 参数描述
        :type param_desc: str
        :param default_value: 默认值
        :type default_value: str
        :param max_value: 最大值
        :type max_value: int
        :param min_value: 最小值
        :type min_value: int
        :param select_item: 选项值
        :type select_item: str
        :param is_show: 是否展示
        :type is_show: int
        :param is_sensitive: 是否敏感
        :type is_sensitive: int
        """
        
        

        self._tips = None
        self._required = None
        self._length = None
        self._language = None
        self._param_key = None
        self._param_name = None
        self._param_type = None
        self._param_desc = None
        self._default_value = None
        self._max_value = None
        self._min_value = None
        self._select_item = None
        self._is_show = None
        self._is_sensitive = None
        self.discriminator = None

        if tips is not None:
            self.tips = tips
        if required is not None:
            self.required = required
        if length is not None:
            self.length = length
        if language is not None:
            self.language = language
        if param_key is not None:
            self.param_key = param_key
        if param_name is not None:
            self.param_name = param_name
        if param_type is not None:
            self.param_type = param_type
        if param_desc is not None:
            self.param_desc = param_desc
        if default_value is not None:
            self.default_value = default_value
        if max_value is not None:
            self.max_value = max_value
        if min_value is not None:
            self.min_value = min_value
        if select_item is not None:
            self.select_item = select_item
        if is_show is not None:
            self.is_show = is_show
        if is_sensitive is not None:
            self.is_sensitive = is_sensitive

    @property
    def tips(self):
        r"""Gets the tips of this ExtendsParamV2.

        提示

        :return: The tips of this ExtendsParamV2.
        :rtype: str
        """
        return self._tips

    @tips.setter
    def tips(self, tips):
        r"""Sets the tips of this ExtendsParamV2.

        提示

        :param tips: The tips of this ExtendsParamV2.
        :type tips: str
        """
        self._tips = tips

    @property
    def required(self):
        r"""Gets the required of this ExtendsParamV2.

        是否必填

        :return: The required of this ExtendsParamV2.
        :rtype: int
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this ExtendsParamV2.

        是否必填

        :param required: The required of this ExtendsParamV2.
        :type required: int
        """
        self._required = required

    @property
    def length(self):
        r"""Gets the length of this ExtendsParamV2.

        限制长度

        :return: The length of this ExtendsParamV2.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        r"""Sets the length of this ExtendsParamV2.

        限制长度

        :param length: The length of this ExtendsParamV2.
        :type length: int
        """
        self._length = length

    @property
    def language(self):
        r"""Gets the language of this ExtendsParamV2.

        语言

        :return: The language of this ExtendsParamV2.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this ExtendsParamV2.

        语言

        :param language: The language of this ExtendsParamV2.
        :type language: str
        """
        self._language = language

    @property
    def param_key(self):
        r"""Gets the param_key of this ExtendsParamV2.

        参数标识

        :return: The param_key of this ExtendsParamV2.
        :rtype: str
        """
        return self._param_key

    @param_key.setter
    def param_key(self, param_key):
        r"""Sets the param_key of this ExtendsParamV2.

        参数标识

        :param param_key: The param_key of this ExtendsParamV2.
        :type param_key: str
        """
        self._param_key = param_key

    @property
    def param_name(self):
        r"""Gets the param_name of this ExtendsParamV2.

        参数名称

        :return: The param_name of this ExtendsParamV2.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        r"""Sets the param_name of this ExtendsParamV2.

        参数名称

        :param param_name: The param_name of this ExtendsParamV2.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def param_type(self):
        r"""Gets the param_type of this ExtendsParamV2.

        参数类型

        :return: The param_type of this ExtendsParamV2.
        :rtype: int
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        r"""Sets the param_type of this ExtendsParamV2.

        参数类型

        :param param_type: The param_type of this ExtendsParamV2.
        :type param_type: int
        """
        self._param_type = param_type

    @property
    def param_desc(self):
        r"""Gets the param_desc of this ExtendsParamV2.

        参数描述

        :return: The param_desc of this ExtendsParamV2.
        :rtype: str
        """
        return self._param_desc

    @param_desc.setter
    def param_desc(self, param_desc):
        r"""Sets the param_desc of this ExtendsParamV2.

        参数描述

        :param param_desc: The param_desc of this ExtendsParamV2.
        :type param_desc: str
        """
        self._param_desc = param_desc

    @property
    def default_value(self):
        r"""Gets the default_value of this ExtendsParamV2.

        默认值

        :return: The default_value of this ExtendsParamV2.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        r"""Sets the default_value of this ExtendsParamV2.

        默认值

        :param default_value: The default_value of this ExtendsParamV2.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def max_value(self):
        r"""Gets the max_value of this ExtendsParamV2.

        最大值

        :return: The max_value of this ExtendsParamV2.
        :rtype: int
        """
        return self._max_value

    @max_value.setter
    def max_value(self, max_value):
        r"""Sets the max_value of this ExtendsParamV2.

        最大值

        :param max_value: The max_value of this ExtendsParamV2.
        :type max_value: int
        """
        self._max_value = max_value

    @property
    def min_value(self):
        r"""Gets the min_value of this ExtendsParamV2.

        最小值

        :return: The min_value of this ExtendsParamV2.
        :rtype: int
        """
        return self._min_value

    @min_value.setter
    def min_value(self, min_value):
        r"""Sets the min_value of this ExtendsParamV2.

        最小值

        :param min_value: The min_value of this ExtendsParamV2.
        :type min_value: int
        """
        self._min_value = min_value

    @property
    def select_item(self):
        r"""Gets the select_item of this ExtendsParamV2.

        选项值

        :return: The select_item of this ExtendsParamV2.
        :rtype: str
        """
        return self._select_item

    @select_item.setter
    def select_item(self, select_item):
        r"""Sets the select_item of this ExtendsParamV2.

        选项值

        :param select_item: The select_item of this ExtendsParamV2.
        :type select_item: str
        """
        self._select_item = select_item

    @property
    def is_show(self):
        r"""Gets the is_show of this ExtendsParamV2.

        是否展示

        :return: The is_show of this ExtendsParamV2.
        :rtype: int
        """
        return self._is_show

    @is_show.setter
    def is_show(self, is_show):
        r"""Sets the is_show of this ExtendsParamV2.

        是否展示

        :param is_show: The is_show of this ExtendsParamV2.
        :type is_show: int
        """
        self._is_show = is_show

    @property
    def is_sensitive(self):
        r"""Gets the is_sensitive of this ExtendsParamV2.

        是否敏感

        :return: The is_sensitive of this ExtendsParamV2.
        :rtype: int
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        r"""Sets the is_sensitive of this ExtendsParamV2.

        是否敏感

        :param is_sensitive: The is_sensitive of this ExtendsParamV2.
        :type is_sensitive: int
        """
        self._is_sensitive = is_sensitive

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
        if not isinstance(other, ExtendsParamV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
