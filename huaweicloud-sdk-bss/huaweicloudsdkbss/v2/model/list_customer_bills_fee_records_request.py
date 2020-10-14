# coding: utf-8

import pprint
import re

import six





class ListCustomerBillsFeeRecordsRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'bill_cycle': 'str',
        'provider_type': 'int',
        'service_type_code': 'str',
        'resource_type_code': 'str',
        'region_code': 'str',
        'charging_mode': 'int',
        'bill_type': 'int',
        'trade_id': 'str',
        'enterprise_project_id': 'str',
        'include_zero_record': 'bool',
        'status': 'int',
        'method': 'str',
        'sub_customer_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'bill_cycle': 'bill_cycle',
        'provider_type': 'provider_type',
        'service_type_code': 'service_type_code',
        'resource_type_code': 'resource_type_code',
        'region_code': 'region_code',
        'charging_mode': 'charging_mode',
        'bill_type': 'bill_type',
        'trade_id': 'trade_id',
        'enterprise_project_id': 'enterprise_project_id',
        'include_zero_record': 'include_zero_record',
        'status': 'status',
        'method': 'method',
        'sub_customer_id': 'sub_customer_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language='zh_cn', bill_cycle=None, provider_type=None, service_type_code=None, resource_type_code=None, region_code=None, charging_mode=None, bill_type=None, trade_id=None, enterprise_project_id=None, include_zero_record=None, status=None, method=None, sub_customer_id=None, offset=0, limit=10):
        """ListCustomerBillsFeeRecordsRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_language = None
        self._bill_cycle = None
        self._provider_type = None
        self._service_type_code = None
        self._resource_type_code = None
        self._region_code = None
        self._charging_mode = None
        self._bill_type = None
        self._trade_id = None
        self._enterprise_project_id = None
        self._include_zero_record = None
        self._status = None
        self._method = None
        self._sub_customer_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.bill_cycle = bill_cycle
        if provider_type is not None:
            self.provider_type = provider_type
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if resource_type_code is not None:
            self.resource_type_code = resource_type_code
        if region_code is not None:
            self.region_code = region_code
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if bill_type is not None:
            self.bill_type = bill_type
        if trade_id is not None:
            self.trade_id = trade_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if include_zero_record is not None:
            self.include_zero_record = include_zero_record
        if status is not None:
            self.status = status
        if method is not None:
            self.method = method
        if sub_customer_id is not None:
            self.sub_customer_id = sub_customer_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        """Gets the x_language of this ListCustomerBillsFeeRecordsRequest.


        :return: The x_language of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListCustomerBillsFeeRecordsRequest.


        :param x_language: The x_language of this ListCustomerBillsFeeRecordsRequest.
        :type: str
        """
        self._x_language = x_language

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this ListCustomerBillsFeeRecordsRequest.


        :return: The bill_cycle of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this ListCustomerBillsFeeRecordsRequest.


        :param bill_cycle: The bill_cycle of this ListCustomerBillsFeeRecordsRequest.
        :type: str
        """
        self._bill_cycle = bill_cycle

    @property
    def provider_type(self):
        """Gets the provider_type of this ListCustomerBillsFeeRecordsRequest.


        :return: The provider_type of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this ListCustomerBillsFeeRecordsRequest.


        :param provider_type: The provider_type of this ListCustomerBillsFeeRecordsRequest.
        :type: int
        """
        self._provider_type = provider_type

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ListCustomerBillsFeeRecordsRequest.


        :return: The service_type_code of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ListCustomerBillsFeeRecordsRequest.


        :param service_type_code: The service_type_code of this ListCustomerBillsFeeRecordsRequest.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def resource_type_code(self):
        """Gets the resource_type_code of this ListCustomerBillsFeeRecordsRequest.


        :return: The resource_type_code of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, resource_type_code):
        """Sets the resource_type_code of this ListCustomerBillsFeeRecordsRequest.


        :param resource_type_code: The resource_type_code of this ListCustomerBillsFeeRecordsRequest.
        :type: str
        """
        self._resource_type_code = resource_type_code

    @property
    def region_code(self):
        """Gets the region_code of this ListCustomerBillsFeeRecordsRequest.


        :return: The region_code of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this ListCustomerBillsFeeRecordsRequest.


        :param region_code: The region_code of this ListCustomerBillsFeeRecordsRequest.
        :type: str
        """
        self._region_code = region_code

    @property
    def charging_mode(self):
        """Gets the charging_mode of this ListCustomerBillsFeeRecordsRequest.


        :return: The charging_mode of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        """Sets the charging_mode of this ListCustomerBillsFeeRecordsRequest.


        :param charging_mode: The charging_mode of this ListCustomerBillsFeeRecordsRequest.
        :type: int
        """
        self._charging_mode = charging_mode

    @property
    def bill_type(self):
        """Gets the bill_type of this ListCustomerBillsFeeRecordsRequest.


        :return: The bill_type of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._bill_type

    @bill_type.setter
    def bill_type(self, bill_type):
        """Sets the bill_type of this ListCustomerBillsFeeRecordsRequest.


        :param bill_type: The bill_type of this ListCustomerBillsFeeRecordsRequest.
        :type: int
        """
        self._bill_type = bill_type

    @property
    def trade_id(self):
        """Gets the trade_id of this ListCustomerBillsFeeRecordsRequest.


        :return: The trade_id of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._trade_id

    @trade_id.setter
    def trade_id(self, trade_id):
        """Sets the trade_id of this ListCustomerBillsFeeRecordsRequest.


        :param trade_id: The trade_id of this ListCustomerBillsFeeRecordsRequest.
        :type: str
        """
        self._trade_id = trade_id

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListCustomerBillsFeeRecordsRequest.


        :return: The enterprise_project_id of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListCustomerBillsFeeRecordsRequest.


        :param enterprise_project_id: The enterprise_project_id of this ListCustomerBillsFeeRecordsRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def include_zero_record(self):
        """Gets the include_zero_record of this ListCustomerBillsFeeRecordsRequest.


        :return: The include_zero_record of this ListCustomerBillsFeeRecordsRequest.
        :rtype: bool
        """
        return self._include_zero_record

    @include_zero_record.setter
    def include_zero_record(self, include_zero_record):
        """Sets the include_zero_record of this ListCustomerBillsFeeRecordsRequest.


        :param include_zero_record: The include_zero_record of this ListCustomerBillsFeeRecordsRequest.
        :type: bool
        """
        self._include_zero_record = include_zero_record

    @property
    def status(self):
        """Gets the status of this ListCustomerBillsFeeRecordsRequest.


        :return: The status of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListCustomerBillsFeeRecordsRequest.


        :param status: The status of this ListCustomerBillsFeeRecordsRequest.
        :type: int
        """
        self._status = status

    @property
    def method(self):
        """Gets the method of this ListCustomerBillsFeeRecordsRequest.


        :return: The method of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ListCustomerBillsFeeRecordsRequest.


        :param method: The method of this ListCustomerBillsFeeRecordsRequest.
        :type: str
        """
        self._method = method

    @property
    def sub_customer_id(self):
        """Gets the sub_customer_id of this ListCustomerBillsFeeRecordsRequest.


        :return: The sub_customer_id of this ListCustomerBillsFeeRecordsRequest.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        """Sets the sub_customer_id of this ListCustomerBillsFeeRecordsRequest.


        :param sub_customer_id: The sub_customer_id of this ListCustomerBillsFeeRecordsRequest.
        :type: str
        """
        self._sub_customer_id = sub_customer_id

    @property
    def offset(self):
        """Gets the offset of this ListCustomerBillsFeeRecordsRequest.


        :return: The offset of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListCustomerBillsFeeRecordsRequest.


        :param offset: The offset of this ListCustomerBillsFeeRecordsRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListCustomerBillsFeeRecordsRequest.


        :return: The limit of this ListCustomerBillsFeeRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListCustomerBillsFeeRecordsRequest.


        :param limit: The limit of this ListCustomerBillsFeeRecordsRequest.
        :type: int
        """
        self._limit = limit

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
        if not isinstance(other, ListCustomerBillsFeeRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
