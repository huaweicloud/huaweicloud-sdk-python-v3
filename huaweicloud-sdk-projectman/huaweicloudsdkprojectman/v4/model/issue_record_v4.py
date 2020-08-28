# coding: utf-8

import pprint
import re

import six





class IssueRecordV4:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user': 'IssueRecordV4User',
        'details': 'list[IssueRecordV4Details]'
    }

    attribute_map = {
        'user': 'user',
        'details': 'details'
    }

    def __init__(self, user=None, details=None):
        """IssueRecordV4 - a model defined in huaweicloud sdk"""
        
        

        self._user = None
        self._details = None
        self.discriminator = None

        if user is not None:
            self.user = user
        if details is not None:
            self.details = details

    @property
    def user(self):
        """Gets the user of this IssueRecordV4.


        :return: The user of this IssueRecordV4.
        :rtype: IssueRecordV4User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this IssueRecordV4.


        :param user: The user of this IssueRecordV4.
        :type: IssueRecordV4User
        """
        self._user = user

    @property
    def details(self):
        """Gets the details of this IssueRecordV4.

        操作的记录

        :return: The details of this IssueRecordV4.
        :rtype: list[IssueRecordV4Details]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this IssueRecordV4.

        操作的记录

        :param details: The details of this IssueRecordV4.
        :type: list[IssueRecordV4Details]
        """
        self._details = details

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
        if not isinstance(other, IssueRecordV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
