# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventAttackTagResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attack_success_num': 'int',
        'attack_attempt_num': 'int',
        'attack_blocked_num': 'int',
        'abnormal_behavior_num': 'int',
        'collapsible_host_num': 'int',
        'system_vulnerability_num': 'int'
    }

    attribute_map = {
        'attack_success_num': 'attack_success_num',
        'attack_attempt_num': 'attack_attempt_num',
        'attack_blocked_num': 'attack_blocked_num',
        'abnormal_behavior_num': 'abnormal_behavior_num',
        'collapsible_host_num': 'collapsible_host_num',
        'system_vulnerability_num': 'system_vulnerability_num'
    }

    def __init__(self, attack_success_num=None, attack_attempt_num=None, attack_blocked_num=None, abnormal_behavior_num=None, collapsible_host_num=None, system_vulnerability_num=None):
        r"""ShowEventAttackTagResponse

        The model defined in huaweicloud sdk

        :param attack_success_num: **参数解释**: 攻击成功阶段的数量 **取值范围**: 最小值0，最大值2147483647 
        :type attack_success_num: int
        :param attack_attempt_num: **参数解释**: 攻击尝试阶段的数量 **取值范围**: 最小值0，最大值2147483647 
        :type attack_attempt_num: int
        :param attack_blocked_num: **参数解释**: 攻击被阻断阶段的数量 **取值范围**: 最小值0，最大值2147483647 
        :type attack_blocked_num: int
        :param abnormal_behavior_num: **参数解释**: 异常行为阶段的数量 **取值范围**: 最小值0，最大值2147483647 
        :type abnormal_behavior_num: int
        :param collapsible_host_num: **参数解释**: 主机失陷阶段的数量 **取值范围**: 最小值0，最大值2147483647 
        :type collapsible_host_num: int
        :param system_vulnerability_num: **参数解释**: 系统脆弱性阶段的数量 **取值范围**: 最小值0，最大值2147483647 
        :type system_vulnerability_num: int
        """
        
        super(ShowEventAttackTagResponse, self).__init__()

        self._attack_success_num = None
        self._attack_attempt_num = None
        self._attack_blocked_num = None
        self._abnormal_behavior_num = None
        self._collapsible_host_num = None
        self._system_vulnerability_num = None
        self.discriminator = None

        if attack_success_num is not None:
            self.attack_success_num = attack_success_num
        if attack_attempt_num is not None:
            self.attack_attempt_num = attack_attempt_num
        if attack_blocked_num is not None:
            self.attack_blocked_num = attack_blocked_num
        if abnormal_behavior_num is not None:
            self.abnormal_behavior_num = abnormal_behavior_num
        if collapsible_host_num is not None:
            self.collapsible_host_num = collapsible_host_num
        if system_vulnerability_num is not None:
            self.system_vulnerability_num = system_vulnerability_num

    @property
    def attack_success_num(self):
        r"""Gets the attack_success_num of this ShowEventAttackTagResponse.

        **参数解释**: 攻击成功阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The attack_success_num of this ShowEventAttackTagResponse.
        :rtype: int
        """
        return self._attack_success_num

    @attack_success_num.setter
    def attack_success_num(self, attack_success_num):
        r"""Sets the attack_success_num of this ShowEventAttackTagResponse.

        **参数解释**: 攻击成功阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :param attack_success_num: The attack_success_num of this ShowEventAttackTagResponse.
        :type attack_success_num: int
        """
        self._attack_success_num = attack_success_num

    @property
    def attack_attempt_num(self):
        r"""Gets the attack_attempt_num of this ShowEventAttackTagResponse.

        **参数解释**: 攻击尝试阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The attack_attempt_num of this ShowEventAttackTagResponse.
        :rtype: int
        """
        return self._attack_attempt_num

    @attack_attempt_num.setter
    def attack_attempt_num(self, attack_attempt_num):
        r"""Sets the attack_attempt_num of this ShowEventAttackTagResponse.

        **参数解释**: 攻击尝试阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :param attack_attempt_num: The attack_attempt_num of this ShowEventAttackTagResponse.
        :type attack_attempt_num: int
        """
        self._attack_attempt_num = attack_attempt_num

    @property
    def attack_blocked_num(self):
        r"""Gets the attack_blocked_num of this ShowEventAttackTagResponse.

        **参数解释**: 攻击被阻断阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The attack_blocked_num of this ShowEventAttackTagResponse.
        :rtype: int
        """
        return self._attack_blocked_num

    @attack_blocked_num.setter
    def attack_blocked_num(self, attack_blocked_num):
        r"""Sets the attack_blocked_num of this ShowEventAttackTagResponse.

        **参数解释**: 攻击被阻断阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :param attack_blocked_num: The attack_blocked_num of this ShowEventAttackTagResponse.
        :type attack_blocked_num: int
        """
        self._attack_blocked_num = attack_blocked_num

    @property
    def abnormal_behavior_num(self):
        r"""Gets the abnormal_behavior_num of this ShowEventAttackTagResponse.

        **参数解释**: 异常行为阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The abnormal_behavior_num of this ShowEventAttackTagResponse.
        :rtype: int
        """
        return self._abnormal_behavior_num

    @abnormal_behavior_num.setter
    def abnormal_behavior_num(self, abnormal_behavior_num):
        r"""Sets the abnormal_behavior_num of this ShowEventAttackTagResponse.

        **参数解释**: 异常行为阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :param abnormal_behavior_num: The abnormal_behavior_num of this ShowEventAttackTagResponse.
        :type abnormal_behavior_num: int
        """
        self._abnormal_behavior_num = abnormal_behavior_num

    @property
    def collapsible_host_num(self):
        r"""Gets the collapsible_host_num of this ShowEventAttackTagResponse.

        **参数解释**: 主机失陷阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The collapsible_host_num of this ShowEventAttackTagResponse.
        :rtype: int
        """
        return self._collapsible_host_num

    @collapsible_host_num.setter
    def collapsible_host_num(self, collapsible_host_num):
        r"""Sets the collapsible_host_num of this ShowEventAttackTagResponse.

        **参数解释**: 主机失陷阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :param collapsible_host_num: The collapsible_host_num of this ShowEventAttackTagResponse.
        :type collapsible_host_num: int
        """
        self._collapsible_host_num = collapsible_host_num

    @property
    def system_vulnerability_num(self):
        r"""Gets the system_vulnerability_num of this ShowEventAttackTagResponse.

        **参数解释**: 系统脆弱性阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :return: The system_vulnerability_num of this ShowEventAttackTagResponse.
        :rtype: int
        """
        return self._system_vulnerability_num

    @system_vulnerability_num.setter
    def system_vulnerability_num(self, system_vulnerability_num):
        r"""Sets the system_vulnerability_num of this ShowEventAttackTagResponse.

        **参数解释**: 系统脆弱性阶段的数量 **取值范围**: 最小值0，最大值2147483647 

        :param system_vulnerability_num: The system_vulnerability_num of this ShowEventAttackTagResponse.
        :type system_vulnerability_num: int
        """
        self._system_vulnerability_num = system_vulnerability_num

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
        if not isinstance(other, ShowEventAttackTagResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
