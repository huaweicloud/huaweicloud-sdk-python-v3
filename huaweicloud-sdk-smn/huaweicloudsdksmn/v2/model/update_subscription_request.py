# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSubscriptionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'subscription_urn': 'str',
        'body': 'UpdateSubscriptionRequestBody'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'subscription_urn': 'subscription_urn',
        'body': 'body'
    }

    def __init__(self, topic_urn=None, subscription_urn=None, body=None):
        """UpdateSubscriptionRequest

        The model defined in huaweicloud sdk

        :param topic_urn: Topic的唯一的资源标识。可以通过[查看主题列表](smn_api_51004.xml)获取该标识。
        :type topic_urn: str
        :param subscription_urn: 订阅者的唯一的资源标识，可通过[查询订阅者列表](ListSubscriptions.xml)获取该标识。
        :type subscription_urn: str
        :param body: Body of the UpdateSubscriptionRequest
        :type body: :class:`huaweicloudsdksmn.v2.UpdateSubscriptionRequestBody`
        """
        
        

        self._topic_urn = None
        self._subscription_urn = None
        self._body = None
        self.discriminator = None

        self.topic_urn = topic_urn
        self.subscription_urn = subscription_urn
        if body is not None:
            self.body = body

    @property
    def topic_urn(self):
        """Gets the topic_urn of this UpdateSubscriptionRequest.

        Topic的唯一的资源标识。可以通过[查看主题列表](smn_api_51004.xml)获取该标识。

        :return: The topic_urn of this UpdateSubscriptionRequest.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this UpdateSubscriptionRequest.

        Topic的唯一的资源标识。可以通过[查看主题列表](smn_api_51004.xml)获取该标识。

        :param topic_urn: The topic_urn of this UpdateSubscriptionRequest.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def subscription_urn(self):
        """Gets the subscription_urn of this UpdateSubscriptionRequest.

        订阅者的唯一的资源标识，可通过[查询订阅者列表](ListSubscriptions.xml)获取该标识。

        :return: The subscription_urn of this UpdateSubscriptionRequest.
        :rtype: str
        """
        return self._subscription_urn

    @subscription_urn.setter
    def subscription_urn(self, subscription_urn):
        """Sets the subscription_urn of this UpdateSubscriptionRequest.

        订阅者的唯一的资源标识，可通过[查询订阅者列表](ListSubscriptions.xml)获取该标识。

        :param subscription_urn: The subscription_urn of this UpdateSubscriptionRequest.
        :type subscription_urn: str
        """
        self._subscription_urn = subscription_urn

    @property
    def body(self):
        """Gets the body of this UpdateSubscriptionRequest.

        :return: The body of this UpdateSubscriptionRequest.
        :rtype: :class:`huaweicloudsdksmn.v2.UpdateSubscriptionRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateSubscriptionRequest.

        :param body: The body of this UpdateSubscriptionRequest.
        :type body: :class:`huaweicloudsdksmn.v2.UpdateSubscriptionRequestBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateSubscriptionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
