# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideosConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'videos_status': 'int',
        'videos_redirection_type': 'int',
        'videos_storage_path': 'str',
        'videos_relative_path': 'str',
        'videos_exclusive_rights': 'int',
        'videos_move_contents': 'int',
        'videos_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'videos_status': 'videos_status',
        'videos_redirection_type': 'videos_redirection_type',
        'videos_storage_path': 'videos_storage_path',
        'videos_relative_path': 'videos_relative_path',
        'videos_exclusive_rights': 'videos_exclusive_rights',
        'videos_move_contents': 'videos_move_contents',
        'videos_move_content_on_policy_removal': 'videos_move_content_on_policy_removal'
    }

    def __init__(self, videos_status=None, videos_redirection_type=None, videos_storage_path=None, videos_relative_path=None, videos_exclusive_rights=None, videos_move_contents=None, videos_move_content_on_policy_removal=None):
        r"""VideosConfigurations

        The model defined in huaweicloud sdk

        :param videos_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type videos_status: int
        :param videos_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type videos_redirection_type: int
        :param videos_storage_path: 文件夹重定向(v2)用户存储路径。
        :type videos_storage_path: str
        :param videos_relative_path: 目标文件夹位置。
        :type videos_relative_path: str
        :param videos_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type videos_exclusive_rights: int
        :param videos_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type videos_move_contents: int
        :param videos_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type videos_move_content_on_policy_removal: int
        """
        
        

        self._videos_status = None
        self._videos_redirection_type = None
        self._videos_storage_path = None
        self._videos_relative_path = None
        self._videos_exclusive_rights = None
        self._videos_move_contents = None
        self._videos_move_content_on_policy_removal = None
        self.discriminator = None

        if videos_status is not None:
            self.videos_status = videos_status
        if videos_redirection_type is not None:
            self.videos_redirection_type = videos_redirection_type
        if videos_storage_path is not None:
            self.videos_storage_path = videos_storage_path
        if videos_relative_path is not None:
            self.videos_relative_path = videos_relative_path
        if videos_exclusive_rights is not None:
            self.videos_exclusive_rights = videos_exclusive_rights
        if videos_move_contents is not None:
            self.videos_move_contents = videos_move_contents
        if videos_move_content_on_policy_removal is not None:
            self.videos_move_content_on_policy_removal = videos_move_content_on_policy_removal

    @property
    def videos_status(self):
        r"""Gets the videos_status of this VideosConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The videos_status of this VideosConfigurations.
        :rtype: int
        """
        return self._videos_status

    @videos_status.setter
    def videos_status(self, videos_status):
        r"""Sets the videos_status of this VideosConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param videos_status: The videos_status of this VideosConfigurations.
        :type videos_status: int
        """
        self._videos_status = videos_status

    @property
    def videos_redirection_type(self):
        r"""Gets the videos_redirection_type of this VideosConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The videos_redirection_type of this VideosConfigurations.
        :rtype: int
        """
        return self._videos_redirection_type

    @videos_redirection_type.setter
    def videos_redirection_type(self, videos_redirection_type):
        r"""Sets the videos_redirection_type of this VideosConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param videos_redirection_type: The videos_redirection_type of this VideosConfigurations.
        :type videos_redirection_type: int
        """
        self._videos_redirection_type = videos_redirection_type

    @property
    def videos_storage_path(self):
        r"""Gets the videos_storage_path of this VideosConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The videos_storage_path of this VideosConfigurations.
        :rtype: str
        """
        return self._videos_storage_path

    @videos_storage_path.setter
    def videos_storage_path(self, videos_storage_path):
        r"""Sets the videos_storage_path of this VideosConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param videos_storage_path: The videos_storage_path of this VideosConfigurations.
        :type videos_storage_path: str
        """
        self._videos_storage_path = videos_storage_path

    @property
    def videos_relative_path(self):
        r"""Gets the videos_relative_path of this VideosConfigurations.

        目标文件夹位置。

        :return: The videos_relative_path of this VideosConfigurations.
        :rtype: str
        """
        return self._videos_relative_path

    @videos_relative_path.setter
    def videos_relative_path(self, videos_relative_path):
        r"""Sets the videos_relative_path of this VideosConfigurations.

        目标文件夹位置。

        :param videos_relative_path: The videos_relative_path of this VideosConfigurations.
        :type videos_relative_path: str
        """
        self._videos_relative_path = videos_relative_path

    @property
    def videos_exclusive_rights(self):
        r"""Gets the videos_exclusive_rights of this VideosConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The videos_exclusive_rights of this VideosConfigurations.
        :rtype: int
        """
        return self._videos_exclusive_rights

    @videos_exclusive_rights.setter
    def videos_exclusive_rights(self, videos_exclusive_rights):
        r"""Sets the videos_exclusive_rights of this VideosConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param videos_exclusive_rights: The videos_exclusive_rights of this VideosConfigurations.
        :type videos_exclusive_rights: int
        """
        self._videos_exclusive_rights = videos_exclusive_rights

    @property
    def videos_move_contents(self):
        r"""Gets the videos_move_contents of this VideosConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The videos_move_contents of this VideosConfigurations.
        :rtype: int
        """
        return self._videos_move_contents

    @videos_move_contents.setter
    def videos_move_contents(self, videos_move_contents):
        r"""Sets the videos_move_contents of this VideosConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param videos_move_contents: The videos_move_contents of this VideosConfigurations.
        :type videos_move_contents: int
        """
        self._videos_move_contents = videos_move_contents

    @property
    def videos_move_content_on_policy_removal(self):
        r"""Gets the videos_move_content_on_policy_removal of this VideosConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The videos_move_content_on_policy_removal of this VideosConfigurations.
        :rtype: int
        """
        return self._videos_move_content_on_policy_removal

    @videos_move_content_on_policy_removal.setter
    def videos_move_content_on_policy_removal(self, videos_move_content_on_policy_removal):
        r"""Sets the videos_move_content_on_policy_removal of this VideosConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param videos_move_content_on_policy_removal: The videos_move_content_on_policy_removal of this VideosConfigurations.
        :type videos_move_content_on_policy_removal: int
        """
        self._videos_move_content_on_policy_removal = videos_move_content_on_policy_removal

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
        if not isinstance(other, VideosConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
