# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerSoftware:

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
        'version': 'str'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, name=None, version=None):
        r"""ContainerSoftware

        The model defined in huaweicloud sdk

        :param name: **参数解释**：软件名称。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、下划线和连字符，2~32个字符。 **默认取值**：不涉及。 
        :type name: str
        :param version: **参数解释**：软件版本。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、下划线和连字符，2~32个字符。 **默认取值**：不涉及。 
        :type version: str
        """
        
        

        self._name = None
        self._version = None
        self.discriminator = None

        self.name = name
        self.version = version

    @property
    def name(self):
        r"""Gets the name of this ContainerSoftware.

        **参数解释**：软件名称。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、下划线和连字符，2~32个字符。 **默认取值**：不涉及。 

        :return: The name of this ContainerSoftware.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ContainerSoftware.

        **参数解释**：软件名称。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、下划线和连字符，2~32个字符。 **默认取值**：不涉及。 

        :param name: The name of this ContainerSoftware.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this ContainerSoftware.

        **参数解释**：软件版本。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、下划线和连字符，2~32个字符。 **默认取值**：不涉及。 

        :return: The version of this ContainerSoftware.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ContainerSoftware.

        **参数解释**：软件版本。 **约束限制**：不涉及。 **取值范围**：支持英文字母、数字、小数点、下划线和连字符，2~32个字符。 **默认取值**：不涉及。 

        :param version: The version of this ContainerSoftware.
        :type version: str
        """
        self._version = version

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
        if not isinstance(other, ContainerSoftware):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
