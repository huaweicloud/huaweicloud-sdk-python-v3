# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceCreationVariables:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'environment': 'object',
        'components': 'object'
    }

    attribute_map = {
        'environment': 'environment',
        'components': 'components'
    }

    def __init__(self, environment=None, components=None):
        r"""InstanceCreationVariables

        The model defined in huaweicloud sdk

        :param environment: 环境变量
        :type environment: object
        :param components: 组件变量
        :type components: object
        """
        
        

        self._environment = None
        self._components = None
        self.discriminator = None

        if environment is not None:
            self.environment = environment
        if components is not None:
            self.components = components

    @property
    def environment(self):
        r"""Gets the environment of this InstanceCreationVariables.

        环境变量

        :return: The environment of this InstanceCreationVariables.
        :rtype: object
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        r"""Sets the environment of this InstanceCreationVariables.

        环境变量

        :param environment: The environment of this InstanceCreationVariables.
        :type environment: object
        """
        self._environment = environment

    @property
    def components(self):
        r"""Gets the components of this InstanceCreationVariables.

        组件变量

        :return: The components of this InstanceCreationVariables.
        :rtype: object
        """
        return self._components

    @components.setter
    def components(self, components):
        r"""Sets the components of this InstanceCreationVariables.

        组件变量

        :param components: The components of this InstanceCreationVariables.
        :type components: object
        """
        self._components = components

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
        if not isinstance(other, InstanceCreationVariables):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
