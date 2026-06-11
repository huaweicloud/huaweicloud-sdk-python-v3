# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_status': 'int',
        'desktop_redirection_type': 'int',
        'desktop_storage_path': 'str',
        'desktop_relative_path': 'str',
        'desktop_exclusive_rights': 'int',
        'desktop_move_contents': 'int',
        'desktop_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'desktop_status': 'desktop_status',
        'desktop_redirection_type': 'desktop_redirection_type',
        'desktop_storage_path': 'desktop_storage_path',
        'desktop_relative_path': 'desktop_relative_path',
        'desktop_exclusive_rights': 'desktop_exclusive_rights',
        'desktop_move_contents': 'desktop_move_contents',
        'desktop_move_content_on_policy_removal': 'desktop_move_content_on_policy_removal'
    }

    def __init__(self, desktop_status=None, desktop_redirection_type=None, desktop_storage_path=None, desktop_relative_path=None, desktop_exclusive_rights=None, desktop_move_contents=None, desktop_move_content_on_policy_removal=None):
        r"""DesktopConfigurations

        The model defined in huaweicloud sdk

        :param desktop_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type desktop_status: int
        :param desktop_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type desktop_redirection_type: int
        :param desktop_storage_path: 文件夹重定向(v2)用户存储路径。
        :type desktop_storage_path: str
        :param desktop_relative_path: 目标文件夹位置。
        :type desktop_relative_path: str
        :param desktop_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type desktop_exclusive_rights: int
        :param desktop_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type desktop_move_contents: int
        :param desktop_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type desktop_move_content_on_policy_removal: int
        """
        
        

        self._desktop_status = None
        self._desktop_redirection_type = None
        self._desktop_storage_path = None
        self._desktop_relative_path = None
        self._desktop_exclusive_rights = None
        self._desktop_move_contents = None
        self._desktop_move_content_on_policy_removal = None
        self.discriminator = None

        if desktop_status is not None:
            self.desktop_status = desktop_status
        if desktop_redirection_type is not None:
            self.desktop_redirection_type = desktop_redirection_type
        if desktop_storage_path is not None:
            self.desktop_storage_path = desktop_storage_path
        if desktop_relative_path is not None:
            self.desktop_relative_path = desktop_relative_path
        if desktop_exclusive_rights is not None:
            self.desktop_exclusive_rights = desktop_exclusive_rights
        if desktop_move_contents is not None:
            self.desktop_move_contents = desktop_move_contents
        if desktop_move_content_on_policy_removal is not None:
            self.desktop_move_content_on_policy_removal = desktop_move_content_on_policy_removal

    @property
    def desktop_status(self):
        r"""Gets the desktop_status of this DesktopConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The desktop_status of this DesktopConfigurations.
        :rtype: int
        """
        return self._desktop_status

    @desktop_status.setter
    def desktop_status(self, desktop_status):
        r"""Sets the desktop_status of this DesktopConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param desktop_status: The desktop_status of this DesktopConfigurations.
        :type desktop_status: int
        """
        self._desktop_status = desktop_status

    @property
    def desktop_redirection_type(self):
        r"""Gets the desktop_redirection_type of this DesktopConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The desktop_redirection_type of this DesktopConfigurations.
        :rtype: int
        """
        return self._desktop_redirection_type

    @desktop_redirection_type.setter
    def desktop_redirection_type(self, desktop_redirection_type):
        r"""Sets the desktop_redirection_type of this DesktopConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param desktop_redirection_type: The desktop_redirection_type of this DesktopConfigurations.
        :type desktop_redirection_type: int
        """
        self._desktop_redirection_type = desktop_redirection_type

    @property
    def desktop_storage_path(self):
        r"""Gets the desktop_storage_path of this DesktopConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The desktop_storage_path of this DesktopConfigurations.
        :rtype: str
        """
        return self._desktop_storage_path

    @desktop_storage_path.setter
    def desktop_storage_path(self, desktop_storage_path):
        r"""Sets the desktop_storage_path of this DesktopConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param desktop_storage_path: The desktop_storage_path of this DesktopConfigurations.
        :type desktop_storage_path: str
        """
        self._desktop_storage_path = desktop_storage_path

    @property
    def desktop_relative_path(self):
        r"""Gets the desktop_relative_path of this DesktopConfigurations.

        目标文件夹位置。

        :return: The desktop_relative_path of this DesktopConfigurations.
        :rtype: str
        """
        return self._desktop_relative_path

    @desktop_relative_path.setter
    def desktop_relative_path(self, desktop_relative_path):
        r"""Sets the desktop_relative_path of this DesktopConfigurations.

        目标文件夹位置。

        :param desktop_relative_path: The desktop_relative_path of this DesktopConfigurations.
        :type desktop_relative_path: str
        """
        self._desktop_relative_path = desktop_relative_path

    @property
    def desktop_exclusive_rights(self):
        r"""Gets the desktop_exclusive_rights of this DesktopConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The desktop_exclusive_rights of this DesktopConfigurations.
        :rtype: int
        """
        return self._desktop_exclusive_rights

    @desktop_exclusive_rights.setter
    def desktop_exclusive_rights(self, desktop_exclusive_rights):
        r"""Sets the desktop_exclusive_rights of this DesktopConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param desktop_exclusive_rights: The desktop_exclusive_rights of this DesktopConfigurations.
        :type desktop_exclusive_rights: int
        """
        self._desktop_exclusive_rights = desktop_exclusive_rights

    @property
    def desktop_move_contents(self):
        r"""Gets the desktop_move_contents of this DesktopConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The desktop_move_contents of this DesktopConfigurations.
        :rtype: int
        """
        return self._desktop_move_contents

    @desktop_move_contents.setter
    def desktop_move_contents(self, desktop_move_contents):
        r"""Sets the desktop_move_contents of this DesktopConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param desktop_move_contents: The desktop_move_contents of this DesktopConfigurations.
        :type desktop_move_contents: int
        """
        self._desktop_move_contents = desktop_move_contents

    @property
    def desktop_move_content_on_policy_removal(self):
        r"""Gets the desktop_move_content_on_policy_removal of this DesktopConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The desktop_move_content_on_policy_removal of this DesktopConfigurations.
        :rtype: int
        """
        return self._desktop_move_content_on_policy_removal

    @desktop_move_content_on_policy_removal.setter
    def desktop_move_content_on_policy_removal(self, desktop_move_content_on_policy_removal):
        r"""Sets the desktop_move_content_on_policy_removal of this DesktopConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param desktop_move_content_on_policy_removal: The desktop_move_content_on_policy_removal of this DesktopConfigurations.
        :type desktop_move_content_on_policy_removal: int
        """
        self._desktop_move_content_on_policy_removal = desktop_move_content_on_policy_removal

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
        if not isinstance(other, DesktopConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
