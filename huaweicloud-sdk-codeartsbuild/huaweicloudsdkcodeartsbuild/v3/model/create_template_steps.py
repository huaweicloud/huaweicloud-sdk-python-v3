# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplateSteps:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'properties': 'dict(str, object)',
        'module_id': 'str',
        'name': 'str',
        'version': 'str',
        'enable': 'bool'
    }

    attribute_map = {
        'properties': 'properties',
        'module_id': 'module_id',
        'name': 'name',
        'version': 'version',
        'enable': 'enable'
    }

    def __init__(self, properties=None, module_id=None, name=None, version=None, enable=None):
        """CreateTemplateSteps

        The model defined in huaweicloud sdk

        :param properties: 具体的构建步骤
        :type properties: dict(str, object)
        :param module_id: 构建模块id
        :type module_id: str
        :param name: 构建模块名称
        :type name: str
        :param version: 构建版本
        :type version: str
        :param enable: 是否开启
        :type enable: bool
        """
        
        

        self._properties = None
        self._module_id = None
        self._name = None
        self._version = None
        self._enable = None
        self.discriminator = None

        if properties is not None:
            self.properties = properties
        self.module_id = module_id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if enable is not None:
            self.enable = enable

    @property
    def properties(self):
        """Gets the properties of this CreateTemplateSteps.

        具体的构建步骤

        :return: The properties of this CreateTemplateSteps.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CreateTemplateSteps.

        具体的构建步骤

        :param properties: The properties of this CreateTemplateSteps.
        :type properties: dict(str, object)
        """
        self._properties = properties

    @property
    def module_id(self):
        """Gets the module_id of this CreateTemplateSteps.

        构建模块id

        :return: The module_id of this CreateTemplateSteps.
        :rtype: str
        """
        return self._module_id

    @module_id.setter
    def module_id(self, module_id):
        """Sets the module_id of this CreateTemplateSteps.

        构建模块id

        :param module_id: The module_id of this CreateTemplateSteps.
        :type module_id: str
        """
        self._module_id = module_id

    @property
    def name(self):
        """Gets the name of this CreateTemplateSteps.

        构建模块名称

        :return: The name of this CreateTemplateSteps.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateTemplateSteps.

        构建模块名称

        :param name: The name of this CreateTemplateSteps.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        """Gets the version of this CreateTemplateSteps.

        构建版本

        :return: The version of this CreateTemplateSteps.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CreateTemplateSteps.

        构建版本

        :param version: The version of this CreateTemplateSteps.
        :type version: str
        """
        self._version = version

    @property
    def enable(self):
        """Gets the enable of this CreateTemplateSteps.

        是否开启

        :return: The enable of this CreateTemplateSteps.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateTemplateSteps.

        是否开启

        :param enable: The enable of this CreateTemplateSteps.
        :type enable: bool
        """
        self._enable = enable

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
        if not isinstance(other, CreateTemplateSteps):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
