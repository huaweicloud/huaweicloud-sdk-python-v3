# coding: utf-8

import pprint
import re

import six





class ListPartnerAdjustRecordsRequest:


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
        'operation_type': 'str',
        'operation_time_begin': 'str',
        'operation_time_end': 'str',
        'trans_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'operation_type': 'operation_type',
        'operation_time_begin': 'operation_time_begin',
        'operation_time_end': 'operation_time_end',
        'trans_id': 'trans_id',
        'offset': 'offset',
        'limit': 'limit',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_id=None, operation_type=None, operation_time_begin=None, operation_time_end=None, trans_id=None, offset=0, limit=10, indirect_partner_id=None):
        """ListPartnerAdjustRecordsRequest - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._operation_type = None
        self._operation_time_begin = None
        self._operation_time_end = None
        self._trans_id = None
        self._offset = None
        self._limit = None
        self._indirect_partner_id = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if operation_type is not None:
            self.operation_type = operation_type
        if operation_time_begin is not None:
            self.operation_time_begin = operation_time_begin
        if operation_time_end is not None:
            self.operation_time_end = operation_time_end
        if trans_id is not None:
            self.trans_id = trans_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ListPartnerAdjustRecordsRequest.


        :return: The customer_id of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListPartnerAdjustRecordsRequest.


        :param customer_id: The customer_id of this ListPartnerAdjustRecordsRequest.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def operation_type(self):
        """Gets the operation_type of this ListPartnerAdjustRecordsRequest.


        :return: The operation_type of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ListPartnerAdjustRecordsRequest.


        :param operation_type: The operation_type of this ListPartnerAdjustRecordsRequest.
        :type: str
        """
        self._operation_type = operation_type

    @property
    def operation_time_begin(self):
        """Gets the operation_time_begin of this ListPartnerAdjustRecordsRequest.


        :return: The operation_time_begin of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._operation_time_begin

    @operation_time_begin.setter
    def operation_time_begin(self, operation_time_begin):
        """Sets the operation_time_begin of this ListPartnerAdjustRecordsRequest.


        :param operation_time_begin: The operation_time_begin of this ListPartnerAdjustRecordsRequest.
        :type: str
        """
        self._operation_time_begin = operation_time_begin

    @property
    def operation_time_end(self):
        """Gets the operation_time_end of this ListPartnerAdjustRecordsRequest.


        :return: The operation_time_end of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._operation_time_end

    @operation_time_end.setter
    def operation_time_end(self, operation_time_end):
        """Sets the operation_time_end of this ListPartnerAdjustRecordsRequest.


        :param operation_time_end: The operation_time_end of this ListPartnerAdjustRecordsRequest.
        :type: str
        """
        self._operation_time_end = operation_time_end

    @property
    def trans_id(self):
        """Gets the trans_id of this ListPartnerAdjustRecordsRequest.


        :return: The trans_id of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._trans_id

    @trans_id.setter
    def trans_id(self, trans_id):
        """Sets the trans_id of this ListPartnerAdjustRecordsRequest.


        :param trans_id: The trans_id of this ListPartnerAdjustRecordsRequest.
        :type: str
        """
        self._trans_id = trans_id

    @property
    def offset(self):
        """Gets the offset of this ListPartnerAdjustRecordsRequest.


        :return: The offset of this ListPartnerAdjustRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListPartnerAdjustRecordsRequest.


        :param offset: The offset of this ListPartnerAdjustRecordsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListPartnerAdjustRecordsRequest.


        :return: The limit of this ListPartnerAdjustRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListPartnerAdjustRecordsRequest.


        :param limit: The limit of this ListPartnerAdjustRecordsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListPartnerAdjustRecordsRequest.


        :return: The indirect_partner_id of this ListPartnerAdjustRecordsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListPartnerAdjustRecordsRequest.


        :param indirect_partner_id: The indirect_partner_id of this ListPartnerAdjustRecordsRequest.
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
        if not isinstance(other, ListPartnerAdjustRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
