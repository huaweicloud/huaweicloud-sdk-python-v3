# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubscriptionUserResponse(SdkResponse):

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
        'count': 'int',
        'subscription_users': 'list[ListSubscriptionUserResponseItemInfo]'
    }

    attribute_map = {
        'request_id': 'request_id',
        'count': 'count',
        'subscription_users': 'subscription_users'
    }

    def __init__(self, request_id=None, count=None, subscription_users=None):
        r"""ListSubscriptionUserResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param count: 订阅用户数量。
        :type count: int
        :param subscription_users: 订阅用户信息列表。
        :type subscription_users: list[:class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseItemInfo`]
        """
        
        super(ListSubscriptionUserResponse, self).__init__()

        self._request_id = None
        self._count = None
        self._subscription_users = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if count is not None:
            self.count = count
        if subscription_users is not None:
            self.subscription_users = subscription_users

    @property
    def request_id(self):
        r"""Gets the request_id of this ListSubscriptionUserResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListSubscriptionUserResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListSubscriptionUserResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListSubscriptionUserResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def count(self):
        r"""Gets the count of this ListSubscriptionUserResponse.

        订阅用户数量。

        :return: The count of this ListSubscriptionUserResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSubscriptionUserResponse.

        订阅用户数量。

        :param count: The count of this ListSubscriptionUserResponse.
        :type count: int
        """
        self._count = count

    @property
    def subscription_users(self):
        r"""Gets the subscription_users of this ListSubscriptionUserResponse.

        订阅用户信息列表。

        :return: The subscription_users of this ListSubscriptionUserResponse.
        :rtype: list[:class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseItemInfo`]
        """
        return self._subscription_users

    @subscription_users.setter
    def subscription_users(self, subscription_users):
        r"""Sets the subscription_users of this ListSubscriptionUserResponse.

        订阅用户信息列表。

        :param subscription_users: The subscription_users of this ListSubscriptionUserResponse.
        :type subscription_users: list[:class:`huaweicloudsdksmnglobal.v2.ListSubscriptionUserResponseItemInfo`]
        """
        self._subscription_users = subscription_users

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
        if not isinstance(other, ListSubscriptionUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
