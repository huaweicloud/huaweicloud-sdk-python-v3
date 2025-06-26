# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabaseUsersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'users': 'list[DatabaseUser]'
    }

    attribute_map = {
        'users': 'users'
    }

    def __init__(self, users=None):
        r"""ListDatabaseUsersResponse

        The model defined in huaweicloud sdk

        :param users: **参数解释**： 用户/角色列表。 **取值范围**： 不涉及。
        :type users: list[:class:`huaweicloudsdkdws.v2.DatabaseUser`]
        """
        
        super(ListDatabaseUsersResponse, self).__init__()

        self._users = None
        self.discriminator = None

        if users is not None:
            self.users = users

    @property
    def users(self):
        r"""Gets the users of this ListDatabaseUsersResponse.

        **参数解释**： 用户/角色列表。 **取值范围**： 不涉及。

        :return: The users of this ListDatabaseUsersResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.DatabaseUser`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this ListDatabaseUsersResponse.

        **参数解释**： 用户/角色列表。 **取值范围**： 不涉及。

        :param users: The users of this ListDatabaseUsersResponse.
        :type users: list[:class:`huaweicloudsdkdws.v2.DatabaseUser`]
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
        if not isinstance(other, ListDatabaseUsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
