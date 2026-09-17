# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsQueryResourceInstancesFilterRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'without_any_tag': 'bool',
        'tags': 'list[OpsTmsTagFilter]',
        'sys_tags': 'list[OpsTmsTagFilter]',
        'matches': 'list[OpsTmsMatch]'
    }

    attribute_map = {
        'without_any_tag': 'without_any_tag',
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'matches': 'matches'
    }

    def __init__(self, without_any_tag=None, tags=None, sys_tags=None, matches=None):
        r"""OpsQueryResourceInstancesFilterRequestBody

        The model defined in huaweicloud sdk

        :param without_any_tag: **参数解释：** 是否查询未打标签的资源。 **约束限制：** 不涉及。 **取值范围：** - true：查询所有不带标签的资源，此时忽略tags和sys_tags字段。 - false：正常按标签条件过滤。 **默认取值：** 不涉及。
        :type without_any_tag: bool
        :param tags: **参数解释：** 用户标签匹配条件列表。数组元素为OpsTmsTagFilter对象，包含key和values字段。最多包含20个key，每个key下最多20个value。Key不能重复，同一个key中values不能重复。key之间是与关系，key-value结构中value是或关系。无tag过滤条件时返回全量数据。value以*开头时使用LIKE模糊匹配（contains），否则使用精确匹配。 **约束限制：** 数组元素最大数量为20。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        :param sys_tags: **参数解释：** 系统标签匹配条件列表。数组元素为OpsTmsTagFilter对象，包含key和values字段。仅op_service权限可使用。与tags字段可同时使用（与关系），key之间是与关系，key-value结构中value是或关系。无sys_tags时按照仅tags条件处理。value以*开头时使用LIKE模糊匹配（contains），否则使用精确匹配。 **约束限制：** 数组元素最大数量为20。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type sys_tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        :param matches: **参数解释：** 标签匹配条件列表。数组元素为OpsTmsMatch对象，包含key和value字段。多个match之间为OR关系。key支持resource_name（前缀模糊匹配，空值精确匹配空串返回空列表）和resource_id（精确匹配，空值返回空列表）。 **约束限制：** 数组元素最大数量为20。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type matches: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsMatch`]
        """
        
        

        self._without_any_tag = None
        self._tags = None
        self._sys_tags = None
        self._matches = None
        self.discriminator = None

        if without_any_tag is not None:
            self.without_any_tag = without_any_tag
        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if matches is not None:
            self.matches = matches

    @property
    def without_any_tag(self):
        r"""Gets the without_any_tag of this OpsQueryResourceInstancesFilterRequestBody.

        **参数解释：** 是否查询未打标签的资源。 **约束限制：** 不涉及。 **取值范围：** - true：查询所有不带标签的资源，此时忽略tags和sys_tags字段。 - false：正常按标签条件过滤。 **默认取值：** 不涉及。

        :return: The without_any_tag of this OpsQueryResourceInstancesFilterRequestBody.
        :rtype: bool
        """
        return self._without_any_tag

    @without_any_tag.setter
    def without_any_tag(self, without_any_tag):
        r"""Sets the without_any_tag of this OpsQueryResourceInstancesFilterRequestBody.

        **参数解释：** 是否查询未打标签的资源。 **约束限制：** 不涉及。 **取值范围：** - true：查询所有不带标签的资源，此时忽略tags和sys_tags字段。 - false：正常按标签条件过滤。 **默认取值：** 不涉及。

        :param without_any_tag: The without_any_tag of this OpsQueryResourceInstancesFilterRequestBody.
        :type without_any_tag: bool
        """
        self._without_any_tag = without_any_tag

    @property
    def tags(self):
        r"""Gets the tags of this OpsQueryResourceInstancesFilterRequestBody.

        **参数解释：** 用户标签匹配条件列表。数组元素为OpsTmsTagFilter对象，包含key和values字段。最多包含20个key，每个key下最多20个value。Key不能重复，同一个key中values不能重复。key之间是与关系，key-value结构中value是或关系。无tag过滤条件时返回全量数据。value以*开头时使用LIKE模糊匹配（contains），否则使用精确匹配。 **约束限制：** 数组元素最大数量为20。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The tags of this OpsQueryResourceInstancesFilterRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this OpsQueryResourceInstancesFilterRequestBody.

        **参数解释：** 用户标签匹配条件列表。数组元素为OpsTmsTagFilter对象，包含key和values字段。最多包含20个key，每个key下最多20个value。Key不能重复，同一个key中values不能重复。key之间是与关系，key-value结构中value是或关系。无tag过滤条件时返回全量数据。value以*开头时使用LIKE模糊匹配（contains），否则使用精确匹配。 **约束限制：** 数组元素最大数量为20。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param tags: The tags of this OpsQueryResourceInstancesFilterRequestBody.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this OpsQueryResourceInstancesFilterRequestBody.

        **参数解释：** 系统标签匹配条件列表。数组元素为OpsTmsTagFilter对象，包含key和values字段。仅op_service权限可使用。与tags字段可同时使用（与关系），key之间是与关系，key-value结构中value是或关系。无sys_tags时按照仅tags条件处理。value以*开头时使用LIKE模糊匹配（contains），否则使用精确匹配。 **约束限制：** 数组元素最大数量为20。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The sys_tags of this OpsQueryResourceInstancesFilterRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this OpsQueryResourceInstancesFilterRequestBody.

        **参数解释：** 系统标签匹配条件列表。数组元素为OpsTmsTagFilter对象，包含key和values字段。仅op_service权限可使用。与tags字段可同时使用（与关系），key之间是与关系，key-value结构中value是或关系。无sys_tags时按照仅tags条件处理。value以*开头时使用LIKE模糊匹配（contains），否则使用精确匹配。 **约束限制：** 数组元素最大数量为20。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param sys_tags: The sys_tags of this OpsQueryResourceInstancesFilterRequestBody.
        :type sys_tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        """
        self._sys_tags = sys_tags

    @property
    def matches(self):
        r"""Gets the matches of this OpsQueryResourceInstancesFilterRequestBody.

        **参数解释：** 标签匹配条件列表。数组元素为OpsTmsMatch对象，包含key和value字段。多个match之间为OR关系。key支持resource_name（前缀模糊匹配，空值精确匹配空串返回空列表）和resource_id（精确匹配，空值返回空列表）。 **约束限制：** 数组元素最大数量为20。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The matches of this OpsQueryResourceInstancesFilterRequestBody.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsMatch`]
        """
        return self._matches

    @matches.setter
    def matches(self, matches):
        r"""Sets the matches of this OpsQueryResourceInstancesFilterRequestBody.

        **参数解释：** 标签匹配条件列表。数组元素为OpsTmsMatch对象，包含key和value字段。多个match之间为OR关系。key支持resource_name（前缀模糊匹配，空值精确匹配空串返回空列表）和resource_id（精确匹配，空值返回空列表）。 **约束限制：** 数组元素最大数量为20。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param matches: The matches of this OpsQueryResourceInstancesFilterRequestBody.
        :type matches: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsMatch`]
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
        if not isinstance(other, OpsQueryResourceInstancesFilterRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
