# coding: utf-8

import pprint
import re

import six





class DeleteServerGroupMemberRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'server_group_id': 'str',
        'body': 'DeleteServerGroupMemberRequestBody'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'body': 'body'
    }

    def __init__(self, server_group_id=None, body=None):
        """DeleteServerGroupMemberRequest - a model defined in huaweicloud sdk"""
        
        

        self._server_group_id = None
        self._body = None
        self.discriminator = None

        self.server_group_id = server_group_id
        if body is not None:
            self.body = body

    @property
    def server_group_id(self):
        """Gets the server_group_id of this DeleteServerGroupMemberRequest.


        :return: The server_group_id of this DeleteServerGroupMemberRequest.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this DeleteServerGroupMemberRequest.


        :param server_group_id: The server_group_id of this DeleteServerGroupMemberRequest.
        :type: str
        """
        self._server_group_id = server_group_id

    @property
    def body(self):
        """Gets the body of this DeleteServerGroupMemberRequest.


        :return: The body of this DeleteServerGroupMemberRequest.
        :rtype: DeleteServerGroupMemberRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteServerGroupMemberRequest.


        :param body: The body of this DeleteServerGroupMemberRequest.
        :type: DeleteServerGroupMemberRequestBody
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
        if not isinstance(other, DeleteServerGroupMemberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
