# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlaybookVersionListEntity:

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
        'description': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'project_id': 'str',
        'creator_id': 'str',
        'modifier_id': 'str',
        'playbook_id': 'str',
        'version': 'str',
        'enabled': 'bool',
        'status': 'str',
        'action_strategy': 'str',
        'rule_enable': 'bool',
        'dataclass_id': 'str',
        'trigger_type': 'str',
        'dataobject_create': 'bool',
        'dataobject_update': 'bool',
        'dataobject_delete': 'bool',
        'version_type': 'int',
        'rule_id': 'str',
        'dataclass_name': 'str',
        'approve_name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'project_id': 'project_id',
        'creator_id': 'creator_id',
        'modifier_id': 'modifier_id',
        'playbook_id': 'playbook_id',
        'version': 'version',
        'enabled': 'enabled',
        'status': 'status',
        'action_strategy': 'action_strategy',
        'rule_enable': 'rule_enable',
        'dataclass_id': 'dataclass_id',
        'trigger_type': 'trigger_type',
        'dataobject_create': 'dataobject_create',
        'dataobject_update': 'dataobject_update',
        'dataobject_delete': 'dataobject_delete',
        'version_type': 'version_type',
        'rule_id': 'rule_id',
        'dataclass_name': 'dataclass_name',
        'approve_name': 'approve_name'
    }

    def __init__(self, id=None, description=None, create_time=None, update_time=None, project_id=None, creator_id=None, modifier_id=None, playbook_id=None, version=None, enabled=None, status=None, action_strategy=None, rule_enable=None, dataclass_id=None, trigger_type=None, dataobject_create=None, dataobject_update=None, dataobject_delete=None, version_type=None, rule_id=None, dataclass_name=None, approve_name=None):
        """PlaybookVersionListEntity

        The model defined in huaweicloud sdk

        :param id: 剧本版本ID
        :type id: str
        :param description: 描述
        :type description: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        :param project_id: 项目ID
        :type project_id: str
        :param creator_id: 创建者ID
        :type creator_id: str
        :param modifier_id: 修改者ID
        :type modifier_id: str
        :param playbook_id: 剧本ID
        :type playbook_id: str
        :param version: 版本号
        :type version: str
        :param enabled: 是否激活
        :type enabled: bool
        :param status: 状态. (EDITING--编辑中, APPROVING--审核中, UNPASSED--审核不通过, PUBLISHED--审核通过)
        :type status: str
        :param action_strategy: 执行策略. 目前仅支持异步并发执行，对应值为ASYNC
        :type action_strategy: str
        :param rule_enable: 过滤规则是否启用
        :type rule_enable: bool
        :param dataclass_id: 数据类ID
        :type dataclass_id: str
        :param trigger_type: 触发方式. EVENT--事件触发, TIMER--定时触发
        :type trigger_type: str
        :param dataobject_create: 标识数据对象是否创建时触发剧本
        :type dataobject_create: bool
        :param dataobject_update: 标识数据对象是否更新时触发剧本
        :type dataobject_update: bool
        :param dataobject_delete: 标识数据对象是否删除时触发剧本
        :type dataobject_delete: bool
        :param version_type: 版本类型
        :type version_type: int
        :param rule_id: 过滤规则ID
        :type rule_id: str
        :param dataclass_name: 数据类名称
        :type dataclass_name: str
        :param approve_name: 审核者
        :type approve_name: str
        """
        
        

        self._id = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._project_id = None
        self._creator_id = None
        self._modifier_id = None
        self._playbook_id = None
        self._version = None
        self._enabled = None
        self._status = None
        self._action_strategy = None
        self._rule_enable = None
        self._dataclass_id = None
        self._trigger_type = None
        self._dataobject_create = None
        self._dataobject_update = None
        self._dataobject_delete = None
        self._version_type = None
        self._rule_id = None
        self._dataclass_name = None
        self._approve_name = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if project_id is not None:
            self.project_id = project_id
        if creator_id is not None:
            self.creator_id = creator_id
        if modifier_id is not None:
            self.modifier_id = modifier_id
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if version is not None:
            self.version = version
        if enabled is not None:
            self.enabled = enabled
        if status is not None:
            self.status = status
        if action_strategy is not None:
            self.action_strategy = action_strategy
        if rule_enable is not None:
            self.rule_enable = rule_enable
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if dataobject_create is not None:
            self.dataobject_create = dataobject_create
        if dataobject_update is not None:
            self.dataobject_update = dataobject_update
        if dataobject_delete is not None:
            self.dataobject_delete = dataobject_delete
        if version_type is not None:
            self.version_type = version_type
        if rule_id is not None:
            self.rule_id = rule_id
        if dataclass_name is not None:
            self.dataclass_name = dataclass_name
        if approve_name is not None:
            self.approve_name = approve_name

    @property
    def id(self):
        """Gets the id of this PlaybookVersionListEntity.

        剧本版本ID

        :return: The id of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlaybookVersionListEntity.

        剧本版本ID

        :param id: The id of this PlaybookVersionListEntity.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this PlaybookVersionListEntity.

        描述

        :return: The description of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PlaybookVersionListEntity.

        描述

        :param description: The description of this PlaybookVersionListEntity.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this PlaybookVersionListEntity.

        创建时间

        :return: The create_time of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PlaybookVersionListEntity.

        创建时间

        :param create_time: The create_time of this PlaybookVersionListEntity.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this PlaybookVersionListEntity.

        更新时间

        :return: The update_time of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this PlaybookVersionListEntity.

        更新时间

        :param update_time: The update_time of this PlaybookVersionListEntity.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def project_id(self):
        """Gets the project_id of this PlaybookVersionListEntity.

        项目ID

        :return: The project_id of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PlaybookVersionListEntity.

        项目ID

        :param project_id: The project_id of this PlaybookVersionListEntity.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def creator_id(self):
        """Gets the creator_id of this PlaybookVersionListEntity.

        创建者ID

        :return: The creator_id of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this PlaybookVersionListEntity.

        创建者ID

        :param creator_id: The creator_id of this PlaybookVersionListEntity.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def modifier_id(self):
        """Gets the modifier_id of this PlaybookVersionListEntity.

        修改者ID

        :return: The modifier_id of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        """Sets the modifier_id of this PlaybookVersionListEntity.

        修改者ID

        :param modifier_id: The modifier_id of this PlaybookVersionListEntity.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def playbook_id(self):
        """Gets the playbook_id of this PlaybookVersionListEntity.

        剧本ID

        :return: The playbook_id of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        """Sets the playbook_id of this PlaybookVersionListEntity.

        剧本ID

        :param playbook_id: The playbook_id of this PlaybookVersionListEntity.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def version(self):
        """Gets the version of this PlaybookVersionListEntity.

        版本号

        :return: The version of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PlaybookVersionListEntity.

        版本号

        :param version: The version of this PlaybookVersionListEntity.
        :type version: str
        """
        self._version = version

    @property
    def enabled(self):
        """Gets the enabled of this PlaybookVersionListEntity.

        是否激活

        :return: The enabled of this PlaybookVersionListEntity.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PlaybookVersionListEntity.

        是否激活

        :param enabled: The enabled of this PlaybookVersionListEntity.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def status(self):
        """Gets the status of this PlaybookVersionListEntity.

        状态. (EDITING--编辑中, APPROVING--审核中, UNPASSED--审核不通过, PUBLISHED--审核通过)

        :return: The status of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlaybookVersionListEntity.

        状态. (EDITING--编辑中, APPROVING--审核中, UNPASSED--审核不通过, PUBLISHED--审核通过)

        :param status: The status of this PlaybookVersionListEntity.
        :type status: str
        """
        self._status = status

    @property
    def action_strategy(self):
        """Gets the action_strategy of this PlaybookVersionListEntity.

        执行策略. 目前仅支持异步并发执行，对应值为ASYNC

        :return: The action_strategy of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._action_strategy

    @action_strategy.setter
    def action_strategy(self, action_strategy):
        """Sets the action_strategy of this PlaybookVersionListEntity.

        执行策略. 目前仅支持异步并发执行，对应值为ASYNC

        :param action_strategy: The action_strategy of this PlaybookVersionListEntity.
        :type action_strategy: str
        """
        self._action_strategy = action_strategy

    @property
    def rule_enable(self):
        """Gets the rule_enable of this PlaybookVersionListEntity.

        过滤规则是否启用

        :return: The rule_enable of this PlaybookVersionListEntity.
        :rtype: bool
        """
        return self._rule_enable

    @rule_enable.setter
    def rule_enable(self, rule_enable):
        """Sets the rule_enable of this PlaybookVersionListEntity.

        过滤规则是否启用

        :param rule_enable: The rule_enable of this PlaybookVersionListEntity.
        :type rule_enable: bool
        """
        self._rule_enable = rule_enable

    @property
    def dataclass_id(self):
        """Gets the dataclass_id of this PlaybookVersionListEntity.

        数据类ID

        :return: The dataclass_id of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        """Sets the dataclass_id of this PlaybookVersionListEntity.

        数据类ID

        :param dataclass_id: The dataclass_id of this PlaybookVersionListEntity.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def trigger_type(self):
        """Gets the trigger_type of this PlaybookVersionListEntity.

        触发方式. EVENT--事件触发, TIMER--定时触发

        :return: The trigger_type of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this PlaybookVersionListEntity.

        触发方式. EVENT--事件触发, TIMER--定时触发

        :param trigger_type: The trigger_type of this PlaybookVersionListEntity.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def dataobject_create(self):
        """Gets the dataobject_create of this PlaybookVersionListEntity.

        标识数据对象是否创建时触发剧本

        :return: The dataobject_create of this PlaybookVersionListEntity.
        :rtype: bool
        """
        return self._dataobject_create

    @dataobject_create.setter
    def dataobject_create(self, dataobject_create):
        """Sets the dataobject_create of this PlaybookVersionListEntity.

        标识数据对象是否创建时触发剧本

        :param dataobject_create: The dataobject_create of this PlaybookVersionListEntity.
        :type dataobject_create: bool
        """
        self._dataobject_create = dataobject_create

    @property
    def dataobject_update(self):
        """Gets the dataobject_update of this PlaybookVersionListEntity.

        标识数据对象是否更新时触发剧本

        :return: The dataobject_update of this PlaybookVersionListEntity.
        :rtype: bool
        """
        return self._dataobject_update

    @dataobject_update.setter
    def dataobject_update(self, dataobject_update):
        """Sets the dataobject_update of this PlaybookVersionListEntity.

        标识数据对象是否更新时触发剧本

        :param dataobject_update: The dataobject_update of this PlaybookVersionListEntity.
        :type dataobject_update: bool
        """
        self._dataobject_update = dataobject_update

    @property
    def dataobject_delete(self):
        """Gets the dataobject_delete of this PlaybookVersionListEntity.

        标识数据对象是否删除时触发剧本

        :return: The dataobject_delete of this PlaybookVersionListEntity.
        :rtype: bool
        """
        return self._dataobject_delete

    @dataobject_delete.setter
    def dataobject_delete(self, dataobject_delete):
        """Sets the dataobject_delete of this PlaybookVersionListEntity.

        标识数据对象是否删除时触发剧本

        :param dataobject_delete: The dataobject_delete of this PlaybookVersionListEntity.
        :type dataobject_delete: bool
        """
        self._dataobject_delete = dataobject_delete

    @property
    def version_type(self):
        """Gets the version_type of this PlaybookVersionListEntity.

        版本类型

        :return: The version_type of this PlaybookVersionListEntity.
        :rtype: int
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this PlaybookVersionListEntity.

        版本类型

        :param version_type: The version_type of this PlaybookVersionListEntity.
        :type version_type: int
        """
        self._version_type = version_type

    @property
    def rule_id(self):
        """Gets the rule_id of this PlaybookVersionListEntity.

        过滤规则ID

        :return: The rule_id of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this PlaybookVersionListEntity.

        过滤规则ID

        :param rule_id: The rule_id of this PlaybookVersionListEntity.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def dataclass_name(self):
        """Gets the dataclass_name of this PlaybookVersionListEntity.

        数据类名称

        :return: The dataclass_name of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        """Sets the dataclass_name of this PlaybookVersionListEntity.

        数据类名称

        :param dataclass_name: The dataclass_name of this PlaybookVersionListEntity.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def approve_name(self):
        """Gets the approve_name of this PlaybookVersionListEntity.

        审核者

        :return: The approve_name of this PlaybookVersionListEntity.
        :rtype: str
        """
        return self._approve_name

    @approve_name.setter
    def approve_name(self, approve_name):
        """Sets the approve_name of this PlaybookVersionListEntity.

        审核者

        :param approve_name: The approve_name of this PlaybookVersionListEntity.
        :type approve_name: str
        """
        self._approve_name = approve_name

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
        if not isinstance(other, PlaybookVersionListEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
