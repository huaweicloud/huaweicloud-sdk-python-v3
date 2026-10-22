# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAiGuardPolicyRequest:

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
        'name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name'
    }

    def __init__(self, limit=None, offset=None, name=None):
        r"""ListAiGuardPolicyRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释：** 最大数量 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 10
        :type limit: int
        :param offset: **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 0-10000 **默认取值：** 0
        :type offset: int
        :param name: **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type name: str
        """
        
        

        self._limit = None
        self._offset = None
        self._name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListAiGuardPolicyRequest.

        **参数解释：** 最大数量 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 10

        :return: The limit of this ListAiGuardPolicyRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAiGuardPolicyRequest.

        **参数解释：** 最大数量 **约束限制：** 不涉及 **取值范围：** 1-100 **默认取值：** 10

        :param limit: The limit of this ListAiGuardPolicyRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAiGuardPolicyRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 0-10000 **默认取值：** 0

        :return: The offset of this ListAiGuardPolicyRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAiGuardPolicyRequest.

        **参数解释：** 偏移量 **约束限制：** 不涉及 **取值范围：** 0-10000 **默认取值：** 0

        :param offset: The offset of this ListAiGuardPolicyRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListAiGuardPolicyRequest.

        **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The name of this ListAiGuardPolicyRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListAiGuardPolicyRequest.

        **参数解释：** 策略名称 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param name: The name of this ListAiGuardPolicyRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListAiGuardPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
