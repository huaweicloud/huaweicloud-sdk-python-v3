# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AopWorkflowInfo:

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
        'project_id': 'str',
        'owner_id': 'str',
        'creator_id': 'str',
        'edit_role': 'str',
        'use_role': 'str',
        'approve_role': 'str',
        'enabled': 'bool',
        'workspace_id': 'str',
        'version_id': 'str',
        'current_approval_version_id': 'str',
        'current_rejected_version_id': 'str',
        'aop_type': 'str',
        'engine_type': 'str',
        'dataclass_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'owner_id': 'owner_id',
        'creator_id': 'creator_id',
        'edit_role': 'edit_role',
        'use_role': 'use_role',
        'approve_role': 'approve_role',
        'enabled': 'enabled',
        'workspace_id': 'workspace_id',
        'version_id': 'version_id',
        'current_approval_version_id': 'current_approval_version_id',
        'current_rejected_version_id': 'current_rejected_version_id',
        'aop_type': 'aop_type',
        'engine_type': 'engine_type',
        'dataclass_id': 'dataclass_id'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, owner_id=None, creator_id=None, edit_role=None, use_role=None, approve_role=None, enabled=None, workspace_id=None, version_id=None, current_approval_version_id=None, current_rejected_version_id=None, aop_type=None, engine_type=None, dataclass_id=None):
        r"""AopWorkflowInfo

        The model defined in huaweicloud sdk

        :param id: 流程ID
        :type id: str
        :param name: 流程名称
        :type name: str
        :param description: 描述
        :type description: str
        :param project_id: 租户ID
        :type project_id: str
        :param owner_id: 所有者ID
        :type owner_id: str
        :param creator_id: 创建者ID
        :type creator_id: str
        :param edit_role: 编辑角色
        :type edit_role: str
        :param use_role: 是用角色
        :type use_role: str
        :param approve_role: 审核人
        :type approve_role: str
        :param enabled: 是否已启用
        :type enabled: bool
        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param version_id: 流程版本ID
        :type version_id: str
        :param current_approval_version_id: 当前待审核版本号
        :type current_approval_version_id: str
        :param current_rejected_version_id: 当前拒绝的版本号
        :type current_rejected_version_id: str
        :param aop_type: aop的类型有以下的值     NORMAL, 通用     SURVEY, 调查     HEMOSTASIS,止血     EASE;缓解
        :type aop_type: str
        :param engine_type: 引擎的类型分为共享版和专项版
        :type engine_type: str
        :param dataclass_id: 数据类的ID
        :type dataclass_id: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._owner_id = None
        self._creator_id = None
        self._edit_role = None
        self._use_role = None
        self._approve_role = None
        self._enabled = None
        self._workspace_id = None
        self._version_id = None
        self._current_approval_version_id = None
        self._current_rejected_version_id = None
        self._aop_type = None
        self._engine_type = None
        self._dataclass_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if owner_id is not None:
            self.owner_id = owner_id
        if creator_id is not None:
            self.creator_id = creator_id
        if edit_role is not None:
            self.edit_role = edit_role
        if use_role is not None:
            self.use_role = use_role
        if approve_role is not None:
            self.approve_role = approve_role
        if enabled is not None:
            self.enabled = enabled
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if version_id is not None:
            self.version_id = version_id
        if current_approval_version_id is not None:
            self.current_approval_version_id = current_approval_version_id
        if current_rejected_version_id is not None:
            self.current_rejected_version_id = current_rejected_version_id
        if aop_type is not None:
            self.aop_type = aop_type
        if engine_type is not None:
            self.engine_type = engine_type
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id

    @property
    def id(self):
        r"""Gets the id of this AopWorkflowInfo.

        流程ID

        :return: The id of this AopWorkflowInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AopWorkflowInfo.

        流程ID

        :param id: The id of this AopWorkflowInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AopWorkflowInfo.

        流程名称

        :return: The name of this AopWorkflowInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AopWorkflowInfo.

        流程名称

        :param name: The name of this AopWorkflowInfo.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AopWorkflowInfo.

        描述

        :return: The description of this AopWorkflowInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AopWorkflowInfo.

        描述

        :param description: The description of this AopWorkflowInfo.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this AopWorkflowInfo.

        租户ID

        :return: The project_id of this AopWorkflowInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AopWorkflowInfo.

        租户ID

        :param project_id: The project_id of this AopWorkflowInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def owner_id(self):
        r"""Gets the owner_id of this AopWorkflowInfo.

        所有者ID

        :return: The owner_id of this AopWorkflowInfo.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this AopWorkflowInfo.

        所有者ID

        :param owner_id: The owner_id of this AopWorkflowInfo.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def creator_id(self):
        r"""Gets the creator_id of this AopWorkflowInfo.

        创建者ID

        :return: The creator_id of this AopWorkflowInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this AopWorkflowInfo.

        创建者ID

        :param creator_id: The creator_id of this AopWorkflowInfo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def edit_role(self):
        r"""Gets the edit_role of this AopWorkflowInfo.

        编辑角色

        :return: The edit_role of this AopWorkflowInfo.
        :rtype: str
        """
        return self._edit_role

    @edit_role.setter
    def edit_role(self, edit_role):
        r"""Sets the edit_role of this AopWorkflowInfo.

        编辑角色

        :param edit_role: The edit_role of this AopWorkflowInfo.
        :type edit_role: str
        """
        self._edit_role = edit_role

    @property
    def use_role(self):
        r"""Gets the use_role of this AopWorkflowInfo.

        是用角色

        :return: The use_role of this AopWorkflowInfo.
        :rtype: str
        """
        return self._use_role

    @use_role.setter
    def use_role(self, use_role):
        r"""Sets the use_role of this AopWorkflowInfo.

        是用角色

        :param use_role: The use_role of this AopWorkflowInfo.
        :type use_role: str
        """
        self._use_role = use_role

    @property
    def approve_role(self):
        r"""Gets the approve_role of this AopWorkflowInfo.

        审核人

        :return: The approve_role of this AopWorkflowInfo.
        :rtype: str
        """
        return self._approve_role

    @approve_role.setter
    def approve_role(self, approve_role):
        r"""Sets the approve_role of this AopWorkflowInfo.

        审核人

        :param approve_role: The approve_role of this AopWorkflowInfo.
        :type approve_role: str
        """
        self._approve_role = approve_role

    @property
    def enabled(self):
        r"""Gets the enabled of this AopWorkflowInfo.

        是否已启用

        :return: The enabled of this AopWorkflowInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this AopWorkflowInfo.

        是否已启用

        :param enabled: The enabled of this AopWorkflowInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AopWorkflowInfo.

        工作空间ID

        :return: The workspace_id of this AopWorkflowInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AopWorkflowInfo.

        工作空间ID

        :param workspace_id: The workspace_id of this AopWorkflowInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def version_id(self):
        r"""Gets the version_id of this AopWorkflowInfo.

        流程版本ID

        :return: The version_id of this AopWorkflowInfo.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this AopWorkflowInfo.

        流程版本ID

        :param version_id: The version_id of this AopWorkflowInfo.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def current_approval_version_id(self):
        r"""Gets the current_approval_version_id of this AopWorkflowInfo.

        当前待审核版本号

        :return: The current_approval_version_id of this AopWorkflowInfo.
        :rtype: str
        """
        return self._current_approval_version_id

    @current_approval_version_id.setter
    def current_approval_version_id(self, current_approval_version_id):
        r"""Sets the current_approval_version_id of this AopWorkflowInfo.

        当前待审核版本号

        :param current_approval_version_id: The current_approval_version_id of this AopWorkflowInfo.
        :type current_approval_version_id: str
        """
        self._current_approval_version_id = current_approval_version_id

    @property
    def current_rejected_version_id(self):
        r"""Gets the current_rejected_version_id of this AopWorkflowInfo.

        当前拒绝的版本号

        :return: The current_rejected_version_id of this AopWorkflowInfo.
        :rtype: str
        """
        return self._current_rejected_version_id

    @current_rejected_version_id.setter
    def current_rejected_version_id(self, current_rejected_version_id):
        r"""Sets the current_rejected_version_id of this AopWorkflowInfo.

        当前拒绝的版本号

        :param current_rejected_version_id: The current_rejected_version_id of this AopWorkflowInfo.
        :type current_rejected_version_id: str
        """
        self._current_rejected_version_id = current_rejected_version_id

    @property
    def aop_type(self):
        r"""Gets the aop_type of this AopWorkflowInfo.

        aop的类型有以下的值     NORMAL, 通用     SURVEY, 调查     HEMOSTASIS,止血     EASE;缓解

        :return: The aop_type of this AopWorkflowInfo.
        :rtype: str
        """
        return self._aop_type

    @aop_type.setter
    def aop_type(self, aop_type):
        r"""Sets the aop_type of this AopWorkflowInfo.

        aop的类型有以下的值     NORMAL, 通用     SURVEY, 调查     HEMOSTASIS,止血     EASE;缓解

        :param aop_type: The aop_type of this AopWorkflowInfo.
        :type aop_type: str
        """
        self._aop_type = aop_type

    @property
    def engine_type(self):
        r"""Gets the engine_type of this AopWorkflowInfo.

        引擎的类型分为共享版和专项版

        :return: The engine_type of this AopWorkflowInfo.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this AopWorkflowInfo.

        引擎的类型分为共享版和专项版

        :param engine_type: The engine_type of this AopWorkflowInfo.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def dataclass_id(self):
        r"""Gets the dataclass_id of this AopWorkflowInfo.

        数据类的ID

        :return: The dataclass_id of this AopWorkflowInfo.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        r"""Sets the dataclass_id of this AopWorkflowInfo.

        数据类的ID

        :param dataclass_id: The dataclass_id of this AopWorkflowInfo.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

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
        if not isinstance(other, AopWorkflowInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
