# coding: utf-8

import pprint
import re

import six





class Rule:


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
        'condition_group': 'ConditionGroup',
        'actions': 'list[RuleAction]',
        'rule_type': 'str',
        'status': 'str',
        'app_id': 'str',
        'edge_node_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'condition_group': 'condition_group',
        'actions': 'actions',
        'rule_type': 'rule_type',
        'status': 'status',
        'app_id': 'app_id',
        'edge_node_ids': 'edge_node_ids'
    }

    def __init__(self, name=None, description=None, condition_group=None, actions=None, rule_type=None, status=None, app_id=None, edge_node_ids=None):
        """Rule - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._description = None
        self._condition_group = None
        self._actions = None
        self._rule_type = None
        self._status = None
        self._app_id = None
        self._edge_node_ids = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.condition_group = condition_group
        self.actions = actions
        self.rule_type = rule_type
        if status is not None:
            self.status = status
        if app_id is not None:
            self.app_id = app_id
        if edge_node_ids is not None:
            self.edge_node_ids = edge_node_ids

    @property
    def name(self):
        """Gets the name of this Rule.

        规则名称。

        :return: The name of this Rule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rule.

        规则名称。

        :param name: The name of this Rule.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Rule.

        规则的描述信息。

        :return: The description of this Rule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rule.

        规则的描述信息。

        :param description: The description of this Rule.
        :type: str
        """
        self._description = description

    @property
    def condition_group(self):
        """Gets the condition_group of this Rule.


        :return: The condition_group of this Rule.
        :rtype: ConditionGroup
        """
        return self._condition_group

    @condition_group.setter
    def condition_group(self, condition_group):
        """Sets the condition_group of this Rule.


        :param condition_group: The condition_group of this Rule.
        :type: ConditionGroup
        """
        self._condition_group = condition_group

    @property
    def actions(self):
        """Gets the actions of this Rule.

        规则的动作列表，单个规则最多支持设置10个动作。

        :return: The actions of this Rule.
        :rtype: list[RuleAction]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Rule.

        规则的动作列表，单个规则最多支持设置10个动作。

        :param actions: The actions of this Rule.
        :type: list[RuleAction]
        """
        self._actions = actions

    @property
    def rule_type(self):
        """Gets the rule_type of this Rule.

        规则的类型 - DEVICE_LINKAGE：设备联动。 - DATA_FORWARDING：数据转发。 - EDGE：边缘侧。 

        :return: The rule_type of this Rule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this Rule.

        规则的类型 - DEVICE_LINKAGE：设备联动。 - DATA_FORWARDING：数据转发。 - EDGE：边缘侧。 

        :param rule_type: The rule_type of this Rule.
        :type: str
        """
        self._rule_type = rule_type

    @property
    def status(self):
        """Gets the status of this Rule.

        规则的状态，默认值：active。 - active：激活。 - inactive：未激活。 

        :return: The status of this Rule.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Rule.

        规则的状态，默认值：active。 - active：激活。 - inactive：未激活。 

        :param status: The status of this Rule.
        :type: str
        """
        self._status = status

    @property
    def app_id(self):
        """Gets the app_id of this Rule.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的规则归属到哪个资源空间下，否则创建的规则将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :return: The app_id of this Rule.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this Rule.

        资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的规则归属到哪个资源空间下，否则创建的规则将会归属到[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)下。

        :param app_id: The app_id of this Rule.
        :type: str
        """
        self._app_id = app_id

    @property
    def edge_node_ids(self):
        """Gets the edge_node_ids of this Rule.

        归属边缘侧节点设备ID列表。

        :return: The edge_node_ids of this Rule.
        :rtype: list[str]
        """
        return self._edge_node_ids

    @edge_node_ids.setter
    def edge_node_ids(self, edge_node_ids):
        """Sets the edge_node_ids of this Rule.

        归属边缘侧节点设备ID列表。

        :param edge_node_ids: The edge_node_ids of this Rule.
        :type: list[str]
        """
        self._edge_node_ids = edge_node_ids

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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
