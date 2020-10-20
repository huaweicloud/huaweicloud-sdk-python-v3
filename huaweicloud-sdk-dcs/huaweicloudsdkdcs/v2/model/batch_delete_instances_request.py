# coding: utf-8

import pprint
import re

import six





class BatchDeleteInstancesRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'all_failure': 'bool',
        'body': 'BatchDeleteBody'
    }

    attribute_map = {
        'all_failure': 'all_failure',
        'body': 'body'
    }

    def __init__(self, all_failure=None, body=None):
        """BatchDeleteInstancesRequest - a model defined in huaweicloud sdk"""
        
        

        self._all_failure = None
        self._body = None
        self.discriminator = None

        if all_failure is not None:
            self.all_failure = all_failure
        if body is not None:
            self.body = body

    @property
    def all_failure(self):
        """Gets the all_failure of this BatchDeleteInstancesRequest.


        :return: The all_failure of this BatchDeleteInstancesRequest.
        :rtype: bool
        """
        return self._all_failure

    @all_failure.setter
    def all_failure(self, all_failure):
        """Sets the all_failure of this BatchDeleteInstancesRequest.


        :param all_failure: The all_failure of this BatchDeleteInstancesRequest.
        :type: bool
        """
        self._all_failure = all_failure

    @property
    def body(self):
        """Gets the body of this BatchDeleteInstancesRequest.


        :return: The body of this BatchDeleteInstancesRequest.
        :rtype: BatchDeleteBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchDeleteInstancesRequest.


        :param body: The body of this BatchDeleteInstancesRequest.
        :type: BatchDeleteBody
        """
        self._body = body

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
        if not isinstance(other, BatchDeleteInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
