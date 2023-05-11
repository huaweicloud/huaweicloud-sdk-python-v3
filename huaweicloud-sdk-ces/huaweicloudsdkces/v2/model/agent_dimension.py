# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentDimension:

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
        'value': 'str',
        'origin_value': 'str'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'origin_value': 'origin_value'
    }

    def __init__(self, name=None, value=None, origin_value=None):
        """AgentDimension

        The model defined in huaweicloud sdk

        :param name: 维度名称，枚举类型，类型有：   mount_point：挂载点，   disk：磁盘，   proc：进程，   gpu：显卡，   raid: RAID控制器
        :type name: str
        :param value: 维度值，32位字符串，如：2e84018fc8b4484b94e89aae212fe615
        :type value: str
        :param origin_value: 实际维度信息，字符串，如：vda。
        :type origin_value: str
        """
        
        

        self._name = None
        self._value = None
        self._origin_value = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if origin_value is not None:
            self.origin_value = origin_value

    @property
    def name(self):
        """Gets the name of this AgentDimension.

        维度名称，枚举类型，类型有：   mount_point：挂载点，   disk：磁盘，   proc：进程，   gpu：显卡，   raid: RAID控制器

        :return: The name of this AgentDimension.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgentDimension.

        维度名称，枚举类型，类型有：   mount_point：挂载点，   disk：磁盘，   proc：进程，   gpu：显卡，   raid: RAID控制器

        :param name: The name of this AgentDimension.
        :type name: str
        """
        self._name = name

    @property
    def value(self):
        """Gets the value of this AgentDimension.

        维度值，32位字符串，如：2e84018fc8b4484b94e89aae212fe615

        :return: The value of this AgentDimension.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this AgentDimension.

        维度值，32位字符串，如：2e84018fc8b4484b94e89aae212fe615

        :param value: The value of this AgentDimension.
        :type value: str
        """
        self._value = value

    @property
    def origin_value(self):
        """Gets the origin_value of this AgentDimension.

        实际维度信息，字符串，如：vda。

        :return: The origin_value of this AgentDimension.
        :rtype: str
        """
        return self._origin_value

    @origin_value.setter
    def origin_value(self, origin_value):
        """Sets the origin_value of this AgentDimension.

        实际维度信息，字符串，如：vda。

        :param origin_value: The origin_value of this AgentDimension.
        :type origin_value: str
        """
        self._origin_value = origin_value

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
        if not isinstance(other, AgentDimension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
