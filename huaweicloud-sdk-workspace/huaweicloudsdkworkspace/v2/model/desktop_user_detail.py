# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopUserDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'user_name': 'str',
        'domain': 'str',
        'user_email': 'str',
        'permission_group': 'str',
        'desktop_name': 'str',
        'desktop_ip': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_name': 'user_name',
        'domain': 'domain',
        'user_email': 'user_email',
        'permission_group': 'permission_group',
        'desktop_name': 'desktop_name',
        'desktop_ip': 'desktop_ip',
        'description': 'description'
    }

    def __init__(self, id=None, user_name=None, domain=None, user_email=None, permission_group=None, desktop_name=None, desktop_ip=None, description=None):
        r"""DesktopUserDetail

        The model defined in huaweicloud sdk

        :param id: 用户id。
        :type id: str
        :param user_name: 用户名。
        :type user_name: str
        :param domain: 用户所属域，domain为空时，默认主域。
        :type domain: str
        :param user_email: 邮箱。
        :type user_email: str
        :param permission_group: 权限组。
        :type permission_group: str
        :param desktop_name: 桌面名称。
        :type desktop_name: str
        :param desktop_ip: 桌面ip。
        :type desktop_ip: str
        :param description: 描述。
        :type description: str
        """
        
        

        self._id = None
        self._user_name = None
        self._domain = None
        self._user_email = None
        self._permission_group = None
        self._desktop_name = None
        self._desktop_ip = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_name is not None:
            self.user_name = user_name
        if domain is not None:
            self.domain = domain
        if user_email is not None:
            self.user_email = user_email
        if permission_group is not None:
            self.permission_group = permission_group
        if desktop_name is not None:
            self.desktop_name = desktop_name
        if desktop_ip is not None:
            self.desktop_ip = desktop_ip
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this DesktopUserDetail.

        用户id。

        :return: The id of this DesktopUserDetail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DesktopUserDetail.

        用户id。

        :param id: The id of this DesktopUserDetail.
        :type id: str
        """
        self._id = id

    @property
    def user_name(self):
        r"""Gets the user_name of this DesktopUserDetail.

        用户名。

        :return: The user_name of this DesktopUserDetail.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this DesktopUserDetail.

        用户名。

        :param user_name: The user_name of this DesktopUserDetail.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain(self):
        r"""Gets the domain of this DesktopUserDetail.

        用户所属域，domain为空时，默认主域。

        :return: The domain of this DesktopUserDetail.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this DesktopUserDetail.

        用户所属域，domain为空时，默认主域。

        :param domain: The domain of this DesktopUserDetail.
        :type domain: str
        """
        self._domain = domain

    @property
    def user_email(self):
        r"""Gets the user_email of this DesktopUserDetail.

        邮箱。

        :return: The user_email of this DesktopUserDetail.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        r"""Sets the user_email of this DesktopUserDetail.

        邮箱。

        :param user_email: The user_email of this DesktopUserDetail.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def permission_group(self):
        r"""Gets the permission_group of this DesktopUserDetail.

        权限组。

        :return: The permission_group of this DesktopUserDetail.
        :rtype: str
        """
        return self._permission_group

    @permission_group.setter
    def permission_group(self, permission_group):
        r"""Sets the permission_group of this DesktopUserDetail.

        权限组。

        :param permission_group: The permission_group of this DesktopUserDetail.
        :type permission_group: str
        """
        self._permission_group = permission_group

    @property
    def desktop_name(self):
        r"""Gets the desktop_name of this DesktopUserDetail.

        桌面名称。

        :return: The desktop_name of this DesktopUserDetail.
        :rtype: str
        """
        return self._desktop_name

    @desktop_name.setter
    def desktop_name(self, desktop_name):
        r"""Sets the desktop_name of this DesktopUserDetail.

        桌面名称。

        :param desktop_name: The desktop_name of this DesktopUserDetail.
        :type desktop_name: str
        """
        self._desktop_name = desktop_name

    @property
    def desktop_ip(self):
        r"""Gets the desktop_ip of this DesktopUserDetail.

        桌面ip。

        :return: The desktop_ip of this DesktopUserDetail.
        :rtype: str
        """
        return self._desktop_ip

    @desktop_ip.setter
    def desktop_ip(self, desktop_ip):
        r"""Sets the desktop_ip of this DesktopUserDetail.

        桌面ip。

        :param desktop_ip: The desktop_ip of this DesktopUserDetail.
        :type desktop_ip: str
        """
        self._desktop_ip = desktop_ip

    @property
    def description(self):
        r"""Gets the description of this DesktopUserDetail.

        描述。

        :return: The description of this DesktopUserDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DesktopUserDetail.

        描述。

        :param description: The description of this DesktopUserDetail.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DesktopUserDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
