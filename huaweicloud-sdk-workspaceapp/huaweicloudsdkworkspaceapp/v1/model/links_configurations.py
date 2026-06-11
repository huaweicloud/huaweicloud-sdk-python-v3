# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LinksConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'links_status': 'int',
        'links_redirection_type': 'int',
        'links_storage_path': 'str',
        'links_relative_path': 'str',
        'links_exclusive_rights': 'int',
        'links_move_contents': 'int',
        'links_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'links_status': 'links_status',
        'links_redirection_type': 'links_redirection_type',
        'links_storage_path': 'links_storage_path',
        'links_relative_path': 'links_relative_path',
        'links_exclusive_rights': 'links_exclusive_rights',
        'links_move_contents': 'links_move_contents',
        'links_move_content_on_policy_removal': 'links_move_content_on_policy_removal'
    }

    def __init__(self, links_status=None, links_redirection_type=None, links_storage_path=None, links_relative_path=None, links_exclusive_rights=None, links_move_contents=None, links_move_content_on_policy_removal=None):
        r"""LinksConfigurations

        The model defined in huaweicloud sdk

        :param links_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type links_status: int
        :param links_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type links_redirection_type: int
        :param links_storage_path: 文件夹重定向(v2)用户存储路径。
        :type links_storage_path: str
        :param links_relative_path: 目标文件夹位置。
        :type links_relative_path: str
        :param links_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type links_exclusive_rights: int
        :param links_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type links_move_contents: int
        :param links_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type links_move_content_on_policy_removal: int
        """
        
        

        self._links_status = None
        self._links_redirection_type = None
        self._links_storage_path = None
        self._links_relative_path = None
        self._links_exclusive_rights = None
        self._links_move_contents = None
        self._links_move_content_on_policy_removal = None
        self.discriminator = None

        if links_status is not None:
            self.links_status = links_status
        if links_redirection_type is not None:
            self.links_redirection_type = links_redirection_type
        if links_storage_path is not None:
            self.links_storage_path = links_storage_path
        if links_relative_path is not None:
            self.links_relative_path = links_relative_path
        if links_exclusive_rights is not None:
            self.links_exclusive_rights = links_exclusive_rights
        if links_move_contents is not None:
            self.links_move_contents = links_move_contents
        if links_move_content_on_policy_removal is not None:
            self.links_move_content_on_policy_removal = links_move_content_on_policy_removal

    @property
    def links_status(self):
        r"""Gets the links_status of this LinksConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The links_status of this LinksConfigurations.
        :rtype: int
        """
        return self._links_status

    @links_status.setter
    def links_status(self, links_status):
        r"""Sets the links_status of this LinksConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param links_status: The links_status of this LinksConfigurations.
        :type links_status: int
        """
        self._links_status = links_status

    @property
    def links_redirection_type(self):
        r"""Gets the links_redirection_type of this LinksConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The links_redirection_type of this LinksConfigurations.
        :rtype: int
        """
        return self._links_redirection_type

    @links_redirection_type.setter
    def links_redirection_type(self, links_redirection_type):
        r"""Sets the links_redirection_type of this LinksConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param links_redirection_type: The links_redirection_type of this LinksConfigurations.
        :type links_redirection_type: int
        """
        self._links_redirection_type = links_redirection_type

    @property
    def links_storage_path(self):
        r"""Gets the links_storage_path of this LinksConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The links_storage_path of this LinksConfigurations.
        :rtype: str
        """
        return self._links_storage_path

    @links_storage_path.setter
    def links_storage_path(self, links_storage_path):
        r"""Sets the links_storage_path of this LinksConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param links_storage_path: The links_storage_path of this LinksConfigurations.
        :type links_storage_path: str
        """
        self._links_storage_path = links_storage_path

    @property
    def links_relative_path(self):
        r"""Gets the links_relative_path of this LinksConfigurations.

        目标文件夹位置。

        :return: The links_relative_path of this LinksConfigurations.
        :rtype: str
        """
        return self._links_relative_path

    @links_relative_path.setter
    def links_relative_path(self, links_relative_path):
        r"""Sets the links_relative_path of this LinksConfigurations.

        目标文件夹位置。

        :param links_relative_path: The links_relative_path of this LinksConfigurations.
        :type links_relative_path: str
        """
        self._links_relative_path = links_relative_path

    @property
    def links_exclusive_rights(self):
        r"""Gets the links_exclusive_rights of this LinksConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The links_exclusive_rights of this LinksConfigurations.
        :rtype: int
        """
        return self._links_exclusive_rights

    @links_exclusive_rights.setter
    def links_exclusive_rights(self, links_exclusive_rights):
        r"""Sets the links_exclusive_rights of this LinksConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param links_exclusive_rights: The links_exclusive_rights of this LinksConfigurations.
        :type links_exclusive_rights: int
        """
        self._links_exclusive_rights = links_exclusive_rights

    @property
    def links_move_contents(self):
        r"""Gets the links_move_contents of this LinksConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The links_move_contents of this LinksConfigurations.
        :rtype: int
        """
        return self._links_move_contents

    @links_move_contents.setter
    def links_move_contents(self, links_move_contents):
        r"""Sets the links_move_contents of this LinksConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param links_move_contents: The links_move_contents of this LinksConfigurations.
        :type links_move_contents: int
        """
        self._links_move_contents = links_move_contents

    @property
    def links_move_content_on_policy_removal(self):
        r"""Gets the links_move_content_on_policy_removal of this LinksConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The links_move_content_on_policy_removal of this LinksConfigurations.
        :rtype: int
        """
        return self._links_move_content_on_policy_removal

    @links_move_content_on_policy_removal.setter
    def links_move_content_on_policy_removal(self, links_move_content_on_policy_removal):
        r"""Sets the links_move_content_on_policy_removal of this LinksConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param links_move_content_on_policy_removal: The links_move_content_on_policy_removal of this LinksConfigurations.
        :type links_move_content_on_policy_removal: int
        """
        self._links_move_content_on_policy_removal = links_move_content_on_policy_removal

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
        if not isinstance(other, LinksConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
