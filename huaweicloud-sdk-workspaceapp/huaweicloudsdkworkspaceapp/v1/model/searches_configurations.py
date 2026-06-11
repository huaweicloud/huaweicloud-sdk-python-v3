# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchesConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'searches_status': 'int',
        'searches_redirection_type': 'int',
        'searches_storage_path': 'str',
        'searches_relative_path': 'str',
        'searches_exclusive_rights': 'int',
        'searches_move_contents': 'int',
        'searches_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'searches_status': 'searches_status',
        'searches_redirection_type': 'searches_redirection_type',
        'searches_storage_path': 'searches_storage_path',
        'searches_relative_path': 'searches_relative_path',
        'searches_exclusive_rights': 'searches_exclusive_rights',
        'searches_move_contents': 'searches_move_contents',
        'searches_move_content_on_policy_removal': 'searches_move_content_on_policy_removal'
    }

    def __init__(self, searches_status=None, searches_redirection_type=None, searches_storage_path=None, searches_relative_path=None, searches_exclusive_rights=None, searches_move_contents=None, searches_move_content_on_policy_removal=None):
        r"""SearchesConfigurations

        The model defined in huaweicloud sdk

        :param searches_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type searches_status: int
        :param searches_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type searches_redirection_type: int
        :param searches_storage_path: 文件夹重定向(v2)用户存储路径。
        :type searches_storage_path: str
        :param searches_relative_path: 目标文件夹位置。
        :type searches_relative_path: str
        :param searches_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type searches_exclusive_rights: int
        :param searches_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type searches_move_contents: int
        :param searches_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type searches_move_content_on_policy_removal: int
        """
        
        

        self._searches_status = None
        self._searches_redirection_type = None
        self._searches_storage_path = None
        self._searches_relative_path = None
        self._searches_exclusive_rights = None
        self._searches_move_contents = None
        self._searches_move_content_on_policy_removal = None
        self.discriminator = None

        if searches_status is not None:
            self.searches_status = searches_status
        if searches_redirection_type is not None:
            self.searches_redirection_type = searches_redirection_type
        if searches_storage_path is not None:
            self.searches_storage_path = searches_storage_path
        if searches_relative_path is not None:
            self.searches_relative_path = searches_relative_path
        if searches_exclusive_rights is not None:
            self.searches_exclusive_rights = searches_exclusive_rights
        if searches_move_contents is not None:
            self.searches_move_contents = searches_move_contents
        if searches_move_content_on_policy_removal is not None:
            self.searches_move_content_on_policy_removal = searches_move_content_on_policy_removal

    @property
    def searches_status(self):
        r"""Gets the searches_status of this SearchesConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The searches_status of this SearchesConfigurations.
        :rtype: int
        """
        return self._searches_status

    @searches_status.setter
    def searches_status(self, searches_status):
        r"""Sets the searches_status of this SearchesConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param searches_status: The searches_status of this SearchesConfigurations.
        :type searches_status: int
        """
        self._searches_status = searches_status

    @property
    def searches_redirection_type(self):
        r"""Gets the searches_redirection_type of this SearchesConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The searches_redirection_type of this SearchesConfigurations.
        :rtype: int
        """
        return self._searches_redirection_type

    @searches_redirection_type.setter
    def searches_redirection_type(self, searches_redirection_type):
        r"""Sets the searches_redirection_type of this SearchesConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param searches_redirection_type: The searches_redirection_type of this SearchesConfigurations.
        :type searches_redirection_type: int
        """
        self._searches_redirection_type = searches_redirection_type

    @property
    def searches_storage_path(self):
        r"""Gets the searches_storage_path of this SearchesConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The searches_storage_path of this SearchesConfigurations.
        :rtype: str
        """
        return self._searches_storage_path

    @searches_storage_path.setter
    def searches_storage_path(self, searches_storage_path):
        r"""Sets the searches_storage_path of this SearchesConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param searches_storage_path: The searches_storage_path of this SearchesConfigurations.
        :type searches_storage_path: str
        """
        self._searches_storage_path = searches_storage_path

    @property
    def searches_relative_path(self):
        r"""Gets the searches_relative_path of this SearchesConfigurations.

        目标文件夹位置。

        :return: The searches_relative_path of this SearchesConfigurations.
        :rtype: str
        """
        return self._searches_relative_path

    @searches_relative_path.setter
    def searches_relative_path(self, searches_relative_path):
        r"""Sets the searches_relative_path of this SearchesConfigurations.

        目标文件夹位置。

        :param searches_relative_path: The searches_relative_path of this SearchesConfigurations.
        :type searches_relative_path: str
        """
        self._searches_relative_path = searches_relative_path

    @property
    def searches_exclusive_rights(self):
        r"""Gets the searches_exclusive_rights of this SearchesConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The searches_exclusive_rights of this SearchesConfigurations.
        :rtype: int
        """
        return self._searches_exclusive_rights

    @searches_exclusive_rights.setter
    def searches_exclusive_rights(self, searches_exclusive_rights):
        r"""Sets the searches_exclusive_rights of this SearchesConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param searches_exclusive_rights: The searches_exclusive_rights of this SearchesConfigurations.
        :type searches_exclusive_rights: int
        """
        self._searches_exclusive_rights = searches_exclusive_rights

    @property
    def searches_move_contents(self):
        r"""Gets the searches_move_contents of this SearchesConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The searches_move_contents of this SearchesConfigurations.
        :rtype: int
        """
        return self._searches_move_contents

    @searches_move_contents.setter
    def searches_move_contents(self, searches_move_contents):
        r"""Sets the searches_move_contents of this SearchesConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param searches_move_contents: The searches_move_contents of this SearchesConfigurations.
        :type searches_move_contents: int
        """
        self._searches_move_contents = searches_move_contents

    @property
    def searches_move_content_on_policy_removal(self):
        r"""Gets the searches_move_content_on_policy_removal of this SearchesConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The searches_move_content_on_policy_removal of this SearchesConfigurations.
        :rtype: int
        """
        return self._searches_move_content_on_policy_removal

    @searches_move_content_on_policy_removal.setter
    def searches_move_content_on_policy_removal(self, searches_move_content_on_policy_removal):
        r"""Sets the searches_move_content_on_policy_removal of this SearchesConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param searches_move_content_on_policy_removal: The searches_move_content_on_policy_removal of this SearchesConfigurations.
        :type searches_move_content_on_policy_removal: int
        """
        self._searches_move_content_on_policy_removal = searches_move_content_on_policy_removal

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
        if not isinstance(other, SearchesConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
