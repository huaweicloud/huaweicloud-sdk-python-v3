# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'policy_name': 'str',
        'os_type': 'str',
        'host_num': 'int',
        'rule_name': 'str'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'os_type': 'os_type',
        'host_num': 'host_num',
        'rule_name': 'rule_name'
    }

    def __init__(self, policy_id=None, policy_name=None, os_type=None, host_num=None, rule_name=None):
        r"""PolicyInfo

        The model defined in huaweicloud sdk

        :param policy_id: 策略ID
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param os_type: 操作系统类型
        :type os_type: str
        :param host_num: 关联服务器数
        :type host_num: int
        :param rule_name: 检测特性规则名称，中间以逗号隔开
        :type rule_name: str
        """
        
        

        self._policy_id = None
        self._policy_name = None
        self._os_type = None
        self._host_num = None
        self._rule_name = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if os_type is not None:
            self.os_type = os_type
        if host_num is not None:
            self.host_num = host_num
        if rule_name is not None:
            self.rule_name = rule_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this PolicyInfo.

        策略ID

        :return: The policy_id of this PolicyInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this PolicyInfo.

        策略ID

        :param policy_id: The policy_id of this PolicyInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this PolicyInfo.

        策略名称

        :return: The policy_name of this PolicyInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this PolicyInfo.

        策略名称

        :param policy_name: The policy_name of this PolicyInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def os_type(self):
        r"""Gets the os_type of this PolicyInfo.

        操作系统类型

        :return: The os_type of this PolicyInfo.
        :rtype: str
        """
        return self._os_type

    @os_type.setter
    def os_type(self, os_type):
        r"""Sets the os_type of this PolicyInfo.

        操作系统类型

        :param os_type: The os_type of this PolicyInfo.
        :type os_type: str
        """
        self._os_type = os_type

    @property
    def host_num(self):
        r"""Gets the host_num of this PolicyInfo.

        关联服务器数

        :return: The host_num of this PolicyInfo.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this PolicyInfo.

        关联服务器数

        :param host_num: The host_num of this PolicyInfo.
        :type host_num: int
        """
        self._host_num = host_num

    @property
    def rule_name(self):
        r"""Gets the rule_name of this PolicyInfo.

        检测特性规则名称，中间以逗号隔开

        :return: The rule_name of this PolicyInfo.
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        r"""Sets the rule_name of this PolicyInfo.

        检测特性规则名称，中间以逗号隔开

        :param rule_name: The rule_name of this PolicyInfo.
        :type rule_name: str
        """
        self._rule_name = rule_name

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
        if not isinstance(other, PolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
