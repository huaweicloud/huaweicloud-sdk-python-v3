# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneListUsersForGroupByAdminResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'links': 'Links',
        'users': 'list[KeystoneUserResult]'
    }

    attribute_map = {
        'links': 'links',
        'users': 'users'
    }

    def __init__(self, links=None, users=None):
        r"""KeystoneListUsersForGroupByAdminResponse

        The model defined in huaweicloud sdk

        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        :param users: IAM用户信息列表。
        :type users: list[:class:`huaweicloudsdkiam.v3.KeystoneUserResult`]
        """
        
        super(KeystoneListUsersForGroupByAdminResponse, self).__init__()

        self._links = None
        self._users = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if users is not None:
            self.users = users

    @property
    def links(self):
        r"""Gets the links of this KeystoneListUsersForGroupByAdminResponse.

        :return: The links of this KeystoneListUsersForGroupByAdminResponse.
        :rtype: :class:`huaweicloudsdkiam.v3.Links`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this KeystoneListUsersForGroupByAdminResponse.

        :param links: The links of this KeystoneListUsersForGroupByAdminResponse.
        :type links: :class:`huaweicloudsdkiam.v3.Links`
        """
        self._links = links

    @property
    def users(self):
        r"""Gets the users of this KeystoneListUsersForGroupByAdminResponse.

        IAM用户信息列表。

        :return: The users of this KeystoneListUsersForGroupByAdminResponse.
        :rtype: list[:class:`huaweicloudsdkiam.v3.KeystoneUserResult`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this KeystoneListUsersForGroupByAdminResponse.

        IAM用户信息列表。

        :param users: The users of this KeystoneListUsersForGroupByAdminResponse.
        :type users: list[:class:`huaweicloudsdkiam.v3.KeystoneUserResult`]
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
        if not isinstance(other, KeystoneListUsersForGroupByAdminResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
