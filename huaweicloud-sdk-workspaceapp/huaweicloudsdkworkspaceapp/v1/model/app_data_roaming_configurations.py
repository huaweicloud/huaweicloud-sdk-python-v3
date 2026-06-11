# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AppDataRoamingConfigurations:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_data_roaming_status': 'int',
        'app_data_roaming_redirection_type': 'int',
        'app_data_roaming_storage_path': 'str',
        'app_data_roaming_relative_path': 'str',
        'app_data_roaming_exclusive_rights': 'int',
        'app_data_roaming_move_contents': 'int',
        'app_data_roaming_move_content_on_policy_removal': 'int'
    }

    attribute_map = {
        'app_data_roaming_status': 'app_data_roaming_status',
        'app_data_roaming_redirection_type': 'app_data_roaming_redirection_type',
        'app_data_roaming_storage_path': 'app_data_roaming_storage_path',
        'app_data_roaming_relative_path': 'app_data_roaming_relative_path',
        'app_data_roaming_exclusive_rights': 'app_data_roaming_exclusive_rights',
        'app_data_roaming_move_contents': 'app_data_roaming_move_contents',
        'app_data_roaming_move_content_on_policy_removal': 'app_data_roaming_move_content_on_policy_removal'
    }

    def __init__(self, app_data_roaming_status=None, app_data_roaming_redirection_type=None, app_data_roaming_storage_path=None, app_data_roaming_relative_path=None, app_data_roaming_exclusive_rights=None, app_data_roaming_move_contents=None, app_data_roaming_move_content_on_policy_removal=None):
        r"""AppDataRoamingConfigurations

        The model defined in huaweicloud sdk

        :param app_data_roaming_status: 配置文件夹重定向状态： 0: 未选取 1: 已选取
        :type app_data_roaming_status: int
        :param app_data_roaming_redirection_type: 配置文件夹重定向类型： 0: 远程 1: 本地
        :type app_data_roaming_redirection_type: int
        :param app_data_roaming_storage_path: 文件夹重定向(v2)用户存储路径。
        :type app_data_roaming_storage_path: str
        :param app_data_roaming_relative_path: 目标文件夹位置。
        :type app_data_roaming_relative_path: str
        :param app_data_roaming_exclusive_rights: 是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启
        :type app_data_roaming_exclusive_rights: int
        :param app_data_roaming_move_contents: 启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是
        :type app_data_roaming_move_contents: int
        :param app_data_roaming_move_content_on_policy_removal: 禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是
        :type app_data_roaming_move_content_on_policy_removal: int
        """
        
        

        self._app_data_roaming_status = None
        self._app_data_roaming_redirection_type = None
        self._app_data_roaming_storage_path = None
        self._app_data_roaming_relative_path = None
        self._app_data_roaming_exclusive_rights = None
        self._app_data_roaming_move_contents = None
        self._app_data_roaming_move_content_on_policy_removal = None
        self.discriminator = None

        if app_data_roaming_status is not None:
            self.app_data_roaming_status = app_data_roaming_status
        if app_data_roaming_redirection_type is not None:
            self.app_data_roaming_redirection_type = app_data_roaming_redirection_type
        if app_data_roaming_storage_path is not None:
            self.app_data_roaming_storage_path = app_data_roaming_storage_path
        if app_data_roaming_relative_path is not None:
            self.app_data_roaming_relative_path = app_data_roaming_relative_path
        if app_data_roaming_exclusive_rights is not None:
            self.app_data_roaming_exclusive_rights = app_data_roaming_exclusive_rights
        if app_data_roaming_move_contents is not None:
            self.app_data_roaming_move_contents = app_data_roaming_move_contents
        if app_data_roaming_move_content_on_policy_removal is not None:
            self.app_data_roaming_move_content_on_policy_removal = app_data_roaming_move_content_on_policy_removal

    @property
    def app_data_roaming_status(self):
        r"""Gets the app_data_roaming_status of this AppDataRoamingConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :return: The app_data_roaming_status of this AppDataRoamingConfigurations.
        :rtype: int
        """
        return self._app_data_roaming_status

    @app_data_roaming_status.setter
    def app_data_roaming_status(self, app_data_roaming_status):
        r"""Sets the app_data_roaming_status of this AppDataRoamingConfigurations.

        配置文件夹重定向状态： 0: 未选取 1: 已选取

        :param app_data_roaming_status: The app_data_roaming_status of this AppDataRoamingConfigurations.
        :type app_data_roaming_status: int
        """
        self._app_data_roaming_status = app_data_roaming_status

    @property
    def app_data_roaming_redirection_type(self):
        r"""Gets the app_data_roaming_redirection_type of this AppDataRoamingConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :return: The app_data_roaming_redirection_type of this AppDataRoamingConfigurations.
        :rtype: int
        """
        return self._app_data_roaming_redirection_type

    @app_data_roaming_redirection_type.setter
    def app_data_roaming_redirection_type(self, app_data_roaming_redirection_type):
        r"""Sets the app_data_roaming_redirection_type of this AppDataRoamingConfigurations.

        配置文件夹重定向类型： 0: 远程 1: 本地

        :param app_data_roaming_redirection_type: The app_data_roaming_redirection_type of this AppDataRoamingConfigurations.
        :type app_data_roaming_redirection_type: int
        """
        self._app_data_roaming_redirection_type = app_data_roaming_redirection_type

    @property
    def app_data_roaming_storage_path(self):
        r"""Gets the app_data_roaming_storage_path of this AppDataRoamingConfigurations.

        文件夹重定向(v2)用户存储路径。

        :return: The app_data_roaming_storage_path of this AppDataRoamingConfigurations.
        :rtype: str
        """
        return self._app_data_roaming_storage_path

    @app_data_roaming_storage_path.setter
    def app_data_roaming_storage_path(self, app_data_roaming_storage_path):
        r"""Sets the app_data_roaming_storage_path of this AppDataRoamingConfigurations.

        文件夹重定向(v2)用户存储路径。

        :param app_data_roaming_storage_path: The app_data_roaming_storage_path of this AppDataRoamingConfigurations.
        :type app_data_roaming_storage_path: str
        """
        self._app_data_roaming_storage_path = app_data_roaming_storage_path

    @property
    def app_data_roaming_relative_path(self):
        r"""Gets the app_data_roaming_relative_path of this AppDataRoamingConfigurations.

        目标文件夹位置。

        :return: The app_data_roaming_relative_path of this AppDataRoamingConfigurations.
        :rtype: str
        """
        return self._app_data_roaming_relative_path

    @app_data_roaming_relative_path.setter
    def app_data_roaming_relative_path(self, app_data_roaming_relative_path):
        r"""Sets the app_data_roaming_relative_path of this AppDataRoamingConfigurations.

        目标文件夹位置。

        :param app_data_roaming_relative_path: The app_data_roaming_relative_path of this AppDataRoamingConfigurations.
        :type app_data_roaming_relative_path: str
        """
        self._app_data_roaming_relative_path = app_data_roaming_relative_path

    @property
    def app_data_roaming_exclusive_rights(self):
        r"""Gets the app_data_roaming_exclusive_rights of this AppDataRoamingConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :return: The app_data_roaming_exclusive_rights of this AppDataRoamingConfigurations.
        :rtype: int
        """
        return self._app_data_roaming_exclusive_rights

    @app_data_roaming_exclusive_rights.setter
    def app_data_roaming_exclusive_rights(self, app_data_roaming_exclusive_rights):
        r"""Sets the app_data_roaming_exclusive_rights of this AppDataRoamingConfigurations.

        是否开启用户对该文件夹的独占控制权限： 0: 禁用 1: 开启

        :param app_data_roaming_exclusive_rights: The app_data_roaming_exclusive_rights of this AppDataRoamingConfigurations.
        :type app_data_roaming_exclusive_rights: int
        """
        self._app_data_roaming_exclusive_rights = app_data_roaming_exclusive_rights

    @property
    def app_data_roaming_move_contents(self):
        r"""Gets the app_data_roaming_move_contents of this AppDataRoamingConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :return: The app_data_roaming_move_contents of this AppDataRoamingConfigurations.
        :rtype: int
        """
        return self._app_data_roaming_move_contents

    @app_data_roaming_move_contents.setter
    def app_data_roaming_move_contents(self, app_data_roaming_move_contents):
        r"""Sets the app_data_roaming_move_contents of this AppDataRoamingConfigurations.

        启用文件夹重定向策略时，是否将现有内容移动到新位置： 0: 否 1: 是

        :param app_data_roaming_move_contents: The app_data_roaming_move_contents of this AppDataRoamingConfigurations.
        :type app_data_roaming_move_contents: int
        """
        self._app_data_roaming_move_contents = app_data_roaming_move_contents

    @property
    def app_data_roaming_move_content_on_policy_removal(self):
        r"""Gets the app_data_roaming_move_content_on_policy_removal of this AppDataRoamingConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :return: The app_data_roaming_move_content_on_policy_removal of this AppDataRoamingConfigurations.
        :rtype: int
        """
        return self._app_data_roaming_move_content_on_policy_removal

    @app_data_roaming_move_content_on_policy_removal.setter
    def app_data_roaming_move_content_on_policy_removal(self, app_data_roaming_move_content_on_policy_removal):
        r"""Sets the app_data_roaming_move_content_on_policy_removal of this AppDataRoamingConfigurations.

        禁用或删除策略时，是否将内容移回本地用户配置文件位置： 0: 否 1: 是

        :param app_data_roaming_move_content_on_policy_removal: The app_data_roaming_move_content_on_policy_removal of this AppDataRoamingConfigurations.
        :type app_data_roaming_move_content_on_policy_removal: int
        """
        self._app_data_roaming_move_content_on_policy_removal = app_data_roaming_move_content_on_policy_removal

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
        if not isinstance(other, AppDataRoamingConfigurations):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
