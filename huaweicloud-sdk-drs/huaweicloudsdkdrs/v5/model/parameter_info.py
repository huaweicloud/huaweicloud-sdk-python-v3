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
        'parameter_name': 'str',
        'parameter_value': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'parameter_value': 'parameter_value'
    }

    def __init__(self, parameter_name=None, parameter_value=None):
        r"""ParameterInfo

        The model defined in huaweicloud sdk

        :param parameter_name: 参数名称，如：“applier_thread_num”，“read_task_num”等
        :type parameter_name: str
        :param parameter_value: 参数名称对应的参数值，如：“20”，“false”
        :type parameter_value: str
        """
        
        

        self._parameter_name = None
        self._parameter_value = None
        self.discriminator = None

        self.parameter_name = parameter_name
        self.parameter_value = parameter_value

    @property
    def parameter_name(self):
        r"""Gets the parameter_name of this ParameterInfo.

        参数名称，如：“applier_thread_num”，“read_task_num”等

        :return: The parameter_name of this ParameterInfo.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        r"""Sets the parameter_name of this ParameterInfo.

        参数名称，如：“applier_thread_num”，“read_task_num”等

        :param parameter_name: The parameter_name of this ParameterInfo.
        :type parameter_name: str
        """
        self._parameter_name = parameter_name

    @property
    def parameter_value(self):
        r"""Gets the parameter_value of this ParameterInfo.

        参数名称对应的参数值，如：“20”，“false”

        :return: The parameter_value of this ParameterInfo.
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        r"""Sets the parameter_value of this ParameterInfo.

        参数名称对应的参数值，如：“20”，“false”

        :param parameter_value: The parameter_value of this ParameterInfo.
        :type parameter_value: str
        """
        self._parameter_value = parameter_value

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
