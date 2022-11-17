# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionsByTopicResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'subscription_count': 'int',
        'subscriptions': 'list[ListSubscriptionsItem]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'subscription_count': 'subscription_count',
        'subscriptions': 'subscriptions'
    }

    def __init__(self, request_id=None, subscription_count=None, subscriptions=None):
        """ListSubscriptionsByTopicResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param subscription_count: 订阅者个数。
        :type subscription_count: int
        :param subscriptions: Subscription结构体。
        :type subscriptions: list[:class:`huaweicloudsdksmn.v2.ListSubscriptionsItem`]
        """
        
        super(ListSubscriptionsByTopicResponse, self).__init__()

        self._request_id = None
        self._subscription_count = None
        self._subscriptions = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if subscription_count is not None:
            self.subscription_count = subscription_count
        if subscriptions is not None:
            self.subscriptions = subscriptions

    @property
    def request_id(self):
        """Gets the request_id of this ListSubscriptionsByTopicResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListSubscriptionsByTopicResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListSubscriptionsByTopicResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListSubscriptionsByTopicResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def subscription_count(self):
        """Gets the subscription_count of this ListSubscriptionsByTopicResponse.

        订阅者个数。

        :return: The subscription_count of this ListSubscriptionsByTopicResponse.
        :rtype: int
        """
        return self._subscription_count

    @subscription_count.setter
    def subscription_count(self, subscription_count):
        """Sets the subscription_count of this ListSubscriptionsByTopicResponse.

        订阅者个数。

        :param subscription_count: The subscription_count of this ListSubscriptionsByTopicResponse.
        :type subscription_count: int
        """
        self._subscription_count = subscription_count

    @property
    def subscriptions(self):
        """Gets the subscriptions of this ListSubscriptionsByTopicResponse.

        Subscription结构体。

        :return: The subscriptions of this ListSubscriptionsByTopicResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.ListSubscriptionsItem`]
        """
        return self._subscriptions

    @subscriptions.setter
    def subscriptions(self, subscriptions):
        """Sets the subscriptions of this ListSubscriptionsByTopicResponse.

        Subscription结构体。

        :param subscriptions: The subscriptions of this ListSubscriptionsByTopicResponse.
        :type subscriptions: list[:class:`huaweicloudsdksmn.v2.ListSubscriptionsItem`]
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
        if not isinstance(other, ListSubscriptionsByTopicResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
