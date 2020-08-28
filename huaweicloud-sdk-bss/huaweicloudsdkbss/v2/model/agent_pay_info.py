# coding: utf-8

import pprint
import re

import six





class AgentPayInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'is_agent_pay': 'int',
        'paying_agent_id': 'str'
    }

    attribute_map = {
        'is_agent_pay': 'is_agent_pay',
        'paying_agent_id': 'paying_agent_id'
    }

    def __init__(self, is_agent_pay=None, paying_agent_id=None):
        """AgentPayInfo - a model defined in huaweicloud sdk"""
        
        

        self._is_agent_pay = None
        self._paying_agent_id = None
        self.discriminator = None

        if is_agent_pay is not None:
            self.is_agent_pay = is_agent_pay
        if paying_agent_id is not None:
            self.paying_agent_id = paying_agent_id

    @property
    def is_agent_pay(self):
        """Gets the is_agent_pay of this AgentPayInfo.

        |参数名称：是否代付. 0, 租户自己支付;1，合作伙伴代付。如果是待支付状态，这个地方是表明是否申请了代付人支付，如果是已支付状态，是表明是不是由代付人支付。| |参数的约束及描述：支付类型. 0, 租户自己支付;1，合作伙伴代付。|

        :return: The is_agent_pay of this AgentPayInfo.
        :rtype: int
        """
        return self._is_agent_pay

    @is_agent_pay.setter
    def is_agent_pay(self, is_agent_pay):
        """Sets the is_agent_pay of this AgentPayInfo.

        |参数名称：是否代付. 0, 租户自己支付;1，合作伙伴代付。如果是待支付状态，这个地方是表明是否申请了代付人支付，如果是已支付状态，是表明是不是由代付人支付。| |参数的约束及描述：支付类型. 0, 租户自己支付;1，合作伙伴代付。|

        :param is_agent_pay: The is_agent_pay of this AgentPayInfo.
        :type: int
        """
        self._is_agent_pay = is_agent_pay

    @property
    def paying_agent_id(self):
        """Gets the paying_agent_id of this AgentPayInfo.

        |参数名称：代付人，当payingType=1的时候有值| |参数约束及描述：代付人，当payingType=1的时候有值|

        :return: The paying_agent_id of this AgentPayInfo.
        :rtype: str
        """
        return self._paying_agent_id

    @paying_agent_id.setter
    def paying_agent_id(self, paying_agent_id):
        """Sets the paying_agent_id of this AgentPayInfo.

        |参数名称：代付人，当payingType=1的时候有值| |参数约束及描述：代付人，当payingType=1的时候有值|

        :param paying_agent_id: The paying_agent_id of this AgentPayInfo.
        :type: str
        """
        self._paying_agent_id = paying_agent_id

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
        if not isinstance(other, AgentPayInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
