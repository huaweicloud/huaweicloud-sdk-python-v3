# coding: utf-8

import pprint
import re

import six





class ShowMultiAccountTransferAmountRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'balance_type': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'balance_type': 'balance_type',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, balance_type=None, offset=0, limit=10):
        """ShowMultiAccountTransferAmountRequest - a model defined in huaweicloud sdk"""
        
        

        self._balance_type = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.balance_type = balance_type
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def balance_type(self):
        """Gets the balance_type of this ShowMultiAccountTransferAmountRequest.


        :return: The balance_type of this ShowMultiAccountTransferAmountRequest.
        :rtype: str
        """
        return self._balance_type

    @balance_type.setter
    def balance_type(self, balance_type):
        """Sets the balance_type of this ShowMultiAccountTransferAmountRequest.


        :param balance_type: The balance_type of this ShowMultiAccountTransferAmountRequest.
        :type: str
        """
        self._balance_type = balance_type

    @property
    def offset(self):
        """Gets the offset of this ShowMultiAccountTransferAmountRequest.


        :return: The offset of this ShowMultiAccountTransferAmountRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowMultiAccountTransferAmountRequest.


        :param offset: The offset of this ShowMultiAccountTransferAmountRequest.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowMultiAccountTransferAmountRequest.


        :return: The limit of this ShowMultiAccountTransferAmountRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowMultiAccountTransferAmountRequest.


        :param limit: The limit of this ShowMultiAccountTransferAmountRequest.
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
        if not isinstance(other, ShowMultiAccountTransferAmountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
