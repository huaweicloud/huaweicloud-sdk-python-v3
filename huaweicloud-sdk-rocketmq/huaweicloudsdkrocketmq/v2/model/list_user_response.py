# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'users': 'list[User]',
        'total': 'float'
    }

    attribute_map = {
        'users': 'users',
        'total': 'total'
    }

    def __init__(self, users=None, total=None):
        r"""ListUserResponse

        The model defined in huaweicloud sdk

        :param users: 用户列表。
        :type users: list[:class:`huaweicloudsdkrocketmq.v2.User`]
        :param total: 总用户个数。
        :type total: float
        """
        
        super(ListUserResponse, self).__init__()

        self._users = None
        self._total = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if total is not None:
            self.total = total

    @property
    def users(self):
        r"""Gets the users of this ListUserResponse.

        用户列表。

        :return: The users of this ListUserResponse.
        :rtype: list[:class:`huaweicloudsdkrocketmq.v2.User`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ListUserResponse.

        用户列表。

        :param users: The users of this ListUserResponse.
        :type users: list[:class:`huaweicloudsdkrocketmq.v2.User`]
        """
        self._users = users

    @property
    def total(self):
        r"""Gets the total of this ListUserResponse.

        总用户个数。

        :return: The total of this ListUserResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListUserResponse.

        总用户个数。

        :param total: The total of this ListUserResponse.
        :type total: float
        """
        self._total = total

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
        if not isinstance(other, ListUserResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
