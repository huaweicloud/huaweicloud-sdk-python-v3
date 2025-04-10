# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddSubscriptionFromSubscriptionUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subscriptions_result': 'list[AddSubscriptionFromSubscriptionUserResponseItem]'
    }

    attribute_map = {
        'subscriptions_result': 'subscriptions_result'
    }

    def __init__(self, subscriptions_result=None):
        r"""AddSubscriptionFromSubscriptionUserResponse

        The model defined in huaweicloud sdk

        :param subscriptions_result: 添加订阅返回结果。
        :type subscriptions_result: list[:class:`huaweicloudsdksmn.v2.AddSubscriptionFromSubscriptionUserResponseItem`]
        """
        
        super(AddSubscriptionFromSubscriptionUserResponse, self).__init__()

        self._subscriptions_result = None
        self.discriminator = None

        if subscriptions_result is not None:
            self.subscriptions_result = subscriptions_result

    @property
    def subscriptions_result(self):
        r"""Gets the subscriptions_result of this AddSubscriptionFromSubscriptionUserResponse.

        添加订阅返回结果。

        :return: The subscriptions_result of this AddSubscriptionFromSubscriptionUserResponse.
        :rtype: list[:class:`huaweicloudsdksmn.v2.AddSubscriptionFromSubscriptionUserResponseItem`]
        """
        return self._subscriptions_result

    @subscriptions_result.setter
    def subscriptions_result(self, subscriptions_result):
        r"""Sets the subscriptions_result of this AddSubscriptionFromSubscriptionUserResponse.

        添加订阅返回结果。

        :param subscriptions_result: The subscriptions_result of this AddSubscriptionFromSubscriptionUserResponse.
        :type subscriptions_result: list[:class:`huaweicloudsdksmn.v2.AddSubscriptionFromSubscriptionUserResponseItem`]
        """
        self._subscriptions_result = subscriptions_result

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
        if not isinstance(other, AddSubscriptionFromSubscriptionUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
