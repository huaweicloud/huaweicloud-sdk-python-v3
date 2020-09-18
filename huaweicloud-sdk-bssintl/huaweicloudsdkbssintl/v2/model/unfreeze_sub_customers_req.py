# coding: utf-8

import pprint
import re

import six





class UnfreezeSubCustomersReq:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customer_ids': 'list[str]',
        'reason': 'str'
    }

    attribute_map = {
        'customer_ids': 'customer_ids',
        'reason': 'reason'
    }

    def __init__(self, customer_ids=None, reason=None):
        """UnfreezeSubCustomersReq - a model defined in huaweicloud sdk"""
        
        

        self._customer_ids = None
        self._reason = None
        self.discriminator = None

        self.customer_ids = customer_ids
        self.reason = reason

    @property
    def customer_ids(self):
        """Gets the customer_ids of this UnfreezeSubCustomersReq.

        |参数名称：需要解冻的客户ID列表。| |参数约束以及描述：需要解冻的客户ID列表。|

        :return: The customer_ids of this UnfreezeSubCustomersReq.
        :rtype: list[str]
        """
        return self._customer_ids

    @customer_ids.setter
    def customer_ids(self, customer_ids):
        """Sets the customer_ids of this UnfreezeSubCustomersReq.

        |参数名称：需要解冻的客户ID列表。| |参数约束以及描述：需要解冻的客户ID列表。|

        :param customer_ids: The customer_ids of this UnfreezeSubCustomersReq.
        :type: list[str]
        """
        self._customer_ids = customer_ids

    @property
    def reason(self):
        """Gets the reason of this UnfreezeSubCustomersReq.

        |参数名称：解冻原因。| |参数约束及描述：解冻原因。|

        :return: The reason of this UnfreezeSubCustomersReq.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this UnfreezeSubCustomersReq.

        |参数名称：解冻原因。| |参数约束及描述：解冻原因。|

        :param reason: The reason of this UnfreezeSubCustomersReq.
        :type: str
        """
        self._reason = reason

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
        if not isinstance(other, UnfreezeSubCustomersReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
