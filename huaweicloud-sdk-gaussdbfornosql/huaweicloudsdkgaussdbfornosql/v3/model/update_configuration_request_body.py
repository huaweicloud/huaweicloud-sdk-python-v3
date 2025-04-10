# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateConfigurationRequestBody:

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
        'values': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'values': 'values'
    }

    def __init__(self, name=None, description=None, values=None):
        r"""UpdateConfigurationRequestBody

        The model defined in huaweicloud sdk

        :param name: 参数模板名称。最长64个字符，只允许大写字母、小写字母、数字和特殊字符中划线、下划线和点。
        :type name: str
        :param description: 参数模板描述。最长256个字符，不支持!&lt;&gt;&#x3D;&amp;\&quot;&#39;特殊字符。默认为空。
        :type description: str
        :param values: 参数值对象，用户基于默认参数模板自定义的参数值。为空时不修改参数值。
        :type values: dict(str, str)
        """
        
        

        self._name = None
        self._description = None
        self._values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if values is not None:
            self.values = values

    @property
    def name(self):
        r"""Gets the name of this UpdateConfigurationRequestBody.

        参数模板名称。最长64个字符，只允许大写字母、小写字母、数字和特殊字符中划线、下划线和点。

        :return: The name of this UpdateConfigurationRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateConfigurationRequestBody.

        参数模板名称。最长64个字符，只允许大写字母、小写字母、数字和特殊字符中划线、下划线和点。

        :param name: The name of this UpdateConfigurationRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateConfigurationRequestBody.

        参数模板描述。最长256个字符，不支持!<>=&\"'特殊字符。默认为空。

        :return: The description of this UpdateConfigurationRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateConfigurationRequestBody.

        参数模板描述。最长256个字符，不支持!<>=&\"'特殊字符。默认为空。

        :param description: The description of this UpdateConfigurationRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def values(self):
        r"""Gets the values of this UpdateConfigurationRequestBody.

        参数值对象，用户基于默认参数模板自定义的参数值。为空时不修改参数值。

        :return: The values of this UpdateConfigurationRequestBody.
        :rtype: dict(str, str)
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this UpdateConfigurationRequestBody.

        参数值对象，用户基于默认参数模板自定义的参数值。为空时不修改参数值。

        :param values: The values of this UpdateConfigurationRequestBody.
        :type values: dict(str, str)
        """
        self._values = values

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
        if not isinstance(other, UpdateConfigurationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
