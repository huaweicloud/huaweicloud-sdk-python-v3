# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyPlaybookVersionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'workspace_id': 'str',
        'playbook_id': 'str',
        'dataclass_id': 'str',
        'rule_enable': 'bool',
        'enabled': 'bool',
        'status': 'str',
        'rule_id': 'str',
        'trigger_type': 'str',
        'dataobject_create': 'bool',
        'dataobject_update': 'bool',
        'dataobject_delete': 'bool',
        'action_strategy': 'str'
    }

    attribute_map = {
        'description': 'description',
        'workspace_id': 'workspace_id',
        'playbook_id': 'playbook_id',
        'dataclass_id': 'dataclass_id',
        'rule_enable': 'rule_enable',
        'enabled': 'enabled',
        'status': 'status',
        'rule_id': 'rule_id',
        'trigger_type': 'trigger_type',
        'dataobject_create': 'dataobject_create',
        'dataobject_update': 'dataobject_update',
        'dataobject_delete': 'dataobject_delete',
        'action_strategy': 'action_strategy'
    }

    def __init__(self, description=None, workspace_id=None, playbook_id=None, dataclass_id=None, rule_enable=None, enabled=None, status=None, rule_id=None, trigger_type=None, dataobject_create=None, dataobject_update=None, dataobject_delete=None, action_strategy=None):
        """ModifyPlaybookVersionInfo

        The model defined in huaweicloud sdk

        :param description: The description, display only
        :type description: str
        :param workspace_id: 工作空间id
        :type workspace_id: str
        :param playbook_id: Playbook id.
        :type playbook_id: str
        :param dataclass_id: dataclass id.
        :type dataclass_id: str
        :param rule_enable: If the condition filter is enabled.
        :type rule_enable: bool
        :param enabled: If is enabled, false for disenabled, true for enabled
        :type enabled: bool
        :param status: 状态
        :type status: str
        :param rule_id: 规则ID
        :type rule_id: str
        :param trigger_type: Strategy of action. event, timer
        :type trigger_type: str
        :param dataobject_create: if trigger when dataobject is created
        :type dataobject_create: bool
        :param dataobject_update: if trigger when dataobject is updated
        :type dataobject_update: bool
        :param dataobject_delete: if trigger when dataobject is deleted
        :type dataobject_delete: bool
        :param action_strategy: Strategy of action. sync or async
        :type action_strategy: str
        """
        
        

        self._description = None
        self._workspace_id = None
        self._playbook_id = None
        self._dataclass_id = None
        self._rule_enable = None
        self._enabled = None
        self._status = None
        self._rule_id = None
        self._trigger_type = None
        self._dataobject_create = None
        self._dataobject_update = None
        self._dataobject_delete = None
        self._action_strategy = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if playbook_id is not None:
            self.playbook_id = playbook_id
        if dataclass_id is not None:
            self.dataclass_id = dataclass_id
        if rule_enable is not None:
            self.rule_enable = rule_enable
        if enabled is not None:
            self.enabled = enabled
        if status is not None:
            self.status = status
        if rule_id is not None:
            self.rule_id = rule_id
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if dataobject_create is not None:
            self.dataobject_create = dataobject_create
        if dataobject_update is not None:
            self.dataobject_update = dataobject_update
        if dataobject_delete is not None:
            self.dataobject_delete = dataobject_delete
        if action_strategy is not None:
            self.action_strategy = action_strategy

    @property
    def description(self):
        """Gets the description of this ModifyPlaybookVersionInfo.

        The description, display only

        :return: The description of this ModifyPlaybookVersionInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyPlaybookVersionInfo.

        The description, display only

        :param description: The description of this ModifyPlaybookVersionInfo.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ModifyPlaybookVersionInfo.

        工作空间id

        :return: The workspace_id of this ModifyPlaybookVersionInfo.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ModifyPlaybookVersionInfo.

        工作空间id

        :param workspace_id: The workspace_id of this ModifyPlaybookVersionInfo.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def playbook_id(self):
        """Gets the playbook_id of this ModifyPlaybookVersionInfo.

        Playbook id.

        :return: The playbook_id of this ModifyPlaybookVersionInfo.
        :rtype: str
        """
        return self._playbook_id

    @playbook_id.setter
    def playbook_id(self, playbook_id):
        """Sets the playbook_id of this ModifyPlaybookVersionInfo.

        Playbook id.

        :param playbook_id: The playbook_id of this ModifyPlaybookVersionInfo.
        :type playbook_id: str
        """
        self._playbook_id = playbook_id

    @property
    def dataclass_id(self):
        """Gets the dataclass_id of this ModifyPlaybookVersionInfo.

        dataclass id.

        :return: The dataclass_id of this ModifyPlaybookVersionInfo.
        :rtype: str
        """
        return self._dataclass_id

    @dataclass_id.setter
    def dataclass_id(self, dataclass_id):
        """Sets the dataclass_id of this ModifyPlaybookVersionInfo.

        dataclass id.

        :param dataclass_id: The dataclass_id of this ModifyPlaybookVersionInfo.
        :type dataclass_id: str
        """
        self._dataclass_id = dataclass_id

    @property
    def rule_enable(self):
        """Gets the rule_enable of this ModifyPlaybookVersionInfo.

        If the condition filter is enabled.

        :return: The rule_enable of this ModifyPlaybookVersionInfo.
        :rtype: bool
        """
        return self._rule_enable

    @rule_enable.setter
    def rule_enable(self, rule_enable):
        """Sets the rule_enable of this ModifyPlaybookVersionInfo.

        If the condition filter is enabled.

        :param rule_enable: The rule_enable of this ModifyPlaybookVersionInfo.
        :type rule_enable: bool
        """
        self._rule_enable = rule_enable

    @property
    def enabled(self):
        """Gets the enabled of this ModifyPlaybookVersionInfo.

        If is enabled, false for disenabled, true for enabled

        :return: The enabled of this ModifyPlaybookVersionInfo.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ModifyPlaybookVersionInfo.

        If is enabled, false for disenabled, true for enabled

        :param enabled: The enabled of this ModifyPlaybookVersionInfo.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def status(self):
        """Gets the status of this ModifyPlaybookVersionInfo.

        状态

        :return: The status of this ModifyPlaybookVersionInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModifyPlaybookVersionInfo.

        状态

        :param status: The status of this ModifyPlaybookVersionInfo.
        :type status: str
        """
        self._status = status

    @property
    def rule_id(self):
        """Gets the rule_id of this ModifyPlaybookVersionInfo.

        规则ID

        :return: The rule_id of this ModifyPlaybookVersionInfo.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ModifyPlaybookVersionInfo.

        规则ID

        :param rule_id: The rule_id of this ModifyPlaybookVersionInfo.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def trigger_type(self):
        """Gets the trigger_type of this ModifyPlaybookVersionInfo.

        Strategy of action. event, timer

        :return: The trigger_type of this ModifyPlaybookVersionInfo.
        :rtype: str
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        """Sets the trigger_type of this ModifyPlaybookVersionInfo.

        Strategy of action. event, timer

        :param trigger_type: The trigger_type of this ModifyPlaybookVersionInfo.
        :type trigger_type: str
        """
        self._trigger_type = trigger_type

    @property
    def dataobject_create(self):
        """Gets the dataobject_create of this ModifyPlaybookVersionInfo.

        if trigger when dataobject is created

        :return: The dataobject_create of this ModifyPlaybookVersionInfo.
        :rtype: bool
        """
        return self._dataobject_create

    @dataobject_create.setter
    def dataobject_create(self, dataobject_create):
        """Sets the dataobject_create of this ModifyPlaybookVersionInfo.

        if trigger when dataobject is created

        :param dataobject_create: The dataobject_create of this ModifyPlaybookVersionInfo.
        :type dataobject_create: bool
        """
        self._dataobject_create = dataobject_create

    @property
    def dataobject_update(self):
        """Gets the dataobject_update of this ModifyPlaybookVersionInfo.

        if trigger when dataobject is updated

        :return: The dataobject_update of this ModifyPlaybookVersionInfo.
        :rtype: bool
        """
        return self._dataobject_update

    @dataobject_update.setter
    def dataobject_update(self, dataobject_update):
        """Sets the dataobject_update of this ModifyPlaybookVersionInfo.

        if trigger when dataobject is updated

        :param dataobject_update: The dataobject_update of this ModifyPlaybookVersionInfo.
        :type dataobject_update: bool
        """
        self._dataobject_update = dataobject_update

    @property
    def dataobject_delete(self):
        """Gets the dataobject_delete of this ModifyPlaybookVersionInfo.

        if trigger when dataobject is deleted

        :return: The dataobject_delete of this ModifyPlaybookVersionInfo.
        :rtype: bool
        """
        return self._dataobject_delete

    @dataobject_delete.setter
    def dataobject_delete(self, dataobject_delete):
        """Sets the dataobject_delete of this ModifyPlaybookVersionInfo.

        if trigger when dataobject is deleted

        :param dataobject_delete: The dataobject_delete of this ModifyPlaybookVersionInfo.
        :type dataobject_delete: bool
        """
        self._dataobject_delete = dataobject_delete

    @property
    def action_strategy(self):
        """Gets the action_strategy of this ModifyPlaybookVersionInfo.

        Strategy of action. sync or async

        :return: The action_strategy of this ModifyPlaybookVersionInfo.
        :rtype: str
        """
        return self._action_strategy

    @action_strategy.setter
    def action_strategy(self, action_strategy):
        """Sets the action_strategy of this ModifyPlaybookVersionInfo.

        Strategy of action. sync or async

        :param action_strategy: The action_strategy of this ModifyPlaybookVersionInfo.
        :type action_strategy: str
        """
        self._action_strategy = action_strategy

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
        if not isinstance(other, ModifyPlaybookVersionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
