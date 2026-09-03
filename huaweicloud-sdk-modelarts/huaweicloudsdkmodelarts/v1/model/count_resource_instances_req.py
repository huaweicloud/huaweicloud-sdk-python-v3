# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CountResourceInstancesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[CountResourceInstancesReqTags]',
        'matches': 'list[CountResourceInstancesReqMatches]',
        'workspace_id': 'str',
        'without_any_tag': 'bool'
    }

    attribute_map = {
        'tags': 'tags',
        'matches': 'matches',
        'workspace_id': 'workspace_id',
        'without_any_tag': 'without_any_tag'
    }

    def __init__(self, tags=None, matches=None, workspace_id=None, without_any_tag=None):
        r"""CountResourceInstancesReq

        The model defined in huaweicloud sdk

        :param tags: **参数解释**：标签过滤条件，返回同时包含列表中所有标签的训练作业。 **约束限制**：标签个数不能超过系统允许的最大标签数。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.CountResourceInstancesReqTags`]
        :param matches: **参数解释**：模糊匹配条件，支持按资源名称等字段进行模糊查询。 **约束限制**：最多1个匹配条件。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type matches: list[:class:`huaweicloudsdkmodelarts.v1.CountResourceInstancesReqMatches`]
        :param workspace_id: **参数解释**：工作空间ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。
        :type workspace_id: str
        :param without_any_tag: **参数解释**：是否查询不带任何标签的训练作业。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：false。
        :type without_any_tag: bool
        """
        
        

        self._tags = None
        self._matches = None
        self._workspace_id = None
        self._without_any_tag = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if matches is not None:
            self.matches = matches
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if without_any_tag is not None:
            self.without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this CountResourceInstancesReq.

        **参数解释**：标签过滤条件，返回同时包含列表中所有标签的训练作业。 **约束限制**：标签个数不能超过系统允许的最大标签数。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The tags of this CountResourceInstancesReq.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.CountResourceInstancesReqTags`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CountResourceInstancesReq.

        **参数解释**：标签过滤条件，返回同时包含列表中所有标签的训练作业。 **约束限制**：标签个数不能超过系统允许的最大标签数。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param tags: The tags of this CountResourceInstancesReq.
        :type tags: list[:class:`huaweicloudsdkmodelarts.v1.CountResourceInstancesReqTags`]
        """
        self._tags = tags

    @property
    def matches(self):
        r"""Gets the matches of this CountResourceInstancesReq.

        **参数解释**：模糊匹配条件，支持按资源名称等字段进行模糊查询。 **约束限制**：最多1个匹配条件。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The matches of this CountResourceInstancesReq.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.CountResourceInstancesReqMatches`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this CountResourceInstancesReq.

        **参数解释**：模糊匹配条件，支持按资源名称等字段进行模糊查询。 **约束限制**：最多1个匹配条件。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param matches: The matches of this CountResourceInstancesReq.
        :type matches: list[:class:`huaweicloudsdkmodelarts.v1.CountResourceInstancesReqMatches`]
        """
        self._matches = matches

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CountResourceInstancesReq.

        **参数解释**：工作空间ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :return: The workspace_id of this CountResourceInstancesReq.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CountResourceInstancesReq.

        **参数解释**：工作空间ID。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：0。

        :param workspace_id: The workspace_id of this CountResourceInstancesReq.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this CountResourceInstancesReq.

        **参数解释**：是否查询不带任何标签的训练作业。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：false。

        :return: The without_any_tag of this CountResourceInstancesReq.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this CountResourceInstancesReq.

        **参数解释**：是否查询不带任何标签的训练作业。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：false。

        :param without_any_tag: The without_any_tag of this CountResourceInstancesReq.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

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
        if not isinstance(other, CountResourceInstancesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
