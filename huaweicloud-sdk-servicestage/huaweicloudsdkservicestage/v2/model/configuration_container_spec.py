# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationContainerSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'containers': 'list[ComponentContainerParameter]',
        'type': 'str'
    }

    attribute_map = {
        'containers': 'containers',
        'type': 'type'
    }

    def __init__(self, containers=None, type=None):
        r"""ConfigurationContainerSpec

        The model defined in huaweicloud sdk

        :param containers: 容器信息
        :type containers: list[:class:`huaweicloudsdkservicestage.v2.ComponentContainerParameter`]
        :param type: 工作负载类型。
        :type type: str
        """
        
        

        self._containers = None
        self._type = None
        self.discriminator = None

        if containers is not None:
            self.containers = containers
        if type is not None:
            self.type = type

    @property
    def containers(self):
        r"""Gets the containers of this ConfigurationContainerSpec.

        容器信息

        :return: The containers of this ConfigurationContainerSpec.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ComponentContainerParameter`]
        """
        return self._containers

    @containers.setter
    def containers(self, containers):
        r"""Sets the containers of this ConfigurationContainerSpec.

        容器信息

        :param containers: The containers of this ConfigurationContainerSpec.
        :type containers: list[:class:`huaweicloudsdkservicestage.v2.ComponentContainerParameter`]
        """
        self._containers = containers

    @property
    def type(self):
        r"""Gets the type of this ConfigurationContainerSpec.

        工作负载类型。

        :return: The type of this ConfigurationContainerSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConfigurationContainerSpec.

        工作负载类型。

        :param type: The type of this ConfigurationContainerSpec.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ConfigurationContainerSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
