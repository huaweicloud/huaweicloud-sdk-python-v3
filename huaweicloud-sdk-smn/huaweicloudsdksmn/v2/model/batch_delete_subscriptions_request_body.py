# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteSubscriptionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscription_urns': 'list[BatchDeleteSubscriptionsRequestItemInfo]'
    }

    attribute_map = {
        'subscription_urns': 'subscription_urns'
    }

    def __init__(self, subscription_urns=None):
        r"""BatchDeleteSubscriptionsRequestBody

        The model defined in huaweicloud sdk

        :param subscription_urns: 订阅者信息列表。
        :type subscription_urns: list[:class:`huaweicloudsdksmn.v2.BatchDeleteSubscriptionsRequestItemInfo`]
        """
        
        

        self._subscription_urns = None
        self.discriminator = None

        self.subscription_urns = subscription_urns

    @property
    def subscription_urns(self):
        r"""Gets the subscription_urns of this BatchDeleteSubscriptionsRequestBody.

        订阅者信息列表。

        :return: The subscription_urns of this BatchDeleteSubscriptionsRequestBody.
        :rtype: list[:class:`huaweicloudsdksmn.v2.BatchDeleteSubscriptionsRequestItemInfo`]
        """
        return self._subscription_urns

    @subscription_urns.setter
    def subscription_urns(self, subscription_urns):
        r"""Sets the subscription_urns of this BatchDeleteSubscriptionsRequestBody.

        订阅者信息列表。

        :param subscription_urns: The subscription_urns of this BatchDeleteSubscriptionsRequestBody.
        :type subscription_urns: list[:class:`huaweicloudsdksmn.v2.BatchDeleteSubscriptionsRequestItemInfo`]
        """
        self._subscription_urns = subscription_urns

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
        if not isinstance(other, BatchDeleteSubscriptionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
