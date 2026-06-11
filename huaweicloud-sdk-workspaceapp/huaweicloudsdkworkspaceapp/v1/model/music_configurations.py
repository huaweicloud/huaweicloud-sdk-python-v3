# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MusicConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'music_status': 'int',
        'music_redirection_type': 'int',
        'music_storage_path': 'str',
        'music_relative_path': 'str',
        'music_exclusive_rights': 'int',
        'music_move_contents': 'int',
        'music_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'music_status': 'music_status',
        'music_redirection_type': 'music_redirection_type',
        'music_storage_path': 'music_storage_path',
        'music_relative_path': 'music_relative_path',
        'music_exclusive_rights': 'music_exclusive_rights',
        'music_move_contents': 'music_move_contents',
        'music_move_content_on_policy_removal': 'music_move_content_on_policy_removal'
    }

    def __init__(self, music_status=None, music_redirection_type=None, music_storage_path=None, music_relative_path=None, music_exclusive_rights=None, music_move_contents=None, music_move_content_on_policy_removal=None):
        r"""MusicConfigurations

        The model defined in huaweicloud sdk

        :param music_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type music_status: int
        :param music_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type music_redirection_type: int
        :param music_storage_path: 文件夹重定向(v2)用户存储路径。
        :type music_storage_path: str
        :param music_relative_path: 目标文件夹位置。
        :type music_relative_path: str
        :param music_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type music_exclusive_rights: int
        :param music_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type music_move_contents: int
        :param music_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type music_move_content_on_policy_removal: int
        """
        
        

        self._music_status = None
        self._music_redirection_type = None
        self._music_storage_path = None
        self._music_relative_path = None
        self._music_exclusive_rights = None
        self._music_move_contents = None
        self._music_move_content_on_policy_removal = None
        self.discriminator = None

        if music_status is not None:
            self.music_status = music_status
        if music_redirection_type is not None:
            self.music_redirection_type = music_redirection_type
        if music_storage_path is not None:
            self.music_storage_path = music_storage_path
        if music_relative_path is not None:
            self.music_relative_path = music_relative_path
        if music_exclusive_rights is not None:
            self.music_exclusive_rights = music_exclusive_rights
        if music_move_contents is not None:
            self.music_move_contents = music_move_contents
        if music_move_content_on_policy_removal is not None:
            self.music_move_content_on_policy_removal = music_move_content_on_policy_removal

    @property
    def music_status(self):
        r"""Gets the music_status of this MusicConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The music_status of this MusicConfigurations.
        :rtype: int
        """
        return self._music_status

    @music_status.setter
    def music_status(self, music_status):
        r"""Sets the music_status of this MusicConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param music_status: The music_status of this MusicConfigurations.
        :type music_status: int
        """
        self._music_status = music_status

    @property
    def music_redirection_type(self):
        r"""Gets the music_redirection_type of this MusicConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The music_redirection_type of this MusicConfigurations.
        :rtype: int
        """
        return self._music_redirection_type

    @music_redirection_type.setter
    def music_redirection_type(self, music_redirection_type):
        r"""Sets the music_redirection_type of this MusicConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param music_redirection_type: The music_redirection_type of this MusicConfigurations.
        :type music_redirection_type: int
        """
        self._music_redirection_type = music_redirection_type

    @property
    def music_storage_path(self):
        r"""Gets the music_storage_path of this MusicConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The music_storage_path of this MusicConfigurations.
        :rtype: str
        """
        return self._music_storage_path

    @music_storage_path.setter
    def music_storage_path(self, music_storage_path):
        r"""Sets the music_storage_path of this MusicConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param music_storage_path: The music_storage_path of this MusicConfigurations.
        :type music_storage_path: str
        """
        self._music_storage_path = music_storage_path

    @property
    def music_relative_path(self):
        r"""Gets the music_relative_path of this MusicConfigurations.

        目标文件夹位置。

        :return: The music_relative_path of this MusicConfigurations.
        :rtype: str
        """
        return self._music_relative_path

    @music_relative_path.setter
    def music_relative_path(self, music_relative_path):
        r"""Sets the music_relative_path of this MusicConfigurations.

        目标文件夹位置。

        :param music_relative_path: The music_relative_path of this MusicConfigurations.
        :type music_relative_path: str
        """
        self._music_relative_path = music_relative_path

    @property
    def music_exclusive_rights(self):
        r"""Gets the music_exclusive_rights of this MusicConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The music_exclusive_rights of this MusicConfigurations.
        :rtype: int
        """
        return self._music_exclusive_rights

    @music_exclusive_rights.setter
    def music_exclusive_rights(self, music_exclusive_rights):
        r"""Sets the music_exclusive_rights of this MusicConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param music_exclusive_rights: The music_exclusive_rights of this MusicConfigurations.
        :type music_exclusive_rights: int
        """
        self._music_exclusive_rights = music_exclusive_rights

    @property
    def music_move_contents(self):
        r"""Gets the music_move_contents of this MusicConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The music_move_contents of this MusicConfigurations.
        :rtype: int
        """
        return self._music_move_contents

    @music_move_contents.setter
    def music_move_contents(self, music_move_contents):
        r"""Sets the music_move_contents of this MusicConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param music_move_contents: The music_move_contents of this MusicConfigurations.
        :type music_move_contents: int
        """
        self._music_move_contents = music_move_contents

    @property
    def music_move_content_on_policy_removal(self):
        r"""Gets the music_move_content_on_policy_removal of this MusicConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The music_move_content_on_policy_removal of this MusicConfigurations.
        :rtype: int
        """
        return self._music_move_content_on_policy_removal

    @music_move_content_on_policy_removal.setter
    def music_move_content_on_policy_removal(self, music_move_content_on_policy_removal):
        r"""Sets the music_move_content_on_policy_removal of this MusicConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param music_move_content_on_policy_removal: The music_move_content_on_policy_removal of this MusicConfigurations.
        :type music_move_content_on_policy_removal: int
        """
        self._music_move_content_on_policy_removal = music_move_content_on_policy_removal

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
        if not isinstance(other, MusicConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
