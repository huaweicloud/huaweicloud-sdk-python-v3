# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'param_name': 'str',
        'param_type': 'str',
        'param_group': 'str',
        'default_value': 'str'
    }

    attribute_map = {
        'param_name': 'param_name',
        'param_type': 'param_type',
        'param_group': 'param_group',
        'default_value': 'default_value'
    }

    def __init__(self, param_name=None, param_type=None, param_group=None, default_value=None):
        """TaskParam

        The model defined in huaweicloud sdk

        :param param_name: 参数名称。
        :type param_name: str
        :param param_type: 参数类型。
        :type param_type: str
        :param param_group: 参数分组。
        :type param_group: str
        :param default_value: 参数初始值。
        :type default_value: str
        """
        
        

        self._param_name = None
        self._param_type = None
        self._param_group = None
        self._default_value = None
        self.discriminator = None

        self.param_name = param_name
        if param_type is not None:
            self.param_type = param_type
        if param_group is not None:
            self.param_group = param_group
        if default_value is not None:
            self.default_value = default_value

    @property
    def param_name(self):
        """Gets the param_name of this TaskParam.

        参数名称。

        :return: The param_name of this TaskParam.
        :rtype: str
        """
        return self._param_name

    @param_name.setter
    def param_name(self, param_name):
        """Sets the param_name of this TaskParam.

        参数名称。

        :param param_name: The param_name of this TaskParam.
        :type param_name: str
        """
        self._param_name = param_name

    @property
    def param_type(self):
        """Gets the param_type of this TaskParam.

        参数类型。

        :return: The param_type of this TaskParam.
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        """Sets the param_type of this TaskParam.

        参数类型。

        :param param_type: The param_type of this TaskParam.
        :type param_type: str
        """
        self._param_type = param_type

    @property
    def param_group(self):
        """Gets the param_group of this TaskParam.

        参数分组。

        :return: The param_group of this TaskParam.
        :rtype: str
        """
        return self._param_group

    @param_group.setter
    def param_group(self, param_group):
        """Sets the param_group of this TaskParam.

        参数分组。

        :param param_group: The param_group of this TaskParam.
        :type param_group: str
        """
        self._param_group = param_group

    @property
    def default_value(self):
        """Gets the default_value of this TaskParam.

        参数初始值。

        :return: The default_value of this TaskParam.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this TaskParam.

        参数初始值。

        :param default_value: The default_value of this TaskParam.
        :type default_value: str
        """
        self._default_value = default_value

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
        if not isinstance(other, TaskParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
