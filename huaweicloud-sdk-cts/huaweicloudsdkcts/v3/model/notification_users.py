# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotificationUsers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_group': 'str',
        'user_list': 'list[str]'
    }

    attribute_map = {
        'user_group': 'user_group',
        'user_list': 'user_list'
    }

    def __init__(self, user_group=None, user_list=None):
        """NotificationUsers

        The model defined in huaweicloud sdk

        :param user_group: IAM用户组。
        :type user_group: str
        :param user_list: IAM用户。
        :type user_list: list[str]
        """
        
        

        self._user_group = None
        self._user_list = None
        self.discriminator = None

        self.user_group = user_group
        self.user_list = user_list

    @property
    def user_group(self):
        """Gets the user_group of this NotificationUsers.

        IAM用户组。

        :return: The user_group of this NotificationUsers.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this NotificationUsers.

        IAM用户组。

        :param user_group: The user_group of this NotificationUsers.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def user_list(self):
        """Gets the user_list of this NotificationUsers.

        IAM用户。

        :return: The user_list of this NotificationUsers.
        :rtype: list[str]
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        """Sets the user_list of this NotificationUsers.

        IAM用户。

        :param user_list: The user_list of this NotificationUsers.
        :type user_list: list[str]
        """
        self._user_list = user_list

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
        if not isinstance(other, NotificationUsers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
