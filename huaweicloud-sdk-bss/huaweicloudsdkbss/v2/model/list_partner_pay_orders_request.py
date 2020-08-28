# coding: utf-8

import pprint
import re

import six





class ListPartnerPayOrdersRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'order_id': 'str',
        'customer_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'status': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'order_id': 'order_id',
        'customer_id': 'customer_id',
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, order_id=None, customer_id=None, limit=10, offset=0, status=None, indirect_partner_id=None):
        """ListPartnerPayOrdersRequest - a model defined in huaweicloud sdk"""
        
        

        self._order_id = None
        self._customer_id = None
        self._limit = None
        self._offset = None
        self._status = None
        self._indirect_partner_id = None
        self.discriminator = None

        if order_id is not None:
            self.order_id = order_id
        if customer_id is not None:
            self.customer_id = customer_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def order_id(self):
        """Gets the order_id of this ListPartnerPayOrdersRequest.


        :return: The order_id of this ListPartnerPayOrdersRequest.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ListPartnerPayOrdersRequest.


        :param order_id: The order_id of this ListPartnerPayOrdersRequest.
        :type: str
        """
        self._order_id = order_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ListPartnerPayOrdersRequest.


        :return: The customer_id of this ListPartnerPayOrdersRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListPartnerPayOrdersRequest.


        :param customer_id: The customer_id of this ListPartnerPayOrdersRequest.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def limit(self):
        """Gets the limit of this ListPartnerPayOrdersRequest.


        :return: The limit of this ListPartnerPayOrdersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPartnerPayOrdersRequest.


        :param limit: The limit of this ListPartnerPayOrdersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListPartnerPayOrdersRequest.


        :return: The offset of this ListPartnerPayOrdersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPartnerPayOrdersRequest.


        :param offset: The offset of this ListPartnerPayOrdersRequest.
        :type: int
        """
        self._offset = offset

    @property
    def status(self):
        """Gets the status of this ListPartnerPayOrdersRequest.


        :return: The status of this ListPartnerPayOrdersRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListPartnerPayOrdersRequest.


        :param status: The status of this ListPartnerPayOrdersRequest.
        :type: int
        """
        self._status = status

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListPartnerPayOrdersRequest.


        :return: The indirect_partner_id of this ListPartnerPayOrdersRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListPartnerPayOrdersRequest.


        :param indirect_partner_id: The indirect_partner_id of this ListPartnerPayOrdersRequest.
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
        if not isinstance(other, ListPartnerPayOrdersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
