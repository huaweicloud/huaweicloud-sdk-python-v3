# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSubscriptionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_ids': 'list[str]',
        'clean_subscription': 'bool'
    }

    attribute_map = {
        'subscription_ids': 'subscription_ids',
        'clean_subscription': 'clean_subscription'
    }

    def __init__(self, subscription_ids=None, clean_subscription=None):
        r"""DeleteSubscriptionRequestBody

        The model defined in huaweicloud sdk

        :param subscription_ids: 删除的订阅id列表。每次删除的订阅必须属于同一实例。
        :type subscription_ids: list[str]
        :param clean_subscription: 清理订阅配置。默认为false。  true：清理。 false：不清理。
        :type clean_subscription: bool
        """
        
        

        self._subscription_ids = None
        self._clean_subscription = None
        self.discriminator = None

        self.subscription_ids = subscription_ids
        if clean_subscription is not None:
            self.clean_subscription = clean_subscription

    @property
    def subscription_ids(self):
        r"""Gets the subscription_ids of this DeleteSubscriptionRequestBody.

        删除的订阅id列表。每次删除的订阅必须属于同一实例。

        :return: The subscription_ids of this DeleteSubscriptionRequestBody.
        :rtype: list[str]
        """
        return self._subscription_ids

    @subscription_ids.setter
    def subscription_ids(self, subscription_ids):
        r"""Sets the subscription_ids of this DeleteSubscriptionRequestBody.

        删除的订阅id列表。每次删除的订阅必须属于同一实例。

        :param subscription_ids: The subscription_ids of this DeleteSubscriptionRequestBody.
        :type subscription_ids: list[str]
        """
        self._subscription_ids = subscription_ids

    @property
    def clean_subscription(self):
        r"""Gets the clean_subscription of this DeleteSubscriptionRequestBody.

        清理订阅配置。默认为false。  true：清理。 false：不清理。

        :return: The clean_subscription of this DeleteSubscriptionRequestBody.
        :rtype: bool
        """
        return self._clean_subscription

    @clean_subscription.setter
    def clean_subscription(self, clean_subscription):
        r"""Sets the clean_subscription of this DeleteSubscriptionRequestBody.

        清理订阅配置。默认为false。  true：清理。 false：不清理。

        :param clean_subscription: The clean_subscription of this DeleteSubscriptionRequestBody.
        :type clean_subscription: bool
        """
        self._clean_subscription = clean_subscription

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
        if not isinstance(other, DeleteSubscriptionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
