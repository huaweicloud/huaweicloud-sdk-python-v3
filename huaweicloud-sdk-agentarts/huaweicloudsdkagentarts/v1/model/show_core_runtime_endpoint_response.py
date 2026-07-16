# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCoreRuntimeEndpointResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'runtime_id': 'str',
        'id': 'str',
        'name': 'str',
        'description': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'target_version_name': 'str',
        'routing_config': 'CoreRunRoutingConfigurationResp',
        'tags': 'list[CoreRunTagItemResp]'
    }

    attribute_map = {
        'runtime_id': 'runtime_id',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'target_version_name': 'target_version_name',
        'routing_config': 'routing_config',
        'tags': 'tags'
    }

    def __init__(self, runtime_id=None, id=None, name=None, description=None, created_at=None, updated_at=None, target_version_name=None, routing_config=None, tags=None):
        r"""ShowCoreRuntimeEndpointResponse

        The model defined in huaweicloud sdk

        :param runtime_id: **参数解释**: 运行时ID。 
        :type runtime_id: str
        :param id: **参数解释**: 运行时访问方式ID。 
        :type id: str
        :param name: **参数解释**: 运行时访问方式名称。 
        :type name: str
        :param description: **参数解释**: 运行时访问方式描述。 
        :type description: str
        :param created_at: **参数解释**: 创建时间。 
        :type created_at: datetime
        :param updated_at: **参数解释**: 最后更新时间。 
        :type updated_at: datetime
        :param target_version_name: **参数解释**: 目标版本名称。 
        :type target_version_name: str
        :param routing_config: 
        :type routing_config: :class:`huaweicloudsdkagentarts.v1.CoreRunRoutingConfigurationResp`
        :param tags: **参数解释**: 标签配置列表。 
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItemResp`]
        """
        
        super().__init__()

        self._runtime_id = None
        self._id = None
        self._name = None
        self._description = None
        self._created_at = None
        self._updated_at = None
        self._target_version_name = None
        self._routing_config = None
        self._tags = None
        self.discriminator = None

        if runtime_id is not None:
            self.runtime_id = runtime_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if target_version_name is not None:
            self.target_version_name = target_version_name
        if routing_config is not None:
            self.routing_config = routing_config
        if tags is not None:
            self.tags = tags

    @property
    def runtime_id(self):
        r"""Gets the runtime_id of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 运行时ID。 

        :return: The runtime_id of this ShowCoreRuntimeEndpointResponse.
        :rtype: str
        """
        return self._runtime_id

    @runtime_id.setter
    def runtime_id(self, runtime_id):
        r"""Sets the runtime_id of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 运行时ID。 

        :param runtime_id: The runtime_id of this ShowCoreRuntimeEndpointResponse.
        :type runtime_id: str
        """
        self._runtime_id = runtime_id

    @property
    def id(self):
        r"""Gets the id of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 运行时访问方式ID。 

        :return: The id of this ShowCoreRuntimeEndpointResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 运行时访问方式ID。 

        :param id: The id of this ShowCoreRuntimeEndpointResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 运行时访问方式名称。 

        :return: The name of this ShowCoreRuntimeEndpointResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 运行时访问方式名称。 

        :param name: The name of this ShowCoreRuntimeEndpointResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 运行时访问方式描述。 

        :return: The description of this ShowCoreRuntimeEndpointResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 运行时访问方式描述。 

        :param description: The description of this ShowCoreRuntimeEndpointResponse.
        :type description: str
        """
        self._description = description

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 创建时间。 

        :return: The created_at of this ShowCoreRuntimeEndpointResponse.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 创建时间。 

        :param created_at: The created_at of this ShowCoreRuntimeEndpointResponse.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 最后更新时间。 

        :return: The updated_at of this ShowCoreRuntimeEndpointResponse.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 最后更新时间。 

        :param updated_at: The updated_at of this ShowCoreRuntimeEndpointResponse.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def target_version_name(self):
        r"""Gets the target_version_name of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 目标版本名称。 

        :return: The target_version_name of this ShowCoreRuntimeEndpointResponse.
        :rtype: str
        """
        return self._target_version_name

    @target_version_name.setter
    def target_version_name(self, target_version_name):
        r"""Sets the target_version_name of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 目标版本名称。 

        :param target_version_name: The target_version_name of this ShowCoreRuntimeEndpointResponse.
        :type target_version_name: str
        """
        self._target_version_name = target_version_name

    @property
    def routing_config(self):
        r"""Gets the routing_config of this ShowCoreRuntimeEndpointResponse.

        :return: The routing_config of this ShowCoreRuntimeEndpointResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.CoreRunRoutingConfigurationResp`
        """
        return self._routing_config

    @routing_config.setter
    def routing_config(self, routing_config):
        r"""Sets the routing_config of this ShowCoreRuntimeEndpointResponse.

        :param routing_config: The routing_config of this ShowCoreRuntimeEndpointResponse.
        :type routing_config: :class:`huaweicloudsdkagentarts.v1.CoreRunRoutingConfigurationResp`
        """
        self._routing_config = routing_config

    @property
    def tags(self):
        r"""Gets the tags of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 标签配置列表。 

        :return: The tags of this ShowCoreRuntimeEndpointResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItemResp`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowCoreRuntimeEndpointResponse.

        **参数解释**: 标签配置列表。 

        :param tags: The tags of this ShowCoreRuntimeEndpointResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.CoreRunTagItemResp`]
        """
        self._tags = tags

    def to_dict(self):
        import warnings
        warnings.warn("ShowCoreRuntimeEndpointResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowCoreRuntimeEndpointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
