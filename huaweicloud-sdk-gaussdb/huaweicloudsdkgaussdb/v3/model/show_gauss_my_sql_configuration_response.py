# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGaussMySqlConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configurations': 'ConfigurationSummary2',
        'parameter_values': 'dict(str, str)'
    }

    attribute_map = {
        'configurations': 'configurations',
        'parameter_values': 'parameter_values'
    }

    def __init__(self, configurations=None, parameter_values=None):
        """ShowGaussMySqlConfigurationResponse

        The model defined in huaweicloud sdk

        :param configurations: 
        :type configurations: :class:`huaweicloudsdkgaussdb.v3.ConfigurationSummary2`
        :param parameter_values: 参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。
        :type parameter_values: dict(str, str)
        """
        
        super(ShowGaussMySqlConfigurationResponse, self).__init__()

        self._configurations = None
        self._parameter_values = None
        self.discriminator = None

        if configurations is not None:
            self.configurations = configurations
        if parameter_values is not None:
            self.parameter_values = parameter_values

    @property
    def configurations(self):
        """Gets the configurations of this ShowGaussMySqlConfigurationResponse.

        :return: The configurations of this ShowGaussMySqlConfigurationResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.ConfigurationSummary2`
        """
        return self._configurations

    @configurations.setter
    def configurations(self, configurations):
        """Sets the configurations of this ShowGaussMySqlConfigurationResponse.

        :param configurations: The configurations of this ShowGaussMySqlConfigurationResponse.
        :type configurations: :class:`huaweicloudsdkgaussdb.v3.ConfigurationSummary2`
        """
        self._configurations = configurations

    @property
    def parameter_values(self):
        """Gets the parameter_values of this ShowGaussMySqlConfigurationResponse.

        参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。

        :return: The parameter_values of this ShowGaussMySqlConfigurationResponse.
        :rtype: dict(str, str)
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, parameter_values):
        """Sets the parameter_values of this ShowGaussMySqlConfigurationResponse.

        参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。

        :param parameter_values: The parameter_values of this ShowGaussMySqlConfigurationResponse.
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
        if not isinstance(other, ShowGaussMySqlConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
