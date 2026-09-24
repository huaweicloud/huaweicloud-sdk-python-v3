# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InlineResponse204Data:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_ids': 'list[str]',
        'failed_ids': 'list[str]',
        'total_requested': 'int',
        'total_deleted': 'int'
    }

    attribute_map = {
        'success_ids': 'success_ids',
        'failed_ids': 'failed_ids',
        'total_requested': 'total_requested',
        'total_deleted': 'total_deleted'
    }

    def __init__(self, success_ids=None, failed_ids=None, total_requested=None, total_deleted=None):
        r"""InlineResponse204Data

        The model defined in huaweicloud sdk

        :param success_ids: **参数解释：** 成功删除的任务ID列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type success_ids: list[str]
        :param failed_ids: **参数解释：** 删除失败的任务ID列表（通常因为ID不存在、状态已删除或权限不足）。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type failed_ids: list[str]
        :param total_requested: **参数解释：** 请求删除的任务总数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 **默认取值：** 不涉及。 
        :type total_requested: int
        :param total_deleted: **参数解释：** 实际删除成功的任务数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 **默认取值：** 不涉及。 
        :type total_deleted: int
        """
        
        

        self._success_ids = None
        self._failed_ids = None
        self._total_requested = None
        self._total_deleted = None
        self.discriminator = None

        self.success_ids = success_ids
        self.failed_ids = failed_ids
        self.total_requested = total_requested
        self.total_deleted = total_deleted

    @property
    def success_ids(self):
        r"""Gets the success_ids of this InlineResponse204Data.

        **参数解释：** 成功删除的任务ID列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The success_ids of this InlineResponse204Data.
        :rtype: list[str]
        """
        return self._success_ids

    @success_ids.setter
    def success_ids(self, success_ids):
        r"""Sets the success_ids of this InlineResponse204Data.

        **参数解释：** 成功删除的任务ID列表。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param success_ids: The success_ids of this InlineResponse204Data.
        :type success_ids: list[str]
        """
        self._success_ids = success_ids

    @property
    def failed_ids(self):
        r"""Gets the failed_ids of this InlineResponse204Data.

        **参数解释：** 删除失败的任务ID列表（通常因为ID不存在、状态已删除或权限不足）。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The failed_ids of this InlineResponse204Data.
        :rtype: list[str]
        """
        return self._failed_ids

    @failed_ids.setter
    def failed_ids(self, failed_ids):
        r"""Sets the failed_ids of this InlineResponse204Data.

        **参数解释：** 删除失败的任务ID列表（通常因为ID不存在、状态已删除或权限不足）。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param failed_ids: The failed_ids of this InlineResponse204Data.
        :type failed_ids: list[str]
        """
        self._failed_ids = failed_ids

    @property
    def total_requested(self):
        r"""Gets the total_requested of this InlineResponse204Data.

        **参数解释：** 请求删除的任务总数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 **默认取值：** 不涉及。 

        :return: The total_requested of this InlineResponse204Data.
        :rtype: int
        """
        return self._total_requested

    @total_requested.setter
    def total_requested(self, total_requested):
        r"""Sets the total_requested of this InlineResponse204Data.

        **参数解释：** 请求删除的任务总数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 **默认取值：** 不涉及。 

        :param total_requested: The total_requested of this InlineResponse204Data.
        :type total_requested: int
        """
        self._total_requested = total_requested

    @property
    def total_deleted(self):
        r"""Gets the total_deleted of this InlineResponse204Data.

        **参数解释：** 实际删除成功的任务数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 **默认取值：** 不涉及。 

        :return: The total_deleted of this InlineResponse204Data.
        :rtype: int
        """
        return self._total_deleted

    @total_deleted.setter
    def total_deleted(self, total_deleted):
        r"""Sets the total_deleted of this InlineResponse204Data.

        **参数解释：** 实际删除成功的任务数。 **约束限制：** 不涉及。 **取值范围：** 非负整数。 **默认取值：** 不涉及。 

        :param total_deleted: The total_deleted of this InlineResponse204Data.
        :type total_deleted: int
        """
        self._total_deleted = total_deleted

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
        if not isinstance(other, InlineResponse204Data):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
