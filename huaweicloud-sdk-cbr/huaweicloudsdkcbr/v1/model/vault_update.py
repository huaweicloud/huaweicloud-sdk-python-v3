# coding: utf-8

import pprint
import re

import six





class VaultUpdate:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'billing': 'BillingUpdate',
        'name': 'str',
        'auto_bind': 'bool',
        'bind_rules': 'list[VaultBindRules]'
    }

    attribute_map = {
        'billing': 'billing',
        'name': 'name',
        'auto_bind': 'auto_bind',
        'bind_rules': 'bind_rules'
    }

    def __init__(self, billing=None, name=None, auto_bind=None, bind_rules=None):
        """VaultUpdate - a model defined in huaweicloud sdk"""
        
        

        self._billing = None
        self._name = None
        self._auto_bind = None
        self._bind_rules = None
        self.discriminator = None

        if billing is not None:
            self.billing = billing
        if name is not None:
            self.name = name
        if auto_bind is not None:
            self.auto_bind = auto_bind
        if bind_rules is not None:
            self.bind_rules = bind_rules

    @property
    def billing(self):
        """Gets the billing of this VaultUpdate.


        :return: The billing of this VaultUpdate.
        :rtype: BillingUpdate
        """
        return self._billing

    @billing.setter
    def billing(self, billing):
        """Sets the billing of this VaultUpdate.


        :param billing: The billing of this VaultUpdate.
        :type: BillingUpdate
        """
        self._billing = billing

    @property
    def name(self):
        """Gets the name of this VaultUpdate.

        存储库名称

        :return: The name of this VaultUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VaultUpdate.

        存储库名称

        :param name: The name of this VaultUpdate.
        :type: str
        """
        self._name = name

    @property
    def auto_bind(self):
        """Gets the auto_bind of this VaultUpdate.

        是否支持自动挂载

        :return: The auto_bind of this VaultUpdate.
        :rtype: bool
        """
        return self._auto_bind

    @auto_bind.setter
    def auto_bind(self, auto_bind):
        """Sets the auto_bind of this VaultUpdate.

        是否支持自动挂载

        :param auto_bind: The auto_bind of this VaultUpdate.
        :type: bool
        """
        self._auto_bind = auto_bind

    @property
    def bind_rules(self):
        """Gets the bind_rules of this VaultUpdate.

        

        :return: The bind_rules of this VaultUpdate.
        :rtype: list[VaultBindRules]
        """
        return self._bind_rules

    @bind_rules.setter
    def bind_rules(self, bind_rules):
        """Sets the bind_rules of this VaultUpdate.

        

        :param bind_rules: The bind_rules of this VaultUpdate.
        :type: list[VaultBindRules]
        """
        self._bind_rules = bind_rules

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
        if not isinstance(other, VaultUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
