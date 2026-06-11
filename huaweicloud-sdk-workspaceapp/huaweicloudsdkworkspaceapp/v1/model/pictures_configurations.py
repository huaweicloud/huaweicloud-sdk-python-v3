# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PicturesConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pictures_status': 'int',
        'pictures_redirection_type': 'int',
        'pictures_storage_path': 'str',
        'pictures_relative_path': 'str',
        'pictures_exclusive_rights': 'int',
        'pictures_move_contents': 'int',
        'pictures_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'pictures_status': 'pictures_status',
        'pictures_redirection_type': 'pictures_redirection_type',
        'pictures_storage_path': 'pictures_storage_path',
        'pictures_relative_path': 'pictures_relative_path',
        'pictures_exclusive_rights': 'pictures_exclusive_rights',
        'pictures_move_contents': 'pictures_move_contents',
        'pictures_move_content_on_policy_removal': 'pictures_move_content_on_policy_removal'
    }

    def __init__(self, pictures_status=None, pictures_redirection_type=None, pictures_storage_path=None, pictures_relative_path=None, pictures_exclusive_rights=None, pictures_move_contents=None, pictures_move_content_on_policy_removal=None):
        r"""PicturesConfigurations

        The model defined in huaweicloud sdk

        :param pictures_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type pictures_status: int
        :param pictures_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type pictures_redirection_type: int
        :param pictures_storage_path: 文件夹重定向(v2)用户存储路径。
        :type pictures_storage_path: str
        :param pictures_relative_path: 目标文件夹位置。
        :type pictures_relative_path: str
        :param pictures_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type pictures_exclusive_rights: int
        :param pictures_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type pictures_move_contents: int
        :param pictures_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type pictures_move_content_on_policy_removal: int
        """
        
        

        self._pictures_status = None
        self._pictures_redirection_type = None
        self._pictures_storage_path = None
        self._pictures_relative_path = None
        self._pictures_exclusive_rights = None
        self._pictures_move_contents = None
        self._pictures_move_content_on_policy_removal = None
        self.discriminator = None

        if pictures_status is not None:
            self.pictures_status = pictures_status
        if pictures_redirection_type is not None:
            self.pictures_redirection_type = pictures_redirection_type
        if pictures_storage_path is not None:
            self.pictures_storage_path = pictures_storage_path
        if pictures_relative_path is not None:
            self.pictures_relative_path = pictures_relative_path
        if pictures_exclusive_rights is not None:
            self.pictures_exclusive_rights = pictures_exclusive_rights
        if pictures_move_contents is not None:
            self.pictures_move_contents = pictures_move_contents
        if pictures_move_content_on_policy_removal is not None:
            self.pictures_move_content_on_policy_removal = pictures_move_content_on_policy_removal

    @property
    def pictures_status(self):
        r"""Gets the pictures_status of this PicturesConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The pictures_status of this PicturesConfigurations.
        :rtype: int
        """
        return self._pictures_status

    @pictures_status.setter
    def pictures_status(self, pictures_status):
        r"""Sets the pictures_status of this PicturesConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param pictures_status: The pictures_status of this PicturesConfigurations.
        :type pictures_status: int
        """
        self._pictures_status = pictures_status

    @property
    def pictures_redirection_type(self):
        r"""Gets the pictures_redirection_type of this PicturesConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The pictures_redirection_type of this PicturesConfigurations.
        :rtype: int
        """
        return self._pictures_redirection_type

    @pictures_redirection_type.setter
    def pictures_redirection_type(self, pictures_redirection_type):
        r"""Sets the pictures_redirection_type of this PicturesConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param pictures_redirection_type: The pictures_redirection_type of this PicturesConfigurations.
        :type pictures_redirection_type: int
        """
        self._pictures_redirection_type = pictures_redirection_type

    @property
    def pictures_storage_path(self):
        r"""Gets the pictures_storage_path of this PicturesConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The pictures_storage_path of this PicturesConfigurations.
        :rtype: str
        """
        return self._pictures_storage_path

    @pictures_storage_path.setter
    def pictures_storage_path(self, pictures_storage_path):
        r"""Sets the pictures_storage_path of this PicturesConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param pictures_storage_path: The pictures_storage_path of this PicturesConfigurations.
        :type pictures_storage_path: str
        """
        self._pictures_storage_path = pictures_storage_path

    @property
    def pictures_relative_path(self):
        r"""Gets the pictures_relative_path of this PicturesConfigurations.

        目标文件夹位置。

        :return: The pictures_relative_path of this PicturesConfigurations.
        :rtype: str
        """
        return self._pictures_relative_path

    @pictures_relative_path.setter
    def pictures_relative_path(self, pictures_relative_path):
        r"""Sets the pictures_relative_path of this PicturesConfigurations.

        目标文件夹位置。

        :param pictures_relative_path: The pictures_relative_path of this PicturesConfigurations.
        :type pictures_relative_path: str
        """
        self._pictures_relative_path = pictures_relative_path

    @property
    def pictures_exclusive_rights(self):
        r"""Gets the pictures_exclusive_rights of this PicturesConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The pictures_exclusive_rights of this PicturesConfigurations.
        :rtype: int
        """
        return self._pictures_exclusive_rights

    @pictures_exclusive_rights.setter
    def pictures_exclusive_rights(self, pictures_exclusive_rights):
        r"""Sets the pictures_exclusive_rights of this PicturesConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param pictures_exclusive_rights: The pictures_exclusive_rights of this PicturesConfigurations.
        :type pictures_exclusive_rights: int
        """
        self._pictures_exclusive_rights = pictures_exclusive_rights

    @property
    def pictures_move_contents(self):
        r"""Gets the pictures_move_contents of this PicturesConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The pictures_move_contents of this PicturesConfigurations.
        :rtype: int
        """
        return self._pictures_move_contents

    @pictures_move_contents.setter
    def pictures_move_contents(self, pictures_move_contents):
        r"""Sets the pictures_move_contents of this PicturesConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param pictures_move_contents: The pictures_move_contents of this PicturesConfigurations.
        :type pictures_move_contents: int
        """
        self._pictures_move_contents = pictures_move_contents

    @property
    def pictures_move_content_on_policy_removal(self):
        r"""Gets the pictures_move_content_on_policy_removal of this PicturesConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The pictures_move_content_on_policy_removal of this PicturesConfigurations.
        :rtype: int
        """
        return self._pictures_move_content_on_policy_removal

    @pictures_move_content_on_policy_removal.setter
    def pictures_move_content_on_policy_removal(self, pictures_move_content_on_policy_removal):
        r"""Sets the pictures_move_content_on_policy_removal of this PicturesConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param pictures_move_content_on_policy_removal: The pictures_move_content_on_policy_removal of this PicturesConfigurations.
        :type pictures_move_content_on_policy_removal: int
        """
        self._pictures_move_content_on_policy_removal = pictures_move_content_on_policy_removal

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
        if not isinstance(other, PicturesConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
