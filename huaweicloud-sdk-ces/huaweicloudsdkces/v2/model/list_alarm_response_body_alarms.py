# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAlarmResponseBodyAlarms:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'alarm_id': 'str',
        'name': 'str',
        'description': 'str',
        'namespace': 'str',
        'policies': 'list[Policy]',
        'resources': 'list[ResourcesInListResp]',
        'type': 'str',
        'enabled': 'bool',
        'action_enabled': 'bool',
        'alarm_actions': 'list[SMNAction]',
        'ok_actions': 'list[SMNAction]',
        'insufficientdata_actions': 'list[SMNAction]',
        'action_begin_time': 'str',
        'action_end_time': 'str',
        'update_time': 'str',
        'one_click_alarm_flag': 'int',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'alarm_id': 'alarm_id',
        'name': 'name',
        'description': 'description',
        'namespace': 'namespace',
        'policies': 'policies',
        'resources': 'resources',
        'type': 'type',
        'enabled': 'enabled',
        'action_enabled': 'action_enabled',
        'alarm_actions': 'alarm_actions',
        'ok_actions': 'ok_actions',
        'insufficientdata_actions': 'insufficientdata_actions',
        'action_begin_time': 'action_begin_time',
        'action_end_time': 'action_end_time',
        'update_time': 'update_time',
        'one_click_alarm_flag': 'one_click_alarm_flag',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, alarm_id=None, name=None, description=None, namespace=None, policies=None, resources=None, type=None, enabled=None, action_enabled=None, alarm_actions=None, ok_actions=None, insufficientdata_actions=None, action_begin_time=None, action_end_time=None, update_time=None, one_click_alarm_flag=None, enterprise_project_id=None):
        """ListAlarmResponseBodyAlarms - a model defined in huaweicloud sdk"""
        
        

        self._alarm_id = None
        self._name = None
        self._description = None
        self._namespace = None
        self._policies = None
        self._resources = None
        self._type = None
        self._enabled = None
        self._action_enabled = None
        self._alarm_actions = None
        self._ok_actions = None
        self._insufficientdata_actions = None
        self._action_begin_time = None
        self._action_end_time = None
        self._update_time = None
        self._one_click_alarm_flag = None
        self._enterprise_project_id = None
        self.discriminator = None

        if alarm_id is not None:
            self.alarm_id = alarm_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if namespace is not None:
            self.namespace = namespace
        if policies is not None:
            self.policies = policies
        if resources is not None:
            self.resources = resources
        if type is not None:
            self.type = type
        if enabled is not None:
            self.enabled = enabled
        if action_enabled is not None:
            self.action_enabled = action_enabled
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if insufficientdata_actions is not None:
            self.insufficientdata_actions = insufficientdata_actions
        if action_begin_time is not None:
            self.action_begin_time = action_begin_time
        if action_end_time is not None:
            self.action_end_time = action_end_time
        if update_time is not None:
            self.update_time = update_time
        if one_click_alarm_flag is not None:
            self.one_click_alarm_flag = one_click_alarm_flag
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def alarm_id(self):
        """Gets the alarm_id of this ListAlarmResponseBodyAlarms.

        告警规则ID

        :return: The alarm_id of this ListAlarmResponseBodyAlarms.
        :rtype: str
        """
        return self._alarm_id

    @alarm_id.setter
    def alarm_id(self, alarm_id):
        """Sets the alarm_id of this ListAlarmResponseBodyAlarms.

        告警规则ID

        :param alarm_id: The alarm_id of this ListAlarmResponseBodyAlarms.
        :type: str
        """
        self._alarm_id = alarm_id

    @property
    def name(self):
        """Gets the name of this ListAlarmResponseBodyAlarms.

        告警规则名称

        :return: The name of this ListAlarmResponseBodyAlarms.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListAlarmResponseBodyAlarms.

        告警规则名称

        :param name: The name of this ListAlarmResponseBodyAlarms.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ListAlarmResponseBodyAlarms.

        告警规则描述

        :return: The description of this ListAlarmResponseBodyAlarms.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ListAlarmResponseBodyAlarms.

        告警规则描述

        :param description: The description of this ListAlarmResponseBodyAlarms.
        :type: str
        """
        self._description = description

    @property
    def namespace(self):
        """Gets the namespace of this ListAlarmResponseBodyAlarms.

        告警规则的命名空间

        :return: The namespace of this ListAlarmResponseBodyAlarms.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListAlarmResponseBodyAlarms.

        告警规则的命名空间

        :param namespace: The namespace of this ListAlarmResponseBodyAlarms.
        :type: str
        """
        self._namespace = namespace

    @property
    def policies(self):
        """Gets the policies of this ListAlarmResponseBodyAlarms.

        策略

        :return: The policies of this ListAlarmResponseBodyAlarms.
        :rtype: list[Policy]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this ListAlarmResponseBodyAlarms.

        策略

        :param policies: The policies of this ListAlarmResponseBodyAlarms.
        :type: list[Policy]
        """
        self._policies = policies

    @property
    def resources(self):
        """Gets the resources of this ListAlarmResponseBodyAlarms.

        资源

        :return: The resources of this ListAlarmResponseBodyAlarms.
        :rtype: list[ResourcesInListResp]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ListAlarmResponseBodyAlarms.

        资源

        :param resources: The resources of this ListAlarmResponseBodyAlarms.
        :type: list[ResourcesInListResp]
        """
        self._resources = resources

    @property
    def type(self):
        """Gets the type of this ListAlarmResponseBodyAlarms.

        告警类型

        :return: The type of this ListAlarmResponseBodyAlarms.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListAlarmResponseBodyAlarms.

        告警类型

        :param type: The type of this ListAlarmResponseBodyAlarms.
        :type: str
        """
        self._type = type

    @property
    def enabled(self):
        """Gets the enabled of this ListAlarmResponseBodyAlarms.

        告警开关

        :return: The enabled of this ListAlarmResponseBodyAlarms.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ListAlarmResponseBodyAlarms.

        告警开关

        :param enabled: The enabled of this ListAlarmResponseBodyAlarms.
        :type: bool
        """
        self._enabled = enabled

    @property
    def action_enabled(self):
        """Gets the action_enabled of this ListAlarmResponseBodyAlarms.

        告警通知开关

        :return: The action_enabled of this ListAlarmResponseBodyAlarms.
        :rtype: bool
        """
        return self._action_enabled

    @action_enabled.setter
    def action_enabled(self, action_enabled):
        """Sets the action_enabled of this ListAlarmResponseBodyAlarms.

        告警通知开关

        :param action_enabled: The action_enabled of this ListAlarmResponseBodyAlarms.
        :type: bool
        """
        self._action_enabled = action_enabled

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this ListAlarmResponseBodyAlarms.

        告警通知

        :return: The alarm_actions of this ListAlarmResponseBodyAlarms.
        :rtype: list[SMNAction]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this ListAlarmResponseBodyAlarms.

        告警通知

        :param alarm_actions: The alarm_actions of this ListAlarmResponseBodyAlarms.
        :type: list[SMNAction]
        """
        self._alarm_actions = alarm_actions

    @property
    def ok_actions(self):
        """Gets the ok_actions of this ListAlarmResponseBodyAlarms.

        告警恢复通知

        :return: The ok_actions of this ListAlarmResponseBodyAlarms.
        :rtype: list[SMNAction]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this ListAlarmResponseBodyAlarms.

        告警恢复通知

        :param ok_actions: The ok_actions of this ListAlarmResponseBodyAlarms.
        :type: list[SMNAction]
        """
        self._ok_actions = ok_actions

    @property
    def insufficientdata_actions(self):
        """Gets the insufficientdata_actions of this ListAlarmResponseBodyAlarms.

        数据不足通知

        :return: The insufficientdata_actions of this ListAlarmResponseBodyAlarms.
        :rtype: list[SMNAction]
        """
        return self._insufficientdata_actions

    @insufficientdata_actions.setter
    def insufficientdata_actions(self, insufficientdata_actions):
        """Sets the insufficientdata_actions of this ListAlarmResponseBodyAlarms.

        数据不足通知

        :param insufficientdata_actions: The insufficientdata_actions of this ListAlarmResponseBodyAlarms.
        :type: list[SMNAction]
        """
        self._insufficientdata_actions = insufficientdata_actions

    @property
    def action_begin_time(self):
        """Gets the action_begin_time of this ListAlarmResponseBodyAlarms.

        告警通知起始时间

        :return: The action_begin_time of this ListAlarmResponseBodyAlarms.
        :rtype: str
        """
        return self._action_begin_time

    @action_begin_time.setter
    def action_begin_time(self, action_begin_time):
        """Sets the action_begin_time of this ListAlarmResponseBodyAlarms.

        告警通知起始时间

        :param action_begin_time: The action_begin_time of this ListAlarmResponseBodyAlarms.
        :type: str
        """
        self._action_begin_time = action_begin_time

    @property
    def action_end_time(self):
        """Gets the action_end_time of this ListAlarmResponseBodyAlarms.

        告警通知结束时间

        :return: The action_end_time of this ListAlarmResponseBodyAlarms.
        :rtype: str
        """
        return self._action_end_time

    @action_end_time.setter
    def action_end_time(self, action_end_time):
        """Sets the action_end_time of this ListAlarmResponseBodyAlarms.

        告警通知结束时间

        :param action_end_time: The action_end_time of this ListAlarmResponseBodyAlarms.
        :type: str
        """
        self._action_end_time = action_end_time

    @property
    def update_time(self):
        """Gets the update_time of this ListAlarmResponseBodyAlarms.

        告警更新时间，参考API规范，使用UTC时间

        :return: The update_time of this ListAlarmResponseBodyAlarms.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ListAlarmResponseBodyAlarms.

        告警更新时间，参考API规范，使用UTC时间

        :param update_time: The update_time of this ListAlarmResponseBodyAlarms.
        :type: str
        """
        self._update_time = update_time

    @property
    def one_click_alarm_flag(self):
        """Gets the one_click_alarm_flag of this ListAlarmResponseBodyAlarms.

        一键告警标志

        :return: The one_click_alarm_flag of this ListAlarmResponseBodyAlarms.
        :rtype: int
        """
        return self._one_click_alarm_flag

    @one_click_alarm_flag.setter
    def one_click_alarm_flag(self, one_click_alarm_flag):
        """Sets the one_click_alarm_flag of this ListAlarmResponseBodyAlarms.

        一键告警标志

        :param one_click_alarm_flag: The one_click_alarm_flag of this ListAlarmResponseBodyAlarms.
        :type: int
        """
        self._one_click_alarm_flag = one_click_alarm_flag

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListAlarmResponseBodyAlarms.

        企业项目ID

        :return: The enterprise_project_id of this ListAlarmResponseBodyAlarms.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListAlarmResponseBodyAlarms.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListAlarmResponseBodyAlarms.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListAlarmResponseBodyAlarms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
