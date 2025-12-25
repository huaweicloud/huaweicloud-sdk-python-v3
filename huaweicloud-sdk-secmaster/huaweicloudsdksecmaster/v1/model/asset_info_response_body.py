# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssetInfoResponseBody:

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
        'workspace_id': 'str',
        'name': 'str',
        'component_id': 'str',
        'component_name': 'str',
        'component_version_id': 'str',
        'type': 'str',
        'status': 'str',
        'config': 'str',
        'description': 'str',
        'enabled': 'bool',
        'create_time': 'str',
        'creator_id': 'str',
        'creator_name': 'str',
        'update_time': 'str',
        'modifier_id': 'str',
        'modifier_name': 'str',
        'defense_type': 'str',
        'target_project_id': 'str',
        'target_project_name': 'str',
        'target_enterprise_id': 'str',
        'target_enterprise_name': 'str',
        'region_id': 'str',
        'region_name': 'str',
        'can_be_deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'name': 'name',
        'component_id': 'component_id',
        'component_name': 'component_name',
        'component_version_id': 'component_version_id',
        'type': 'type',
        'status': 'status',
        'config': 'config',
        'description': 'description',
        'enabled': 'enabled',
        'create_time': 'create_time',
        'creator_id': 'creator_id',
        'creator_name': 'creator_name',
        'update_time': 'update_time',
        'modifier_id': 'modifier_id',
        'modifier_name': 'modifier_name',
        'defense_type': 'defense_type',
        'target_project_id': 'target_project_id',
        'target_project_name': 'target_project_name',
        'target_enterprise_id': 'target_enterprise_id',
        'target_enterprise_name': 'target_enterprise_name',
        'region_id': 'region_id',
        'region_name': 'region_name',
        'can_be_deleted': 'can_be_deleted'
    }

    def __init__(self, id=None, project_id=None, workspace_id=None, name=None, component_id=None, component_name=None, component_version_id=None, type=None, status=None, config=None, description=None, enabled=None, create_time=None, creator_id=None, creator_name=None, update_time=None, modifier_id=None, modifier_name=None, defense_type=None, target_project_id=None, target_project_name=None, target_enterprise_id=None, target_enterprise_name=None, region_id=None, region_name=None, can_be_deleted=None):
        r"""AssetInfoResponseBody

        The model defined in huaweicloud sdk

        :param id: 操作连接ID
        :type id: str
        :param project_id: 项目ID
        :type project_id: str
        :param workspace_id: 空间ID
        :type workspace_id: str
        :param name: 操作连接名称
        :type name: str
        :param component_id: 操作连接所属的插件id
        :type component_id: str
        :param component_name: 操作连接所属的插件id名称
        :type component_name: str
        :param component_version_id: 插件版本ID
        :type component_version_id: str
        :param type: 操作连接类型
        :type type: str
        :param status: 操作连接状态（SUCCESS/FAILED）
        :type status: str
        :param config: 具体的操作连接配置字符串，根据插件的操作连接schema配置对应字段值
        :type config: str
        :param description: 操作连接描述
        :type description: str
        :param enabled: 是否启用
        :type enabled: bool
        :param create_time: 创建时间
        :type create_time: str
        :param creator_id: 创建者ID
        :type creator_id: str
        :param creator_name: 创建者名称
        :type creator_name: str
        :param update_time: 更新时间
        :type update_time: str
        :param modifier_id: 更新者ID
        :type modifier_id: str
        :param modifier_name: 更新者名称
        :type modifier_name: str
        :param defense_type: 下发应急策略时的所属的防线分类
        :type defense_type: str
        :param target_project_id: 下发应急策略时的IAM项目ID
        :type target_project_id: str
        :param target_project_name: 下发应急策略时的IAM项目名称
        :type target_project_name: str
        :param target_enterprise_id: 下发应急策略时的企业项目ID
        :type target_enterprise_id: str
        :param target_enterprise_name: 下发应急策略时的企业项目名称
        :type target_enterprise_name: str
        :param region_id: 下发应急策略时的区域ID
        :type region_id: str
        :param region_name: 下发应急策略时的区域名称
        :type region_name: str
        :param can_be_deleted: 是否可删除，操作连接有流程在使用时，返回false
        :type can_be_deleted: bool
        """
        
        

        self._id = None
        self._project_id = None
        self._workspace_id = None
        self._name = None
        self._component_id = None
        self._component_name = None
        self._component_version_id = None
        self._type = None
        self._status = None
        self._config = None
        self._description = None
        self._enabled = None
        self._create_time = None
        self._creator_id = None
        self._creator_name = None
        self._update_time = None
        self._modifier_id = None
        self._modifier_name = None
        self._defense_type = None
        self._target_project_id = None
        self._target_project_name = None
        self._target_enterprise_id = None
        self._target_enterprise_name = None
        self._region_id = None
        self._region_name = None
        self._can_be_deleted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if name is not None:
            self.name = name
        if component_id is not None:
            self.component_id = component_id
        if component_name is not None:
            self.component_name = component_name
        if component_version_id is not None:
            self.component_version_id = component_version_id
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if config is not None:
            self.config = config
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if create_time is not None:
            self.create_time = create_time
        if creator_id is not None:
            self.creator_id = creator_id
        if creator_name is not None:
            self.creator_name = creator_name
        if update_time is not None:
            self.update_time = update_time
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if modifier_name is not None:
            self.modifier_name = modifier_name
        if defense_type is not None:
            self.defense_type = defense_type
        if target_project_id is not None:
            self.target_project_id = target_project_id
        if target_project_name is not None:
            self.target_project_name = target_project_name
        if target_enterprise_id is not None:
            self.target_enterprise_id = target_enterprise_id
        if target_enterprise_name is not None:
            self.target_enterprise_name = target_enterprise_name
        if region_id is not None:
            self.region_id = region_id
        if region_name is not None:
            self.region_name = region_name
        if can_be_deleted is not None:
            self.can_be_deleted = can_be_deleted

    @property
    def id(self):
        r"""Gets the id of this AssetInfoResponseBody.

        操作连接ID

        :return: The id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AssetInfoResponseBody.

        操作连接ID

        :param id: The id of this AssetInfoResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def project_id(self):
        r"""Gets the project_id of this AssetInfoResponseBody.

        项目ID

        :return: The project_id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this AssetInfoResponseBody.

        项目ID

        :param project_id: The project_id of this AssetInfoResponseBody.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AssetInfoResponseBody.

        空间ID

        :return: The workspace_id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AssetInfoResponseBody.

        空间ID

        :param workspace_id: The workspace_id of this AssetInfoResponseBody.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def name(self):
        r"""Gets the name of this AssetInfoResponseBody.

        操作连接名称

        :return: The name of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AssetInfoResponseBody.

        操作连接名称

        :param name: The name of this AssetInfoResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def component_id(self):
        r"""Gets the component_id of this AssetInfoResponseBody.

        操作连接所属的插件id

        :return: The component_id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this AssetInfoResponseBody.

        操作连接所属的插件id

        :param component_id: The component_id of this AssetInfoResponseBody.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def component_name(self):
        r"""Gets the component_name of this AssetInfoResponseBody.

        操作连接所属的插件id名称

        :return: The component_name of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        r"""Sets the component_name of this AssetInfoResponseBody.

        操作连接所属的插件id名称

        :param component_name: The component_name of this AssetInfoResponseBody.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def component_version_id(self):
        r"""Gets the component_version_id of this AssetInfoResponseBody.

        插件版本ID

        :return: The component_version_id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._component_version_id

    @component_version_id.setter
    def component_version_id(self, component_version_id):
        r"""Sets the component_version_id of this AssetInfoResponseBody.

        插件版本ID

        :param component_version_id: The component_version_id of this AssetInfoResponseBody.
        :type component_version_id: str
        """
        self._component_version_id = component_version_id

    @property
    def type(self):
        r"""Gets the type of this AssetInfoResponseBody.

        操作连接类型

        :return: The type of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AssetInfoResponseBody.

        操作连接类型

        :param type: The type of this AssetInfoResponseBody.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this AssetInfoResponseBody.

        操作连接状态（SUCCESS/FAILED）

        :return: The status of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AssetInfoResponseBody.

        操作连接状态（SUCCESS/FAILED）

        :param status: The status of this AssetInfoResponseBody.
        :type status: str
        """
        self._status = status

    @property
    def config(self):
        r"""Gets the config of this AssetInfoResponseBody.

        具体的操作连接配置字符串，根据插件的操作连接schema配置对应字段值

        :return: The config of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this AssetInfoResponseBody.

        具体的操作连接配置字符串，根据插件的操作连接schema配置对应字段值

        :param config: The config of this AssetInfoResponseBody.
        :type config: str
        """
        self._config = config

    @property
    def description(self):
        r"""Gets the description of this AssetInfoResponseBody.

        操作连接描述

        :return: The description of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AssetInfoResponseBody.

        操作连接描述

        :param description: The description of this AssetInfoResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def enabled(self):
        r"""Gets the enabled of this AssetInfoResponseBody.

        是否启用

        :return: The enabled of this AssetInfoResponseBody.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this AssetInfoResponseBody.

        是否启用

        :param enabled: The enabled of this AssetInfoResponseBody.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def create_time(self):
        r"""Gets the create_time of this AssetInfoResponseBody.

        创建时间

        :return: The create_time of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AssetInfoResponseBody.

        创建时间

        :param create_time: The create_time of this AssetInfoResponseBody.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def creator_id(self):
        r"""Gets the creator_id of this AssetInfoResponseBody.

        创建者ID

        :return: The creator_id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this AssetInfoResponseBody.

        创建者ID

        :param creator_id: The creator_id of this AssetInfoResponseBody.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def creator_name(self):
        r"""Gets the creator_name of this AssetInfoResponseBody.

        创建者名称

        :return: The creator_name of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._creator_name

    @creator_name.setter
    def creator_name(self, creator_name):
        r"""Sets the creator_name of this AssetInfoResponseBody.

        创建者名称

        :param creator_name: The creator_name of this AssetInfoResponseBody.
        :type creator_name: str
        """
        self._creator_name = creator_name

    @property
    def update_time(self):
        r"""Gets the update_time of this AssetInfoResponseBody.

        更新时间

        :return: The update_time of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AssetInfoResponseBody.

        更新时间

        :param update_time: The update_time of this AssetInfoResponseBody.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def modifier_id(self):
        r"""Gets the modifier_id of this AssetInfoResponseBody.

        更新者ID

        :return: The modifier_id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        r"""Sets the modifier_id of this AssetInfoResponseBody.

        更新者ID

        :param modifier_id: The modifier_id of this AssetInfoResponseBody.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def modifier_name(self):
        r"""Gets the modifier_name of this AssetInfoResponseBody.

        更新者名称

        :return: The modifier_name of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._modifier_name

    @modifier_name.setter
    def modifier_name(self, modifier_name):
        r"""Sets the modifier_name of this AssetInfoResponseBody.

        更新者名称

        :param modifier_name: The modifier_name of this AssetInfoResponseBody.
        :type modifier_name: str
        """
        self._modifier_name = modifier_name

    @property
    def defense_type(self):
        r"""Gets the defense_type of this AssetInfoResponseBody.

        下发应急策略时的所属的防线分类

        :return: The defense_type of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._defense_type

    @defense_type.setter
    def defense_type(self, defense_type):
        r"""Sets the defense_type of this AssetInfoResponseBody.

        下发应急策略时的所属的防线分类

        :param defense_type: The defense_type of this AssetInfoResponseBody.
        :type defense_type: str
        """
        self._defense_type = defense_type

    @property
    def target_project_id(self):
        r"""Gets the target_project_id of this AssetInfoResponseBody.

        下发应急策略时的IAM项目ID

        :return: The target_project_id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._target_project_id

    @target_project_id.setter
    def target_project_id(self, target_project_id):
        r"""Sets the target_project_id of this AssetInfoResponseBody.

        下发应急策略时的IAM项目ID

        :param target_project_id: The target_project_id of this AssetInfoResponseBody.
        :type target_project_id: str
        """
        self._target_project_id = target_project_id

    @property
    def target_project_name(self):
        r"""Gets the target_project_name of this AssetInfoResponseBody.

        下发应急策略时的IAM项目名称

        :return: The target_project_name of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._target_project_name

    @target_project_name.setter
    def target_project_name(self, target_project_name):
        r"""Sets the target_project_name of this AssetInfoResponseBody.

        下发应急策略时的IAM项目名称

        :param target_project_name: The target_project_name of this AssetInfoResponseBody.
        :type target_project_name: str
        """
        self._target_project_name = target_project_name

    @property
    def target_enterprise_id(self):
        r"""Gets the target_enterprise_id of this AssetInfoResponseBody.

        下发应急策略时的企业项目ID

        :return: The target_enterprise_id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._target_enterprise_id

    @target_enterprise_id.setter
    def target_enterprise_id(self, target_enterprise_id):
        r"""Sets the target_enterprise_id of this AssetInfoResponseBody.

        下发应急策略时的企业项目ID

        :param target_enterprise_id: The target_enterprise_id of this AssetInfoResponseBody.
        :type target_enterprise_id: str
        """
        self._target_enterprise_id = target_enterprise_id

    @property
    def target_enterprise_name(self):
        r"""Gets the target_enterprise_name of this AssetInfoResponseBody.

        下发应急策略时的企业项目名称

        :return: The target_enterprise_name of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._target_enterprise_name

    @target_enterprise_name.setter
    def target_enterprise_name(self, target_enterprise_name):
        r"""Sets the target_enterprise_name of this AssetInfoResponseBody.

        下发应急策略时的企业项目名称

        :param target_enterprise_name: The target_enterprise_name of this AssetInfoResponseBody.
        :type target_enterprise_name: str
        """
        self._target_enterprise_name = target_enterprise_name

    @property
    def region_id(self):
        r"""Gets the region_id of this AssetInfoResponseBody.

        下发应急策略时的区域ID

        :return: The region_id of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this AssetInfoResponseBody.

        下发应急策略时的区域ID

        :param region_id: The region_id of this AssetInfoResponseBody.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def region_name(self):
        r"""Gets the region_name of this AssetInfoResponseBody.

        下发应急策略时的区域名称

        :return: The region_name of this AssetInfoResponseBody.
        :rtype: str
        """
        return self._region_name

    @region_name.setter
    def region_name(self, region_name):
        r"""Sets the region_name of this AssetInfoResponseBody.

        下发应急策略时的区域名称

        :param region_name: The region_name of this AssetInfoResponseBody.
        :type region_name: str
        """
        self._region_name = region_name

    @property
    def can_be_deleted(self):
        r"""Gets the can_be_deleted of this AssetInfoResponseBody.

        是否可删除，操作连接有流程在使用时，返回false

        :return: The can_be_deleted of this AssetInfoResponseBody.
        :rtype: bool
        """
        return self._can_be_deleted

    @can_be_deleted.setter
    def can_be_deleted(self, can_be_deleted):
        r"""Sets the can_be_deleted of this AssetInfoResponseBody.

        是否可删除，操作连接有流程在使用时，返回false

        :param can_be_deleted: The can_be_deleted of this AssetInfoResponseBody.
        :type can_be_deleted: bool
        """
        self._can_be_deleted = can_be_deleted

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
        if not isinstance(other, AssetInfoResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
