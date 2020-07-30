# coding: utf-8

import pprint
import re

import six





class AddMemberRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'body': 'AddMembersReq'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'body': 'body'
    }

    def __init__(self, backup_id=None, body=None):
        """AddMemberRequest - a model defined in huaweicloud sdk"""
        
        

        self._backup_id = None
        self._body = None
        self.discriminator = None

        self.backup_id = backup_id
        if body is not None:
            self.body = body

    @property
    def backup_id(self):
        """Gets the backup_id of this AddMemberRequest.


        :return: The backup_id of this AddMemberRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this AddMemberRequest.


        :param backup_id: The backup_id of this AddMemberRequest.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def body(self):
        """Gets the body of this AddMemberRequest.


        :return: The body of this AddMemberRequest.
        :rtype: AddMembersReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this AddMemberRequest.


        :param body: The body of this AddMemberRequest.
        :type: AddMembersReq
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
        if not isinstance(other, AddMemberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
