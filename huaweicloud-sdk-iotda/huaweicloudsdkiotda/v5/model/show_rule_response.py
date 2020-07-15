# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowRuleResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'rule_id': 'str',
        'name': 'str',
        'description': 'str',
        'condition_group': 'ConditionGroup',
        'actions': 'list[RuleAction]',
        'rule_type': 'str',
        'status': 'str',
        'app_id': 'str',
        'edge_node_ids': 'list[str]',
        'last_update_time': 'str'
    }

    attribute_map = {
        'rule_id': 'rule_id',
        'name': 'name',
        'description': 'description',
        'condition_group': 'condition_group',
        'actions': 'actions',
        'rule_type': 'rule_type',
        'status': 'status',
        'app_id': 'app_id',
        'edge_node_ids': 'edge_node_ids',
        'last_update_time': 'last_update_time'
    }

    def __init__(self, rule_id=None, name=None, description=None, condition_group=None, actions=None, rule_type=None, status=None, app_id=None, edge_node_ids=None, last_update_time=None):
        """ShowRuleResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._rule_id = None
        self._name = None
        self._description = None
        self._condition_group = None
        self._actions = None
        self._rule_type = None
        self._status = None
        self._app_id = None
        self._edge_node_ids = None
        self._last_update_time = None
        self.discriminator = None

        if rule_id is not None:
            self.rule_id = rule_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if condition_group is not None:
            self.condition_group = condition_group
        if actions is not None:
            self.actions = actions
        if rule_type is not None:
            self.rule_type = rule_type
        if status is not None:
            self.status = status
        if app_id is not None:
            self.app_id = app_id
        if edge_node_ids is not None:
            self.edge_node_ids = edge_node_ids
        if last_update_time is not None:
            self.last_update_time = last_update_time

    @property
    def rule_id(self):
        """Gets the rule_id of this ShowRuleResponse.

        规则id。

        :return: The rule_id of this ShowRuleResponse.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ShowRuleResponse.

        规则id。

        :param rule_id: The rule_id of this ShowRuleResponse.
        :type: str
        """
        self._rule_id = rule_id

    @property
    def name(self):
        """Gets the name of this ShowRuleResponse.

        规则名称。

        :return: The name of this ShowRuleResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowRuleResponse.

        规则名称。

        :param name: The name of this ShowRuleResponse.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowRuleResponse.

        规则的描述信息。

        :return: The description of this ShowRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowRuleResponse.

        规则的描述信息。

        :param description: The description of this ShowRuleResponse.
        :type: str
        """
        self._description = description

    @property
    def condition_group(self):
        """Gets the condition_group of this ShowRuleResponse.


        :return: The condition_group of this ShowRuleResponse.
        :rtype: ConditionGroup
        """
        return self._condition_group

    @condition_group.setter
    def condition_group(self, condition_group):
        """Sets the condition_group of this ShowRuleResponse.


        :param condition_group: The condition_group of this ShowRuleResponse.
        :type: ConditionGroup
        """
        self._condition_group = condition_group

    @property
    def actions(self):
        """Gets the actions of this ShowRuleResponse.

        规则的动作列表，单个规则最多支持设置10个动作。

        :return: The actions of this ShowRuleResponse.
        :rtype: list[RuleAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ShowRuleResponse.

        规则的动作列表，单个规则最多支持设置10个动作。

        :param actions: The actions of this ShowRuleResponse.
        :type: list[RuleAction]
        """
        self._actions = actions

    @property
    def rule_type(self):
        """Gets the rule_type of this ShowRuleResponse.

        规则的类型 - DEVICE_LINKAGE：设备联动。 - DATA_FORWARDING：数据转发。 - EDGE：边缘侧。 

        :return: The rule_type of this ShowRuleResponse.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this ShowRuleResponse.

        规则的类型 - DEVICE_LINKAGE：设备联动。 - DATA_FORWARDING：数据转发。 - EDGE：边缘侧。 

        :param rule_type: The rule_type of this ShowRuleResponse.
        :type: str
        """
        self._rule_type = rule_type

    @property
    def status(self):
        """Gets the status of this ShowRuleResponse.

        规则的状态，默认值：active。 - active：激活。 - inactive：未激活。 

        :return: The status of this ShowRuleResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowRuleResponse.

        规则的状态，默认值：active。 - active：激活。 - inactive：未激活。 

        :param status: The status of this ShowRuleResponse.
        :type: str
        """
        self._status = status

    @property
    def app_id(self):
        """Gets the app_id of this ShowRuleResponse.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的规则归属到哪个资源空间下，否则创建的规则将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :return: The app_id of this ShowRuleResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ShowRuleResponse.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的规则归属到哪个资源空间下，否则创建的规则将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :param app_id: The app_id of this ShowRuleResponse.
        :type: str
        """
        self._app_id = app_id

    @property
    def edge_node_ids(self):
        """Gets the edge_node_ids of this ShowRuleResponse.

        归属边缘侧节点设备ID列表。

        :return: The edge_node_ids of this ShowRuleResponse.
        :rtype: list[str]
        """
        return self._edge_node_ids

    @edge_node_ids.setter
    def edge_node_ids(self, edge_node_ids):
        """Sets the edge_node_ids of this ShowRuleResponse.

        归属边缘侧节点设备ID列表。

        :param edge_node_ids: The edge_node_ids of this ShowRuleResponse.
        :type: list[str]
        """
        self._edge_node_ids = edge_node_ids

    @property
    def last_update_time(self):
        """Gets the last_update_time of this ShowRuleResponse.

        规则最后更新时间，使用UTC时区，格式：yyyyMMdd'T'HHmmss'Z'。

        :return: The last_update_time of this ShowRuleResponse.
        :rtype: str
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this ShowRuleResponse.

        规则最后更新时间，使用UTC时区，格式：yyyyMMdd'T'HHmmss'Z'。

        :param last_update_time: The last_update_time of this ShowRuleResponse.
        :type: str
        """
        self._last_update_time = last_update_time

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
