# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetIdentityStoreSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'users': 'int',
        'users_quota': 'int',
        'groups': 'int',
        'groups_quota': 'int'
    }

    attribute_map = {
        'users': 'users',
        'users_quota': 'users_quota',
        'groups': 'groups',
        'groups_quota': 'groups_quota'
    }

    def __init__(self, users=None, users_quota=None, groups=None, groups_quota=None):
        r"""GetIdentityStoreSummaryResponse

        The model defined in huaweicloud sdk

        :param users: 已创建的用户数量
        :type users: int
        :param users_quota: 用户配额
        :type users_quota: int
        :param groups: 已创建的用户组数量
        :type groups: int
        :param groups_quota: 用户组配额
        :type groups_quota: int
        """
        
        super(GetIdentityStoreSummaryResponse, self).__init__()

        self._users = None
        self._users_quota = None
        self._groups = None
        self._groups_quota = None
        self.discriminator = None

        if users is not None:
            self.users = users
        if users_quota is not None:
            self.users_quota = users_quota
        if groups is not None:
            self.groups = groups
        if groups_quota is not None:
            self.groups_quota = groups_quota

    @property
    def users(self):
        r"""Gets the users of this GetIdentityStoreSummaryResponse.

        已创建的用户数量

        :return: The users of this GetIdentityStoreSummaryResponse.
        :rtype: int
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this GetIdentityStoreSummaryResponse.

        已创建的用户数量

        :param users: The users of this GetIdentityStoreSummaryResponse.
        :type users: int
        """
        self._users = users

    @property
    def users_quota(self):
        r"""Gets the users_quota of this GetIdentityStoreSummaryResponse.

        用户配额

        :return: The users_quota of this GetIdentityStoreSummaryResponse.
        :rtype: int
        """
        return self._users_quota

    @users_quota.setter
    def users_quota(self, users_quota):
        r"""Sets the users_quota of this GetIdentityStoreSummaryResponse.

        用户配额

        :param users_quota: The users_quota of this GetIdentityStoreSummaryResponse.
        :type users_quota: int
        """
        self._users_quota = users_quota

    @property
    def groups(self):
        r"""Gets the groups of this GetIdentityStoreSummaryResponse.

        已创建的用户组数量

        :return: The groups of this GetIdentityStoreSummaryResponse.
        :rtype: int
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        r"""Sets the groups of this GetIdentityStoreSummaryResponse.

        已创建的用户组数量

        :param groups: The groups of this GetIdentityStoreSummaryResponse.
        :type groups: int
        """
        self._groups = groups

    @property
    def groups_quota(self):
        r"""Gets the groups_quota of this GetIdentityStoreSummaryResponse.

        用户组配额

        :return: The groups_quota of this GetIdentityStoreSummaryResponse.
        :rtype: int
        """
        return self._groups_quota

    @groups_quota.setter
    def groups_quota(self, groups_quota):
        r"""Sets the groups_quota of this GetIdentityStoreSummaryResponse.

        用户组配额

        :param groups_quota: The groups_quota of this GetIdentityStoreSummaryResponse.
        :type groups_quota: int
        """
        self._groups_quota = groups_quota

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
        if not isinstance(other, GetIdentityStoreSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
