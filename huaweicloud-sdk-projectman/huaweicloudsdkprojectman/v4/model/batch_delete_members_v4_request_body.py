# coding: utf-8

import pprint
import re

import six





class BatchDeleteMembersV4RequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_ids': 'list[str]'
    }

    attribute_map = {
        'user_ids': 'user_ids'
    }

    def __init__(self, user_ids=None):
        """BatchDeleteMembersV4RequestBody - a model defined in huaweicloud sdk"""
        
        

        self._user_ids = None
        self.discriminator = None

        self.user_ids = user_ids

    @property
    def user_ids(self):
        """Gets the user_ids of this BatchDeleteMembersV4RequestBody.

        用户id

        :return: The user_ids of this BatchDeleteMembersV4RequestBody.
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this BatchDeleteMembersV4RequestBody.

        用户id

        :param user_ids: The user_ids of this BatchDeleteMembersV4RequestBody.
        :type: list[str]
        """
        self._user_ids = user_ids

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
        if not isinstance(other, BatchDeleteMembersV4RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
