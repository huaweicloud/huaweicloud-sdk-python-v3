# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PollingPolicyResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'order': 'int',
        'subscriptions': 'list[PollingPolicySubscriptionDetails]'
    }

    attribute_map = {
        'order': 'order',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, order=None, subscriptions=None):
        r"""PollingPolicyResponse

        The model defined in huaweicloud sdk

        :param order: 当前轮询的序号。
        :type order: int
        :param subscriptions: 订阅终端urn列表。
        :type subscriptions: list[:class:`huaweicloudsdksmn.v2.PollingPolicySubscriptionDetails`]
        """
        
        

        self._order = None
        self._subscriptions = None
        self.discriminator = None

        if order is not None:
            self.order = order
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def order(self):
        r"""Gets the order of this PollingPolicyResponse.

        当前轮询的序号。

        :return: The order of this PollingPolicyResponse.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        r"""Sets the order of this PollingPolicyResponse.

        当前轮询的序号。

        :param order: The order of this PollingPolicyResponse.
        :type order: int
        """
        self._order = order

    @property
    def subscriptions(self):
        r"""Gets the subscriptions of this PollingPolicyResponse.

        订阅终端urn列表。

        :return: The subscriptions of this PollingPolicyResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.PollingPolicySubscriptionDetails`]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        r"""Sets the subscriptions of this PollingPolicyResponse.

        订阅终端urn列表。

        :param subscriptions: The subscriptions of this PollingPolicyResponse.
        :type subscriptions: list[:class:`huaweicloudsdksmn.v2.PollingPolicySubscriptionDetails`]
        """
        self._subscriptions = subscriptions

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
        if not isinstance(other, PollingPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
