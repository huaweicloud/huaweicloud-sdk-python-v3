# coding: utf-8

import pprint
import re

import six





class ListEnterpriseSubCustomersRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'sub_customer_account_name': 'str',
        'sub_customer_display_name': 'str',
        'fuzzy_query': 'int',
        'offset': 'int',
        'limit': 'int',
        'org_id': 'str'
    }

    attribute_map = {
        'sub_customer_account_name': 'sub_customer_account_name',
        'sub_customer_display_name': 'sub_customer_display_name',
        'fuzzy_query': 'fuzzy_query',
        'offset': 'offset',
        'limit': 'limit',
        'org_id': 'org_id'
    }

    def __init__(self, sub_customer_account_name=None, sub_customer_display_name=None, fuzzy_query=None, offset=0, limit=10, org_id=None):
        """ListEnterpriseSubCustomersRequest - a model defined in huaweicloud sdk"""
        
        

        self._sub_customer_account_name = None
        self._sub_customer_display_name = None
        self._fuzzy_query = None
        self._offset = None
        self._limit = None
        self._org_id = None
        self.discriminator = None

        if sub_customer_account_name is not None:
            self.sub_customer_account_name = sub_customer_account_name
        if sub_customer_display_name is not None:
            self.sub_customer_display_name = sub_customer_display_name
        if fuzzy_query is not None:
            self.fuzzy_query = fuzzy_query
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if org_id is not None:
            self.org_id = org_id

    @property
    def sub_customer_account_name(self):
        """Gets the sub_customer_account_name of this ListEnterpriseSubCustomersRequest.


        :return: The sub_customer_account_name of this ListEnterpriseSubCustomersRequest.
        :rtype: str
        """
        return self._sub_customer_account_name

    @sub_customer_account_name.setter
    def sub_customer_account_name(self, sub_customer_account_name):
        """Sets the sub_customer_account_name of this ListEnterpriseSubCustomersRequest.


        :param sub_customer_account_name: The sub_customer_account_name of this ListEnterpriseSubCustomersRequest.
        :type: str
        """
        self._sub_customer_account_name = sub_customer_account_name

    @property
    def sub_customer_display_name(self):
        """Gets the sub_customer_display_name of this ListEnterpriseSubCustomersRequest.


        :return: The sub_customer_display_name of this ListEnterpriseSubCustomersRequest.
        :rtype: str
        """
        return self._sub_customer_display_name

    @sub_customer_display_name.setter
    def sub_customer_display_name(self, sub_customer_display_name):
        """Sets the sub_customer_display_name of this ListEnterpriseSubCustomersRequest.


        :param sub_customer_display_name: The sub_customer_display_name of this ListEnterpriseSubCustomersRequest.
        :type: str
        """
        self._sub_customer_display_name = sub_customer_display_name

    @property
    def fuzzy_query(self):
        """Gets the fuzzy_query of this ListEnterpriseSubCustomersRequest.


        :return: The fuzzy_query of this ListEnterpriseSubCustomersRequest.
        :rtype: int
        """
        return self._fuzzy_query

    @fuzzy_query.setter
    def fuzzy_query(self, fuzzy_query):
        """Sets the fuzzy_query of this ListEnterpriseSubCustomersRequest.


        :param fuzzy_query: The fuzzy_query of this ListEnterpriseSubCustomersRequest.
        :type: int
        """
        self._fuzzy_query = fuzzy_query

    @property
    def offset(self):
        """Gets the offset of this ListEnterpriseSubCustomersRequest.


        :return: The offset of this ListEnterpriseSubCustomersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListEnterpriseSubCustomersRequest.


        :param offset: The offset of this ListEnterpriseSubCustomersRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListEnterpriseSubCustomersRequest.


        :return: The limit of this ListEnterpriseSubCustomersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListEnterpriseSubCustomersRequest.


        :param limit: The limit of this ListEnterpriseSubCustomersRequest.
        :type: int
        """
        self._limit = limit

    @property
    def org_id(self):
        """Gets the org_id of this ListEnterpriseSubCustomersRequest.


        :return: The org_id of this ListEnterpriseSubCustomersRequest.
        :rtype: str
        """
        return self._org_id

    @org_id.setter
    def org_id(self, org_id):
        """Sets the org_id of this ListEnterpriseSubCustomersRequest.


        :param org_id: The org_id of this ListEnterpriseSubCustomersRequest.
        :type: str
        """
        self._org_id = org_id

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
        if not isinstance(other, ListEnterpriseSubCustomersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
