# coding: utf-8

import pprint
import re

import six





class ShowCustomerMonthlySumRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'bill_cycle': 'str',
        'service_type_code': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'method': 'str',
        'sub_customer_id': 'str'
    }

    attribute_map = {
        'bill_cycle': 'bill_cycle',
        'service_type_code': 'service_type_code',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'method': 'method',
        'sub_customer_id': 'sub_customer_id'
    }

    def __init__(self, bill_cycle=None, service_type_code=None, enterprise_project_id=None, offset=None, limit=None, method=None, sub_customer_id=None):
        """ShowCustomerMonthlySumRequest - a model defined in huaweicloud sdk"""
        
        

        self._bill_cycle = None
        self._service_type_code = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._method = None
        self._sub_customer_id = None
        self.discriminator = None

        self.bill_cycle = bill_cycle
        if service_type_code is not None:
            self.service_type_code = service_type_code
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if method is not None:
            self.method = method
        if sub_customer_id is not None:
            self.sub_customer_id = sub_customer_id

    @property
    def bill_cycle(self):
        """Gets the bill_cycle of this ShowCustomerMonthlySumRequest.


        :return: The bill_cycle of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._bill_cycle

    @bill_cycle.setter
    def bill_cycle(self, bill_cycle):
        """Sets the bill_cycle of this ShowCustomerMonthlySumRequest.


        :param bill_cycle: The bill_cycle of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._bill_cycle = bill_cycle

    @property
    def service_type_code(self):
        """Gets the service_type_code of this ShowCustomerMonthlySumRequest.


        :return: The service_type_code of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._service_type_code

    @service_type_code.setter
    def service_type_code(self, service_type_code):
        """Sets the service_type_code of this ShowCustomerMonthlySumRequest.


        :param service_type_code: The service_type_code of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._service_type_code = service_type_code

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ShowCustomerMonthlySumRequest.


        :return: The enterprise_project_id of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ShowCustomerMonthlySumRequest.


        :param enterprise_project_id: The enterprise_project_id of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        """Gets the offset of this ShowCustomerMonthlySumRequest.


        :return: The offset of this ShowCustomerMonthlySumRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowCustomerMonthlySumRequest.


        :param offset: The offset of this ShowCustomerMonthlySumRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowCustomerMonthlySumRequest.


        :return: The limit of this ShowCustomerMonthlySumRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowCustomerMonthlySumRequest.


        :param limit: The limit of this ShowCustomerMonthlySumRequest.
        :type: int
        """
        self._limit = limit

    @property
    def method(self):
        """Gets the method of this ShowCustomerMonthlySumRequest.


        :return: The method of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this ShowCustomerMonthlySumRequest.


        :param method: The method of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._method = method

    @property
    def sub_customer_id(self):
        """Gets the sub_customer_id of this ShowCustomerMonthlySumRequest.


        :return: The sub_customer_id of this ShowCustomerMonthlySumRequest.
        :rtype: str
        """
        return self._sub_customer_id

    @sub_customer_id.setter
    def sub_customer_id(self, sub_customer_id):
        """Sets the sub_customer_id of this ShowCustomerMonthlySumRequest.


        :param sub_customer_id: The sub_customer_id of this ShowCustomerMonthlySumRequest.
        :type: str
        """
        self._sub_customer_id = sub_customer_id

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
        if not isinstance(other, ShowCustomerMonthlySumRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
