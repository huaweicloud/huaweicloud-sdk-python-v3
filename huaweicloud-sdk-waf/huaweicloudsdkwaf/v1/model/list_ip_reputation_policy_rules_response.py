# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIpReputationPolicyRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'items': 'list[IpReputationRulesListInfo]'
    }

    attribute_map = {
        'total': 'total',
        'items': 'items'
    }

    def __init__(self, total=None, items=None):
        r"""ListIpReputationPolicyRulesResponse

        The model defined in huaweicloud sdk

        :param total: **参数解释：** Number of rules in the policy **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type total: int
        :param items: **参数解释：** Array of IpReputation rules **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type items: list[:class:`huaweicloudsdkwaf.v1.IpReputationRulesListInfo`]
        """
        
        super(ListIpReputationPolicyRulesResponse, self).__init__()

        self._total = None
        self._items = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if items is not None:
            self.items = items

    @property
    def total(self):
        r"""Gets the total of this ListIpReputationPolicyRulesResponse.

        **参数解释：** Number of rules in the policy **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The total of this ListIpReputationPolicyRulesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListIpReputationPolicyRulesResponse.

        **参数解释：** Number of rules in the policy **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param total: The total of this ListIpReputationPolicyRulesResponse.
        :type total: int
        """
        self._total = total

    @property
    def items(self):
        r"""Gets the items of this ListIpReputationPolicyRulesResponse.

        **参数解释：** Array of IpReputation rules **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The items of this ListIpReputationPolicyRulesResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.IpReputationRulesListInfo`]
        """
        return self._items

    @items.setter
    def items(self, items):
        r"""Sets the items of this ListIpReputationPolicyRulesResponse.

        **参数解释：** Array of IpReputation rules **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param items: The items of this ListIpReputationPolicyRulesResponse.
        :type items: list[:class:`huaweicloudsdkwaf.v1.IpReputationRulesListInfo`]
        """
        self._items = items

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListIpReputationPolicyRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
