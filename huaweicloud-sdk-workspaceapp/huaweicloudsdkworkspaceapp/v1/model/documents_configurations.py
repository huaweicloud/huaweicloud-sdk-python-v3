# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DocumentsConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'documents_status': 'int',
        'documents_redirection_type': 'int',
        'documents_storage_path': 'str',
        'documents_relative_path': 'str',
        'documents_exclusive_rights': 'int',
        'documents_move_contents': 'int',
        'documents_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'documents_status': 'documents_status',
        'documents_redirection_type': 'documents_redirection_type',
        'documents_storage_path': 'documents_storage_path',
        'documents_relative_path': 'documents_relative_path',
        'documents_exclusive_rights': 'documents_exclusive_rights',
        'documents_move_contents': 'documents_move_contents',
        'documents_move_content_on_policy_removal': 'documents_move_content_on_policy_removal'
    }

    def __init__(self, documents_status=None, documents_redirection_type=None, documents_storage_path=None, documents_relative_path=None, documents_exclusive_rights=None, documents_move_contents=None, documents_move_content_on_policy_removal=None):
        r"""DocumentsConfigurations

        The model defined in huaweicloud sdk

        :param documents_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type documents_status: int
        :param documents_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type documents_redirection_type: int
        :param documents_storage_path: 文件夹重定向(v2)用户存储路径。
        :type documents_storage_path: str
        :param documents_relative_path: 目标文件夹位置。
        :type documents_relative_path: str
        :param documents_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type documents_exclusive_rights: int
        :param documents_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type documents_move_contents: int
        :param documents_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type documents_move_content_on_policy_removal: int
        """
        
        

        self._documents_status = None
        self._documents_redirection_type = None
        self._documents_storage_path = None
        self._documents_relative_path = None
        self._documents_exclusive_rights = None
        self._documents_move_contents = None
        self._documents_move_content_on_policy_removal = None
        self.discriminator = None

        if documents_status is not None:
            self.documents_status = documents_status
        if documents_redirection_type is not None:
            self.documents_redirection_type = documents_redirection_type
        if documents_storage_path is not None:
            self.documents_storage_path = documents_storage_path
        if documents_relative_path is not None:
            self.documents_relative_path = documents_relative_path
        if documents_exclusive_rights is not None:
            self.documents_exclusive_rights = documents_exclusive_rights
        if documents_move_contents is not None:
            self.documents_move_contents = documents_move_contents
        if documents_move_content_on_policy_removal is not None:
            self.documents_move_content_on_policy_removal = documents_move_content_on_policy_removal

    @property
    def documents_status(self):
        r"""Gets the documents_status of this DocumentsConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The documents_status of this DocumentsConfigurations.
        :rtype: int
        """
        return self._documents_status

    @documents_status.setter
    def documents_status(self, documents_status):
        r"""Sets the documents_status of this DocumentsConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param documents_status: The documents_status of this DocumentsConfigurations.
        :type documents_status: int
        """
        self._documents_status = documents_status

    @property
    def documents_redirection_type(self):
        r"""Gets the documents_redirection_type of this DocumentsConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The documents_redirection_type of this DocumentsConfigurations.
        :rtype: int
        """
        return self._documents_redirection_type

    @documents_redirection_type.setter
    def documents_redirection_type(self, documents_redirection_type):
        r"""Sets the documents_redirection_type of this DocumentsConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param documents_redirection_type: The documents_redirection_type of this DocumentsConfigurations.
        :type documents_redirection_type: int
        """
        self._documents_redirection_type = documents_redirection_type

    @property
    def documents_storage_path(self):
        r"""Gets the documents_storage_path of this DocumentsConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The documents_storage_path of this DocumentsConfigurations.
        :rtype: str
        """
        return self._documents_storage_path

    @documents_storage_path.setter
    def documents_storage_path(self, documents_storage_path):
        r"""Sets the documents_storage_path of this DocumentsConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param documents_storage_path: The documents_storage_path of this DocumentsConfigurations.
        :type documents_storage_path: str
        """
        self._documents_storage_path = documents_storage_path

    @property
    def documents_relative_path(self):
        r"""Gets the documents_relative_path of this DocumentsConfigurations.

        目标文件夹位置。

        :return: The documents_relative_path of this DocumentsConfigurations.
        :rtype: str
        """
        return self._documents_relative_path

    @documents_relative_path.setter
    def documents_relative_path(self, documents_relative_path):
        r"""Sets the documents_relative_path of this DocumentsConfigurations.

        目标文件夹位置。

        :param documents_relative_path: The documents_relative_path of this DocumentsConfigurations.
        :type documents_relative_path: str
        """
        self._documents_relative_path = documents_relative_path

    @property
    def documents_exclusive_rights(self):
        r"""Gets the documents_exclusive_rights of this DocumentsConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The documents_exclusive_rights of this DocumentsConfigurations.
        :rtype: int
        """
        return self._documents_exclusive_rights

    @documents_exclusive_rights.setter
    def documents_exclusive_rights(self, documents_exclusive_rights):
        r"""Sets the documents_exclusive_rights of this DocumentsConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param documents_exclusive_rights: The documents_exclusive_rights of this DocumentsConfigurations.
        :type documents_exclusive_rights: int
        """
        self._documents_exclusive_rights = documents_exclusive_rights

    @property
    def documents_move_contents(self):
        r"""Gets the documents_move_contents of this DocumentsConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The documents_move_contents of this DocumentsConfigurations.
        :rtype: int
        """
        return self._documents_move_contents

    @documents_move_contents.setter
    def documents_move_contents(self, documents_move_contents):
        r"""Sets the documents_move_contents of this DocumentsConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param documents_move_contents: The documents_move_contents of this DocumentsConfigurations.
        :type documents_move_contents: int
        """
        self._documents_move_contents = documents_move_contents

    @property
    def documents_move_content_on_policy_removal(self):
        r"""Gets the documents_move_content_on_policy_removal of this DocumentsConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The documents_move_content_on_policy_removal of this DocumentsConfigurations.
        :rtype: int
        """
        return self._documents_move_content_on_policy_removal

    @documents_move_content_on_policy_removal.setter
    def documents_move_content_on_policy_removal(self, documents_move_content_on_policy_removal):
        r"""Sets the documents_move_content_on_policy_removal of this DocumentsConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param documents_move_content_on_policy_removal: The documents_move_content_on_policy_removal of this DocumentsConfigurations.
        :type documents_move_content_on_policy_removal: int
        """
        self._documents_move_content_on_policy_removal = documents_move_content_on_policy_removal

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
        if not isinstance(other, DocumentsConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
