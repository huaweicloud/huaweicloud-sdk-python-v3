# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyParameterConfigTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'values': 'dict(str, str)',
        'description': 'str'
    }

    attribute_map = {
        'values': 'values',
        'description': 'description'
    }

    def __init__(self, values=None, description=None):
        r"""ModifyParameterConfigTemplateRequestBody

        The model defined in huaweicloud sdk

        :param values: 参数值对象Map&lt;String,String&gt;，用户基于默认参数模板自定义的参数值。
        :type values: dict(str, str)
        :param description: 参数组模板描述。
        :type description: str
        """
        
        

        self._values = None
        self._description = None
        self.discriminator = None

        if values is not None:
            self.values = values
        if description is not None:
            self.description = description

    @property
    def values(self):
        r"""Gets the values of this ModifyParameterConfigTemplateRequestBody.

        参数值对象Map<String,String>，用户基于默认参数模板自定义的参数值。

        :return: The values of this ModifyParameterConfigTemplateRequestBody.
        :rtype: dict(str, str)
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this ModifyParameterConfigTemplateRequestBody.

        参数值对象Map<String,String>，用户基于默认参数模板自定义的参数值。

        :param values: The values of this ModifyParameterConfigTemplateRequestBody.
        :type values: dict(str, str)
        """
        self._values = values

    @property
    def description(self):
        r"""Gets the description of this ModifyParameterConfigTemplateRequestBody.

        参数组模板描述。

        :return: The description of this ModifyParameterConfigTemplateRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModifyParameterConfigTemplateRequestBody.

        参数组模板描述。

        :param description: The description of this ModifyParameterConfigTemplateRequestBody.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModifyParameterConfigTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
