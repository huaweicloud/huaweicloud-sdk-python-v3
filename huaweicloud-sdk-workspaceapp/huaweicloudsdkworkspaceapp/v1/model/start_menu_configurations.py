# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartMenuConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_menu_status': 'int',
        'start_menu_redirection_type': 'int',
        'start_menu_storage_path': 'str',
        'start_menu_relative_path': 'str',
        'start_menu_exclusive_rights': 'int',
        'start_menu_move_contents': 'int',
        'start_menu_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'start_menu_status': 'start_menu_status',
        'start_menu_redirection_type': 'start_menu_redirection_type',
        'start_menu_storage_path': 'start_menu_storage_path',
        'start_menu_relative_path': 'start_menu_relative_path',
        'start_menu_exclusive_rights': 'start_menu_exclusive_rights',
        'start_menu_move_contents': 'start_menu_move_contents',
        'start_menu_move_content_on_policy_removal': 'start_menu_move_content_on_policy_removal'
    }

    def __init__(self, start_menu_status=None, start_menu_redirection_type=None, start_menu_storage_path=None, start_menu_relative_path=None, start_menu_exclusive_rights=None, start_menu_move_contents=None, start_menu_move_content_on_policy_removal=None):
        r"""StartMenuConfigurations

        The model defined in huaweicloud sdk

        :param start_menu_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type start_menu_status: int
        :param start_menu_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type start_menu_redirection_type: int
        :param start_menu_storage_path: 文件夹重定向(v2)用户存储路径。
        :type start_menu_storage_path: str
        :param start_menu_relative_path: 目标文件夹位置。
        :type start_menu_relative_path: str
        :param start_menu_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type start_menu_exclusive_rights: int
        :param start_menu_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type start_menu_move_contents: int
        :param start_menu_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type start_menu_move_content_on_policy_removal: int
        """
        
        

        self._start_menu_status = None
        self._start_menu_redirection_type = None
        self._start_menu_storage_path = None
        self._start_menu_relative_path = None
        self._start_menu_exclusive_rights = None
        self._start_menu_move_contents = None
        self._start_menu_move_content_on_policy_removal = None
        self.discriminator = None

        if start_menu_status is not None:
            self.start_menu_status = start_menu_status
        if start_menu_redirection_type is not None:
            self.start_menu_redirection_type = start_menu_redirection_type
        if start_menu_storage_path is not None:
            self.start_menu_storage_path = start_menu_storage_path
        if start_menu_relative_path is not None:
            self.start_menu_relative_path = start_menu_relative_path
        if start_menu_exclusive_rights is not None:
            self.start_menu_exclusive_rights = start_menu_exclusive_rights
        if start_menu_move_contents is not None:
            self.start_menu_move_contents = start_menu_move_contents
        if start_menu_move_content_on_policy_removal is not None:
            self.start_menu_move_content_on_policy_removal = start_menu_move_content_on_policy_removal

    @property
    def start_menu_status(self):
        r"""Gets the start_menu_status of this StartMenuConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The start_menu_status of this StartMenuConfigurations.
        :rtype: int
        """
        return self._start_menu_status

    @start_menu_status.setter
    def start_menu_status(self, start_menu_status):
        r"""Sets the start_menu_status of this StartMenuConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param start_menu_status: The start_menu_status of this StartMenuConfigurations.
        :type start_menu_status: int
        """
        self._start_menu_status = start_menu_status

    @property
    def start_menu_redirection_type(self):
        r"""Gets the start_menu_redirection_type of this StartMenuConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The start_menu_redirection_type of this StartMenuConfigurations.
        :rtype: int
        """
        return self._start_menu_redirection_type

    @start_menu_redirection_type.setter
    def start_menu_redirection_type(self, start_menu_redirection_type):
        r"""Sets the start_menu_redirection_type of this StartMenuConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param start_menu_redirection_type: The start_menu_redirection_type of this StartMenuConfigurations.
        :type start_menu_redirection_type: int
        """
        self._start_menu_redirection_type = start_menu_redirection_type

    @property
    def start_menu_storage_path(self):
        r"""Gets the start_menu_storage_path of this StartMenuConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The start_menu_storage_path of this StartMenuConfigurations.
        :rtype: str
        """
        return self._start_menu_storage_path

    @start_menu_storage_path.setter
    def start_menu_storage_path(self, start_menu_storage_path):
        r"""Sets the start_menu_storage_path of this StartMenuConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param start_menu_storage_path: The start_menu_storage_path of this StartMenuConfigurations.
        :type start_menu_storage_path: str
        """
        self._start_menu_storage_path = start_menu_storage_path

    @property
    def start_menu_relative_path(self):
        r"""Gets the start_menu_relative_path of this StartMenuConfigurations.

        目标文件夹位置。

        :return: The start_menu_relative_path of this StartMenuConfigurations.
        :rtype: str
        """
        return self._start_menu_relative_path

    @start_menu_relative_path.setter
    def start_menu_relative_path(self, start_menu_relative_path):
        r"""Sets the start_menu_relative_path of this StartMenuConfigurations.

        目标文件夹位置。

        :param start_menu_relative_path: The start_menu_relative_path of this StartMenuConfigurations.
        :type start_menu_relative_path: str
        """
        self._start_menu_relative_path = start_menu_relative_path

    @property
    def start_menu_exclusive_rights(self):
        r"""Gets the start_menu_exclusive_rights of this StartMenuConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The start_menu_exclusive_rights of this StartMenuConfigurations.
        :rtype: int
        """
        return self._start_menu_exclusive_rights

    @start_menu_exclusive_rights.setter
    def start_menu_exclusive_rights(self, start_menu_exclusive_rights):
        r"""Sets the start_menu_exclusive_rights of this StartMenuConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param start_menu_exclusive_rights: The start_menu_exclusive_rights of this StartMenuConfigurations.
        :type start_menu_exclusive_rights: int
        """
        self._start_menu_exclusive_rights = start_menu_exclusive_rights

    @property
    def start_menu_move_contents(self):
        r"""Gets the start_menu_move_contents of this StartMenuConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The start_menu_move_contents of this StartMenuConfigurations.
        :rtype: int
        """
        return self._start_menu_move_contents

    @start_menu_move_contents.setter
    def start_menu_move_contents(self, start_menu_move_contents):
        r"""Sets the start_menu_move_contents of this StartMenuConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param start_menu_move_contents: The start_menu_move_contents of this StartMenuConfigurations.
        :type start_menu_move_contents: int
        """
        self._start_menu_move_contents = start_menu_move_contents

    @property
    def start_menu_move_content_on_policy_removal(self):
        r"""Gets the start_menu_move_content_on_policy_removal of this StartMenuConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The start_menu_move_content_on_policy_removal of this StartMenuConfigurations.
        :rtype: int
        """
        return self._start_menu_move_content_on_policy_removal

    @start_menu_move_content_on_policy_removal.setter
    def start_menu_move_content_on_policy_removal(self, start_menu_move_content_on_policy_removal):
        r"""Sets the start_menu_move_content_on_policy_removal of this StartMenuConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param start_menu_move_content_on_policy_removal: The start_menu_move_content_on_policy_removal of this StartMenuConfigurations.
        :type start_menu_move_content_on_policy_removal: int
        """
        self._start_menu_move_content_on_policy_removal = start_menu_move_content_on_policy_removal

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
        if not isinstance(other, StartMenuConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
