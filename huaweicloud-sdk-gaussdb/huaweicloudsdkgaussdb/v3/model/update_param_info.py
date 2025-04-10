# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateParamInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_type': 'str',
        'parameter_values': 'dict(str, str)'
    }

    attribute_map = {
        'node_type': 'node_type',
        'parameter_values': 'parameter_values'
    }

    def __init__(self, node_type=None, parameter_values=None):
        r"""UpdateParamInfo

        The model defined in huaweicloud sdk

        :param node_type: 节点类型。取值范围： - be - fe
        :type node_type: str
        :param parameter_values: 参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。不传入该参数，则保持原参数信息。
        :type parameter_values: dict(str, str)
        """
        
        

        self._node_type = None
        self._parameter_values = None
        self.discriminator = None

        self.node_type = node_type
        self.parameter_values = parameter_values

    @property
    def node_type(self):
        r"""Gets the node_type of this UpdateParamInfo.

        节点类型。取值范围： - be - fe

        :return: The node_type of this UpdateParamInfo.
        :rtype: str
        """
        return self._node_type

    @node_type.setter
    def node_type(self, node_type):
        r"""Sets the node_type of this UpdateParamInfo.

        节点类型。取值范围： - be - fe

        :param node_type: The node_type of this UpdateParamInfo.
        :type node_type: str
        """
        self._node_type = node_type

    @property
    def parameter_values(self):
        r"""Gets the parameter_values of this UpdateParamInfo.

        参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。不传入该参数，则保持原参数信息。

        :return: The parameter_values of this UpdateParamInfo.
        :rtype: dict(str, str)
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, parameter_values):
        r"""Sets the parameter_values of this UpdateParamInfo.

        参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。不传入该参数，则保持原参数信息。

        :param parameter_values: The parameter_values of this UpdateParamInfo.
        :type parameter_values: dict(str, str)
        """
        self._parameter_values = parameter_values

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
        if not isinstance(other, UpdateParamInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
