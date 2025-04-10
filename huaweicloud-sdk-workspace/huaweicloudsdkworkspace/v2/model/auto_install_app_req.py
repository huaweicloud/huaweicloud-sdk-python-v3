# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AutoInstallAppReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'install_command': 'str',
        'uninstall_command': 'str',
        'users': 'list[AccountInfo]'
    }

    attribute_map = {
        'install_command': 'install_command',
        'uninstall_command': 'uninstall_command',
        'users': 'users'
    }

    def __init__(self, install_command=None, uninstall_command=None, users=None):
        r"""AutoInstallAppReq

        The model defined in huaweicloud sdk

        :param install_command: 安装命令(静默安装命令)。 例: ${FILE_PATH} /S 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。
        :type install_command: str
        :param uninstall_command: 卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。
        :type uninstall_command: str
        :param users: 指定安装用户。
        :type users: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        
        

        self._install_command = None
        self._uninstall_command = None
        self._users = None
        self.discriminator = None

        if install_command is not None:
            self.install_command = install_command
        if uninstall_command is not None:
            self.uninstall_command = uninstall_command
        if users is not None:
            self.users = users

    @property
    def install_command(self):
        r"""Gets the install_command of this AutoInstallAppReq.

        安装命令(静默安装命令)。 例: ${FILE_PATH} /S 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :return: The install_command of this AutoInstallAppReq.
        :rtype: str
        """
        return self._install_command

    @install_command.setter
    def install_command(self, install_command):
        r"""Sets the install_command of this AutoInstallAppReq.

        安装命令(静默安装命令)。 例: ${FILE_PATH} /S 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :param install_command: The install_command of this AutoInstallAppReq.
        :type install_command: str
        """
        self._install_command = install_command

    @property
    def uninstall_command(self):
        r"""Gets the uninstall_command of this AutoInstallAppReq.

        卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :return: The uninstall_command of this AutoInstallAppReq.
        :rtype: str
        """
        return self._uninstall_command

    @uninstall_command.setter
    def uninstall_command(self, uninstall_command):
        r"""Sets the uninstall_command of this AutoInstallAppReq.

        卸载命令(静默卸载命令)。 例: msiexec /uninstall ${FILE_PATH} /quiet。 预定义变量将采用以下值: ${FILE_PATH}: 应用安装包在桌面本地的存储路径。

        :param uninstall_command: The uninstall_command of this AutoInstallAppReq.
        :type uninstall_command: str
        """
        self._uninstall_command = uninstall_command

    @property
    def users(self):
        r"""Gets the users of this AutoInstallAppReq.

        指定安装用户。

        :return: The users of this AutoInstallAppReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
        """
        return self._users

    @users.setter
    def users(self, users):
        r"""Sets the users of this AutoInstallAppReq.

        指定安装用户。

        :param users: The users of this AutoInstallAppReq.
        :type users: list[:class:`huaweicloudsdkworkspace.v2.AccountInfo`]
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
        if not isinstance(other, AutoInstallAppReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
