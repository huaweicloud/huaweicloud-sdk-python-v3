# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadsConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'downloads_status': 'int',
        'downloads_redirection_type': 'int',
        'downloads_storage_path': 'str',
        'downloads_relative_path': 'str',
        'downloads_exclusive_rights': 'int',
        'downloads_move_contents': 'int',
        'downloads_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'downloads_status': 'downloads_status',
        'downloads_redirection_type': 'downloads_redirection_type',
        'downloads_storage_path': 'downloads_storage_path',
        'downloads_relative_path': 'downloads_relative_path',
        'downloads_exclusive_rights': 'downloads_exclusive_rights',
        'downloads_move_contents': 'downloads_move_contents',
        'downloads_move_content_on_policy_removal': 'downloads_move_content_on_policy_removal'
    }

    def __init__(self, downloads_status=None, downloads_redirection_type=None, downloads_storage_path=None, downloads_relative_path=None, downloads_exclusive_rights=None, downloads_move_contents=None, downloads_move_content_on_policy_removal=None):
        r"""DownloadsConfigurations

        The model defined in huaweicloud sdk

        :param downloads_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type downloads_status: int
        :param downloads_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type downloads_redirection_type: int
        :param downloads_storage_path: 文件夹重定向(v2)用户存储路径。
        :type downloads_storage_path: str
        :param downloads_relative_path: 目标文件夹位置。
        :type downloads_relative_path: str
        :param downloads_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type downloads_exclusive_rights: int
        :param downloads_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type downloads_move_contents: int
        :param downloads_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type downloads_move_content_on_policy_removal: int
        """
        
        

        self._downloads_status = None
        self._downloads_redirection_type = None
        self._downloads_storage_path = None
        self._downloads_relative_path = None
        self._downloads_exclusive_rights = None
        self._downloads_move_contents = None
        self._downloads_move_content_on_policy_removal = None
        self.discriminator = None

        if downloads_status is not None:
            self.downloads_status = downloads_status
        if downloads_redirection_type is not None:
            self.downloads_redirection_type = downloads_redirection_type
        if downloads_storage_path is not None:
            self.downloads_storage_path = downloads_storage_path
        if downloads_relative_path is not None:
            self.downloads_relative_path = downloads_relative_path
        if downloads_exclusive_rights is not None:
            self.downloads_exclusive_rights = downloads_exclusive_rights
        if downloads_move_contents is not None:
            self.downloads_move_contents = downloads_move_contents
        if downloads_move_content_on_policy_removal is not None:
            self.downloads_move_content_on_policy_removal = downloads_move_content_on_policy_removal

    @property
    def downloads_status(self):
        r"""Gets the downloads_status of this DownloadsConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The downloads_status of this DownloadsConfigurations.
        :rtype: int
        """
        return self._downloads_status

    @downloads_status.setter
    def downloads_status(self, downloads_status):
        r"""Sets the downloads_status of this DownloadsConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param downloads_status: The downloads_status of this DownloadsConfigurations.
        :type downloads_status: int
        """
        self._downloads_status = downloads_status

    @property
    def downloads_redirection_type(self):
        r"""Gets the downloads_redirection_type of this DownloadsConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The downloads_redirection_type of this DownloadsConfigurations.
        :rtype: int
        """
        return self._downloads_redirection_type

    @downloads_redirection_type.setter
    def downloads_redirection_type(self, downloads_redirection_type):
        r"""Sets the downloads_redirection_type of this DownloadsConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param downloads_redirection_type: The downloads_redirection_type of this DownloadsConfigurations.
        :type downloads_redirection_type: int
        """
        self._downloads_redirection_type = downloads_redirection_type

    @property
    def downloads_storage_path(self):
        r"""Gets the downloads_storage_path of this DownloadsConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The downloads_storage_path of this DownloadsConfigurations.
        :rtype: str
        """
        return self._downloads_storage_path

    @downloads_storage_path.setter
    def downloads_storage_path(self, downloads_storage_path):
        r"""Sets the downloads_storage_path of this DownloadsConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param downloads_storage_path: The downloads_storage_path of this DownloadsConfigurations.
        :type downloads_storage_path: str
        """
        self._downloads_storage_path = downloads_storage_path

    @property
    def downloads_relative_path(self):
        r"""Gets the downloads_relative_path of this DownloadsConfigurations.

        目标文件夹位置。

        :return: The downloads_relative_path of this DownloadsConfigurations.
        :rtype: str
        """
        return self._downloads_relative_path

    @downloads_relative_path.setter
    def downloads_relative_path(self, downloads_relative_path):
        r"""Sets the downloads_relative_path of this DownloadsConfigurations.

        目标文件夹位置。

        :param downloads_relative_path: The downloads_relative_path of this DownloadsConfigurations.
        :type downloads_relative_path: str
        """
        self._downloads_relative_path = downloads_relative_path

    @property
    def downloads_exclusive_rights(self):
        r"""Gets the downloads_exclusive_rights of this DownloadsConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The downloads_exclusive_rights of this DownloadsConfigurations.
        :rtype: int
        """
        return self._downloads_exclusive_rights

    @downloads_exclusive_rights.setter
    def downloads_exclusive_rights(self, downloads_exclusive_rights):
        r"""Sets the downloads_exclusive_rights of this DownloadsConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param downloads_exclusive_rights: The downloads_exclusive_rights of this DownloadsConfigurations.
        :type downloads_exclusive_rights: int
        """
        self._downloads_exclusive_rights = downloads_exclusive_rights

    @property
    def downloads_move_contents(self):
        r"""Gets the downloads_move_contents of this DownloadsConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The downloads_move_contents of this DownloadsConfigurations.
        :rtype: int
        """
        return self._downloads_move_contents

    @downloads_move_contents.setter
    def downloads_move_contents(self, downloads_move_contents):
        r"""Sets the downloads_move_contents of this DownloadsConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param downloads_move_contents: The downloads_move_contents of this DownloadsConfigurations.
        :type downloads_move_contents: int
        """
        self._downloads_move_contents = downloads_move_contents

    @property
    def downloads_move_content_on_policy_removal(self):
        r"""Gets the downloads_move_content_on_policy_removal of this DownloadsConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The downloads_move_content_on_policy_removal of this DownloadsConfigurations.
        :rtype: int
        """
        return self._downloads_move_content_on_policy_removal

    @downloads_move_content_on_policy_removal.setter
    def downloads_move_content_on_policy_removal(self, downloads_move_content_on_policy_removal):
        r"""Sets the downloads_move_content_on_policy_removal of this DownloadsConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param downloads_move_content_on_policy_removal: The downloads_move_content_on_policy_removal of this DownloadsConfigurations.
        :type downloads_move_content_on_policy_removal: int
        """
        self._downloads_move_content_on_policy_removal = downloads_move_content_on_policy_removal

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
        if not isinstance(other, DownloadsConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
