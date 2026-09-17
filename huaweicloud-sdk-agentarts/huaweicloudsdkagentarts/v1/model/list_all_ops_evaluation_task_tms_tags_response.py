# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllOpsEvaluationTaskTmsTagsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'list[OpsTmsTagFilter]',
        'sys_tags': 'list[OpsTmsTagFilter]',
        'total_count': 'int'
    }

    attribute_map = {
        'tags': 'tags',
        'sys_tags': 'sys_tags',
        'total_count': 'total_count'
    }

    def __init__(self, tags=None, sys_tags=None, total_count=None):
        r"""ListAllOpsEvaluationTaskTmsTagsResponse

        The model defined in huaweicloud sdk

        :param tags: **参数解释：** 用户标签列表，包含所有出现在账号下的用户标签键及其值集合（已分页）。数组元素为OpsTmsTagFilter对象，包含key和values字段。 **约束限制：** 不涉及。
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        :param sys_tags: **参数解释：** 系统标签列表，仅op_service权限可获取。包含所有出现在账号下的系统标签键及其值集合。数组元素为OpsTmsTagFilter对象，包含key和values字段。 **约束限制：** 不涉及。
        :type sys_tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        :param total_count: **参数解释：** 用户标签总数数量（分页后的总数），取值为分页前tags数组的长度。 **约束限制：** 不涉及。 **取值范围：** 不涉及。
        :type total_count: int
        """
        
        super().__init__()

        self._tags = None
        self._sys_tags = None
        self._total_count = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if sys_tags is not None:
            self.sys_tags = sys_tags
        if total_count is not None:
            self.total_count = total_count

    @property
    def tags(self):
        r"""Gets the tags of this ListAllOpsEvaluationTaskTmsTagsResponse.

        **参数解释：** 用户标签列表，包含所有出现在账号下的用户标签键及其值集合（已分页）。数组元素为OpsTmsTagFilter对象，包含key和values字段。 **约束限制：** 不涉及。

        :return: The tags of this ListAllOpsEvaluationTaskTmsTagsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ListAllOpsEvaluationTaskTmsTagsResponse.

        **参数解释：** 用户标签列表，包含所有出现在账号下的用户标签键及其值集合（已分页）。数组元素为OpsTmsTagFilter对象，包含key和values字段。 **约束限制：** 不涉及。

        :param tags: The tags of this ListAllOpsEvaluationTaskTmsTagsResponse.
        :type tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        """
        self._tags = tags

    @property
    def sys_tags(self):
        r"""Gets the sys_tags of this ListAllOpsEvaluationTaskTmsTagsResponse.

        **参数解释：** 系统标签列表，仅op_service权限可获取。包含所有出现在账号下的系统标签键及其值集合。数组元素为OpsTmsTagFilter对象，包含key和values字段。 **约束限制：** 不涉及。

        :return: The sys_tags of this ListAllOpsEvaluationTaskTmsTagsResponse.
        :rtype: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        """
        return self._sys_tags

    @sys_tags.setter
    def sys_tags(self, sys_tags):
        r"""Sets the sys_tags of this ListAllOpsEvaluationTaskTmsTagsResponse.

        **参数解释：** 系统标签列表，仅op_service权限可获取。包含所有出现在账号下的系统标签键及其值集合。数组元素为OpsTmsTagFilter对象，包含key和values字段。 **约束限制：** 不涉及。

        :param sys_tags: The sys_tags of this ListAllOpsEvaluationTaskTmsTagsResponse.
        :type sys_tags: list[:class:`huaweicloudsdkagentarts.v1.OpsTmsTagFilter`]
        """
        self._sys_tags = sys_tags

    @property
    def total_count(self):
        r"""Gets the total_count of this ListAllOpsEvaluationTaskTmsTagsResponse.

        **参数解释：** 用户标签总数数量（分页后的总数），取值为分页前tags数组的长度。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :return: The total_count of this ListAllOpsEvaluationTaskTmsTagsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListAllOpsEvaluationTaskTmsTagsResponse.

        **参数解释：** 用户标签总数数量（分页后的总数），取值为分页前tags数组的长度。 **约束限制：** 不涉及。 **取值范围：** 不涉及。

        :param total_count: The total_count of this ListAllOpsEvaluationTaskTmsTagsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListAllOpsEvaluationTaskTmsTagsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAllOpsEvaluationTaskTmsTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
