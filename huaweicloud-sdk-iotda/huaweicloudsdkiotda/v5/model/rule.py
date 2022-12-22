# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


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
        'device_side': 'DeviceSide'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'condition_group': 'condition_group',
        'actions': 'actions',
        'rule_type': 'rule_type',
        'status': 'status',
        'app_id': 'app_id',
        'device_side': 'device_side'
    }

    def __init__(self, name=None, description=None, condition_group=None, actions=None, rule_type=None, status=None, app_id=None, device_side=None):
        """Rule

        The model defined in huaweicloud sdk

        :param name: **参数说明**：规则名称。
        :type name: str
        :param description: **参数说明**：规则的描述信息。
        :type description: str
        :param condition_group: 
        :type condition_group: :class:`huaweicloudsdkiotda.v5.ConditionGroup`
        :param actions: **参数说明**：规则的动作列表，单个规则最多支持设置10个动作。
        :type actions: list[:class:`huaweicloudsdkiotda.v5.RuleAction`]
        :param rule_type: **参数说明**：规则的类型。 **取值范围**： - DEVICE_LINKAGE：云端联动规则。  - DEVICE_SIDE：端侧规则。
        :type rule_type: str
        :param status: **参数说明**：规则的状态，默认值：active。 **取值范围**： - active：激活。 - inactive：未激活。
        :type status: str
        :param app_id: **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的规则归属到哪个资源空间下，否则创建的规则将会归属到[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type app_id: str
        :param device_side: 
        :type device_side: :class:`huaweicloudsdkiotda.v5.DeviceSide`
        """
        
        

        self._name = None
        self._description = None
        self._condition_group = None
        self._actions = None
        self._rule_type = None
        self._status = None
        self._app_id = None
        self._device_side = None
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
        if device_side is not None:
            self.device_side = device_side

    @property
    def name(self):
        """Gets the name of this Rule.

        **参数说明**：规则名称。

        :return: The name of this Rule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Rule.

        **参数说明**：规则名称。

        :param name: The name of this Rule.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this Rule.

        **参数说明**：规则的描述信息。

        :return: The description of this Rule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Rule.

        **参数说明**：规则的描述信息。

        :param description: The description of this Rule.
        :type description: str
        """
        self._description = description

    @property
    def condition_group(self):
        """Gets the condition_group of this Rule.

        :return: The condition_group of this Rule.
        :rtype: :class:`huaweicloudsdkiotda.v5.ConditionGroup`
        """
        return self._condition_group

    @condition_group.setter
    def condition_group(self, condition_group):
        """Sets the condition_group of this Rule.

        :param condition_group: The condition_group of this Rule.
        :type condition_group: :class:`huaweicloudsdkiotda.v5.ConditionGroup`
        """
        self._condition_group = condition_group

    @property
    def actions(self):
        """Gets the actions of this Rule.

        **参数说明**：规则的动作列表，单个规则最多支持设置10个动作。

        :return: The actions of this Rule.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.RuleAction`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this Rule.

        **参数说明**：规则的动作列表，单个规则最多支持设置10个动作。

        :param actions: The actions of this Rule.
        :type actions: list[:class:`huaweicloudsdkiotda.v5.RuleAction`]
        """
        self._actions = actions

    @property
    def rule_type(self):
        """Gets the rule_type of this Rule.

        **参数说明**：规则的类型。 **取值范围**： - DEVICE_LINKAGE：云端联动规则。  - DEVICE_SIDE：端侧规则。

        :return: The rule_type of this Rule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """Sets the rule_type of this Rule.

        **参数说明**：规则的类型。 **取值范围**： - DEVICE_LINKAGE：云端联动规则。  - DEVICE_SIDE：端侧规则。

        :param rule_type: The rule_type of this Rule.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def status(self):
        """Gets the status of this Rule.

        **参数说明**：规则的状态，默认值：active。 **取值范围**： - active：激活。 - inactive：未激活。

        :return: The status of this Rule.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Rule.

        **参数说明**：规则的状态，默认值：active。 **取值范围**： - active：激活。 - inactive：未激活。

        :param status: The status of this Rule.
        :type status: str
        """
        self._status = status

    @property
    def app_id(self):
        """Gets the app_id of this Rule.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的规则归属到哪个资源空间下，否则创建的规则将会归属到[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The app_id of this Rule.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this Rule.

        **参数说明**：资源空间ID。此参数为非必选参数，存在多资源空间的用户需要使用该接口时，建议携带该参数指定创建的规则归属到哪个资源空间下，否则创建的规则将会归属到[[默认资源空间](https://support.huaweicloud.com/usermanual-iothub/iot_01_0006.html#section0)](tag:hws)[[默认资源空间](https://support.huaweicloud.com/intl/zh-cn/usermanual-iothub/iot_01_0006.html#section0)](tag:hws_hk)下。 **取值范围**：长度不超过36，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param app_id: The app_id of this Rule.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def device_side(self):
        """Gets the device_side of this Rule.

        :return: The device_side of this Rule.
        :rtype: :class:`huaweicloudsdkiotda.v5.DeviceSide`
        """
        return self._device_side

    @device_side.setter
    def device_side(self, device_side):
        """Sets the device_side of this Rule.

        :param device_side: The device_side of this Rule.
        :type device_side: :class:`huaweicloudsdkiotda.v5.DeviceSide`
        """
        self._device_side = device_side

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
        if not isinstance(other, Rule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
