# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceConfigurationsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parameter_values': 'dict(str, str)'
    }

    attribute_map = {
        'parameter_values': 'parameter_values'
    }

    def __init__(self, parameter_values=None):
        r"""UpdateInstanceConfigurationsRequestBody

        The model defined in huaweicloud sdk

        :param parameter_values: 参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。不传入该参数，则保持原参数信息。
        :type parameter_values: dict(str, str)
        """
        
        

        self._parameter_values = None
        self.discriminator = None

        self.parameter_values = parameter_values

    @property
    def parameter_values(self):
        r"""Gets the parameter_values of this UpdateInstanceConfigurationsRequestBody.

        参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。不传入该参数，则保持原参数信息。

        :return: The parameter_values of this UpdateInstanceConfigurationsRequestBody.
        :rtype: dict(str, str)
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, parameter_values):
        r"""Sets the parameter_values of this UpdateInstanceConfigurationsRequestBody.

        参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。不传入该参数，则保持原参数信息。

        :param parameter_values: The parameter_values of this UpdateInstanceConfigurationsRequestBody.
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
        if not isinstance(other, UpdateInstanceConfigurationsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
