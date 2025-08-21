# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdvancedIpsRuleVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'int',
        'ips_rule_id': 'str',
        'ips_rule_type': 'int',
        'param': 'str',
        'status': 'int'
    }

    attribute_map = {
        'action': 'action',
        'ips_rule_id': 'ips_rule_id',
        'ips_rule_type': 'ips_rule_type',
        'param': 'param',
        'status': 'status'
    }

    def __init__(self, action=None, ips_rule_id=None, ips_rule_type=None, param=None, status=None):
        r"""AdvancedIpsRuleVo

        The model defined in huaweicloud sdk

        :param action: 动作：0表示仅记录日志、1表示拦截session、2表示拦截ip
        :type action: int
        :param ips_rule_id: 高级ips规则id
        :type ips_rule_id: str
        :param ips_rule_type: ips规则类型：0表示敏感目录扫描、1表示反弹xshell
        :type ips_rule_type: int
        :param param: 包含特殊参数的JSON字符串
        :type param: str
        :param status: 开关状态：0表示关闭、1表示开启
        :type status: int
        """
        
        

        self._action = None
        self._ips_rule_id = None
        self._ips_rule_type = None
        self._param = None
        self._status = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if ips_rule_id is not None:
            self.ips_rule_id = ips_rule_id
        if ips_rule_type is not None:
            self.ips_rule_type = ips_rule_type
        if param is not None:
            self.param = param
        if status is not None:
            self.status = status

    @property
    def action(self):
        r"""Gets the action of this AdvancedIpsRuleVo.

        动作：0表示仅记录日志、1表示拦截session、2表示拦截ip

        :return: The action of this AdvancedIpsRuleVo.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AdvancedIpsRuleVo.

        动作：0表示仅记录日志、1表示拦截session、2表示拦截ip

        :param action: The action of this AdvancedIpsRuleVo.
        :type action: int
        """
        self._action = action

    @property
    def ips_rule_id(self):
        r"""Gets the ips_rule_id of this AdvancedIpsRuleVo.

        高级ips规则id

        :return: The ips_rule_id of this AdvancedIpsRuleVo.
        :rtype: str
        """
        return self._ips_rule_id

    @ips_rule_id.setter
    def ips_rule_id(self, ips_rule_id):
        r"""Sets the ips_rule_id of this AdvancedIpsRuleVo.

        高级ips规则id

        :param ips_rule_id: The ips_rule_id of this AdvancedIpsRuleVo.
        :type ips_rule_id: str
        """
        self._ips_rule_id = ips_rule_id

    @property
    def ips_rule_type(self):
        r"""Gets the ips_rule_type of this AdvancedIpsRuleVo.

        ips规则类型：0表示敏感目录扫描、1表示反弹xshell

        :return: The ips_rule_type of this AdvancedIpsRuleVo.
        :rtype: int
        """
        return self._ips_rule_type

    @ips_rule_type.setter
    def ips_rule_type(self, ips_rule_type):
        r"""Sets the ips_rule_type of this AdvancedIpsRuleVo.

        ips规则类型：0表示敏感目录扫描、1表示反弹xshell

        :param ips_rule_type: The ips_rule_type of this AdvancedIpsRuleVo.
        :type ips_rule_type: int
        """
        self._ips_rule_type = ips_rule_type

    @property
    def param(self):
        r"""Gets the param of this AdvancedIpsRuleVo.

        包含特殊参数的JSON字符串

        :return: The param of this AdvancedIpsRuleVo.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        r"""Sets the param of this AdvancedIpsRuleVo.

        包含特殊参数的JSON字符串

        :param param: The param of this AdvancedIpsRuleVo.
        :type param: str
        """
        self._param = param

    @property
    def status(self):
        r"""Gets the status of this AdvancedIpsRuleVo.

        开关状态：0表示关闭、1表示开启

        :return: The status of this AdvancedIpsRuleVo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AdvancedIpsRuleVo.

        开关状态：0表示关闭、1表示开启

        :param status: The status of this AdvancedIpsRuleVo.
        :type status: int
        """
        self._status = status

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
        if not isinstance(other, AdvancedIpsRuleVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
