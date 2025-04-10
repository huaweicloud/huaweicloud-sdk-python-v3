# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateModuleDescriptionPrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'module_description': 'str'
    }

    attribute_map = {
        'module_description': 'module_description'
    }

    def __init__(self, module_description=None):
        r"""PrivateModuleDescriptionPrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param module_description: 私有模块（private-module）的描述。可用于客户识别被管理的私有模块。如果想要更新私有模块的描述，可以通过UpdatePrivateModuleMetadata API。
        :type module_description: str
        """
        
        

        self._module_description = None
        self.discriminator = None

        if module_description is not None:
            self.module_description = module_description

    @property
    def module_description(self):
        r"""Gets the module_description of this PrivateModuleDescriptionPrimitiveTypeHolder.

        私有模块（private-module）的描述。可用于客户识别被管理的私有模块。如果想要更新私有模块的描述，可以通过UpdatePrivateModuleMetadata API。

        :return: The module_description of this PrivateModuleDescriptionPrimitiveTypeHolder.
        :rtype: str
        """
        return self._module_description

    @module_description.setter
    def module_description(self, module_description):
        r"""Sets the module_description of this PrivateModuleDescriptionPrimitiveTypeHolder.

        私有模块（private-module）的描述。可用于客户识别被管理的私有模块。如果想要更新私有模块的描述，可以通过UpdatePrivateModuleMetadata API。

        :param module_description: The module_description of this PrivateModuleDescriptionPrimitiveTypeHolder.
        :type module_description: str
        """
        self._module_description = module_description

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
        if not isinstance(other, PrivateModuleDescriptionPrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
