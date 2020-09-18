# coding: utf-8

import pprint
import re

import six





class QuotaReclaim:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'quota_id': 'str',
        'quota_balance': 'float'
    }

    attribute_map = {
        'quota_id': 'quota_id',
        'quota_balance': 'quota_balance'
    }

    def __init__(self, quota_id=None, quota_balance=None):
        """QuotaReclaim - a model defined in huaweicloud sdk"""
        
        

        self._quota_id = None
        self._quota_balance = None
        self.discriminator = None

        if quota_id is not None:
            self.quota_id = quota_id
        if quota_balance is not None:
            self.quota_balance = quota_balance

    @property
    def quota_id(self):
        """Gets the quota_id of this QuotaReclaim.

        |参数名称：被回收的二级经销商代金券额度ID| |参数约束及描述：被回收的二级经销商代金券额度ID|

        :return: The quota_id of this QuotaReclaim.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this QuotaReclaim.

        |参数名称：被回收的二级经销商代金券额度ID| |参数约束及描述：被回收的二级经销商代金券额度ID|

        :param quota_id: The quota_id of this QuotaReclaim.
        :type: str
        """
        self._quota_id = quota_id

    @property
    def quota_balance(self):
        """Gets the quota_balance of this QuotaReclaim.

        |参数名称：被回收的代金券的余额| |参数的约束及描述：被回收的代金券的余额|

        :return: The quota_balance of this QuotaReclaim.
        :rtype: float
        """
        return self._quota_balance

    @quota_balance.setter
    def quota_balance(self, quota_balance):
        """Sets the quota_balance of this QuotaReclaim.

        |参数名称：被回收的代金券的余额| |参数的约束及描述：被回收的代金券的余额|

        :param quota_balance: The quota_balance of this QuotaReclaim.
        :type: float
        """
        self._quota_balance = quota_balance

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
        if not isinstance(other, QuotaReclaim):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
