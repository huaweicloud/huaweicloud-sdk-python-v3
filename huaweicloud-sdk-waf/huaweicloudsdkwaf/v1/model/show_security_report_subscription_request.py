# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSecurityReportSubscriptionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_id': 'str'
    }

    attribute_map = {
        'subscription_id': 'subscription_id'
    }

    def __init__(self, subscription_id=None):
        r"""ShowSecurityReportSubscriptionRequest

        The model defined in huaweicloud sdk

        :param subscription_id: **参数解释：** 需要查询的订阅id，从“查询安全报告订阅列表”中获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type subscription_id: str
        """
        
        

        self._subscription_id = None
        self.discriminator = None

        self.subscription_id = subscription_id

    @property
    def subscription_id(self):
        r"""Gets the subscription_id of this ShowSecurityReportSubscriptionRequest.

        **参数解释：** 需要查询的订阅id，从“查询安全报告订阅列表”中获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The subscription_id of this ShowSecurityReportSubscriptionRequest.
        :rtype: str
        """
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, subscription_id):
        r"""Sets the subscription_id of this ShowSecurityReportSubscriptionRequest.

        **参数解释：** 需要查询的订阅id，从“查询安全报告订阅列表”中获取 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param subscription_id: The subscription_id of this ShowSecurityReportSubscriptionRequest.
        :type subscription_id: str
        """
        self._subscription_id = subscription_id

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
        if not isinstance(other, ShowSecurityReportSubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
