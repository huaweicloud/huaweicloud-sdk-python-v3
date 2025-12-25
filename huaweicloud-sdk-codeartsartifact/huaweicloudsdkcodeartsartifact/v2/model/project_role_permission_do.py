# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProjectRolePermissionDo:

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
        'role_id': 'int',
        'devuc_role_id': 'str',
        'project_id': 'str',
        'is_permission_config': 'bool',
        'is_change_pkg_status': 'bool',
        'is_upload': 'bool',
        'is_delete_restore_test_pkg': 'bool',
        'is_delete_restore_prod_pkg': 'bool',
        'is_edit_test_pkg': 'bool',
        'is_mkdir': 'bool',
        'is_download': 'bool',
        'is_restore_all': 'bool',
        'is_empty': 'bool',
        'create_time': 'int',
        'update_time': 'int',
        'migrated_630': 'int',
        'region': 'str',
        'user_id': 'str',
        'roles': 'str'
    }

    attribute_map = {
        'id': 'id',
        'role_id': 'role_id',
        'devuc_role_id': 'devuc_role_id',
        'project_id': 'project_id',
        'is_permission_config': 'is_permission_config',
        'is_change_pkg_status': 'is_change_pkg_status',
        'is_upload': 'is_upload',
        'is_delete_restore_test_pkg': 'is_delete_restore_test_pkg',
        'is_delete_restore_prod_pkg': 'is_delete_restore_prod_pkg',
        'is_edit_test_pkg': 'is_edit_test_pkg',
        'is_mkdir': 'is_mkdir',
        'is_download': 'is_download',
        'is_restore_all': 'is_restore_all',
        'is_empty': 'is_empty',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'migrated_630': 'migrated_630',
        'region': 'region',
        'user_id': 'user_id',
        'roles': 'roles'
    }

    def __init__(self, id=None, role_id=None, devuc_role_id=None, project_id=None, is_permission_config=None, is_change_pkg_status=None, is_upload=None, is_delete_restore_test_pkg=None, is_delete_restore_prod_pkg=None, is_edit_test_pkg=None, is_mkdir=None, is_download=None, is_restore_all=None, is_empty=None, create_time=None, update_time=None, migrated_630=None, region=None, user_id=None, roles=None):
        r"""ProjectRolePermissionDo

        The model defined in huaweicloud sdk

        :param id: **参数解释**: ID。 **取值范围**: 不涉及。
        :type id: str
        :param role_id: **参数解释**: 角色ID。 **取值范围**: 不涉及。
        :type role_id: int
        :param devuc_role_id: **参数解释**: DEVUC角色ID。 **取值范围**: 不涉及。
        :type devuc_role_id: str
        :param project_id: **参数解释**: 项目ID。 **取值范围**: 不涉及。
        :type project_id: str
        :param is_permission_config: **参数解释**: 是否具有权限配置能力。 **取值范围**: - true：能够配置权限。 - false：不能配置权限。
        :type is_permission_config: bool
        :param is_change_pkg_status: **参数解释**: 能否更改软件包状态。 **取值范围**: - true：能够更改软件包状态。 - false：不能更改软件包状态。
        :type is_change_pkg_status: bool
        :param is_upload: **参数解释**: 能否进行上传。 **取值范围**: - true：能够进行上传。 - false：不能上传。
        :type is_upload: bool
        :param is_delete_restore_test_pkg: **参数解释**: 能否删除和还原测试状态的软件包。 **取值范围**: - true：能够删除和还原测试状态的软件包。 - false：不能删除和还原测试状态的软件包。
        :type is_delete_restore_test_pkg: bool
        :param is_delete_restore_prod_pkg: **参数解释**: 能否删除和还原生产状态的软件包。 **取值范围**: - true：能够删除和还原生产状态的软件包。 - false：不能删除和还原生产状态的软件包。
        :type is_delete_restore_prod_pkg: bool
        :param is_edit_test_pkg: **参数解释**: 能否编辑测试状态的软件包。 **取值范围**: - true：能够编辑测试状态的软件包。 - false：不能编辑测试状态的软件包。
        :type is_edit_test_pkg: bool
        :param is_mkdir: **参数解释**: 能否创建文件夹。 **取值范围**: - true：能够创建目录。 - false：不能创建目录。
        :type is_mkdir: bool
        :param is_download: **参数解释**: 能否进行下载。 **取值范围**: - true：能够下载。 - false：不能下载。
        :type is_download: bool
        :param is_restore_all: **参数解释**: 能否还原回收站。 **取值范围**: - true：能够在回收站还原所有。 - false：不能在回收站还原所有。
        :type is_restore_all: bool
        :param is_empty: **参数解释**: 能否清空回收站。 **取值范围**: - true：能够清空回收站。 - false：不能清空回收站。
        :type is_empty: bool
        :param create_time: **参数解释**: 创建时间。 **取值范围**: 不涉及。
        :type create_time: int
        :param update_time: **参数解释**: 更新时间。 **取值范围**: 不涉及。
        :type update_time: int
        :param migrated_630: **参数解释**: 权限迁移状态。 **取值范围**: 不涉及。
        :type migrated_630: int
        :param region: **参数解释**: 区域。 **取值范围**: 不涉及。
        :type region: str
        :param user_id: **参数解释**: 用户id。 **取值范围**: 不涉及。
        :type user_id: str
        :param roles: **参数解释**: 角色。 **取值范围**: 不涉及。
        :type roles: str
        """
        
        

        self._id = None
        self._role_id = None
        self._devuc_role_id = None
        self._project_id = None
        self._is_permission_config = None
        self._is_change_pkg_status = None
        self._is_upload = None
        self._is_delete_restore_test_pkg = None
        self._is_delete_restore_prod_pkg = None
        self._is_edit_test_pkg = None
        self._is_mkdir = None
        self._is_download = None
        self._is_restore_all = None
        self._is_empty = None
        self._create_time = None
        self._update_time = None
        self._migrated_630 = None
        self._region = None
        self._user_id = None
        self._roles = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if role_id is not None:
            self.role_id = role_id
        if devuc_role_id is not None:
            self.devuc_role_id = devuc_role_id
        if project_id is not None:
            self.project_id = project_id
        if is_permission_config is not None:
            self.is_permission_config = is_permission_config
        if is_change_pkg_status is not None:
            self.is_change_pkg_status = is_change_pkg_status
        if is_upload is not None:
            self.is_upload = is_upload
        if is_delete_restore_test_pkg is not None:
            self.is_delete_restore_test_pkg = is_delete_restore_test_pkg
        if is_delete_restore_prod_pkg is not None:
            self.is_delete_restore_prod_pkg = is_delete_restore_prod_pkg
        if is_edit_test_pkg is not None:
            self.is_edit_test_pkg = is_edit_test_pkg
        if is_mkdir is not None:
            self.is_mkdir = is_mkdir
        if is_download is not None:
            self.is_download = is_download
        if is_restore_all is not None:
            self.is_restore_all = is_restore_all
        if is_empty is not None:
            self.is_empty = is_empty
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if migrated_630 is not None:
            self.migrated_630 = migrated_630
        if region is not None:
            self.region = region
        if user_id is not None:
            self.user_id = user_id
        if roles is not None:
            self.roles = roles

    @property
    def id(self):
        r"""Gets the id of this ProjectRolePermissionDo.

        **参数解释**: ID。 **取值范围**: 不涉及。

        :return: The id of this ProjectRolePermissionDo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ProjectRolePermissionDo.

        **参数解释**: ID。 **取值范围**: 不涉及。

        :param id: The id of this ProjectRolePermissionDo.
        :type id: str
        """
        self._id = id

    @property
    def role_id(self):
        r"""Gets the role_id of this ProjectRolePermissionDo.

        **参数解释**: 角色ID。 **取值范围**: 不涉及。

        :return: The role_id of this ProjectRolePermissionDo.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this ProjectRolePermissionDo.

        **参数解释**: 角色ID。 **取值范围**: 不涉及。

        :param role_id: The role_id of this ProjectRolePermissionDo.
        :type role_id: int
        """
        self._role_id = role_id

    @property
    def devuc_role_id(self):
        r"""Gets the devuc_role_id of this ProjectRolePermissionDo.

        **参数解释**: DEVUC角色ID。 **取值范围**: 不涉及。

        :return: The devuc_role_id of this ProjectRolePermissionDo.
        :rtype: str
        """
        return self._devuc_role_id

    @devuc_role_id.setter
    def devuc_role_id(self, devuc_role_id):
        r"""Sets the devuc_role_id of this ProjectRolePermissionDo.

        **参数解释**: DEVUC角色ID。 **取值范围**: 不涉及。

        :param devuc_role_id: The devuc_role_id of this ProjectRolePermissionDo.
        :type devuc_role_id: str
        """
        self._devuc_role_id = devuc_role_id

    @property
    def project_id(self):
        r"""Gets the project_id of this ProjectRolePermissionDo.

        **参数解释**: 项目ID。 **取值范围**: 不涉及。

        :return: The project_id of this ProjectRolePermissionDo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ProjectRolePermissionDo.

        **参数解释**: 项目ID。 **取值范围**: 不涉及。

        :param project_id: The project_id of this ProjectRolePermissionDo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_permission_config(self):
        r"""Gets the is_permission_config of this ProjectRolePermissionDo.

        **参数解释**: 是否具有权限配置能力。 **取值范围**: - true：能够配置权限。 - false：不能配置权限。

        :return: The is_permission_config of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_permission_config

    @is_permission_config.setter
    def is_permission_config(self, is_permission_config):
        r"""Sets the is_permission_config of this ProjectRolePermissionDo.

        **参数解释**: 是否具有权限配置能力。 **取值范围**: - true：能够配置权限。 - false：不能配置权限。

        :param is_permission_config: The is_permission_config of this ProjectRolePermissionDo.
        :type is_permission_config: bool
        """
        self._is_permission_config = is_permission_config

    @property
    def is_change_pkg_status(self):
        r"""Gets the is_change_pkg_status of this ProjectRolePermissionDo.

        **参数解释**: 能否更改软件包状态。 **取值范围**: - true：能够更改软件包状态。 - false：不能更改软件包状态。

        :return: The is_change_pkg_status of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_change_pkg_status

    @is_change_pkg_status.setter
    def is_change_pkg_status(self, is_change_pkg_status):
        r"""Sets the is_change_pkg_status of this ProjectRolePermissionDo.

        **参数解释**: 能否更改软件包状态。 **取值范围**: - true：能够更改软件包状态。 - false：不能更改软件包状态。

        :param is_change_pkg_status: The is_change_pkg_status of this ProjectRolePermissionDo.
        :type is_change_pkg_status: bool
        """
        self._is_change_pkg_status = is_change_pkg_status

    @property
    def is_upload(self):
        r"""Gets the is_upload of this ProjectRolePermissionDo.

        **参数解释**: 能否进行上传。 **取值范围**: - true：能够进行上传。 - false：不能上传。

        :return: The is_upload of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_upload

    @is_upload.setter
    def is_upload(self, is_upload):
        r"""Sets the is_upload of this ProjectRolePermissionDo.

        **参数解释**: 能否进行上传。 **取值范围**: - true：能够进行上传。 - false：不能上传。

        :param is_upload: The is_upload of this ProjectRolePermissionDo.
        :type is_upload: bool
        """
        self._is_upload = is_upload

    @property
    def is_delete_restore_test_pkg(self):
        r"""Gets the is_delete_restore_test_pkg of this ProjectRolePermissionDo.

        **参数解释**: 能否删除和还原测试状态的软件包。 **取值范围**: - true：能够删除和还原测试状态的软件包。 - false：不能删除和还原测试状态的软件包。

        :return: The is_delete_restore_test_pkg of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_delete_restore_test_pkg

    @is_delete_restore_test_pkg.setter
    def is_delete_restore_test_pkg(self, is_delete_restore_test_pkg):
        r"""Sets the is_delete_restore_test_pkg of this ProjectRolePermissionDo.

        **参数解释**: 能否删除和还原测试状态的软件包。 **取值范围**: - true：能够删除和还原测试状态的软件包。 - false：不能删除和还原测试状态的软件包。

        :param is_delete_restore_test_pkg: The is_delete_restore_test_pkg of this ProjectRolePermissionDo.
        :type is_delete_restore_test_pkg: bool
        """
        self._is_delete_restore_test_pkg = is_delete_restore_test_pkg

    @property
    def is_delete_restore_prod_pkg(self):
        r"""Gets the is_delete_restore_prod_pkg of this ProjectRolePermissionDo.

        **参数解释**: 能否删除和还原生产状态的软件包。 **取值范围**: - true：能够删除和还原生产状态的软件包。 - false：不能删除和还原生产状态的软件包。

        :return: The is_delete_restore_prod_pkg of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_delete_restore_prod_pkg

    @is_delete_restore_prod_pkg.setter
    def is_delete_restore_prod_pkg(self, is_delete_restore_prod_pkg):
        r"""Sets the is_delete_restore_prod_pkg of this ProjectRolePermissionDo.

        **参数解释**: 能否删除和还原生产状态的软件包。 **取值范围**: - true：能够删除和还原生产状态的软件包。 - false：不能删除和还原生产状态的软件包。

        :param is_delete_restore_prod_pkg: The is_delete_restore_prod_pkg of this ProjectRolePermissionDo.
        :type is_delete_restore_prod_pkg: bool
        """
        self._is_delete_restore_prod_pkg = is_delete_restore_prod_pkg

    @property
    def is_edit_test_pkg(self):
        r"""Gets the is_edit_test_pkg of this ProjectRolePermissionDo.

        **参数解释**: 能否编辑测试状态的软件包。 **取值范围**: - true：能够编辑测试状态的软件包。 - false：不能编辑测试状态的软件包。

        :return: The is_edit_test_pkg of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_edit_test_pkg

    @is_edit_test_pkg.setter
    def is_edit_test_pkg(self, is_edit_test_pkg):
        r"""Sets the is_edit_test_pkg of this ProjectRolePermissionDo.

        **参数解释**: 能否编辑测试状态的软件包。 **取值范围**: - true：能够编辑测试状态的软件包。 - false：不能编辑测试状态的软件包。

        :param is_edit_test_pkg: The is_edit_test_pkg of this ProjectRolePermissionDo.
        :type is_edit_test_pkg: bool
        """
        self._is_edit_test_pkg = is_edit_test_pkg

    @property
    def is_mkdir(self):
        r"""Gets the is_mkdir of this ProjectRolePermissionDo.

        **参数解释**: 能否创建文件夹。 **取值范围**: - true：能够创建目录。 - false：不能创建目录。

        :return: The is_mkdir of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_mkdir

    @is_mkdir.setter
    def is_mkdir(self, is_mkdir):
        r"""Sets the is_mkdir of this ProjectRolePermissionDo.

        **参数解释**: 能否创建文件夹。 **取值范围**: - true：能够创建目录。 - false：不能创建目录。

        :param is_mkdir: The is_mkdir of this ProjectRolePermissionDo.
        :type is_mkdir: bool
        """
        self._is_mkdir = is_mkdir

    @property
    def is_download(self):
        r"""Gets the is_download of this ProjectRolePermissionDo.

        **参数解释**: 能否进行下载。 **取值范围**: - true：能够下载。 - false：不能下载。

        :return: The is_download of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_download

    @is_download.setter
    def is_download(self, is_download):
        r"""Sets the is_download of this ProjectRolePermissionDo.

        **参数解释**: 能否进行下载。 **取值范围**: - true：能够下载。 - false：不能下载。

        :param is_download: The is_download of this ProjectRolePermissionDo.
        :type is_download: bool
        """
        self._is_download = is_download

    @property
    def is_restore_all(self):
        r"""Gets the is_restore_all of this ProjectRolePermissionDo.

        **参数解释**: 能否还原回收站。 **取值范围**: - true：能够在回收站还原所有。 - false：不能在回收站还原所有。

        :return: The is_restore_all of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_restore_all

    @is_restore_all.setter
    def is_restore_all(self, is_restore_all):
        r"""Sets the is_restore_all of this ProjectRolePermissionDo.

        **参数解释**: 能否还原回收站。 **取值范围**: - true：能够在回收站还原所有。 - false：不能在回收站还原所有。

        :param is_restore_all: The is_restore_all of this ProjectRolePermissionDo.
        :type is_restore_all: bool
        """
        self._is_restore_all = is_restore_all

    @property
    def is_empty(self):
        r"""Gets the is_empty of this ProjectRolePermissionDo.

        **参数解释**: 能否清空回收站。 **取值范围**: - true：能够清空回收站。 - false：不能清空回收站。

        :return: The is_empty of this ProjectRolePermissionDo.
        :rtype: bool
        """
        return self._is_empty

    @is_empty.setter
    def is_empty(self, is_empty):
        r"""Sets the is_empty of this ProjectRolePermissionDo.

        **参数解释**: 能否清空回收站。 **取值范围**: - true：能够清空回收站。 - false：不能清空回收站。

        :param is_empty: The is_empty of this ProjectRolePermissionDo.
        :type is_empty: bool
        """
        self._is_empty = is_empty

    @property
    def create_time(self):
        r"""Gets the create_time of this ProjectRolePermissionDo.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。

        :return: The create_time of this ProjectRolePermissionDo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ProjectRolePermissionDo.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。

        :param create_time: The create_time of this ProjectRolePermissionDo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ProjectRolePermissionDo.

        **参数解释**: 更新时间。 **取值范围**: 不涉及。

        :return: The update_time of this ProjectRolePermissionDo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ProjectRolePermissionDo.

        **参数解释**: 更新时间。 **取值范围**: 不涉及。

        :param update_time: The update_time of this ProjectRolePermissionDo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def migrated_630(self):
        r"""Gets the migrated_630 of this ProjectRolePermissionDo.

        **参数解释**: 权限迁移状态。 **取值范围**: 不涉及。

        :return: The migrated_630 of this ProjectRolePermissionDo.
        :rtype: int
        """
        return self._migrated_630

    @migrated_630.setter
    def migrated_630(self, migrated_630):
        r"""Sets the migrated_630 of this ProjectRolePermissionDo.

        **参数解释**: 权限迁移状态。 **取值范围**: 不涉及。

        :param migrated_630: The migrated_630 of this ProjectRolePermissionDo.
        :type migrated_630: int
        """
        self._migrated_630 = migrated_630

    @property
    def region(self):
        r"""Gets the region of this ProjectRolePermissionDo.

        **参数解释**: 区域。 **取值范围**: 不涉及。

        :return: The region of this ProjectRolePermissionDo.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ProjectRolePermissionDo.

        **参数解释**: 区域。 **取值范围**: 不涉及。

        :param region: The region of this ProjectRolePermissionDo.
        :type region: str
        """
        self._region = region

    @property
    def user_id(self):
        r"""Gets the user_id of this ProjectRolePermissionDo.

        **参数解释**: 用户id。 **取值范围**: 不涉及。

        :return: The user_id of this ProjectRolePermissionDo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ProjectRolePermissionDo.

        **参数解释**: 用户id。 **取值范围**: 不涉及。

        :param user_id: The user_id of this ProjectRolePermissionDo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def roles(self):
        r"""Gets the roles of this ProjectRolePermissionDo.

        **参数解释**: 角色。 **取值范围**: 不涉及。

        :return: The roles of this ProjectRolePermissionDo.
        :rtype: str
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this ProjectRolePermissionDo.

        **参数解释**: 角色。 **取值范围**: 不涉及。

        :param roles: The roles of this ProjectRolePermissionDo.
        :type roles: str
        """
        self._roles = roles

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
        if not isinstance(other, ProjectRolePermissionDo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
