# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteInstanceUsersReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'users': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'users': 'users'
    }

    def __init__(self, action=None, users=None):
        """BatchDeleteInstanceUsersReq

        The model defined in huaweicloud sdk

        :param action: 删除类型。当前只支持delete。
        :type action: str
        :param users: 用户列表。
        :type users: list[str]
        """
        
        

        self._action = None
        self._users = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if users is not None:
            self.users = users

    @property
    def action(self):
        """Gets the action of this BatchDeleteInstanceUsersReq.

        删除类型。当前只支持delete。

        :return: The action of this BatchDeleteInstanceUsersReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BatchDeleteInstanceUsersReq.

        删除类型。当前只支持delete。

        :param action: The action of this BatchDeleteInstanceUsersReq.
        :type action: str
        """
        self._action = action

    @property
    def users(self):
        """Gets the users of this BatchDeleteInstanceUsersReq.

        用户列表。

        :return: The users of this BatchDeleteInstanceUsersReq.
        :rtype: list[str]
        """
        return self._users

    @users.setter
    def users(self, users):
        """Sets the users of this BatchDeleteInstanceUsersReq.

        用户列表。

        :param users: The users of this BatchDeleteInstanceUsersReq.
        :type users: list[str]
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
        if not isinstance(other, BatchDeleteInstanceUsersReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
