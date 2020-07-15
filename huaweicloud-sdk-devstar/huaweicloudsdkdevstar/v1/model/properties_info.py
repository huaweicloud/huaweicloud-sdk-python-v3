# coding: utf-8

import pprint
import re

import six





class PropertiesInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'default_value': 'str',
        'label': 'str',
        'type': 'str',
        'help_text': 'str',
        'read_only': 'bool',
        'required': 'bool',
        'reg_type': 'str',
        'reg_pattern': 'str',
        'reg_tip': 'str',
        'is_show': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'default_value': 'defaultValue',
        'label': 'label',
        'type': 'type',
        'help_text': 'helpText',
        'read_only': 'readOnly',
        'required': 'required',
        'reg_type': 'regType',
        'reg_pattern': 'regPattern',
        'reg_tip': 'regTip',
        'is_show': 'isShow'
    }

    def __init__(self, key=None, default_value=None, label=None, type=None, help_text=None, read_only=None, required=None, reg_type=None, reg_pattern=None, reg_tip=None, is_show=None):
        """PropertiesInfo - a model defined in huaweicloud sdk"""
        
        

        self._key = None
        self._default_value = None
        self._label = None
        self._type = None
        self._help_text = None
        self._read_only = None
        self._required = None
        self._reg_type = None
        self._reg_pattern = None
        self._reg_tip = None
        self._is_show = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if default_value is not None:
            self.default_value = default_value
        if label is not None:
            self.label = label
        if type is not None:
            self.type = type
        if help_text is not None:
            self.help_text = help_text
        if read_only is not None:
            self.read_only = read_only
        if required is not None:
            self.required = required
        if reg_type is not None:
            self.reg_type = reg_type
        if reg_pattern is not None:
            self.reg_pattern = reg_pattern
        if reg_tip is not None:
            self.reg_tip = reg_tip
        if is_show is not None:
            self.is_show = is_show

    @property
    def key(self):
        """Gets the key of this PropertiesInfo.

        key

        :return: The key of this PropertiesInfo.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this PropertiesInfo.

        key

        :param key: The key of this PropertiesInfo.
        :type: str
        """
        self._key = key

    @property
    def default_value(self):
        """Gets the default_value of this PropertiesInfo.

        默认值

        :return: The default_value of this PropertiesInfo.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this PropertiesInfo.

        默认值

        :param default_value: The default_value of this PropertiesInfo.
        :type: str
        """
        self._default_value = default_value

    @property
    def label(self):
        """Gets the label of this PropertiesInfo.

        模板的描述信息

        :return: The label of this PropertiesInfo.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this PropertiesInfo.

        模板的描述信息

        :param label: The label of this PropertiesInfo.
        :type: str
        """
        self._label = label

    @property
    def type(self):
        """Gets the type of this PropertiesInfo.

        类型 txet 或 select

        :return: The type of this PropertiesInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PropertiesInfo.

        类型 txet 或 select

        :param type: The type of this PropertiesInfo.
        :type: str
        """
        self._type = type

    @property
    def help_text(self):
        """Gets the help_text of this PropertiesInfo.

        提示信息

        :return: The help_text of this PropertiesInfo.
        :rtype: str
        """
        return self._help_text

    @help_text.setter
    def help_text(self, help_text):
        """Sets the help_text of this PropertiesInfo.

        提示信息

        :param help_text: The help_text of this PropertiesInfo.
        :type: str
        """
        self._help_text = help_text

    @property
    def read_only(self):
        """Gets the read_only of this PropertiesInfo.

        是否只读

        :return: The read_only of this PropertiesInfo.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this PropertiesInfo.

        是否只读

        :param read_only: The read_only of this PropertiesInfo.
        :type: bool
        """
        self._read_only = read_only

    @property
    def required(self):
        """Gets the required of this PropertiesInfo.

        是否必填

        :return: The required of this PropertiesInfo.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this PropertiesInfo.

        是否必填

        :param required: The required of this PropertiesInfo.
        :type: bool
        """
        self._required = required

    @property
    def reg_type(self):
        """Gets the reg_type of this PropertiesInfo.

        正则校验类型

        :return: The reg_type of this PropertiesInfo.
        :rtype: str
        """
        return self._reg_type

    @reg_type.setter
    def reg_type(self, reg_type):
        """Sets the reg_type of this PropertiesInfo.

        正则校验类型

        :param reg_type: The reg_type of this PropertiesInfo.
        :type: str
        """
        self._reg_type = reg_type

    @property
    def reg_pattern(self):
        """Gets the reg_pattern of this PropertiesInfo.

        正则表达式

        :return: The reg_pattern of this PropertiesInfo.
        :rtype: str
        """
        return self._reg_pattern

    @reg_pattern.setter
    def reg_pattern(self, reg_pattern):
        """Sets the reg_pattern of this PropertiesInfo.

        正则表达式

        :param reg_pattern: The reg_pattern of this PropertiesInfo.
        :type: str
        """
        self._reg_pattern = reg_pattern

    @property
    def reg_tip(self):
        """Gets the reg_tip of this PropertiesInfo.

        正则提示信息

        :return: The reg_tip of this PropertiesInfo.
        :rtype: str
        """
        return self._reg_tip

    @reg_tip.setter
    def reg_tip(self, reg_tip):
        """Sets the reg_tip of this PropertiesInfo.

        正则提示信息

        :param reg_tip: The reg_tip of this PropertiesInfo.
        :type: str
        """
        self._reg_tip = reg_tip

    @property
    def is_show(self):
        """Gets the is_show of this PropertiesInfo.

        是否显示

        :return: The is_show of this PropertiesInfo.
        :rtype: bool
        """
        return self._is_show

    @is_show.setter
    def is_show(self, is_show):
        """Sets the is_show of this PropertiesInfo.

        是否显示

        :param is_show: The is_show of this PropertiesInfo.
        :type: bool
        """
        self._is_show = is_show

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PropertiesInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
