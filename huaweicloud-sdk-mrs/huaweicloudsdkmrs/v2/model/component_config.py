# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_name': 'str',
        'configs': 'list[Config]'
    }

    attribute_map = {
        'component_name': 'component_name',
        'configs': 'configs'
    }

    def __init__(self, component_name=None, configs=None):
        """ComponentConfig

        The model defined in huaweicloud sdk

        :param component_name: 组件名称
        :type component_name: str
        :param configs: 组件配置项列表
        :type configs: list[:class:`huaweicloudsdkmrs.v2.Config`]
        """
        
        

        self._component_name = None
        self._configs = None
        self.discriminator = None

        self.component_name = component_name
        if configs is not None:
            self.configs = configs

    @property
    def component_name(self):
        """Gets the component_name of this ComponentConfig.

        组件名称

        :return: The component_name of this ComponentConfig.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this ComponentConfig.

        组件名称

        :param component_name: The component_name of this ComponentConfig.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def configs(self):
        """Gets the configs of this ComponentConfig.

        组件配置项列表

        :return: The configs of this ComponentConfig.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.Config`]
        """
        return self._configs

    @configs.setter
    def configs(self, configs):
        """Sets the configs of this ComponentConfig.

        组件配置项列表

        :param configs: The configs of this ComponentConfig.
        :type configs: list[:class:`huaweicloudsdkmrs.v2.Config`]
        """
        self._configs = configs

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
        if not isinstance(other, ComponentConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
