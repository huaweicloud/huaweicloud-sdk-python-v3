# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ParameterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'default_value': 'str',
        'value_type': 'str',
        'running_value': 'str',
        'unit': 'str',
        'reboot': 'bool',
        'value_range': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'default_value': 'default_value',
        'value_type': 'value_type',
        'running_value': 'running_value',
        'unit': 'unit',
        'reboot': 'reboot',
        'value_range': 'value_range',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, default_value=None, value_type=None, running_value=None, unit=None, reboot=None, value_range=None, description=None):
        """ParameterInfo

        The model defined in huaweicloud sdk

        :param id: 参数ID
        :type id: str
        :param name: 配置名称
        :type name: str
        :param default_value: 默认值
        :type default_value: str
        :param value_type: 配置值类型
        :type value_type: str
        :param running_value: 集群当前运行的配置值
        :type running_value: str
        :param unit: 单位
        :type unit: str
        :param reboot: 是否需要重启生效
        :type reboot: bool
        :param value_range: 配置值取值范围
        :type value_range: str
        :param description: 配置描述信息
        :type description: str
        """
        
        

        self._id = None
        self._name = None
        self._default_value = None
        self._value_type = None
        self._running_value = None
        self._unit = None
        self._reboot = None
        self._value_range = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        self.default_value = default_value
        self.value_type = value_type
        self.running_value = running_value
        self.unit = unit
        self.reboot = reboot
        self.value_range = value_range
        self.description = description

    @property
    def id(self):
        """Gets the id of this ParameterInfo.

        参数ID

        :return: The id of this ParameterInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ParameterInfo.

        参数ID

        :param id: The id of this ParameterInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ParameterInfo.

        配置名称

        :return: The name of this ParameterInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ParameterInfo.

        配置名称

        :param name: The name of this ParameterInfo.
        :type name: str
        """
        self._name = name

    @property
    def default_value(self):
        """Gets the default_value of this ParameterInfo.

        默认值

        :return: The default_value of this ParameterInfo.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this ParameterInfo.

        默认值

        :param default_value: The default_value of this ParameterInfo.
        :type default_value: str
        """
        self._default_value = default_value

    @property
    def value_type(self):
        """Gets the value_type of this ParameterInfo.

        配置值类型

        :return: The value_type of this ParameterInfo.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ParameterInfo.

        配置值类型

        :param value_type: The value_type of this ParameterInfo.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def running_value(self):
        """Gets the running_value of this ParameterInfo.

        集群当前运行的配置值

        :return: The running_value of this ParameterInfo.
        :rtype: str
        """
        return self._running_value

    @running_value.setter
    def running_value(self, running_value):
        """Sets the running_value of this ParameterInfo.

        集群当前运行的配置值

        :param running_value: The running_value of this ParameterInfo.
        :type running_value: str
        """
        self._running_value = running_value

    @property
    def unit(self):
        """Gets the unit of this ParameterInfo.

        单位

        :return: The unit of this ParameterInfo.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this ParameterInfo.

        单位

        :param unit: The unit of this ParameterInfo.
        :type unit: str
        """
        self._unit = unit

    @property
    def reboot(self):
        """Gets the reboot of this ParameterInfo.

        是否需要重启生效

        :return: The reboot of this ParameterInfo.
        :rtype: bool
        """
        return self._reboot

    @reboot.setter
    def reboot(self, reboot):
        """Sets the reboot of this ParameterInfo.

        是否需要重启生效

        :param reboot: The reboot of this ParameterInfo.
        :type reboot: bool
        """
        self._reboot = reboot

    @property
    def value_range(self):
        """Gets the value_range of this ParameterInfo.

        配置值取值范围

        :return: The value_range of this ParameterInfo.
        :rtype: str
        """
        return self._value_range

    @value_range.setter
    def value_range(self, value_range):
        """Sets the value_range of this ParameterInfo.

        配置值取值范围

        :param value_range: The value_range of this ParameterInfo.
        :type value_range: str
        """
        self._value_range = value_range

    @property
    def description(self):
        """Gets the description of this ParameterInfo.

        配置描述信息

        :return: The description of this ParameterInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ParameterInfo.

        配置描述信息

        :param description: The description of this ParameterInfo.
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
        if not isinstance(other, ParameterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
