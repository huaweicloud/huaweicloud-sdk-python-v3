# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeUserPrivilegeGroupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktops': 'list[ChangeUserPrivilegeGroupDesktopInfo]',
        'user_privilege_group': 'str'
    }

    attribute_map = {
        'desktops': 'desktops',
        'user_privilege_group': 'user_privilege_group'
    }

    def __init__(self, desktops=None, user_privilege_group=None):
        """ChangeUserPrivilegeGroupReq

        The model defined in huaweicloud sdk

        :param desktops: 桌面信息列表。
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.ChangeUserPrivilegeGroupDesktopInfo`]
        :param user_privilege_group: 桌面用户所属的用户权限组。desktops参数中，各个桌面所属的未传的桌面用户将应用该权限组。 - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。
        :type user_privilege_group: str
        """
        
        

        self._desktops = None
        self._user_privilege_group = None
        self.discriminator = None

        self.desktops = desktops
        if user_privilege_group is not None:
            self.user_privilege_group = user_privilege_group

    @property
    def desktops(self):
        """Gets the desktops of this ChangeUserPrivilegeGroupReq.

        桌面信息列表。

        :return: The desktops of this ChangeUserPrivilegeGroupReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ChangeUserPrivilegeGroupDesktopInfo`]
        """
        return self._desktops

    @desktops.setter
    def desktops(self, desktops):
        """Sets the desktops of this ChangeUserPrivilegeGroupReq.

        桌面信息列表。

        :param desktops: The desktops of this ChangeUserPrivilegeGroupReq.
        :type desktops: list[:class:`huaweicloudsdkworkspace.v2.ChangeUserPrivilegeGroupDesktopInfo`]
        """
        self._desktops = desktops

    @property
    def user_privilege_group(self):
        """Gets the user_privilege_group of this ChangeUserPrivilegeGroupReq.

        桌面用户所属的用户权限组。desktops参数中，各个桌面所属的未传的桌面用户将应用该权限组。 - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :return: The user_privilege_group of this ChangeUserPrivilegeGroupReq.
        :rtype: str
        """
        return self._user_privilege_group

    @user_privilege_group.setter
    def user_privilege_group(self, user_privilege_group):
        """Sets the user_privilege_group of this ChangeUserPrivilegeGroupReq.

        桌面用户所属的用户权限组。desktops参数中，各个桌面所属的未传的桌面用户将应用该权限组。 - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :param user_privilege_group: The user_privilege_group of this ChangeUserPrivilegeGroupReq.
        :type user_privilege_group: str
        """
        self._user_privilege_group = user_privilege_group

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
        if not isinstance(other, ChangeUserPrivilegeGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
