# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeUserPrivilegeGroupDesktopInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'attach_user_infos': 'list[ChangeUserPrivilegeGroupUserInfo]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'attach_user_infos': 'attach_user_infos'
    }

    def __init__(self, desktop_id=None, attach_user_infos=None):
        r"""ChangeUserPrivilegeGroupDesktopInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 待修改的桌面ID。
        :type desktop_id: str
        :param attach_user_infos: 待修改用户权限组的用户信息。未传该参数的桌面的用于将应用上层结构的参数user_privilege_group作为其用户的用户权限组。
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.ChangeUserPrivilegeGroupUserInfo`]
        """
        
        

        self._desktop_id = None
        self._attach_user_infos = None
        self.discriminator = None

        self.desktop_id = desktop_id
        if attach_user_infos is not None:
            self.attach_user_infos = attach_user_infos

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this ChangeUserPrivilegeGroupDesktopInfo.

        待修改的桌面ID。

        :return: The desktop_id of this ChangeUserPrivilegeGroupDesktopInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this ChangeUserPrivilegeGroupDesktopInfo.

        待修改的桌面ID。

        :param desktop_id: The desktop_id of this ChangeUserPrivilegeGroupDesktopInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def attach_user_infos(self):
        r"""Gets the attach_user_infos of this ChangeUserPrivilegeGroupDesktopInfo.

        待修改用户权限组的用户信息。未传该参数的桌面的用于将应用上层结构的参数user_privilege_group作为其用户的用户权限组。

        :return: The attach_user_infos of this ChangeUserPrivilegeGroupDesktopInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ChangeUserPrivilegeGroupUserInfo`]
        """
        return self._attach_user_infos

    @attach_user_infos.setter
    def attach_user_infos(self, attach_user_infos):
        r"""Sets the attach_user_infos of this ChangeUserPrivilegeGroupDesktopInfo.

        待修改用户权限组的用户信息。未传该参数的桌面的用于将应用上层结构的参数user_privilege_group作为其用户的用户权限组。

        :param attach_user_infos: The attach_user_infos of this ChangeUserPrivilegeGroupDesktopInfo.
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.ChangeUserPrivilegeGroupUserInfo`]
        """
        self._attach_user_infos = attach_user_infos

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
        if not isinstance(other, ChangeUserPrivilegeGroupDesktopInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
