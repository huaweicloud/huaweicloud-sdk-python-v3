# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResponseSchemaPropertiesDetailsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attr_name_format': 'str',
        'include': 'str'
    }

    attribute_map = {
        'attr_name_format': 'attr_name_format',
        'include': 'include'
    }

    def __init__(self, attr_name_format=None, include=None):
        r"""ResponseSchemaPropertiesDetailsDto

        The model defined in huaweicloud sdk

        :param attr_name_format: 额外添加的属性的格式
        :type attr_name_format: str
        :param include: 是否包含额外属性
        :type include: str
        """
        
        

        self._attr_name_format = None
        self._include = None
        self.discriminator = None

        self.attr_name_format = attr_name_format
        self.include = include

    @property
    def attr_name_format(self):
        r"""Gets the attr_name_format of this ResponseSchemaPropertiesDetailsDto.

        额外添加的属性的格式

        :return: The attr_name_format of this ResponseSchemaPropertiesDetailsDto.
        :rtype: str
        """
        return self._attr_name_format

    @attr_name_format.setter
    def attr_name_format(self, attr_name_format):
        r"""Sets the attr_name_format of this ResponseSchemaPropertiesDetailsDto.

        额外添加的属性的格式

        :param attr_name_format: The attr_name_format of this ResponseSchemaPropertiesDetailsDto.
        :type attr_name_format: str
        """
        self._attr_name_format = attr_name_format

    @property
    def include(self):
        r"""Gets the include of this ResponseSchemaPropertiesDetailsDto.

        是否包含额外属性

        :return: The include of this ResponseSchemaPropertiesDetailsDto.
        :rtype: str
        """
        return self._include

    @include.setter
    def include(self, include):
        r"""Sets the include of this ResponseSchemaPropertiesDetailsDto.

        是否包含额外属性

        :param include: The include of this ResponseSchemaPropertiesDetailsDto.
        :type include: str
        """
        self._include = include

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
        if not isinstance(other, ResponseSchemaPropertiesDetailsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
