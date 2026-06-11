# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FavoritesConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'favorites_status': 'int',
        'favorites_redirection_type': 'int',
        'favorites_storage_path': 'str',
        'favorites_relative_path': 'str',
        'favorites_exclusive_rights': 'int',
        'favorites_move_contents': 'int',
        'favorites_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'favorites_status': 'favorites_status',
        'favorites_redirection_type': 'favorites_redirection_type',
        'favorites_storage_path': 'favorites_storage_path',
        'favorites_relative_path': 'favorites_relative_path',
        'favorites_exclusive_rights': 'favorites_exclusive_rights',
        'favorites_move_contents': 'favorites_move_contents',
        'favorites_move_content_on_policy_removal': 'favorites_move_content_on_policy_removal'
    }

    def __init__(self, favorites_status=None, favorites_redirection_type=None, favorites_storage_path=None, favorites_relative_path=None, favorites_exclusive_rights=None, favorites_move_contents=None, favorites_move_content_on_policy_removal=None):
        r"""FavoritesConfigurations

        The model defined in huaweicloud sdk

        :param favorites_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type favorites_status: int
        :param favorites_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type favorites_redirection_type: int
        :param favorites_storage_path: 文件夹重定向(v2)用户存储路径。
        :type favorites_storage_path: str
        :param favorites_relative_path: 目标文件夹位置。
        :type favorites_relative_path: str
        :param favorites_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type favorites_exclusive_rights: int
        :param favorites_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type favorites_move_contents: int
        :param favorites_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type favorites_move_content_on_policy_removal: int
        """
        
        

        self._favorites_status = None
        self._favorites_redirection_type = None
        self._favorites_storage_path = None
        self._favorites_relative_path = None
        self._favorites_exclusive_rights = None
        self._favorites_move_contents = None
        self._favorites_move_content_on_policy_removal = None
        self.discriminator = None

        if favorites_status is not None:
            self.favorites_status = favorites_status
        if favorites_redirection_type is not None:
            self.favorites_redirection_type = favorites_redirection_type
        if favorites_storage_path is not None:
            self.favorites_storage_path = favorites_storage_path
        if favorites_relative_path is not None:
            self.favorites_relative_path = favorites_relative_path
        if favorites_exclusive_rights is not None:
            self.favorites_exclusive_rights = favorites_exclusive_rights
        if favorites_move_contents is not None:
            self.favorites_move_contents = favorites_move_contents
        if favorites_move_content_on_policy_removal is not None:
            self.favorites_move_content_on_policy_removal = favorites_move_content_on_policy_removal

    @property
    def favorites_status(self):
        r"""Gets the favorites_status of this FavoritesConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The favorites_status of this FavoritesConfigurations.
        :rtype: int
        """
        return self._favorites_status

    @favorites_status.setter
    def favorites_status(self, favorites_status):
        r"""Sets the favorites_status of this FavoritesConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param favorites_status: The favorites_status of this FavoritesConfigurations.
        :type favorites_status: int
        """
        self._favorites_status = favorites_status

    @property
    def favorites_redirection_type(self):
        r"""Gets the favorites_redirection_type of this FavoritesConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The favorites_redirection_type of this FavoritesConfigurations.
        :rtype: int
        """
        return self._favorites_redirection_type

    @favorites_redirection_type.setter
    def favorites_redirection_type(self, favorites_redirection_type):
        r"""Sets the favorites_redirection_type of this FavoritesConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param favorites_redirection_type: The favorites_redirection_type of this FavoritesConfigurations.
        :type favorites_redirection_type: int
        """
        self._favorites_redirection_type = favorites_redirection_type

    @property
    def favorites_storage_path(self):
        r"""Gets the favorites_storage_path of this FavoritesConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The favorites_storage_path of this FavoritesConfigurations.
        :rtype: str
        """
        return self._favorites_storage_path

    @favorites_storage_path.setter
    def favorites_storage_path(self, favorites_storage_path):
        r"""Sets the favorites_storage_path of this FavoritesConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param favorites_storage_path: The favorites_storage_path of this FavoritesConfigurations.
        :type favorites_storage_path: str
        """
        self._favorites_storage_path = favorites_storage_path

    @property
    def favorites_relative_path(self):
        r"""Gets the favorites_relative_path of this FavoritesConfigurations.

        目标文件夹位置。

        :return: The favorites_relative_path of this FavoritesConfigurations.
        :rtype: str
        """
        return self._favorites_relative_path

    @favorites_relative_path.setter
    def favorites_relative_path(self, favorites_relative_path):
        r"""Sets the favorites_relative_path of this FavoritesConfigurations.

        目标文件夹位置。

        :param favorites_relative_path: The favorites_relative_path of this FavoritesConfigurations.
        :type favorites_relative_path: str
        """
        self._favorites_relative_path = favorites_relative_path

    @property
    def favorites_exclusive_rights(self):
        r"""Gets the favorites_exclusive_rights of this FavoritesConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The favorites_exclusive_rights of this FavoritesConfigurations.
        :rtype: int
        """
        return self._favorites_exclusive_rights

    @favorites_exclusive_rights.setter
    def favorites_exclusive_rights(self, favorites_exclusive_rights):
        r"""Sets the favorites_exclusive_rights of this FavoritesConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param favorites_exclusive_rights: The favorites_exclusive_rights of this FavoritesConfigurations.
        :type favorites_exclusive_rights: int
        """
        self._favorites_exclusive_rights = favorites_exclusive_rights

    @property
    def favorites_move_contents(self):
        r"""Gets the favorites_move_contents of this FavoritesConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The favorites_move_contents of this FavoritesConfigurations.
        :rtype: int
        """
        return self._favorites_move_contents

    @favorites_move_contents.setter
    def favorites_move_contents(self, favorites_move_contents):
        r"""Sets the favorites_move_contents of this FavoritesConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param favorites_move_contents: The favorites_move_contents of this FavoritesConfigurations.
        :type favorites_move_contents: int
        """
        self._favorites_move_contents = favorites_move_contents

    @property
    def favorites_move_content_on_policy_removal(self):
        r"""Gets the favorites_move_content_on_policy_removal of this FavoritesConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The favorites_move_content_on_policy_removal of this FavoritesConfigurations.
        :rtype: int
        """
        return self._favorites_move_content_on_policy_removal

    @favorites_move_content_on_policy_removal.setter
    def favorites_move_content_on_policy_removal(self, favorites_move_content_on_policy_removal):
        r"""Sets the favorites_move_content_on_policy_removal of this FavoritesConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param favorites_move_content_on_policy_removal: The favorites_move_content_on_policy_removal of this FavoritesConfigurations.
        :type favorites_move_content_on_policy_removal: int
        """
        self._favorites_move_content_on_policy_removal = favorites_move_content_on_policy_removal

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
        if not isinstance(other, FavoritesConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
