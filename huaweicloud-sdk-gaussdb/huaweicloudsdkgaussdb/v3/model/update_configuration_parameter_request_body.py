# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConfigurationParameterRequestBody:

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
        'description': 'str',
        'parameter_values': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'parameter_values': 'parameter_values'
    }

    def __init__(self, name=None, description=None, parameter_values=None):
        """UpdateConfigurationParameterRequestBody

        The model defined in huaweicloud sdk

        :param name: 参数模板名称。  取值范围：长度1到64个字符之间，区分大小写字母，可包含字母、数字、中划线、下划线或句点，不能包含其他特殊字符。参数模板描述，参数名和参数值映射关系三项不能同时为空。
        :type name: str
        :param description: 参数模板描述。默认为空。取值范围：长度不超过256个字符，且不能包含回车和特殊字符 ! &lt; \&quot; &#x3D; &#39; &gt; &amp;
        :type description: str
        :param parameter_values: 参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。不传入该参数，则保持原参数信息。
        :type parameter_values: dict(str, str)
        """
        
        

        self._name = None
        self._description = None
        self._parameter_values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if parameter_values is not None:
            self.parameter_values = parameter_values

    @property
    def name(self):
        """Gets the name of this UpdateConfigurationParameterRequestBody.

        参数模板名称。  取值范围：长度1到64个字符之间，区分大小写字母，可包含字母、数字、中划线、下划线或句点，不能包含其他特殊字符。参数模板描述，参数名和参数值映射关系三项不能同时为空。

        :return: The name of this UpdateConfigurationParameterRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateConfigurationParameterRequestBody.

        参数模板名称。  取值范围：长度1到64个字符之间，区分大小写字母，可包含字母、数字、中划线、下划线或句点，不能包含其他特殊字符。参数模板描述，参数名和参数值映射关系三项不能同时为空。

        :param name: The name of this UpdateConfigurationParameterRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateConfigurationParameterRequestBody.

        参数模板描述。默认为空。取值范围：长度不超过256个字符，且不能包含回车和特殊字符 ! < \" = ' > &

        :return: The description of this UpdateConfigurationParameterRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateConfigurationParameterRequestBody.

        参数模板描述。默认为空。取值范围：长度不超过256个字符，且不能包含回车和特殊字符 ! < \" = ' > &

        :param description: The description of this UpdateConfigurationParameterRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def parameter_values(self):
        """Gets the parameter_values of this UpdateConfigurationParameterRequestBody.

        参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。不传入该参数，则保持原参数信息。

        :return: The parameter_values of this UpdateConfigurationParameterRequestBody.
        :rtype: dict(str, str)
        """
        return self._parameter_values

    @parameter_values.setter
    def parameter_values(self, parameter_values):
        """Sets the parameter_values of this UpdateConfigurationParameterRequestBody.

        参数名和参数值映射关系。用户可以基于默认参数模板的参数，自定义的参数值。不传入该参数，则保持原参数信息。

        :param parameter_values: The parameter_values of this UpdateConfigurationParameterRequestBody.
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
        if not isinstance(other, UpdateConfigurationParameterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
