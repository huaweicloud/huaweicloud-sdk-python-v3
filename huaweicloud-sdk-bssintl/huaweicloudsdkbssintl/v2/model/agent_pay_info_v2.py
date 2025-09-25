# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentPayInfoV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'paying_agent_id': 'str',
        'is_agent_pay': 'bool'
    }

    attribute_map = {
        'paying_agent_id': 'paying_agent_id',
        'is_agent_pay': 'is_agent_pay'
    }

    def __init__(self, paying_agent_id=None, is_agent_pay=None):
        r"""AgentPayInfoV2

        The model defined in huaweicloud sdk

        :param paying_agent_id: |参数名称：订单代理支付人的客户账号ID。| |参数的约束及描述：订单代理支付人的客户账号ID|
        :type paying_agent_id: str
        :param is_agent_pay: |参数名称：是否代理支付。| |参数的约束及描述：是否代理支付。true：代理支付，不为ture时为非代理支付订单|
        :type is_agent_pay: bool
        """
        
        

        self._paying_agent_id = None
        self._is_agent_pay = None
        self.discriminator = None

        if paying_agent_id is not None:
            self.paying_agent_id = paying_agent_id
        if is_agent_pay is not None:
            self.is_agent_pay = is_agent_pay

    @property
    def paying_agent_id(self):
        r"""Gets the paying_agent_id of this AgentPayInfoV2.

        |参数名称：订单代理支付人的客户账号ID。| |参数的约束及描述：订单代理支付人的客户账号ID|

        :return: The paying_agent_id of this AgentPayInfoV2.
        :rtype: str
        """
        return self._paying_agent_id

    @paying_agent_id.setter
    def paying_agent_id(self, paying_agent_id):
        r"""Sets the paying_agent_id of this AgentPayInfoV2.

        |参数名称：订单代理支付人的客户账号ID。| |参数的约束及描述：订单代理支付人的客户账号ID|

        :param paying_agent_id: The paying_agent_id of this AgentPayInfoV2.
        :type paying_agent_id: str
        """
        self._paying_agent_id = paying_agent_id

    @property
    def is_agent_pay(self):
        r"""Gets the is_agent_pay of this AgentPayInfoV2.

        |参数名称：是否代理支付。| |参数的约束及描述：是否代理支付。true：代理支付，不为ture时为非代理支付订单|

        :return: The is_agent_pay of this AgentPayInfoV2.
        :rtype: bool
        """
        return self._is_agent_pay

    @is_agent_pay.setter
    def is_agent_pay(self, is_agent_pay):
        r"""Sets the is_agent_pay of this AgentPayInfoV2.

        |参数名称：是否代理支付。| |参数的约束及描述：是否代理支付。true：代理支付，不为ture时为非代理支付订单|

        :param is_agent_pay: The is_agent_pay of this AgentPayInfoV2.
        :type is_agent_pay: bool
        """
        self._is_agent_pay = is_agent_pay

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
        if not isinstance(other, AgentPayInfoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
