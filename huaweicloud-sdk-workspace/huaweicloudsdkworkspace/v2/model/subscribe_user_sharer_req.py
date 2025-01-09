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
        'order_id': 'str',
        'users': 'list[User]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'user_sharer_sku': 'user_sharer_sku',
        'order_id': 'order_id',
        'users': 'users',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, user_sharer_sku=None, order_id=None, users=None, enterprise_project_id=None):
        """SubscribeUserSharerReq

        The model defined in huaweicloud sdk

        :param user_sharer_sku: 用户协同资源SKU码
        :type user_sharer_sku: str
        :param order_id: 订单ID
        :type order_id: str
        :param users: 开通协同的的用户列表。
        :type users: list[:class:`huaweicloudsdkworkspace.v2.User`]
        :param enterprise_project_id: 企业项目ID
        :type enterprise_project_id: str
        """
        
        

        self._user_sharer_sku = None
        self._order_id = None
        self._users = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.user_sharer_sku = user_sharer_sku
        if order_id is not None:
            self.order_id = order_id
        self.users = users
        self.enterprise_project_id = enterprise_project_id

    @property
    def user_sharer_sku(self):
        """Gets the user_sharer_sku of this SubscribeUserSharerReq.

        用户协同资源SKU码

        :return: The user_sharer_sku of this SubscribeUserSharerReq.
        :rtype: str
        """
        return self._user_sharer_sku

    @user_sharer_sku.setter
    def user_sharer_sku(self, user_sharer_sku):
        """Sets the user_sharer_sku of this SubscribeUserSharerReq.

        用户协同资源SKU码

        :param user_sharer_sku: The user_sharer_sku of this SubscribeUserSharerReq.
        :type user_sharer_sku: str
        """
        self._user_sharer_sku = user_sharer_sku

    @property
    def order_id(self):
        """Gets the order_id of this SubscribeUserSharerReq.

        订单ID

        :return: The order_id of this SubscribeUserSharerReq.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this SubscribeUserSharerReq.

        订单ID

        :param order_id: The order_id of this SubscribeUserSharerReq.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def users(self):
        """Gets the users of this SubscribeUserSharerReq.

        开通协同的的用户列表。

        :return: The users of this SubscribeUserSharerReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.User`]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this SubscribeUserSharerReq.

        开通协同的的用户列表。

        :param users: The users of this SubscribeUserSharerReq.
        :type users: list[:class:`huaweicloudsdkworkspace.v2.User`]
        """
        self._users = users

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this SubscribeUserSharerReq.

        企业项目ID

        :return: The enterprise_project_id of this SubscribeUserSharerReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this SubscribeUserSharerReq.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this SubscribeUserSharerReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
