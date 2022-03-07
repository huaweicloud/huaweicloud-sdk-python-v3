# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostAlarmsReqV2:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'namespace': 'str',
        'resource_group_id': 'str',
        'resources': 'list[list[Dimension]]',
        'policies': 'list[Policy]',
        'type': 'str',
        'alarm_actions': 'list[SMNAction]',
        'ok_actions': 'list[SMNAction]',
        'action_begin_time': 'str',
        'action_end_time': 'str',
        'enterprise_project_id': 'str',
        'enabled': 'bool',
        'action_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'namespace': 'namespace',
        'resource_group_id': 'resource_group_id',
        'resources': 'resources',
        'policies': 'policies',
        'type': 'type',
        'alarm_actions': 'alarm_actions',
        'ok_actions': 'ok_actions',
        'action_begin_time': 'action_begin_time',
        'action_end_time': 'action_end_time',
        'enterprise_project_id': 'enterprise_project_id',
        'enabled': 'enabled',
        'action_enabled': 'action_enabled'
    }

    def __init__(self, name=None, description=None, namespace=None, resource_group_id=None, resources=None, policies=None, type=None, alarm_actions=None, ok_actions=None, action_begin_time=None, action_end_time=None, enterprise_project_id=None, enabled=None, action_enabled=None):
        """PostAlarmsReqV2 - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._namespace = None
        self._resource_group_id = None
        self._resources = None
        self._policies = None
        self._type = None
        self._alarm_actions = None
        self._ok_actions = None
        self._action_begin_time = None
        self._action_end_time = None
        self._enterprise_project_id = None
        self._enabled = None
        self._action_enabled = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.namespace = namespace
        if resource_group_id is not None:
            self.resource_group_id = resource_group_id
        self.resources = resources
        self.policies = policies
        if type is not None:
            self.type = type
        if alarm_actions is not None:
            self.alarm_actions = alarm_actions
        if ok_actions is not None:
            self.ok_actions = ok_actions
        if action_begin_time is not None:
            self.action_begin_time = action_begin_time
        if action_end_time is not None:
            self.action_end_time = action_end_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.enabled = enabled
        self.action_enabled = action_enabled

    @property
    def name(self):
        """Gets the name of this PostAlarmsReqV2.

        告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :return: The name of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PostAlarmsReqV2.

        告警名称, 只能包含0-9/a-z/A-Z/_/-或汉字，长度1-128

        :param name: The name of this PostAlarmsReqV2.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this PostAlarmsReqV2.

        告警规则描述

        :return: The description of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PostAlarmsReqV2.

        告警规则描述

        :param description: The description of this PostAlarmsReqV2.
        :type: str
        """
        self._description = description

    @property
    def namespace(self):
        """Gets the namespace of this PostAlarmsReqV2.

        命名空间

        :return: The namespace of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this PostAlarmsReqV2.

        命名空间

        :param namespace: The namespace of this PostAlarmsReqV2.
        :type: str
        """
        self._namespace = namespace

    @property
    def resource_group_id(self):
        """Gets the resource_group_id of this PostAlarmsReqV2.

        资源分组ID

        :return: The resource_group_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._resource_group_id

    @resource_group_id.setter
    def resource_group_id(self, resource_group_id):
        """Sets the resource_group_id of this PostAlarmsReqV2.

        资源分组ID

        :param resource_group_id: The resource_group_id of this PostAlarmsReqV2.
        :type: str
        """
        self._resource_group_id = resource_group_id

    @property
    def resources(self):
        """Gets the resources of this PostAlarmsReqV2.

        资源信息

        :return: The resources of this PostAlarmsReqV2.
        :rtype: list[list[Dimension]]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this PostAlarmsReqV2.

        资源信息

        :param resources: The resources of this PostAlarmsReqV2.
        :type: list[list[Dimension]]
        """
        self._resources = resources

    @property
    def policies(self):
        """Gets the policies of this PostAlarmsReqV2.

        策略信息

        :return: The policies of this PostAlarmsReqV2.
        :rtype: list[Policy]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        """Sets the policies of this PostAlarmsReqV2.

        策略信息

        :param policies: The policies of this PostAlarmsReqV2.
        :type: list[Policy]
        """
        self._policies = policies

    @property
    def type(self):
        """Gets the type of this PostAlarmsReqV2.

        告警规则类型

        :return: The type of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PostAlarmsReqV2.

        告警规则类型

        :param type: The type of this PostAlarmsReqV2.
        :type: str
        """
        self._type = type

    @property
    def alarm_actions(self):
        """Gets the alarm_actions of this PostAlarmsReqV2.

        告警通知

        :return: The alarm_actions of this PostAlarmsReqV2.
        :rtype: list[SMNAction]
        """
        return self._alarm_actions

    @alarm_actions.setter
    def alarm_actions(self, alarm_actions):
        """Sets the alarm_actions of this PostAlarmsReqV2.

        告警通知

        :param alarm_actions: The alarm_actions of this PostAlarmsReqV2.
        :type: list[SMNAction]
        """
        self._alarm_actions = alarm_actions

    @property
    def ok_actions(self):
        """Gets the ok_actions of this PostAlarmsReqV2.

        告警恢复通知

        :return: The ok_actions of this PostAlarmsReqV2.
        :rtype: list[SMNAction]
        """
        return self._ok_actions

    @ok_actions.setter
    def ok_actions(self, ok_actions):
        """Sets the ok_actions of this PostAlarmsReqV2.

        告警恢复通知

        :param ok_actions: The ok_actions of this PostAlarmsReqV2.
        :type: list[SMNAction]
        """
        self._ok_actions = ok_actions

    @property
    def action_begin_time(self):
        """Gets the action_begin_time of this PostAlarmsReqV2.

        告警通知开始时间

        :return: The action_begin_time of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._action_begin_time

    @action_begin_time.setter
    def action_begin_time(self, action_begin_time):
        """Sets the action_begin_time of this PostAlarmsReqV2.

        告警通知开始时间

        :param action_begin_time: The action_begin_time of this PostAlarmsReqV2.
        :type: str
        """
        self._action_begin_time = action_begin_time

    @property
    def action_end_time(self):
        """Gets the action_end_time of this PostAlarmsReqV2.

        告警通知结束时间

        :return: The action_end_time of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._action_end_time

    @action_end_time.setter
    def action_end_time(self, action_end_time):
        """Sets the action_end_time of this PostAlarmsReqV2.

        告警通知结束时间

        :param action_end_time: The action_end_time of this PostAlarmsReqV2.
        :type: str
        """
        self._action_end_time = action_end_time

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this PostAlarmsReqV2.

        企业项目ID

        :return: The enterprise_project_id of this PostAlarmsReqV2.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this PostAlarmsReqV2.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this PostAlarmsReqV2.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def enabled(self):
        """Gets the enabled of this PostAlarmsReqV2.

        告警开关

        :return: The enabled of this PostAlarmsReqV2.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this PostAlarmsReqV2.

        告警开关

        :param enabled: The enabled of this PostAlarmsReqV2.
        :type: bool
        """
        self._enabled = enabled

    @property
    def action_enabled(self):
        """Gets the action_enabled of this PostAlarmsReqV2.

        告警通知开关

        :return: The action_enabled of this PostAlarmsReqV2.
        :rtype: bool
        """
        return self._action_enabled

    @action_enabled.setter
    def action_enabled(self, action_enabled):
        """Sets the action_enabled of this PostAlarmsReqV2.

        告警通知开关

        :param action_enabled: The action_enabled of this PostAlarmsReqV2.
        :type: bool
        """
        self._action_enabled = action_enabled

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
        if not isinstance(other, PostAlarmsReqV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
