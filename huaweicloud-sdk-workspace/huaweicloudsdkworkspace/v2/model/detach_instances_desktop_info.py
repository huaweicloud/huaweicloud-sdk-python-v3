# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetachInstancesDesktopInfo:

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
        'is_detach_all_users': 'bool',
        'detach_user_infos': 'list[AttachInstancesUserInfo]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'is_detach_all_users': 'is_detach_all_users',
        'detach_user_infos': 'detach_user_infos'
    }

    def __init__(self, desktop_id=None, is_detach_all_users=None, detach_user_infos=None):
        r"""DetachInstancesDesktopInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 分配的桌面ID。
        :type desktop_id: str
        :param is_detach_all_users: 表示解关联所有用户：true，如果指定那么detach_user_infos会失效；指定解关联用户：false，通过detach_user_infos指定解关联的用户。
        :type is_detach_all_users: bool
        :param detach_user_infos: 解分配的用户信息列表。
        :type detach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        
        

        self._desktop_id = None
        self._is_detach_all_users = None
        self._detach_user_infos = None
        self.discriminator = None

        if desktop_id is not None:
            self.desktop_id = desktop_id
        if is_detach_all_users is not None:
            self.is_detach_all_users = is_detach_all_users
        if detach_user_infos is not None:
            self.detach_user_infos = detach_user_infos

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this DetachInstancesDesktopInfo.

        分配的桌面ID。

        :return: The desktop_id of this DetachInstancesDesktopInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this DetachInstancesDesktopInfo.

        分配的桌面ID。

        :param desktop_id: The desktop_id of this DetachInstancesDesktopInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def is_detach_all_users(self):
        r"""Gets the is_detach_all_users of this DetachInstancesDesktopInfo.

        表示解关联所有用户：true，如果指定那么detach_user_infos会失效；指定解关联用户：false，通过detach_user_infos指定解关联的用户。

        :return: The is_detach_all_users of this DetachInstancesDesktopInfo.
        :rtype: bool
        """
        return self._is_detach_all_users

    @is_detach_all_users.setter
    def is_detach_all_users(self, is_detach_all_users):
        r"""Sets the is_detach_all_users of this DetachInstancesDesktopInfo.

        表示解关联所有用户：true，如果指定那么detach_user_infos会失效；指定解关联用户：false，通过detach_user_infos指定解关联的用户。

        :param is_detach_all_users: The is_detach_all_users of this DetachInstancesDesktopInfo.
        :type is_detach_all_users: bool
        """
        self._is_detach_all_users = is_detach_all_users

    @property
    def detach_user_infos(self):
        r"""Gets the detach_user_infos of this DetachInstancesDesktopInfo.

        解分配的用户信息列表。

        :return: The detach_user_infos of this DetachInstancesDesktopInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        return self._detach_user_infos

    @detach_user_infos.setter
    def detach_user_infos(self, detach_user_infos):
        r"""Sets the detach_user_infos of this DetachInstancesDesktopInfo.

        解分配的用户信息列表。

        :param detach_user_infos: The detach_user_infos of this DetachInstancesDesktopInfo.
        :type detach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        self._detach_user_infos = detach_user_infos

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
        if not isinstance(other, DetachInstancesDesktopInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
