# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrivateModuleSourcePrimitiveTypeHolder:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'module_source': 'str'
    }

    attribute_map = {
        'module_source': 'module_source'
    }

    def __init__(self, module_source=None):
        r"""PrivateModuleSourcePrimitiveTypeHolder

        The model defined in huaweicloud sdk

        :param module_source: 在模板中使用模块需要定义如下格式：   module \&quot;my_hello_word_module\&quot; {     source &#x3D; {module_source}   }  其中{module_source}为本参数
        :type module_source: str
        """
        
        

        self._module_source = None
        self.discriminator = None

        if module_source is not None:
            self.module_source = module_source

    @property
    def module_source(self):
        r"""Gets the module_source of this PrivateModuleSourcePrimitiveTypeHolder.

        在模板中使用模块需要定义如下格式：   module \"my_hello_word_module\" {     source = {module_source}   }  其中{module_source}为本参数

        :return: The module_source of this PrivateModuleSourcePrimitiveTypeHolder.
        :rtype: str
        """
        return self._module_source

    @module_source.setter
    def module_source(self, module_source):
        r"""Sets the module_source of this PrivateModuleSourcePrimitiveTypeHolder.

        在模板中使用模块需要定义如下格式：   module \"my_hello_word_module\" {     source = {module_source}   }  其中{module_source}为本参数

        :param module_source: The module_source of this PrivateModuleSourcePrimitiveTypeHolder.
        :type module_source: str
        """
        self._module_source = module_source

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
        if not isinstance(other, PrivateModuleSourcePrimitiveTypeHolder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
