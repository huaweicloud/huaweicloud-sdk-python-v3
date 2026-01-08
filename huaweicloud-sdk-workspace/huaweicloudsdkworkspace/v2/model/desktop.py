# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Desktop:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'domain': 'str',
        'user_email': 'str',
        'user_phone': 'str',
        'user_group': 'str',
        'computer_name': 'str',
        'os_host_name': 'str',
        'desktop_name_prefix': 'str',
        'copy_volume_desktop_id': 'str',
        'copy_volume_ids': 'list[str]',
        'if_delete_old_desktop': 'bool'
    }

    attribute_map = {
        'user_name': 'user_name',
        'domain': 'domain',
        'user_email': 'user_email',
        'user_phone': 'user_phone',
        'user_group': 'user_group',
        'computer_name': 'computer_name',
        'os_host_name': 'os_host_name',
        'desktop_name_prefix': 'desktop_name_prefix',
        'copy_volume_desktop_id': 'copy_volume_desktop_id',
        'copy_volume_ids': 'copy_volume_ids',
        'if_delete_old_desktop': 'if_delete_old_desktop'
    }

    def __init__(self, user_name=None, domain=None, user_email=None, user_phone=None, user_group=None, computer_name=None, os_host_name=None, desktop_name_prefix=None, copy_volume_desktop_id=None, copy_volume_ids=None, if_delete_old_desktop=None):
        r"""Desktop

        The model defined in huaweicloud sdk

        :param user_name: 桌面所属的用户，当桌面创建成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-32]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持32个字符。
        :type user_name: str
        :param domain: 用户所属域。
        :type domain: str
        :param user_email: 合法用户邮箱，桌面创建成功后系统会通过发送邮件的方式通知用户。
        :type user_email: str
        :param user_phone: 合法用户手机号。
        :type user_phone: str
        :param user_group: 桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。
        :type user_group: str
        :param computer_name: 桌面名，桌面名必须保证唯一。桌面名称只允许输入大写字母、小写字母、中文、数字、中划线，以字母或数字开头、不能以中划线结尾，长度范围为1~15(中文字符长度为2，数字及英文字符长度为1)。
        :type computer_name: str
        :param os_host_name: 系统计算机名。
        :type os_host_name: str
        :param desktop_name_prefix: 桌面名称前缀，不指定\&quot;computer_name\&quot;时生效。
        :type desktop_name_prefix: str
        :param copy_volume_desktop_id: 需要拷贝数据盘的桌面ID，如果指定了该参数，那么copy_volume_ids不能为空。
        :type copy_volume_desktop_id: str
        :param copy_volume_ids: 需要拷贝数据盘桌面的磁盘ID列表，如果指定了该参数，copy_volume_desktop_id不能为空，且磁盘必须属于该桌面。
        :type copy_volume_ids: list[str]
        :param if_delete_old_desktop: 是否删除按需旧桌面，值为true时，新发放桌面配置并拷贝磁盘后删除旧桌面
        :type if_delete_old_desktop: bool
        """
        
        

        self._user_name = None
        self._domain = None
        self._user_email = None
        self._user_phone = None
        self._user_group = None
        self._computer_name = None
        self._os_host_name = None
        self._desktop_name_prefix = None
        self._copy_volume_desktop_id = None
        self._copy_volume_ids = None
        self._if_delete_old_desktop = None
        self.discriminator = None

        self.user_name = user_name
        if domain is not None:
            self.domain = domain
        if user_email is not None:
            self.user_email = user_email
        if user_phone is not None:
            self.user_phone = user_phone
        if user_group is not None:
            self.user_group = user_group
        if computer_name is not None:
            self.computer_name = computer_name
        if os_host_name is not None:
            self.os_host_name = os_host_name
        if desktop_name_prefix is not None:
            self.desktop_name_prefix = desktop_name_prefix
        if copy_volume_desktop_id is not None:
            self.copy_volume_desktop_id = copy_volume_desktop_id
        if copy_volume_ids is not None:
            self.copy_volume_ids = copy_volume_ids
        if if_delete_old_desktop is not None:
            self.if_delete_old_desktop = if_delete_old_desktop

    @property
    def user_name(self):
        r"""Gets the user_name of this Desktop.

        桌面所属的用户，当桌面创建成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-32]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持32个字符。

        :return: The user_name of this Desktop.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this Desktop.

        桌面所属的用户，当桌面创建成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-32]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持32个字符。

        :param user_name: The user_name of this Desktop.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def domain(self):
        r"""Gets the domain of this Desktop.

        用户所属域。

        :return: The domain of this Desktop.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this Desktop.

        用户所属域。

        :param domain: The domain of this Desktop.
        :type domain: str
        """
        self._domain = domain

    @property
    def user_email(self):
        r"""Gets the user_email of this Desktop.

        合法用户邮箱，桌面创建成功后系统会通过发送邮件的方式通知用户。

        :return: The user_email of this Desktop.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        r"""Sets the user_email of this Desktop.

        合法用户邮箱，桌面创建成功后系统会通过发送邮件的方式通知用户。

        :param user_email: The user_email of this Desktop.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def user_phone(self):
        r"""Gets the user_phone of this Desktop.

        合法用户手机号。

        :return: The user_phone of this Desktop.
        :rtype: str
        """
        return self._user_phone

    @user_phone.setter
    def user_phone(self, user_phone):
        r"""Sets the user_phone of this Desktop.

        合法用户手机号。

        :param user_phone: The user_phone of this Desktop.
        :type user_phone: str
        """
        self._user_phone = user_phone

    @property
    def user_group(self):
        r"""Gets the user_group of this Desktop.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :return: The user_group of this Desktop.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        r"""Sets the user_group of this Desktop.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :param user_group: The user_group of this Desktop.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def computer_name(self):
        r"""Gets the computer_name of this Desktop.

        桌面名，桌面名必须保证唯一。桌面名称只允许输入大写字母、小写字母、中文、数字、中划线，以字母或数字开头、不能以中划线结尾，长度范围为1~15(中文字符长度为2，数字及英文字符长度为1)。

        :return: The computer_name of this Desktop.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this Desktop.

        桌面名，桌面名必须保证唯一。桌面名称只允许输入大写字母、小写字母、中文、数字、中划线，以字母或数字开头、不能以中划线结尾，长度范围为1~15(中文字符长度为2，数字及英文字符长度为1)。

        :param computer_name: The computer_name of this Desktop.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def os_host_name(self):
        r"""Gets the os_host_name of this Desktop.

        系统计算机名。

        :return: The os_host_name of this Desktop.
        :rtype: str
        """
        return self._os_host_name

    @os_host_name.setter
    def os_host_name(self, os_host_name):
        r"""Sets the os_host_name of this Desktop.

        系统计算机名。

        :param os_host_name: The os_host_name of this Desktop.
        :type os_host_name: str
        """
        self._os_host_name = os_host_name

    @property
    def desktop_name_prefix(self):
        r"""Gets the desktop_name_prefix of this Desktop.

        桌面名称前缀，不指定\"computer_name\"时生效。

        :return: The desktop_name_prefix of this Desktop.
        :rtype: str
        """
        return self._desktop_name_prefix

    @desktop_name_prefix.setter
    def desktop_name_prefix(self, desktop_name_prefix):
        r"""Sets the desktop_name_prefix of this Desktop.

        桌面名称前缀，不指定\"computer_name\"时生效。

        :param desktop_name_prefix: The desktop_name_prefix of this Desktop.
        :type desktop_name_prefix: str
        """
        self._desktop_name_prefix = desktop_name_prefix

    @property
    def copy_volume_desktop_id(self):
        r"""Gets the copy_volume_desktop_id of this Desktop.

        需要拷贝数据盘的桌面ID，如果指定了该参数，那么copy_volume_ids不能为空。

        :return: The copy_volume_desktop_id of this Desktop.
        :rtype: str
        """
        return self._copy_volume_desktop_id

    @copy_volume_desktop_id.setter
    def copy_volume_desktop_id(self, copy_volume_desktop_id):
        r"""Sets the copy_volume_desktop_id of this Desktop.

        需要拷贝数据盘的桌面ID，如果指定了该参数，那么copy_volume_ids不能为空。

        :param copy_volume_desktop_id: The copy_volume_desktop_id of this Desktop.
        :type copy_volume_desktop_id: str
        """
        self._copy_volume_desktop_id = copy_volume_desktop_id

    @property
    def copy_volume_ids(self):
        r"""Gets the copy_volume_ids of this Desktop.

        需要拷贝数据盘桌面的磁盘ID列表，如果指定了该参数，copy_volume_desktop_id不能为空，且磁盘必须属于该桌面。

        :return: The copy_volume_ids of this Desktop.
        :rtype: list[str]
        """
        return self._copy_volume_ids

    @copy_volume_ids.setter
    def copy_volume_ids(self, copy_volume_ids):
        r"""Sets the copy_volume_ids of this Desktop.

        需要拷贝数据盘桌面的磁盘ID列表，如果指定了该参数，copy_volume_desktop_id不能为空，且磁盘必须属于该桌面。

        :param copy_volume_ids: The copy_volume_ids of this Desktop.
        :type copy_volume_ids: list[str]
        """
        self._copy_volume_ids = copy_volume_ids

    @property
    def if_delete_old_desktop(self):
        r"""Gets the if_delete_old_desktop of this Desktop.

        是否删除按需旧桌面，值为true时，新发放桌面配置并拷贝磁盘后删除旧桌面

        :return: The if_delete_old_desktop of this Desktop.
        :rtype: bool
        """
        return self._if_delete_old_desktop

    @if_delete_old_desktop.setter
    def if_delete_old_desktop(self, if_delete_old_desktop):
        r"""Sets the if_delete_old_desktop of this Desktop.

        是否删除按需旧桌面，值为true时，新发放桌面配置并拷贝磁盘后删除旧桌面

        :param if_delete_old_desktop: The if_delete_old_desktop of this Desktop.
        :type if_delete_old_desktop: bool
        """
        self._if_delete_old_desktop = if_delete_old_desktop

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
        if not isinstance(other, Desktop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
