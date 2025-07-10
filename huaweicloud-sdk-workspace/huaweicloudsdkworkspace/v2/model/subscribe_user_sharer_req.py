# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscribeUserSharerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_sharer_sku': 'str',
        'users': 'list[User]'
    }

    attribute_map = {
        'user_sharer_sku': 'user_sharer_sku',
        'users': 'users'
    }

    def __init__(self, user_sharer_sku=None, users=None):
        r"""SubscribeUserSharerReq

        The model defined in huaweicloud sdk

        :param user_sharer_sku: 用户协同资源SKU码。
        :type user_sharer_sku: str
        :param users: 开通协同的的用户列表。
        :type users: list[:class:`huaweicloudsdkworkspace.v2.User`]
        """
        
        

        self._user_sharer_sku = None
        self._users = None
        self.discriminator = None

        self.user_sharer_sku = user_sharer_sku
        self.users = users

    @property
    def user_sharer_sku(self):
        r"""Gets the user_sharer_sku of this SubscribeUserSharerReq.

        用户协同资源SKU码。

        :return: The user_sharer_sku of this SubscribeUserSharerReq.
        :rtype: str
        """
        return self._user_sharer_sku

    @user_sharer_sku.setter
    def user_sharer_sku(self, user_sharer_sku):
        r"""Sets the user_sharer_sku of this SubscribeUserSharerReq.

        用户协同资源SKU码。

        :param user_sharer_sku: The user_sharer_sku of this SubscribeUserSharerReq.
        :type user_sharer_sku: str
        """
        self._user_sharer_sku = user_sharer_sku

    @property
    def users(self):
        r"""Gets the users of this SubscribeUserSharerReq.

        开通协同的的用户列表。

        :return: The users of this SubscribeUserSharerReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.User`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this SubscribeUserSharerReq.

        开通协同的的用户列表。

        :param users: The users of this SubscribeUserSharerReq.
        :type users: list[:class:`huaweicloudsdkworkspace.v2.User`]
        """
        self._users = users

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
        if not isinstance(other, SubscribeUserSharerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
