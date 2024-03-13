# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachInstancesDesktopInfo:

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
        'user_name': 'str',
        'user_email': 'str',
        'user_group': 'str',
        'computer_name': 'str',
        'is_clear_data': 'bool',
        'attach_user_infos': 'list[AttachInstancesUserInfo]'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'user_name': 'user_name',
        'user_email': 'user_email',
        'user_group': 'user_group',
        'computer_name': 'computer_name',
        'is_clear_data': 'is_clear_data',
        'attach_user_infos': 'attach_user_infos'
    }

    def __init__(self, desktop_id=None, user_name=None, user_email=None, user_group=None, computer_name=None, is_clear_data=None, attach_user_infos=None):
        """AttachInstancesDesktopInfo

        The model defined in huaweicloud sdk

        :param desktop_id: 待分配的桌面ID。
        :type desktop_id: str
        :param user_name: 桌面所属的用户，当桌面分配成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-32]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持32个字符。
        :type user_name: str
        :param user_email: 合法用户邮箱，桌面分配成功后系统会通过发送邮件的方式通知用户
        :type user_email: str
        :param user_group: 桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。
        :type user_group: str
        :param computer_name: 桌面名，桌面名必须保证唯一。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）；以字母开头且不允许以中划线（-）结尾；长度范围为[1-15]。
        :type computer_name: str
        :param is_clear_data: 该字段只有当解绑和绑定为同一个用户时生效。表示绑定时是否清理桌面数据，true：清理，false：不清理，默认值为true。
        :type is_clear_data: bool
        :param attach_user_infos: 待分配的用户信息列表。
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        
        

        self._desktop_id = None
        self._user_name = None
        self._user_email = None
        self._user_group = None
        self._computer_name = None
        self._is_clear_data = None
        self._attach_user_infos = None
        self.discriminator = None

        self.desktop_id = desktop_id
        if user_name is not None:
            self.user_name = user_name
        if user_email is not None:
            self.user_email = user_email
        if user_group is not None:
            self.user_group = user_group
        if computer_name is not None:
            self.computer_name = computer_name
        if is_clear_data is not None:
            self.is_clear_data = is_clear_data
        if attach_user_infos is not None:
            self.attach_user_infos = attach_user_infos

    @property
    def desktop_id(self):
        """Gets the desktop_id of this AttachInstancesDesktopInfo.

        待分配的桌面ID。

        :return: The desktop_id of this AttachInstancesDesktopInfo.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this AttachInstancesDesktopInfo.

        待分配的桌面ID。

        :param desktop_id: The desktop_id of this AttachInstancesDesktopInfo.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def user_name(self):
        """Gets the user_name of this AttachInstancesDesktopInfo.

        桌面所属的用户，当桌面分配成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-32]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持32个字符。

        :return: The user_name of this AttachInstancesDesktopInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this AttachInstancesDesktopInfo.

        桌面所属的用户，当桌面分配成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-32]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持32个字符。

        :param user_name: The user_name of this AttachInstancesDesktopInfo.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_email(self):
        """Gets the user_email of this AttachInstancesDesktopInfo.

        合法用户邮箱，桌面分配成功后系统会通过发送邮件的方式通知用户

        :return: The user_email of this AttachInstancesDesktopInfo.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this AttachInstancesDesktopInfo.

        合法用户邮箱，桌面分配成功后系统会通过发送邮件的方式通知用户

        :param user_email: The user_email of this AttachInstancesDesktopInfo.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def user_group(self):
        """Gets the user_group of this AttachInstancesDesktopInfo.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :return: The user_group of this AttachInstancesDesktopInfo.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this AttachInstancesDesktopInfo.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :param user_group: The user_group of this AttachInstancesDesktopInfo.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def computer_name(self):
        """Gets the computer_name of this AttachInstancesDesktopInfo.

        桌面名，桌面名必须保证唯一。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）；以字母开头且不允许以中划线（-）结尾；长度范围为[1-15]。

        :return: The computer_name of this AttachInstancesDesktopInfo.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this AttachInstancesDesktopInfo.

        桌面名，桌面名必须保证唯一。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）；以字母开头且不允许以中划线（-）结尾；长度范围为[1-15]。

        :param computer_name: The computer_name of this AttachInstancesDesktopInfo.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def is_clear_data(self):
        """Gets the is_clear_data of this AttachInstancesDesktopInfo.

        该字段只有当解绑和绑定为同一个用户时生效。表示绑定时是否清理桌面数据，true：清理，false：不清理，默认值为true。

        :return: The is_clear_data of this AttachInstancesDesktopInfo.
        :rtype: bool
        """
        return self._is_clear_data

    @is_clear_data.setter
    def is_clear_data(self, is_clear_data):
        """Sets the is_clear_data of this AttachInstancesDesktopInfo.

        该字段只有当解绑和绑定为同一个用户时生效。表示绑定时是否清理桌面数据，true：清理，false：不清理，默认值为true。

        :param is_clear_data: The is_clear_data of this AttachInstancesDesktopInfo.
        :type is_clear_data: bool
        """
        self._is_clear_data = is_clear_data

    @property
    def attach_user_infos(self):
        """Gets the attach_user_infos of this AttachInstancesDesktopInfo.

        待分配的用户信息列表。

        :return: The attach_user_infos of this AttachInstancesDesktopInfo.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
        """
        return self._attach_user_infos

    @attach_user_infos.setter
    def attach_user_infos(self, attach_user_infos):
        """Sets the attach_user_infos of this AttachInstancesDesktopInfo.

        待分配的用户信息列表。

        :param attach_user_infos: The attach_user_infos of this AttachInstancesDesktopInfo.
        :type attach_user_infos: list[:class:`huaweicloudsdkworkspace.v2.AttachInstancesUserInfo`]
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
        if not isinstance(other, AttachInstancesDesktopInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
