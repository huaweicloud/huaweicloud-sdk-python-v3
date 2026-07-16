# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCoreRuntimeEndpointRequestBody:

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
        'target_version_name': 'str',
        'description': 'str',
        'routing_config': 'CoreRunRoutingConfiguration',
        'tags': 'list[CoreRunTagItem]'
    }

    attribute_map = {
        'name': 'name',
        'target_version_name': 'target_version_name',
        'description': 'description',
        'routing_config': 'routing_config',
        'tags': 'tags'
    }

    def __init__(self, name=None, target_version_name=None, description=None, routing_config=None, tags=None):
        r"""CreateCoreRuntimeEndpointRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**: 访问方式名称。 
        :type name: str
        :param target_version_name: **参数解释**: 目标版本名称。 
        :type target_version_name: str
        :param description: **参数解释**: 描述信息。 
        :type description: str
        :param routing_config: 
        :type routing_config: :class:`huaweicloudsdkagentarts.v1.CoreRunRoutingConfiguration`
        :param tags: **参数解释**: 标签配置列表。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItem`]
        """
        
        

        self._name = None
        self._target_version_name = None
        self._description = None
        self._routing_config = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if target_version_name is not None:
            self.target_version_name = target_version_name
        if description is not None:
            self.description = description
        if routing_config is not None:
            self.routing_config = routing_config
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateCoreRuntimeEndpointRequestBody.

        **参数解释**: 访问方式名称。 

        :return: The name of this CreateCoreRuntimeEndpointRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCoreRuntimeEndpointRequestBody.

        **参数解释**: 访问方式名称。 

        :param name: The name of this CreateCoreRuntimeEndpointRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def target_version_name(self):
        r"""Gets the target_version_name of this CreateCoreRuntimeEndpointRequestBody.

        **参数解释**: 目标版本名称。 

        :return: The target_version_name of this CreateCoreRuntimeEndpointRequestBody.
        :rtype: str
        """
        return self._target_version_name

    @target_version_name.setter
    def target_version_name(self, target_version_name):
        r"""Sets the target_version_name of this CreateCoreRuntimeEndpointRequestBody.

        **参数解释**: 目标版本名称。 

        :param target_version_name: The target_version_name of this CreateCoreRuntimeEndpointRequestBody.
        :type target_version_name: str
        """
        self._target_version_name = target_version_name

    @property
    def description(self):
        r"""Gets the description of this CreateCoreRuntimeEndpointRequestBody.

        **参数解释**: 描述信息。 

        :return: The description of this CreateCoreRuntimeEndpointRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateCoreRuntimeEndpointRequestBody.

        **参数解释**: 描述信息。 

        :param description: The description of this CreateCoreRuntimeEndpointRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def routing_config(self):
        r"""Gets the routing_config of this CreateCoreRuntimeEndpointRequestBody.

        :return: The routing_config of this CreateCoreRuntimeEndpointRequestBody.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunRoutingConfiguration`
        """
        return self._routing_config

    @routing_config.setter
    def routing_config(self, routing_config):
        r"""Sets the routing_config of this CreateCoreRuntimeEndpointRequestBody.

        :param routing_config: The routing_config of this CreateCoreRuntimeEndpointRequestBody.
        :type routing_config: :class:`huaweicloudsdkagentarts.v1.CoreRunRoutingConfiguration`
        """
        self._routing_config = routing_config

    @property
    def tags(self):
        r"""Gets the tags of this CreateCoreRuntimeEndpointRequestBody.

        **参数解释**: 标签配置列表。 

        :return: The tags of this CreateCoreRuntimeEndpointRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItem`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateCoreRuntimeEndpointRequestBody.

        **参数解释**: 标签配置列表。 

        :param tags: The tags of this CreateCoreRuntimeEndpointRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItem`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateCoreRuntimeEndpointRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
