# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolLabelsCreation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_modelarts_name': 'str',
        'os_modelarts_workspace_id': 'str',
        'os_modelarts_node_prefix': 'str'
    }

    attribute_map = {
        'os_modelarts_name': 'os.modelarts/name',
        'os_modelarts_workspace_id': 'os.modelarts/workspace.id',
        'os_modelarts_node_prefix': 'os.modelarts/node.prefix'
    }

    def __init__(self, os_modelarts_name=None, os_modelarts_workspace_id=None, os_modelarts_node_prefix=None):
        r"""PoolLabelsCreation

        The model defined in huaweicloud sdk

        :param os_modelarts_name: **参数解释**：用户指定的资源池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_name: str
        :param os_modelarts_workspace_id: **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc) **约束限制**：不涉及。 **取值范围**：未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **默认取值**：不涉及。
        :type os_modelarts_workspace_id: str
        :param os_modelarts_node_prefix: **参数解释**：自定义节点名称前缀。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type os_modelarts_node_prefix: str
        """
        
        

        self._os_modelarts_name = None
        self._os_modelarts_workspace_id = None
        self._os_modelarts_node_prefix = None
        self.discriminator = None

        self.os_modelarts_name = os_modelarts_name
        if os_modelarts_workspace_id is not None:
            self.os_modelarts_workspace_id = os_modelarts_workspace_id
        if os_modelarts_node_prefix is not None:
            self.os_modelarts_node_prefix = os_modelarts_node_prefix

    @property
    def os_modelarts_name(self):
        r"""Gets the os_modelarts_name of this PoolLabelsCreation.

        **参数解释**：用户指定的资源池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_name of this PoolLabelsCreation.
        :rtype: str
        """
        return self._os_modelarts_name

    @os_modelarts_name.setter
    def os_modelarts_name(self, os_modelarts_name):
        r"""Sets the os_modelarts_name of this PoolLabelsCreation.

        **参数解释**：用户指定的资源池名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_name: The os_modelarts_name of this PoolLabelsCreation.
        :type os_modelarts_name: str
        """
        self._os_modelarts_name = os_modelarts_name

    @property
    def os_modelarts_workspace_id(self):
        r"""Gets the os_modelarts_workspace_id of this PoolLabelsCreation.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc) **约束限制**：不涉及。 **取值范围**：未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **默认取值**：不涉及。

        :return: The os_modelarts_workspace_id of this PoolLabelsCreation.
        :rtype: str
        """
        return self._os_modelarts_workspace_id

    @os_modelarts_workspace_id.setter
    def os_modelarts_workspace_id(self, os_modelarts_workspace_id):
        r"""Sets the os_modelarts_workspace_id of this PoolLabelsCreation.

        **参数解释**：工作空间ID。[获取方法请参见[查询工作空间列表](ListWorkspace.xml)。](tag:hc) **约束限制**：不涉及。 **取值范围**：未创建工作空间时默认值为“0”，存在创建并使用的工作空间，以实际取值为准。 **默认取值**：不涉及。

        :param os_modelarts_workspace_id: The os_modelarts_workspace_id of this PoolLabelsCreation.
        :type os_modelarts_workspace_id: str
        """
        self._os_modelarts_workspace_id = os_modelarts_workspace_id

    @property
    def os_modelarts_node_prefix(self):
        r"""Gets the os_modelarts_node_prefix of this PoolLabelsCreation.

        **参数解释**：自定义节点名称前缀。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The os_modelarts_node_prefix of this PoolLabelsCreation.
        :rtype: str
        """
        return self._os_modelarts_node_prefix

    @os_modelarts_node_prefix.setter
    def os_modelarts_node_prefix(self, os_modelarts_node_prefix):
        r"""Sets the os_modelarts_node_prefix of this PoolLabelsCreation.

        **参数解释**：自定义节点名称前缀。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param os_modelarts_node_prefix: The os_modelarts_node_prefix of this PoolLabelsCreation.
        :type os_modelarts_node_prefix: str
        """
        self._os_modelarts_node_prefix = os_modelarts_node_prefix

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
        if not isinstance(other, PoolLabelsCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
