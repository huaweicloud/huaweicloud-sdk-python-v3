# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HotspotSessionMigrationConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'project_id': 'str',
        'hotspot_session_migration_enable': 'bool',
        'hotspot_exit_session_num': 'int',
        'non_migrate_users': 'list[UserInfo]'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'hotspot_session_migration_enable': 'hotspot_session_migration_enable',
        'hotspot_exit_session_num': 'hotspot_exit_session_num',
        'non_migrate_users': 'non_migrate_users'
    }

    def __init__(self, id=None, project_id=None, hotspot_session_migration_enable=None, hotspot_exit_session_num=None, non_migrate_users=None):
        r"""HotspotSessionMigrationConfig

        The model defined in huaweicloud sdk

        :param id: 唯一标识。
        :type id: str
        :param project_id: 项目id。
        :type project_id: str
        :param hotspot_session_migration_enable: 是否开启热点会话迁移。取值为： false：表示关闭。 true：表示开启。
        :type hotspot_session_migration_enable: bool
        :param hotspot_exit_session_num: 热点时退出会话个数。
        :type hotspot_exit_session_num: int
        :param non_migrate_users: 热点时不迁移用户id列表。
        :type non_migrate_users: list[:class:`huaweicloudsdkworkspaceapp.v1.UserInfo`]
        """
        
        

        self._id = None
        self._project_id = None
        self._hotspot_session_migration_enable = None
        self._hotspot_exit_session_num = None
        self._non_migrate_users = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if hotspot_session_migration_enable is not None:
            self.hotspot_session_migration_enable = hotspot_session_migration_enable
        if hotspot_exit_session_num is not None:
            self.hotspot_exit_session_num = hotspot_exit_session_num
        if non_migrate_users is not None:
            self.non_migrate_users = non_migrate_users

    @property
    def id(self):
        r"""Gets the id of this HotspotSessionMigrationConfig.

        唯一标识。

        :return: The id of this HotspotSessionMigrationConfig.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HotspotSessionMigrationConfig.

        唯一标识。

        :param id: The id of this HotspotSessionMigrationConfig.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this HotspotSessionMigrationConfig.

        项目id。

        :return: The project_id of this HotspotSessionMigrationConfig.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this HotspotSessionMigrationConfig.

        项目id。

        :param project_id: The project_id of this HotspotSessionMigrationConfig.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def hotspot_session_migration_enable(self):
        r"""Gets the hotspot_session_migration_enable of this HotspotSessionMigrationConfig.

        是否开启热点会话迁移。取值为： false：表示关闭。 true：表示开启。

        :return: The hotspot_session_migration_enable of this HotspotSessionMigrationConfig.
        :rtype: bool
        """
        return self._hotspot_session_migration_enable

    @hotspot_session_migration_enable.setter
    def hotspot_session_migration_enable(self, hotspot_session_migration_enable):
        r"""Sets the hotspot_session_migration_enable of this HotspotSessionMigrationConfig.

        是否开启热点会话迁移。取值为： false：表示关闭。 true：表示开启。

        :param hotspot_session_migration_enable: The hotspot_session_migration_enable of this HotspotSessionMigrationConfig.
        :type hotspot_session_migration_enable: bool
        """
        self._hotspot_session_migration_enable = hotspot_session_migration_enable

    @property
    def hotspot_exit_session_num(self):
        r"""Gets the hotspot_exit_session_num of this HotspotSessionMigrationConfig.

        热点时退出会话个数。

        :return: The hotspot_exit_session_num of this HotspotSessionMigrationConfig.
        :rtype: int
        """
        return self._hotspot_exit_session_num

    @hotspot_exit_session_num.setter
    def hotspot_exit_session_num(self, hotspot_exit_session_num):
        r"""Sets the hotspot_exit_session_num of this HotspotSessionMigrationConfig.

        热点时退出会话个数。

        :param hotspot_exit_session_num: The hotspot_exit_session_num of this HotspotSessionMigrationConfig.
        :type hotspot_exit_session_num: int
        """
        self._hotspot_exit_session_num = hotspot_exit_session_num

    @property
    def non_migrate_users(self):
        r"""Gets the non_migrate_users of this HotspotSessionMigrationConfig.

        热点时不迁移用户id列表。

        :return: The non_migrate_users of this HotspotSessionMigrationConfig.
        :rtype: list[:class:`huaweicloudsdkworkspaceapp.v1.UserInfo`]
        """
        return self._non_migrate_users

    @non_migrate_users.setter
    def non_migrate_users(self, non_migrate_users):
        r"""Sets the non_migrate_users of this HotspotSessionMigrationConfig.

        热点时不迁移用户id列表。

        :param non_migrate_users: The non_migrate_users of this HotspotSessionMigrationConfig.
        :type non_migrate_users: list[:class:`huaweicloudsdkworkspaceapp.v1.UserInfo`]
        """
        self._non_migrate_users = non_migrate_users

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
        if not isinstance(other, HotspotSessionMigrationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
