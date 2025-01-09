# coding: utf-8

import six

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
        'user_email': 'str',
        'user_phone': 'str',
        'user_group': 'str',
        'computer_name': 'str',
        'os_host_name': 'str',
        'nics': 'list[Nic]',
        'ou_name': 'str',
        'desktop_name_prefix': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'user_email': 'user_email',
        'user_phone': 'user_phone',
        'user_group': 'user_group',
        'computer_name': 'computer_name',
        'os_host_name': 'os_host_name',
        'nics': 'nics',
        'ou_name': 'ou_name',
        'desktop_name_prefix': 'desktop_name_prefix'
    }

    def __init__(self, user_name=None, user_email=None, user_phone=None, user_group=None, computer_name=None, os_host_name=None, nics=None, ou_name=None, desktop_name_prefix=None):
        """Desktop

        The model defined in huaweicloud sdk

        :param user_name: 桌面所属的用户，当桌面创建成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-32]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持32个字符。
        :type user_name: str
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
        :param nics: 桌面对应的网卡信息，如果不指定则使用默认网卡。
        :type nics: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        :param ou_name: 此参数仅在开通云桌面服务的domain_type为LOCAL_AD时有效。只允许输入汉字，半角字母，数字，空格，以及-_/$!@&amp;*?.范围内的特殊字符，字符范围是1～255，OU名称不能包含分隔符(/),多级OU使用/隔开，最多支持五级，/前后不能有空格，例如3级的OU格式:ab/cd/ef。
        :type ou_name: str
        :param desktop_name_prefix: 桌面名称前缀，不指定\&quot;computer_name\&quot;时生效。
        :type desktop_name_prefix: str
        """
        
        

        self._user_name = None
        self._user_email = None
        self._user_phone = None
        self._user_group = None
        self._computer_name = None
        self._os_host_name = None
        self._nics = None
        self._ou_name = None
        self._desktop_name_prefix = None
        self.discriminator = None

        self.user_name = user_name
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
        if nics is not None:
            self.nics = nics
        if ou_name is not None:
            self.ou_name = ou_name
        if desktop_name_prefix is not None:
            self.desktop_name_prefix = desktop_name_prefix

    @property
    def user_name(self):
        """Gets the user_name of this Desktop.

        桌面所属的用户，当桌面创建成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-32]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持32个字符。

        :return: The user_name of this Desktop.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this Desktop.

        桌面所属的用户，当桌面创建成功后此用户可以登录该桌面。只允许输入大写字母、小写字母、数字、中划线（-）和下划线（_）。域类型为LITE_AD时，使用小写字母或者大写字母开头，长度范围为[1-20]。当域类型为LOCAL_AD时，用户名可以使用小写字母或者大写字母或者数字开头，长度范围为[1-32]。Windows桌面用户最长支持20个字符，Linux桌面用户最长支持32个字符。

        :param user_name: The user_name of this Desktop.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def user_email(self):
        """Gets the user_email of this Desktop.

        合法用户邮箱，桌面创建成功后系统会通过发送邮件的方式通知用户。

        :return: The user_email of this Desktop.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this Desktop.

        合法用户邮箱，桌面创建成功后系统会通过发送邮件的方式通知用户。

        :param user_email: The user_email of this Desktop.
        :type user_email: str
        """
        self._user_email = user_email

    @property
    def user_phone(self):
        """Gets the user_phone of this Desktop.

        合法用户手机号。

        :return: The user_phone of this Desktop.
        :rtype: str
        """
        return self._user_phone

    @user_phone.setter
    def user_phone(self, user_phone):
        """Sets the user_phone of this Desktop.

        合法用户手机号。

        :param user_phone: The user_phone of this Desktop.
        :type user_phone: str
        """
        self._user_phone = user_phone

    @property
    def user_group(self):
        """Gets the user_group of this Desktop.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :return: The user_group of this Desktop.
        :rtype: str
        """
        return self._user_group

    @user_group.setter
    def user_group(self, user_group):
        """Sets the user_group of this Desktop.

        桌面用户所属的用户组。  - sudo：Linux管理员组。 - default：Linux默认用户组。 - administrators：Windows管理员组。管理员拥有对该桌面的完全访问权，可以做任何需要的更改（禁用操作除外）。 - users：Windows标准用户组。标准用户可以使用大多数软件，并可以更改不影响其他用户的系统设置。

        :param user_group: The user_group of this Desktop.
        :type user_group: str
        """
        self._user_group = user_group

    @property
    def computer_name(self):
        """Gets the computer_name of this Desktop.

        桌面名，桌面名必须保证唯一。桌面名称只允许输入大写字母、小写字母、中文、数字、中划线，以字母或数字开头、不能以中划线结尾，长度范围为1~15(中文字符长度为2，数字及英文字符长度为1)。

        :return: The computer_name of this Desktop.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        """Sets the computer_name of this Desktop.

        桌面名，桌面名必须保证唯一。桌面名称只允许输入大写字母、小写字母、中文、数字、中划线，以字母或数字开头、不能以中划线结尾，长度范围为1~15(中文字符长度为2，数字及英文字符长度为1)。

        :param computer_name: The computer_name of this Desktop.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def os_host_name(self):
        """Gets the os_host_name of this Desktop.

        系统计算机名。

        :return: The os_host_name of this Desktop.
        :rtype: str
        """
        return self._os_host_name

    @os_host_name.setter
    def os_host_name(self, os_host_name):
        """Sets the os_host_name of this Desktop.

        系统计算机名。

        :param os_host_name: The os_host_name of this Desktop.
        :type os_host_name: str
        """
        self._os_host_name = os_host_name

    @property
    def nics(self):
        """Gets the nics of this Desktop.

        桌面对应的网卡信息，如果不指定则使用默认网卡。

        :return: The nics of this Desktop.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this Desktop.

        桌面对应的网卡信息，如果不指定则使用默认网卡。

        :param nics: The nics of this Desktop.
        :type nics: list[:class:`huaweicloudsdkworkspace.v2.Nic`]
        """
        self._nics = nics

    @property
    def ou_name(self):
        """Gets the ou_name of this Desktop.

        此参数仅在开通云桌面服务的domain_type为LOCAL_AD时有效。只允许输入汉字，半角字母，数字，空格，以及-_/$!@&*?.范围内的特殊字符，字符范围是1～255，OU名称不能包含分隔符(/),多级OU使用/隔开，最多支持五级，/前后不能有空格，例如3级的OU格式:ab/cd/ef。

        :return: The ou_name of this Desktop.
        :rtype: str
        """
        return self._ou_name

    @ou_name.setter
    def ou_name(self, ou_name):
        """Sets the ou_name of this Desktop.

        此参数仅在开通云桌面服务的domain_type为LOCAL_AD时有效。只允许输入汉字，半角字母，数字，空格，以及-_/$!@&*?.范围内的特殊字符，字符范围是1～255，OU名称不能包含分隔符(/),多级OU使用/隔开，最多支持五级，/前后不能有空格，例如3级的OU格式:ab/cd/ef。

        :param ou_name: The ou_name of this Desktop.
        :type ou_name: str
        """
        self._ou_name = ou_name

    @property
    def desktop_name_prefix(self):
        """Gets the desktop_name_prefix of this Desktop.

        桌面名称前缀，不指定\"computer_name\"时生效。

        :return: The desktop_name_prefix of this Desktop.
        :rtype: str
        """
        return self._desktop_name_prefix

    @desktop_name_prefix.setter
    def desktop_name_prefix(self, desktop_name_prefix):
        """Sets the desktop_name_prefix of this Desktop.

        桌面名称前缀，不指定\"computer_name\"时生效。

        :param desktop_name_prefix: The desktop_name_prefix of this Desktop.
        :type desktop_name_prefix: str
        """
        self._desktop_name_prefix = desktop_name_prefix

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
        if not isinstance(other, Desktop):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
