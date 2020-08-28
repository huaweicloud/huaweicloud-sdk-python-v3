# coding: utf-8

import pprint
import re

import six





class ListSubCustomerResFeeRecordsRequest:


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
        'cycle': 'str',
        'cloud_service_type': 'str',
        'region': 'str',
        'charge_mode': 'str',
        'bill_type': 'int',
        'offset': 'int',
        'limit': 'int',
        'resource_id': 'str',
        'include_zero_record': 'bool',
        'indirect_partner_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customer_id',
        'cycle': 'cycle',
        'cloud_service_type': 'cloud_service_type',
        'region': 'region',
        'charge_mode': 'charge_mode',
        'bill_type': 'bill_type',
        'offset': 'offset',
        'limit': 'limit',
        'resource_id': 'resource_id',
        'include_zero_record': 'include_zero_record',
        'indirect_partner_id': 'indirect_partner_id'
    }

    def __init__(self, customer_id=None, cycle=None, cloud_service_type=None, region=None, charge_mode=None, bill_type=None, offset=0, limit=10, resource_id=None, include_zero_record=None, indirect_partner_id=None):
        """ListSubCustomerResFeeRecordsRequest - a model defined in huaweicloud sdk"""
        
        

        self._customer_id = None
        self._cycle = None
        self._cloud_service_type = None
        self._region = None
        self._charge_mode = None
        self._bill_type = None
        self._offset = None
        self._limit = None
        self._resource_id = None
        self._include_zero_record = None
        self._indirect_partner_id = None
        self.discriminator = None

        self.customer_id = customer_id
        self.cycle = cycle
        if cloud_service_type is not None:
            self.cloud_service_type = cloud_service_type
        if region is not None:
            self.region = region
        self.charge_mode = charge_mode
        if bill_type is not None:
            self.bill_type = bill_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if resource_id is not None:
            self.resource_id = resource_id
        if include_zero_record is not None:
            self.include_zero_record = include_zero_record
        if indirect_partner_id is not None:
            self.indirect_partner_id = indirect_partner_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ListSubCustomerResFeeRecordsRequest.


        :return: The customer_id of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ListSubCustomerResFeeRecordsRequest.


        :param customer_id: The customer_id of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._customer_id = customer_id

    @property
    def cycle(self):
        """Gets the cycle of this ListSubCustomerResFeeRecordsRequest.


        :return: The cycle of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this ListSubCustomerResFeeRecordsRequest.


        :param cycle: The cycle of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._cycle = cycle

    @property
    def cloud_service_type(self):
        """Gets the cloud_service_type of this ListSubCustomerResFeeRecordsRequest.


        :return: The cloud_service_type of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._cloud_service_type

    @cloud_service_type.setter
    def cloud_service_type(self, cloud_service_type):
        """Sets the cloud_service_type of this ListSubCustomerResFeeRecordsRequest.


        :param cloud_service_type: The cloud_service_type of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._cloud_service_type = cloud_service_type

    @property
    def region(self):
        """Gets the region of this ListSubCustomerResFeeRecordsRequest.


        :return: The region of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListSubCustomerResFeeRecordsRequest.


        :param region: The region of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._region = region

    @property
    def charge_mode(self):
        """Gets the charge_mode of this ListSubCustomerResFeeRecordsRequest.


        :return: The charge_mode of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        """Sets the charge_mode of this ListSubCustomerResFeeRecordsRequest.


        :param charge_mode: The charge_mode of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._charge_mode = charge_mode

    @property
    def bill_type(self):
        """Gets the bill_type of this ListSubCustomerResFeeRecordsRequest.


        :return: The bill_type of this ListSubCustomerResFeeRecordsRequest.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this ListSubCustomerResFeeRecordsRequest.


        :param bill_type: The bill_type of this ListSubCustomerResFeeRecordsRequest.
        :type: int
        """
        self._bill_type = bill_type

    @property
    def offset(self):
        """Gets the offset of this ListSubCustomerResFeeRecordsRequest.


        :return: The offset of this ListSubCustomerResFeeRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSubCustomerResFeeRecordsRequest.


        :param offset: The offset of this ListSubCustomerResFeeRecordsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSubCustomerResFeeRecordsRequest.


        :return: The limit of this ListSubCustomerResFeeRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSubCustomerResFeeRecordsRequest.


        :param limit: The limit of this ListSubCustomerResFeeRecordsRequest.
        :type: int
        """
        self._limit = limit

    @property
    def resource_id(self):
        """Gets the resource_id of this ListSubCustomerResFeeRecordsRequest.


        :return: The resource_id of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this ListSubCustomerResFeeRecordsRequest.


        :param resource_id: The resource_id of this ListSubCustomerResFeeRecordsRequest.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def include_zero_record(self):
        """Gets the include_zero_record of this ListSubCustomerResFeeRecordsRequest.


        :return: The include_zero_record of this ListSubCustomerResFeeRecordsRequest.
        :rtype: bool
        """
        return self._include_zero_record

    @include_zero_record.setter
    def include_zero_record(self, include_zero_record):
        """Sets the include_zero_record of this ListSubCustomerResFeeRecordsRequest.


        :param include_zero_record: The include_zero_record of this ListSubCustomerResFeeRecordsRequest.
        :type: bool
        """
        self._include_zero_record = include_zero_record

    @property
    def indirect_partner_id(self):
        """Gets the indirect_partner_id of this ListSubCustomerResFeeRecordsRequest.


        :return: The indirect_partner_id of this ListSubCustomerResFeeRecordsRequest.
        :rtype: str
        """
        return self._indirect_partner_id

    @indirect_partner_id.setter
    def indirect_partner_id(self, indirect_partner_id):
        """Sets the indirect_partner_id of this ListSubCustomerResFeeRecordsRequest.


        :param indirect_partner_id: The indirect_partner_id of this ListSubCustomerResFeeRecordsRequest.
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
        if not isinstance(other, ListSubCustomerResFeeRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
