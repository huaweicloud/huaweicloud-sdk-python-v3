# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AdvancedIpsRuleDto:

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
        'object_id': 'str',
        'param': 'str',
        'status': 'int'
    }

    attribute_map = {
        'action': 'action',
        'ips_rule_id': 'ips_rule_id',
        'ips_rule_type': 'ips_rule_type',
        'object_id': 'object_id',
        'param': 'param',
        'status': 'status'
    }

    def __init__(self, action=None, ips_rule_id=None, ips_rule_type=None, object_id=None, param=None, status=None):
        r"""AdvancedIpsRuleDto

        The model defined in huaweicloud sdk

        :param action: 动作：0表示仅记录日志、1表示拦截session、2表示拦截ip
        :type action: int
        :param ips_rule_id: 高级ips规则id
        :type ips_rule_id: str
        :param ips_rule_type: ips规则类型：0表示敏感目录扫描、1表示反弹xshell
        :type ips_rule_type: int
        :param object_id: 防护对象id
        :type object_id: str
        :param param: 包含特殊参数的JSON字符串
        :type param: str
        :param status: 开关状态：0表示关闭、1表示开启
        :type status: int
        """
        
        

        self._action = None
        self._ips_rule_id = None
        self._ips_rule_type = None
        self._object_id = None
        self._param = None
        self._status = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if ips_rule_id is not None:
            self.ips_rule_id = ips_rule_id
        if ips_rule_type is not None:
            self.ips_rule_type = ips_rule_type
        if object_id is not None:
            self.object_id = object_id
        if param is not None:
            self.param = param
        if status is not None:
            self.status = status

    @property
    def action(self):
        r"""Gets the action of this AdvancedIpsRuleDto.

        动作：0表示仅记录日志、1表示拦截session、2表示拦截ip

        :return: The action of this AdvancedIpsRuleDto.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AdvancedIpsRuleDto.

        动作：0表示仅记录日志、1表示拦截session、2表示拦截ip

        :param action: The action of this AdvancedIpsRuleDto.
        :type action: int
        """
        self._action = action

    @property
    def ips_rule_id(self):
        r"""Gets the ips_rule_id of this AdvancedIpsRuleDto.

        高级ips规则id

        :return: The ips_rule_id of this AdvancedIpsRuleDto.
        :rtype: str
        """
        return self._ips_rule_id

    @ips_rule_id.setter
    def ips_rule_id(self, ips_rule_id):
        r"""Sets the ips_rule_id of this AdvancedIpsRuleDto.

        高级ips规则id

        :param ips_rule_id: The ips_rule_id of this AdvancedIpsRuleDto.
        :type ips_rule_id: str
        """
        self._ips_rule_id = ips_rule_id

    @property
    def ips_rule_type(self):
        r"""Gets the ips_rule_type of this AdvancedIpsRuleDto.

        ips规则类型：0表示敏感目录扫描、1表示反弹xshell

        :return: The ips_rule_type of this AdvancedIpsRuleDto.
        :rtype: int
        """
        return self._ips_rule_type

    @ips_rule_type.setter
    def ips_rule_type(self, ips_rule_type):
        r"""Sets the ips_rule_type of this AdvancedIpsRuleDto.

        ips规则类型：0表示敏感目录扫描、1表示反弹xshell

        :param ips_rule_type: The ips_rule_type of this AdvancedIpsRuleDto.
        :type ips_rule_type: int
        """
        self._ips_rule_type = ips_rule_type

    @property
    def object_id(self):
        r"""Gets the object_id of this AdvancedIpsRuleDto.

        防护对象id

        :return: The object_id of this AdvancedIpsRuleDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this AdvancedIpsRuleDto.

        防护对象id

        :param object_id: The object_id of this AdvancedIpsRuleDto.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def param(self):
        r"""Gets the param of this AdvancedIpsRuleDto.

        包含特殊参数的JSON字符串

        :return: The param of this AdvancedIpsRuleDto.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        r"""Sets the param of this AdvancedIpsRuleDto.

        包含特殊参数的JSON字符串

        :param param: The param of this AdvancedIpsRuleDto.
        :type param: str
        """
        self._param = param

    @property
    def status(self):
        r"""Gets the status of this AdvancedIpsRuleDto.

        开关状态：0表示关闭、1表示开启

        :return: The status of this AdvancedIpsRuleDto.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AdvancedIpsRuleDto.

        开关状态：0表示关闭、1表示开启

        :param status: The status of this AdvancedIpsRuleDto.
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
        if not isinstance(other, AdvancedIpsRuleDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
