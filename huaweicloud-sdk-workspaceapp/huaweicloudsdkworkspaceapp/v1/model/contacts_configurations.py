# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContactsConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'contacts_status': 'int',
        'contacts_redirection_type': 'int',
        'contacts_storage_path': 'str',
        'contacts_relative_path': 'str',
        'contacts_exclusive_rights': 'int',
        'contacts_move_contents': 'int',
        'contacts_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'contacts_status': 'contacts_status',
        'contacts_redirection_type': 'contacts_redirection_type',
        'contacts_storage_path': 'contacts_storage_path',
        'contacts_relative_path': 'contacts_relative_path',
        'contacts_exclusive_rights': 'contacts_exclusive_rights',
        'contacts_move_contents': 'contacts_move_contents',
        'contacts_move_content_on_policy_removal': 'contacts_move_content_on_policy_removal'
    }

    def __init__(self, contacts_status=None, contacts_redirection_type=None, contacts_storage_path=None, contacts_relative_path=None, contacts_exclusive_rights=None, contacts_move_contents=None, contacts_move_content_on_policy_removal=None):
        r"""ContactsConfigurations

        The model defined in huaweicloud sdk

        :param contacts_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type contacts_status: int
        :param contacts_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type contacts_redirection_type: int
        :param contacts_storage_path: 文件夹重定向(v2)用户存储路径。
        :type contacts_storage_path: str
        :param contacts_relative_path: 目标文件夹位置。
        :type contacts_relative_path: str
        :param contacts_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type contacts_exclusive_rights: int
        :param contacts_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type contacts_move_contents: int
        :param contacts_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type contacts_move_content_on_policy_removal: int
        """
        
        

        self._contacts_status = None
        self._contacts_redirection_type = None
        self._contacts_storage_path = None
        self._contacts_relative_path = None
        self._contacts_exclusive_rights = None
        self._contacts_move_contents = None
        self._contacts_move_content_on_policy_removal = None
        self.discriminator = None

        if contacts_status is not None:
            self.contacts_status = contacts_status
        if contacts_redirection_type is not None:
            self.contacts_redirection_type = contacts_redirection_type
        if contacts_storage_path is not None:
            self.contacts_storage_path = contacts_storage_path
        if contacts_relative_path is not None:
            self.contacts_relative_path = contacts_relative_path
        if contacts_exclusive_rights is not None:
            self.contacts_exclusive_rights = contacts_exclusive_rights
        if contacts_move_contents is not None:
            self.contacts_move_contents = contacts_move_contents
        if contacts_move_content_on_policy_removal is not None:
            self.contacts_move_content_on_policy_removal = contacts_move_content_on_policy_removal

    @property
    def contacts_status(self):
        r"""Gets the contacts_status of this ContactsConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The contacts_status of this ContactsConfigurations.
        :rtype: int
        """
        return self._contacts_status

    @contacts_status.setter
    def contacts_status(self, contacts_status):
        r"""Sets the contacts_status of this ContactsConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param contacts_status: The contacts_status of this ContactsConfigurations.
        :type contacts_status: int
        """
        self._contacts_status = contacts_status

    @property
    def contacts_redirection_type(self):
        r"""Gets the contacts_redirection_type of this ContactsConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The contacts_redirection_type of this ContactsConfigurations.
        :rtype: int
        """
        return self._contacts_redirection_type

    @contacts_redirection_type.setter
    def contacts_redirection_type(self, contacts_redirection_type):
        r"""Sets the contacts_redirection_type of this ContactsConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param contacts_redirection_type: The contacts_redirection_type of this ContactsConfigurations.
        :type contacts_redirection_type: int
        """
        self._contacts_redirection_type = contacts_redirection_type

    @property
    def contacts_storage_path(self):
        r"""Gets the contacts_storage_path of this ContactsConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The contacts_storage_path of this ContactsConfigurations.
        :rtype: str
        """
        return self._contacts_storage_path

    @contacts_storage_path.setter
    def contacts_storage_path(self, contacts_storage_path):
        r"""Sets the contacts_storage_path of this ContactsConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param contacts_storage_path: The contacts_storage_path of this ContactsConfigurations.
        :type contacts_storage_path: str
        """
        self._contacts_storage_path = contacts_storage_path

    @property
    def contacts_relative_path(self):
        r"""Gets the contacts_relative_path of this ContactsConfigurations.

        目标文件夹位置。

        :return: The contacts_relative_path of this ContactsConfigurations.
        :rtype: str
        """
        return self._contacts_relative_path

    @contacts_relative_path.setter
    def contacts_relative_path(self, contacts_relative_path):
        r"""Sets the contacts_relative_path of this ContactsConfigurations.

        目标文件夹位置。

        :param contacts_relative_path: The contacts_relative_path of this ContactsConfigurations.
        :type contacts_relative_path: str
        """
        self._contacts_relative_path = contacts_relative_path

    @property
    def contacts_exclusive_rights(self):
        r"""Gets the contacts_exclusive_rights of this ContactsConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The contacts_exclusive_rights of this ContactsConfigurations.
        :rtype: int
        """
        return self._contacts_exclusive_rights

    @contacts_exclusive_rights.setter
    def contacts_exclusive_rights(self, contacts_exclusive_rights):
        r"""Sets the contacts_exclusive_rights of this ContactsConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param contacts_exclusive_rights: The contacts_exclusive_rights of this ContactsConfigurations.
        :type contacts_exclusive_rights: int
        """
        self._contacts_exclusive_rights = contacts_exclusive_rights

    @property
    def contacts_move_contents(self):
        r"""Gets the contacts_move_contents of this ContactsConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The contacts_move_contents of this ContactsConfigurations.
        :rtype: int
        """
        return self._contacts_move_contents

    @contacts_move_contents.setter
    def contacts_move_contents(self, contacts_move_contents):
        r"""Sets the contacts_move_contents of this ContactsConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param contacts_move_contents: The contacts_move_contents of this ContactsConfigurations.
        :type contacts_move_contents: int
        """
        self._contacts_move_contents = contacts_move_contents

    @property
    def contacts_move_content_on_policy_removal(self):
        r"""Gets the contacts_move_content_on_policy_removal of this ContactsConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The contacts_move_content_on_policy_removal of this ContactsConfigurations.
        :rtype: int
        """
        return self._contacts_move_content_on_policy_removal

    @contacts_move_content_on_policy_removal.setter
    def contacts_move_content_on_policy_removal(self, contacts_move_content_on_policy_removal):
        r"""Sets the contacts_move_content_on_policy_removal of this ContactsConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param contacts_move_content_on_policy_removal: The contacts_move_content_on_policy_removal of this ContactsConfigurations.
        :type contacts_move_content_on_policy_removal: int
        """
        self._contacts_move_content_on_policy_removal = contacts_move_content_on_policy_removal

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
        if not isinstance(other, ContactsConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
