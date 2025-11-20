# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConfigurationRequest:

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
        'values': 'object'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'values': 'values'
    }

    def __init__(self, name=None, description=None, values=None):
        r"""CreateConfigurationRequest

        The model defined in huaweicloud sdk

        :param name: 名称。
        :type name: str
        :param description: 描述。
        :type description: str
        :param values: 参数值。
        :type values: object
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
        r"""Gets the name of this CreateConfigurationRequest.

        名称。

        :return: The name of this CreateConfigurationRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateConfigurationRequest.

        名称。

        :param name: The name of this CreateConfigurationRequest.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateConfigurationRequest.

        描述。

        :return: The description of this CreateConfigurationRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateConfigurationRequest.

        描述。

        :param description: The description of this CreateConfigurationRequest.
        :type description: str
        """
        self._description = description

    @property
    def values(self):
        r"""Gets the values of this CreateConfigurationRequest.

        参数值。

        :return: The values of this CreateConfigurationRequest.
        :rtype: object
        """
        return self._values

    @values.setter
    def values(self, values):
        r"""Sets the values of this CreateConfigurationRequest.

        参数值。

        :param values: The values of this CreateConfigurationRequest.
        :type values: object
        """
        self._values = values

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
        if not isinstance(other, CreateConfigurationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
