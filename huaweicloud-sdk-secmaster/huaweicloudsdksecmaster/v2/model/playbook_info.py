# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlaybookInfo:

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
        'name': 'str',
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'project_id': 'str',
        'version_id': 'str',
        'enabled': 'bool',
        'workspace_id': 'str',
        'approve_role': 'str',
        'user_role': 'str',
        'edit_role': 'str',
        'owner_id': 'str',
        'version': 'str',
        'dataclass_name': 'str',
        'dataclass_id': 'str',
        'unaudited_version_id': 'str',
        'reject_version_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'project_id': 'project_id',
        'version_id': 'version_id',
        'enabled': 'enabled',
        'workspace_id': 'workspace_id',
        'approve_role': 'approve_role',
        'user_role': 'user_role',
        'edit_role': 'edit_role',
        'owner_id': 'owner_id',
        'version': 'version',
        'dataclass_name': 'dataclass_name',
        'dataclass_id': 'dataclass_id',
        'unaudited_version_id': 'unaudited_version_id',
        'reject_version_id': 'reject_version_id'
    }

    def __init__(self, id=None, name=None, description=None, create_time=None, update_time=None, project_id=None, version_id=None, enabled=None, workspace_id=None, approve_role=None, user_role=None, edit_role=None, owner_id=None, version=None, dataclass_name=None, dataclass_id=None, unaudited_version_id=None, reject_version_id=None):
        r"""PlaybookInfo

        The model defined in huaweicloud sdk

        :param id: 剧本ID
        :type id: str
        :param name: 剧本名称
        :type name: str
        :param description: 描述信息
        :type description: str
        :param create_time: 剧本创建时间
        :type create_time: str
        :param update_time: 剧本更新时间
        :type update_time: str
        :param project_id: 项目ID
        :type project_id: str
        :param version_id: 剧本版本ID
        :type version_id: str
        :param enabled: 是否启用
        :type enabled: bool
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param approve_role: 审核用户角色
        :type approve_role: str
        :param user_role: 用户角色
        :type user_role: str
        :param edit_role: 编辑用户角色
        :type edit_role: str
        :param owner_id: 所有者ID
        :type owner_id: str
        :param version: 版本号
        :type version: str
        :param dataclass_name: 数据类名称
        :type dataclass_name: str
        :param dataclass_id: 数据类ID
        :type dataclass_id: str
        :param unaudited_version_id: 待审核剧本版本ID
        :type unaudited_version_id: str
        :param reject_version_id: 已驳回剧本版本ID
        :type reject_version_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._project_id = None
        self._version_id = None
        self._enabled = None
        self._workspace_id = None
        self._approve_role = None
        self._user_role = None
        self._edit_role = None
        self._owner_id = None
        self._version = None
        self._dataclass_name = None
        self._dataclass_id = None
        self._unaudited_version_id = None
        self._reject_version_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if project_id is not None:
            self.project_id = project_id
        if version_id is not None:
            self.version_id = version_id
        if enabled is not None:
            self.enabled = enabled
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if approve_role is not None:
            self.approve_role = approve_role
        if user_role is not None:
            self.user_role = user_role
        if edit_role is not None:
            self.edit_role = edit_role
        if owner_id is not None:
            self.owner_id = owner_id
        if version is not None:
            self.version = version
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if unaudited_version_id is not None:
            self.unaudited_version_id = unaudited_version_id
        if reject_version_id is not None:
            self.reject_version_id = reject_version_id

    @property
    def id(self):
        r"""Gets the id of this PlaybookInfo.

        剧本ID

        :return: The id of this PlaybookInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PlaybookInfo.

        剧本ID

        :param id: The id of this PlaybookInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this PlaybookInfo.

        剧本名称

        :return: The name of this PlaybookInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PlaybookInfo.

        剧本名称

        :param name: The name of this PlaybookInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this PlaybookInfo.

        描述信息

        :return: The description of this PlaybookInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PlaybookInfo.

        描述信息

        :param description: The description of this PlaybookInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this PlaybookInfo.

        剧本创建时间

        :return: The create_time of this PlaybookInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this PlaybookInfo.

        剧本创建时间

        :param create_time: The create_time of this PlaybookInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this PlaybookInfo.

        剧本更新时间

        :return: The update_time of this PlaybookInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this PlaybookInfo.

        剧本更新时间

        :param update_time: The update_time of this PlaybookInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def project_id(self):
        r"""Gets the project_id of this PlaybookInfo.

        项目ID

        :return: The project_id of this PlaybookInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this PlaybookInfo.

        项目ID

        :param project_id: The project_id of this PlaybookInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def version_id(self):
        r"""Gets the version_id of this PlaybookInfo.

        剧本版本ID

        :return: The version_id of this PlaybookInfo.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this PlaybookInfo.

        剧本版本ID

        :param version_id: The version_id of this PlaybookInfo.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def enabled(self):
        r"""Gets the enabled of this PlaybookInfo.

        是否启用

        :return: The enabled of this PlaybookInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this PlaybookInfo.

        是否启用

        :param enabled: The enabled of this PlaybookInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this PlaybookInfo.

        工作空间ID

        :return: The workspace_id of this PlaybookInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this PlaybookInfo.

        工作空间ID

        :param workspace_id: The workspace_id of this PlaybookInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def approve_role(self):
        r"""Gets the approve_role of this PlaybookInfo.

        审核用户角色

        :return: The approve_role of this PlaybookInfo.
        :rtype: str
        """
        return self._approve_role

    @approve_role.setter
    def approve_role(self, approve_role):
        r"""Sets the approve_role of this PlaybookInfo.

        审核用户角色

        :param approve_role: The approve_role of this PlaybookInfo.
        :type approve_role: str
        """
        self._approve_role = approve_role

    @property
    def user_role(self):
        r"""Gets the user_role of this PlaybookInfo.

        用户角色

        :return: The user_role of this PlaybookInfo.
        :rtype: str
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        r"""Sets the user_role of this PlaybookInfo.

        用户角色

        :param user_role: The user_role of this PlaybookInfo.
        :type user_role: str
        """
        self._user_role = user_role

    @property
    def edit_role(self):
        r"""Gets the edit_role of this PlaybookInfo.

        编辑用户角色

        :return: The edit_role of this PlaybookInfo.
        :rtype: str
        """
        return self._edit_role

    @edit_role.setter
    def edit_role(self, edit_role):
        r"""Sets the edit_role of this PlaybookInfo.

        编辑用户角色

        :param edit_role: The edit_role of this PlaybookInfo.
        :type edit_role: str
        """
        self._edit_role = edit_role

    @property
    def owner_id(self):
        r"""Gets the owner_id of this PlaybookInfo.

        所有者ID

        :return: The owner_id of this PlaybookInfo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this PlaybookInfo.

        所有者ID

        :param owner_id: The owner_id of this PlaybookInfo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def version(self):
        r"""Gets the version of this PlaybookInfo.

        版本号

        :return: The version of this PlaybookInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this PlaybookInfo.

        版本号

        :param version: The version of this PlaybookInfo.
        :type version: str
        """
        self._version = version

    @property
    def dataclass_name(self):
        r"""Gets the dataclass_name of this PlaybookInfo.

        数据类名称

        :return: The dataclass_name of this PlaybookInfo.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        r"""Sets the dataclass_name of this PlaybookInfo.

        数据类名称

        :param dataclass_name: The dataclass_name of this PlaybookInfo.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this PlaybookInfo.

        数据类ID

        :return: The dataclass_id of this PlaybookInfo.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this PlaybookInfo.

        数据类ID

        :param dataclass_id: The dataclass_id of this PlaybookInfo.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def unaudited_version_id(self):
        r"""Gets the unaudited_version_id of this PlaybookInfo.

        待审核剧本版本ID

        :return: The unaudited_version_id of this PlaybookInfo.
        :rtype: str
        """
        return self._unaudited_version_id

    @unaudited_version_id.setter
    def unaudited_version_id(self, unaudited_version_id):
        r"""Sets the unaudited_version_id of this PlaybookInfo.

        待审核剧本版本ID

        :param unaudited_version_id: The unaudited_version_id of this PlaybookInfo.
        :type unaudited_version_id: str
        """
        self._unaudited_version_id = unaudited_version_id

    @property
    def reject_version_id(self):
        r"""Gets the reject_version_id of this PlaybookInfo.

        已驳回剧本版本ID

        :return: The reject_version_id of this PlaybookInfo.
        :rtype: str
        """
        return self._reject_version_id

    @reject_version_id.setter
    def reject_version_id(self, reject_version_id):
        r"""Sets the reject_version_id of this PlaybookInfo.

        已驳回剧本版本ID

        :param reject_version_id: The reject_version_id of this PlaybookInfo.
        :type reject_version_id: str
        """
        self._reject_version_id = reject_version_id

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PlaybookInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
