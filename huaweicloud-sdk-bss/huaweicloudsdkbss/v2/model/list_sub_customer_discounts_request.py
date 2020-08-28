# coding: utf-8

import pprint
import re

import six





class ListSubCustomerDiscountsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'customer_id': 'str',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_id=None, indirect_partner_id=None):
        """ListSubCustomerDiscountsRequest - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.customer_id = customer_id
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ListSubCustomerDiscountsRequest.


        :return: The customer_id of this ListSubCustomerDiscountsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListSubCustomerDiscountsRequest.


        :param customer_id: The customer_id of this ListSubCustomerDiscountsRequest.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListSubCustomerDiscountsRequest.


        :return: The indirect_partner_id of this ListSubCustomerDiscountsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListSubCustomerDiscountsRequest.


        :param indirect_partner_id: The indirect_partner_id of this ListSubCustomerDiscountsRequest.
        :type: str
        """
        self._indirect_partner_id = indirect_partner_id

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
        if not isinstance(other, ListSubCustomerDiscountsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
