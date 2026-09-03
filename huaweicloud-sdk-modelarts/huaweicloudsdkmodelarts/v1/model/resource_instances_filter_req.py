# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInstancesFilterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'tags': 'list[MutiValueTag]',
        'without_any_tag': 'bool',
        'matches': 'list[Match]'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'tags': 'tags',
        'without_any_tag': 'without_any_tag',
        'matches': 'matches'
    }

    def __init__(self, workspace_id=None, tags=None, without_any_tag=None, matches=None):
        r"""ResourceInstancesFilterReq

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间ID。未创建工作空间时默认值为\&quot;0\&quot;，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。
        :type workspace_id: str
        :param tags: **参数解释**：标签筛选条件，按标签key-value对筛选作业。同一key下多个value为OR关系，不同key之间为AND关系。 **约束限制**：同一key的values不能重复，不同key不能重复。 **取值范围**：不涉及。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.MutiValueTag`]
        :param without_any_tag: **参数解释**：是否查询没有任何标签的作业。 **约束限制**：设为true时忽略tags筛选条件。 **取值范围**： - true：仅查询无标签的作业 - false：按tags条件筛选 **默认取值**：false。
        :type without_any_tag: bool
        :param matches: **参数解释**：资源名称搜索条件。 **约束限制**：最多支持1个匹配项，且key必须为resource_name。 **取值范围**：不涉及。
        :type matches: list[:class:`huaweicloudsdkmodelarts.v1.Match`]
        """
        
        

        self._workspace_id = None
        self._tags = None
        self._without_any_tag = None
        self._matches = None
        self.discriminator = None

        if workspace_id is not None:
            self.workspace_id = workspace_id
        if tags is not None:
            self.tags = tags
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if matches is not None:
            self.matches = matches

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ResourceInstancesFilterReq.

        **参数解释**：工作空间ID。未创建工作空间时默认值为\"0\"，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :return: The workspace_id of this ResourceInstancesFilterReq.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ResourceInstancesFilterReq.

        **参数解释**：工作空间ID。未创建工作空间时默认值为\"0\"，存在创建并使用的工作空间，以实际取值为准。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :param workspace_id: The workspace_id of this ResourceInstancesFilterReq.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def tags(self):
        r"""Gets the tags of this ResourceInstancesFilterReq.

        **参数解释**：标签筛选条件，按标签key-value对筛选作业。同一key下多个value为OR关系，不同key之间为AND关系。 **约束限制**：同一key的values不能重复，不同key不能重复。 **取值范围**：不涉及。

        :return: The tags of this ResourceInstancesFilterReq.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.MutiValueTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ResourceInstancesFilterReq.

        **参数解释**：标签筛选条件，按标签key-value对筛选作业。同一key下多个value为OR关系，不同key之间为AND关系。 **约束限制**：同一key的values不能重复，不同key不能重复。 **取值范围**：不涉及。

        :param tags: The tags of this ResourceInstancesFilterReq.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.MutiValueTag`]
        """
        self._tags = tags

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this ResourceInstancesFilterReq.

        **参数解释**：是否查询没有任何标签的作业。 **约束限制**：设为true时忽略tags筛选条件。 **取值范围**： - true：仅查询无标签的作业 - false：按tags条件筛选 **默认取值**：false。

        :return: The without_any_tag of this ResourceInstancesFilterReq.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this ResourceInstancesFilterReq.

        **参数解释**：是否查询没有任何标签的作业。 **约束限制**：设为true时忽略tags筛选条件。 **取值范围**： - true：仅查询无标签的作业 - false：按tags条件筛选 **默认取值**：false。

        :param without_any_tag: The without_any_tag of this ResourceInstancesFilterReq.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def matches(self):
        r"""Gets the matches of this ResourceInstancesFilterReq.

        **参数解释**：资源名称搜索条件。 **约束限制**：最多支持1个匹配项，且key必须为resource_name。 **取值范围**：不涉及。

        :return: The matches of this ResourceInstancesFilterReq.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.Match`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this ResourceInstancesFilterReq.

        **参数解释**：资源名称搜索条件。 **约束限制**：最多支持1个匹配项，且key必须为resource_name。 **取值范围**：不涉及。

        :param matches: The matches of this ResourceInstancesFilterReq.
        :type matches: list[:class:`huaweicloudsdkmodelarts.v1.Match`]
        """
        self._matches = matches

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
        if not isinstance(other, ResourceInstancesFilterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
