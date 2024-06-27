# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityPolciesActionDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'action': 'str',
        'rule_ids': 'list[str]'
    }

    attribute_map = {
        'object_id': 'object_id',
        'action': 'action',
        'rule_ids': 'rule_ids'
    }

    def __init__(self, object_id=None, action=None, rule_ids=None):
        """UpdateSecurityPolciesActionDto

        The model defined in huaweicloud sdk

        :param object_id: 防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。
        :type object_id: str
        :param action: 动作
        :type action: str
        :param rule_ids: 规则ID列表
        :type rule_ids: list[str]
        """
        
        

        self._object_id = None
        self._action = None
        self._rule_ids = None
        self.discriminator = None

        self.object_id = object_id
        self.action = action
        self.rule_ids = rule_ids

    @property
    def object_id(self):
        """Gets the object_id of this UpdateSecurityPolciesActionDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。

        :return: The object_id of this UpdateSecurityPolciesActionDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this UpdateSecurityPolciesActionDto.

        防护对象id，是创建云防火墙后用于区分互联网边界防护和VPC边界防护的标志id，可通过调用[查询防火墙实例接口](ListFirewallDetail.xml)，注意type为0的为互联网边界防护对象id，type为1的为VPC边界防护对象id。

        :param object_id: The object_id of this UpdateSecurityPolciesActionDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def action(self):
        """Gets the action of this UpdateSecurityPolciesActionDto.

        动作

        :return: The action of this UpdateSecurityPolciesActionDto.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateSecurityPolciesActionDto.

        动作

        :param action: The action of this UpdateSecurityPolciesActionDto.
        :type action: str
        """
        self._action = action

    @property
    def rule_ids(self):
        """Gets the rule_ids of this UpdateSecurityPolciesActionDto.

        规则ID列表

        :return: The rule_ids of this UpdateSecurityPolciesActionDto.
        :rtype: list[str]
        """
        return self._rule_ids

    @rule_ids.setter
    def rule_ids(self, rule_ids):
        """Sets the rule_ids of this UpdateSecurityPolciesActionDto.

        规则ID列表

        :param rule_ids: The rule_ids of this UpdateSecurityPolciesActionDto.
        :type rule_ids: list[str]
        """
        self._rule_ids = rule_ids

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
        if not isinstance(other, UpdateSecurityPolciesActionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
