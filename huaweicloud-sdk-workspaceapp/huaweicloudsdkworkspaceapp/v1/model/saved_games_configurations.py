# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SavedGamesConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'saved_games_status': 'int',
        'saved_games_redirection_type': 'int',
        'saved_games_storage_path': 'str',
        'saved_games_relative_path': 'str',
        'saved_games_exclusive_rights': 'int',
        'saved_games_move_contents': 'int',
        'saved_games_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'saved_games_status': 'saved_games_status',
        'saved_games_redirection_type': 'saved_games_redirection_type',
        'saved_games_storage_path': 'saved_games_storage_path',
        'saved_games_relative_path': 'saved_games_relative_path',
        'saved_games_exclusive_rights': 'saved_games_exclusive_rights',
        'saved_games_move_contents': 'saved_games_move_contents',
        'saved_games_move_content_on_policy_removal': 'saved_games_move_content_on_policy_removal'
    }

    def __init__(self, saved_games_status=None, saved_games_redirection_type=None, saved_games_storage_path=None, saved_games_relative_path=None, saved_games_exclusive_rights=None, saved_games_move_contents=None, saved_games_move_content_on_policy_removal=None):
        r"""SavedGamesConfigurations

        The model defined in huaweicloud sdk

        :param saved_games_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type saved_games_status: int
        :param saved_games_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type saved_games_redirection_type: int
        :param saved_games_storage_path: 文件夹重定向(v2)用户存储路径。
        :type saved_games_storage_path: str
        :param saved_games_relative_path: 目标文件夹位置。
        :type saved_games_relative_path: str
        :param saved_games_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type saved_games_exclusive_rights: int
        :param saved_games_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type saved_games_move_contents: int
        :param saved_games_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type saved_games_move_content_on_policy_removal: int
        """
        
        

        self._saved_games_status = None
        self._saved_games_redirection_type = None
        self._saved_games_storage_path = None
        self._saved_games_relative_path = None
        self._saved_games_exclusive_rights = None
        self._saved_games_move_contents = None
        self._saved_games_move_content_on_policy_removal = None
        self.discriminator = None

        if saved_games_status is not None:
            self.saved_games_status = saved_games_status
        if saved_games_redirection_type is not None:
            self.saved_games_redirection_type = saved_games_redirection_type
        if saved_games_storage_path is not None:
            self.saved_games_storage_path = saved_games_storage_path
        if saved_games_relative_path is not None:
            self.saved_games_relative_path = saved_games_relative_path
        if saved_games_exclusive_rights is not None:
            self.saved_games_exclusive_rights = saved_games_exclusive_rights
        if saved_games_move_contents is not None:
            self.saved_games_move_contents = saved_games_move_contents
        if saved_games_move_content_on_policy_removal is not None:
            self.saved_games_move_content_on_policy_removal = saved_games_move_content_on_policy_removal

    @property
    def saved_games_status(self):
        r"""Gets the saved_games_status of this SavedGamesConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The saved_games_status of this SavedGamesConfigurations.
        :rtype: int
        """
        return self._saved_games_status

    @saved_games_status.setter
    def saved_games_status(self, saved_games_status):
        r"""Sets the saved_games_status of this SavedGamesConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param saved_games_status: The saved_games_status of this SavedGamesConfigurations.
        :type saved_games_status: int
        """
        self._saved_games_status = saved_games_status

    @property
    def saved_games_redirection_type(self):
        r"""Gets the saved_games_redirection_type of this SavedGamesConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The saved_games_redirection_type of this SavedGamesConfigurations.
        :rtype: int
        """
        return self._saved_games_redirection_type

    @saved_games_redirection_type.setter
    def saved_games_redirection_type(self, saved_games_redirection_type):
        r"""Sets the saved_games_redirection_type of this SavedGamesConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param saved_games_redirection_type: The saved_games_redirection_type of this SavedGamesConfigurations.
        :type saved_games_redirection_type: int
        """
        self._saved_games_redirection_type = saved_games_redirection_type

    @property
    def saved_games_storage_path(self):
        r"""Gets the saved_games_storage_path of this SavedGamesConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The saved_games_storage_path of this SavedGamesConfigurations.
        :rtype: str
        """
        return self._saved_games_storage_path

    @saved_games_storage_path.setter
    def saved_games_storage_path(self, saved_games_storage_path):
        r"""Sets the saved_games_storage_path of this SavedGamesConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param saved_games_storage_path: The saved_games_storage_path of this SavedGamesConfigurations.
        :type saved_games_storage_path: str
        """
        self._saved_games_storage_path = saved_games_storage_path

    @property
    def saved_games_relative_path(self):
        r"""Gets the saved_games_relative_path of this SavedGamesConfigurations.

        目标文件夹位置。

        :return: The saved_games_relative_path of this SavedGamesConfigurations.
        :rtype: str
        """
        return self._saved_games_relative_path

    @saved_games_relative_path.setter
    def saved_games_relative_path(self, saved_games_relative_path):
        r"""Sets the saved_games_relative_path of this SavedGamesConfigurations.

        目标文件夹位置。

        :param saved_games_relative_path: The saved_games_relative_path of this SavedGamesConfigurations.
        :type saved_games_relative_path: str
        """
        self._saved_games_relative_path = saved_games_relative_path

    @property
    def saved_games_exclusive_rights(self):
        r"""Gets the saved_games_exclusive_rights of this SavedGamesConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The saved_games_exclusive_rights of this SavedGamesConfigurations.
        :rtype: int
        """
        return self._saved_games_exclusive_rights

    @saved_games_exclusive_rights.setter
    def saved_games_exclusive_rights(self, saved_games_exclusive_rights):
        r"""Sets the saved_games_exclusive_rights of this SavedGamesConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param saved_games_exclusive_rights: The saved_games_exclusive_rights of this SavedGamesConfigurations.
        :type saved_games_exclusive_rights: int
        """
        self._saved_games_exclusive_rights = saved_games_exclusive_rights

    @property
    def saved_games_move_contents(self):
        r"""Gets the saved_games_move_contents of this SavedGamesConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The saved_games_move_contents of this SavedGamesConfigurations.
        :rtype: int
        """
        return self._saved_games_move_contents

    @saved_games_move_contents.setter
    def saved_games_move_contents(self, saved_games_move_contents):
        r"""Sets the saved_games_move_contents of this SavedGamesConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param saved_games_move_contents: The saved_games_move_contents of this SavedGamesConfigurations.
        :type saved_games_move_contents: int
        """
        self._saved_games_move_contents = saved_games_move_contents

    @property
    def saved_games_move_content_on_policy_removal(self):
        r"""Gets the saved_games_move_content_on_policy_removal of this SavedGamesConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The saved_games_move_content_on_policy_removal of this SavedGamesConfigurations.
        :rtype: int
        """
        return self._saved_games_move_content_on_policy_removal

    @saved_games_move_content_on_policy_removal.setter
    def saved_games_move_content_on_policy_removal(self, saved_games_move_content_on_policy_removal):
        r"""Sets the saved_games_move_content_on_policy_removal of this SavedGamesConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param saved_games_move_content_on_policy_removal: The saved_games_move_content_on_policy_removal of this SavedGamesConfigurations.
        :type saved_games_move_content_on_policy_removal: int
        """
        self._saved_games_move_content_on_policy_removal = saved_games_move_content_on_policy_removal

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
        if not isinstance(other, SavedGamesConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
