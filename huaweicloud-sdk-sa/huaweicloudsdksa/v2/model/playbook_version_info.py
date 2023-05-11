# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlaybookVersionInfo:

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
        'run_mode': 'str',
        'enabled': 'bool',
        'status': 'str',
        'action_strategy': 'str',
        'actions': 'list[ActionInfo]',
        'rule_enable': 'bool',
        'rules': 'RuleInfo',
        'dataclass_id': 'str',
        'trigger_type': 'str',
        'dataobject_create': 'bool',
        'dataobject_update': 'bool',
        'dataobject_delete': 'bool',
        'version_type': 'int',
        'rule_id': 'str',
        'dataclass_name': 'str',
        'approve_name': 'str',
        'dataobject_id': 'str'
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
        'run_mode': 'run_mode',
        'enabled': 'enabled',
        'status': 'status',
        'action_strategy': 'action_strategy',
        'actions': 'actions',
        'rule_enable': 'rule_enable',
        'rules': 'rules',
        'dataclass_id': 'dataclass_id',
        'trigger_type': 'trigger_type',
        'dataobject_create': 'dataobject_create',
        'dataobject_update': 'dataobject_update',
        'dataobject_delete': 'dataobject_delete',
        'version_type': 'version_type',
        'rule_id': 'rule_id',
        'dataclass_name': 'dataclass_name',
        'approve_name': 'approve_name',
        'dataobject_id': 'dataobject_id'
    }

    def __init__(self, id=None, description=None, create_time=None, update_time=None, project_id=None, creator_id=None, modifier_id=None, playbook_id=None, version=None, run_mode=None, enabled=None, status=None, action_strategy=None, actions=None, rule_enable=None, rules=None, dataclass_id=None, trigger_type=None, dataobject_create=None, dataobject_update=None, dataobject_delete=None, version_type=None, rule_id=None, dataclass_name=None, approve_name=None, dataobject_id=None):
        """PlaybookVersionInfo

        The model defined in huaweicloud sdk

        :param id: Id value
        :type id: str
        :param description: The description, display only
        :type description: str
        :param create_time: Create time
        :type create_time: str
        :param update_time: Update time
        :type update_time: str
        :param project_id: Project id value
        :type project_id: str
        :param creator_id: Creator id value
        :type creator_id: str
        :param modifier_id: Modifier id value
        :type modifier_id: str
        :param playbook_id: Playbook id.
        :type playbook_id: str
        :param version: version
        :type version: str
        :param run_mode: Run mode of this playbook. automatic, manual
        :type run_mode: str
        :param enabled: If is enabled, false for disenabled, true for enabled
        :type enabled: bool
        :param status: Status of approvement. editing, approving, unpassed, published
        :type status: str
        :param action_strategy: Strategy of action. sync or async
        :type action_strategy: str
        :param actions: Information of actions.
        :type actions: list[:class:`huaweicloudsdksa.v2.ActionInfo`]
        :param rule_enable: If the condition filter is enabled.
        :type rule_enable: bool
        :param rules: 
        :type rules: :class:`huaweicloudsdksa.v2.RuleInfo`
        :param dataclass_id: bind dataclass id
        :type dataclass_id: str
        :param trigger_type: Strategy of action. event, timer
        :type trigger_type: str
        :param dataobject_create: if trigger when dataobject is created
        :type dataobject_create: bool
        :param dataobject_update: if trigger when dataobject is updated
        :type dataobject_update: bool
        :param dataobject_delete: if trigger when dataobject is deleted
        :type dataobject_delete: bool
        :param version_type: 版本类型
        :type version_type: int
        :param rule_id: 过滤规则ID
        :type rule_id: str
        :param dataclass_name: 数据类名称
        :type dataclass_name: str
        :param approve_name: 审核者
        :type approve_name: str
        :param dataobject_id: dataobject id
        :type dataobject_id: str
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
        self._run_mode = None
        self._enabled = None
        self._status = None
        self._action_strategy = None
        self._actions = None
        self._rule_enable = None
        self._rules = None
        self._dataclass_id = None
        self._trigger_type = None
        self._dataobject_create = None
        self._dataobject_update = None
        self._dataobject_delete = None
        self._version_type = None
        self._rule_id = None
        self._dataclass_name = None
        self._approve_name = None
        self._dataobject_id = None
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
        if run_mode is not None:
            self.run_mode = run_mode
        if enabled is not None:
            self.enabled = enabled
        if status is not None:
            self.status = status
        if action_strategy is not None:
            self.action_strategy = action_strategy
        if actions is not None:
            self.actions = actions
        if rule_enable is not None:
            self.rule_enable = rule_enable
        if rules is not None:
            self.rules = rules
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
        if dataobject_id is not None:
            self.dataobject_id = dataobject_id

    @property
    def id(self):
        """Gets the id of this PlaybookVersionInfo.

        Id value

        :return: The id of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PlaybookVersionInfo.

        Id value

        :param id: The id of this PlaybookVersionInfo.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this PlaybookVersionInfo.

        The description, display only

        :return: The description of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PlaybookVersionInfo.

        The description, display only

        :param description: The description of this PlaybookVersionInfo.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this PlaybookVersionInfo.

        Create time

        :return: The create_time of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this PlaybookVersionInfo.

        Create time

        :param create_time: The create_time of this PlaybookVersionInfo.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this PlaybookVersionInfo.

        Update time

        :return: The update_time of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this PlaybookVersionInfo.

        Update time

        :param update_time: The update_time of this PlaybookVersionInfo.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def project_id(self):
        """Gets the project_id of this PlaybookVersionInfo.

        Project id value

        :return: The project_id of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this PlaybookVersionInfo.

        Project id value

        :param project_id: The project_id of this PlaybookVersionInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def creator_id(self):
        """Gets the creator_id of this PlaybookVersionInfo.

        Creator id value

        :return: The creator_id of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this PlaybookVersionInfo.

        Creator id value

        :param creator_id: The creator_id of this PlaybookVersionInfo.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def modifier_id(self):
        """Gets the modifier_id of this PlaybookVersionInfo.

        Modifier id value

        :return: The modifier_id of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._modifier_id

    @modifier_id.setter
    def modifier_id(self, modifier_id):
        """Sets the modifier_id of this PlaybookVersionInfo.

        Modifier id value

        :param modifier_id: The modifier_id of this PlaybookVersionInfo.
        :type modifier_id: str
        """
        self._modifier_id = modifier_id

    @property
    def playbook_id(self):
        """Gets the playbook_id of this PlaybookVersionInfo.

        Playbook id.

        :return: The playbook_id of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        """Sets the playbook_id of this PlaybookVersionInfo.

        Playbook id.

        :param playbook_id: The playbook_id of this PlaybookVersionInfo.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def version(self):
        """Gets the version of this PlaybookVersionInfo.

        version

        :return: The version of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PlaybookVersionInfo.

        version

        :param version: The version of this PlaybookVersionInfo.
        :type version: str
        """
        self._version = version

    @property
    def run_mode(self):
        """Gets the run_mode of this PlaybookVersionInfo.

        Run mode of this playbook. automatic, manual

        :return: The run_mode of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._run_mode

    @run_mode.setter
    def run_mode(self, run_mode):
        """Sets the run_mode of this PlaybookVersionInfo.

        Run mode of this playbook. automatic, manual

        :param run_mode: The run_mode of this PlaybookVersionInfo.
        :type run_mode: str
        """
        self._run_mode = run_mode

    @property
    def enabled(self):
        """Gets the enabled of this PlaybookVersionInfo.

        If is enabled, false for disenabled, true for enabled

        :return: The enabled of this PlaybookVersionInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PlaybookVersionInfo.

        If is enabled, false for disenabled, true for enabled

        :param enabled: The enabled of this PlaybookVersionInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def status(self):
        """Gets the status of this PlaybookVersionInfo.

        Status of approvement. editing, approving, unpassed, published

        :return: The status of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this PlaybookVersionInfo.

        Status of approvement. editing, approving, unpassed, published

        :param status: The status of this PlaybookVersionInfo.
        :type status: str
        """
        self._status = status

    @property
    def action_strategy(self):
        """Gets the action_strategy of this PlaybookVersionInfo.

        Strategy of action. sync or async

        :return: The action_strategy of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._action_strategy

    @action_strategy.setter
    def action_strategy(self, action_strategy):
        """Sets the action_strategy of this PlaybookVersionInfo.

        Strategy of action. sync or async

        :param action_strategy: The action_strategy of this PlaybookVersionInfo.
        :type action_strategy: str
        """
        self._action_strategy = action_strategy

    @property
    def actions(self):
        """Gets the actions of this PlaybookVersionInfo.

        Information of actions.

        :return: The actions of this PlaybookVersionInfo.
        :rtype: list[:class:`huaweicloudsdksa.v2.ActionInfo`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this PlaybookVersionInfo.

        Information of actions.

        :param actions: The actions of this PlaybookVersionInfo.
        :type actions: list[:class:`huaweicloudsdksa.v2.ActionInfo`]
        """
        self._actions = actions

    @property
    def rule_enable(self):
        """Gets the rule_enable of this PlaybookVersionInfo.

        If the condition filter is enabled.

        :return: The rule_enable of this PlaybookVersionInfo.
        :rtype: bool
        """
        return self._rule_enable

    @rule_enable.setter
    def rule_enable(self, rule_enable):
        """Sets the rule_enable of this PlaybookVersionInfo.

        If the condition filter is enabled.

        :param rule_enable: The rule_enable of this PlaybookVersionInfo.
        :type rule_enable: bool
        """
        self._rule_enable = rule_enable

    @property
    def rules(self):
        """Gets the rules of this PlaybookVersionInfo.

        :return: The rules of this PlaybookVersionInfo.
        :rtype: :class:`huaweicloudsdksa.v2.RuleInfo`
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this PlaybookVersionInfo.

        :param rules: The rules of this PlaybookVersionInfo.
        :type rules: :class:`huaweicloudsdksa.v2.RuleInfo`
        """
        self._rules = rules

    @property
    def dataclass_id(self):
        """Gets the dataclass_id of this PlaybookVersionInfo.

        bind dataclass id

        :return: The dataclass_id of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        """Sets the dataclass_id of this PlaybookVersionInfo.

        bind dataclass id

        :param dataclass_id: The dataclass_id of this PlaybookVersionInfo.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def trigger_type(self):
        """Gets the trigger_type of this PlaybookVersionInfo.

        Strategy of action. event, timer

        :return: The trigger_type of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this PlaybookVersionInfo.

        Strategy of action. event, timer

        :param trigger_type: The trigger_type of this PlaybookVersionInfo.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def dataobject_create(self):
        """Gets the dataobject_create of this PlaybookVersionInfo.

        if trigger when dataobject is created

        :return: The dataobject_create of this PlaybookVersionInfo.
        :rtype: bool
        """
        return self._dataobject_create

    @dataobject_create.setter
    def dataobject_create(self, dataobject_create):
        """Sets the dataobject_create of this PlaybookVersionInfo.

        if trigger when dataobject is created

        :param dataobject_create: The dataobject_create of this PlaybookVersionInfo.
        :type dataobject_create: bool
        """
        self._dataobject_create = dataobject_create

    @property
    def dataobject_update(self):
        """Gets the dataobject_update of this PlaybookVersionInfo.

        if trigger when dataobject is updated

        :return: The dataobject_update of this PlaybookVersionInfo.
        :rtype: bool
        """
        return self._dataobject_update

    @dataobject_update.setter
    def dataobject_update(self, dataobject_update):
        """Sets the dataobject_update of this PlaybookVersionInfo.

        if trigger when dataobject is updated

        :param dataobject_update: The dataobject_update of this PlaybookVersionInfo.
        :type dataobject_update: bool
        """
        self._dataobject_update = dataobject_update

    @property
    def dataobject_delete(self):
        """Gets the dataobject_delete of this PlaybookVersionInfo.

        if trigger when dataobject is deleted

        :return: The dataobject_delete of this PlaybookVersionInfo.
        :rtype: bool
        """
        return self._dataobject_delete

    @dataobject_delete.setter
    def dataobject_delete(self, dataobject_delete):
        """Sets the dataobject_delete of this PlaybookVersionInfo.

        if trigger when dataobject is deleted

        :param dataobject_delete: The dataobject_delete of this PlaybookVersionInfo.
        :type dataobject_delete: bool
        """
        self._dataobject_delete = dataobject_delete

    @property
    def version_type(self):
        """Gets the version_type of this PlaybookVersionInfo.

        版本类型

        :return: The version_type of this PlaybookVersionInfo.
        :rtype: int
        """
        return self._version_type

    @version_type.setter
    def version_type(self, version_type):
        """Sets the version_type of this PlaybookVersionInfo.

        版本类型

        :param version_type: The version_type of this PlaybookVersionInfo.
        :type version_type: int
        """
        self._version_type = version_type

    @property
    def rule_id(self):
        """Gets the rule_id of this PlaybookVersionInfo.

        过滤规则ID

        :return: The rule_id of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this PlaybookVersionInfo.

        过滤规则ID

        :param rule_id: The rule_id of this PlaybookVersionInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def dataclass_name(self):
        """Gets the dataclass_name of this PlaybookVersionInfo.

        数据类名称

        :return: The dataclass_name of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._dataclass_name

    @dataclass_name.setter
    def dataclass_name(self, dataclass_name):
        """Sets the dataclass_name of this PlaybookVersionInfo.

        数据类名称

        :param dataclass_name: The dataclass_name of this PlaybookVersionInfo.
        :type dataclass_name: str
        """
        self._dataclass_name = dataclass_name

    @property
    def approve_name(self):
        """Gets the approve_name of this PlaybookVersionInfo.

        审核者

        :return: The approve_name of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._approve_name

    @approve_name.setter
    def approve_name(self, approve_name):
        """Sets the approve_name of this PlaybookVersionInfo.

        审核者

        :param approve_name: The approve_name of this PlaybookVersionInfo.
        :type approve_name: str
        """
        self._approve_name = approve_name

    @property
    def dataobject_id(self):
        """Gets the dataobject_id of this PlaybookVersionInfo.

        dataobject id

        :return: The dataobject_id of this PlaybookVersionInfo.
        :rtype: str
        """
        return self._dataobject_id

    @dataobject_id.setter
    def dataobject_id(self, dataobject_id):
        """Sets the dataobject_id of this PlaybookVersionInfo.

        dataobject id

        :param dataobject_id: The dataobject_id of this PlaybookVersionInfo.
        :type dataobject_id: str
        """
        self._dataobject_id = dataobject_id

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
        if not isinstance(other, PlaybookVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
