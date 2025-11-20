# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceConfiguration:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'str',
        'actions': 'list[str]'
    }

    attribute_map = {
        'resource': 'resource',
        'actions': 'actions'
    }

    def __init__(self, resource=None, actions=None):
        r"""ResourceConfiguration

        The model defined in huaweicloud sdk

        :param resource: 资源的唯一资源标识符。
        :type resource: str
        :param actions: 当前资源要分析的操作列表。
        :type actions: list[str]
        """
        
        

        self._resource = None
        self._actions = None
        self.discriminator = None

        self.resource = resource
        self.actions = actions

    @property
    def resource(self):
        r"""Gets the resource of this ResourceConfiguration.

        资源的唯一资源标识符。

        :return: The resource of this ResourceConfiguration.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ResourceConfiguration.

        资源的唯一资源标识符。

        :param resource: The resource of this ResourceConfiguration.
        :type resource: str
        """
        self._resource = resource

    @property
    def actions(self):
        r"""Gets the actions of this ResourceConfiguration.

        当前资源要分析的操作列表。

        :return: The actions of this ResourceConfiguration.
        :rtype: list[str]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ResourceConfiguration.

        当前资源要分析的操作列表。

        :param actions: The actions of this ResourceConfiguration.
        :type actions: list[str]
        """
        self._actions = actions

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
        if not isinstance(other, ResourceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
