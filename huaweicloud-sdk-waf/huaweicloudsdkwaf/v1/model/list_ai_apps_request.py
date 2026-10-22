# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiAppsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'protect_status': 'int',
        'policy_id': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'protect_status': 'protect_status',
        'policy_id': 'policy_id'
    }

    def __init__(self, limit=None, offset=None, name=None, protect_status=None, policy_id=None):
        r"""ListAiAppsRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释：** 最大返回条目数 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 10
        :type limit: int
        :param offset: **参数解释：** 跳过的条目数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 0
        :type offset: int
        :param name: **参数解释：** 按应用名称过滤 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        :param protect_status: **参数解释：** 按防护状态过滤 **约束限制：** 不涉及 **取值范围：** 0(禁用), 1(启用) **默认取值：** 不涉及
        :type protect_status: int
        :param policy_id: **参数解释：** 按策略ID过滤 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type policy_id: str
        """
        
        

        self._limit = None
        self._offset = None
        self._name = None
        self._protect_status = None
        self._policy_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if protect_status is not None:
            self.protect_status = protect_status
        if policy_id is not None:
            self.policy_id = policy_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAiAppsRequest.

        **参数解释：** 最大返回条目数 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 10

        :return: The limit of this ListAiAppsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAiAppsRequest.

        **参数解释：** 最大返回条目数 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 10

        :param limit: The limit of this ListAiAppsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAiAppsRequest.

        **参数解释：** 跳过的条目数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 0

        :return: The offset of this ListAiAppsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAiAppsRequest.

        **参数解释：** 跳过的条目数 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 0

        :param offset: The offset of this ListAiAppsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListAiAppsRequest.

        **参数解释：** 按应用名称过滤 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this ListAiAppsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAiAppsRequest.

        **参数解释：** 按应用名称过滤 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this ListAiAppsRequest.
        :type name: str
        """
        self._name = name

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ListAiAppsRequest.

        **参数解释：** 按防护状态过滤 **约束限制：** 不涉及 **取值范围：** 0(禁用), 1(启用) **默认取值：** 不涉及

        :return: The protect_status of this ListAiAppsRequest.
        :rtype: int
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ListAiAppsRequest.

        **参数解释：** 按防护状态过滤 **约束限制：** 不涉及 **取值范围：** 0(禁用), 1(启用) **默认取值：** 不涉及

        :param protect_status: The protect_status of this ListAiAppsRequest.
        :type protect_status: int
        """
        self._protect_status = protect_status

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListAiAppsRequest.

        **参数解释：** 按策略ID过滤 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The policy_id of this ListAiAppsRequest.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListAiAppsRequest.

        **参数解释：** 按策略ID过滤 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param policy_id: The policy_id of this ListAiAppsRequest.
        :type policy_id: str
        """
        self._policy_id = policy_id

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
        if not isinstance(other, ListAiAppsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
