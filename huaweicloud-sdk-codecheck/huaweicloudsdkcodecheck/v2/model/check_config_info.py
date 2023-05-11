# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckConfigInfo:

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
        'cfg_key': 'str',
        'default_value': 'str',
        'option_value': 'str',
        'is_required': 'int',
        'description': 'str',
        'type': 'int',
        'status': 'str',
        'value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'cfg_key': 'cfg_key',
        'default_value': 'default_value',
        'option_value': 'option_value',
        'is_required': 'is_required',
        'description': 'description',
        'type': 'type',
        'status': 'status',
        'value': 'value'
    }

    def __init__(self, name=None, cfg_key=None, default_value=None, option_value=None, is_required=None, description=None, type=None, status=None, value=None):
        """CheckConfigInfo

        The model defined in huaweicloud sdk

        :param name: 检查参数名称
        :type name: str
        :param cfg_key: 检查参数对应的key值
        :type cfg_key: str
        :param default_value: 检查参数默认值
        :type default_value: str
        :param option_value: 检查参数可选项
        :type option_value: str
        :param is_required: 0：非必填，1：必填
        :type is_required: int
        :param description: 检查参数说明
        :type description: str
        :param type: 参数类型，0：文本，2：有可选项
        :type type: int
        :param status: 参数状态，on：启用，off：未启用
        :type status: str
        :param value: 检查参数值
        :type value: str
        """
        
        

        self._name = None
        self._cfg_key = None
        self._default_value = None
        self._option_value = None
        self._is_required = None
        self._description = None
        self._type = None
        self._status = None
        self._value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if cfg_key is not None:
            self.cfg_key = cfg_key
        if default_value is not None:
            self.default_value = default_value
        if option_value is not None:
            self.option_value = option_value
        if is_required is not None:
            self.is_required = is_required
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if value is not None:
            self.value = value

    @property
    def name(self):
        """Gets the name of this CheckConfigInfo.

        检查参数名称

        :return: The name of this CheckConfigInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CheckConfigInfo.

        检查参数名称

        :param name: The name of this CheckConfigInfo.
        :type name: str
        """
        self._name = name

    @property
    def cfg_key(self):
        """Gets the cfg_key of this CheckConfigInfo.

        检查参数对应的key值

        :return: The cfg_key of this CheckConfigInfo.
        :rtype: str
        """
        return self._cfg_key

    @cfg_key.setter
    def cfg_key(self, cfg_key):
        """Sets the cfg_key of this CheckConfigInfo.

        检查参数对应的key值

        :param cfg_key: The cfg_key of this CheckConfigInfo.
        :type cfg_key: str
        """
        self._cfg_key = cfg_key

    @property
    def default_value(self):
        """Gets the default_value of this CheckConfigInfo.

        检查参数默认值

        :return: The default_value of this CheckConfigInfo.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this CheckConfigInfo.

        检查参数默认值

        :param default_value: The default_value of this CheckConfigInfo.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def option_value(self):
        """Gets the option_value of this CheckConfigInfo.

        检查参数可选项

        :return: The option_value of this CheckConfigInfo.
        :rtype: str
        """
        return self._option_value

    @option_value.setter
    def option_value(self, option_value):
        """Sets the option_value of this CheckConfigInfo.

        检查参数可选项

        :param option_value: The option_value of this CheckConfigInfo.
        :type option_value: str
        """
        self._option_value = option_value

    @property
    def is_required(self):
        """Gets the is_required of this CheckConfigInfo.

        0：非必填，1：必填

        :return: The is_required of this CheckConfigInfo.
        :rtype: int
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this CheckConfigInfo.

        0：非必填，1：必填

        :param is_required: The is_required of this CheckConfigInfo.
        :type is_required: int
        """
        self._is_required = is_required

    @property
    def description(self):
        """Gets the description of this CheckConfigInfo.

        检查参数说明

        :return: The description of this CheckConfigInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CheckConfigInfo.

        检查参数说明

        :param description: The description of this CheckConfigInfo.
        :type description: str
        """
        self._description = description

    @property
    def type(self):
        """Gets the type of this CheckConfigInfo.

        参数类型，0：文本，2：有可选项

        :return: The type of this CheckConfigInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CheckConfigInfo.

        参数类型，0：文本，2：有可选项

        :param type: The type of this CheckConfigInfo.
        :type type: int
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this CheckConfigInfo.

        参数状态，on：启用，off：未启用

        :return: The status of this CheckConfigInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CheckConfigInfo.

        参数状态，on：启用，off：未启用

        :param status: The status of this CheckConfigInfo.
        :type status: str
        """
        self._status = status

    @property
    def value(self):
        """Gets the value of this CheckConfigInfo.

        检查参数值

        :return: The value of this CheckConfigInfo.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CheckConfigInfo.

        检查参数值

        :param value: The value of this CheckConfigInfo.
        :type value: str
        """
        self._value = value

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
        if not isinstance(other, CheckConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
