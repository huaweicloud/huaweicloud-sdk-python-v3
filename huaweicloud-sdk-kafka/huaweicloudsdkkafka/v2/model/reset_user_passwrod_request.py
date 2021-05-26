# coding: utf-8

import pprint
import re

import six





class ResetUserPasswrodRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'user_name': 'str',
        'body': 'ResetUserPasswrodReq'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'user_name': 'user_name',
        'body': 'body'
    }

    def __init__(self, instance_id=None, user_name=None, body=None):
        """ResetUserPasswrodRequest - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._user_name = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.user_name = user_name
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this ResetUserPasswrodRequest.

        实例ID。

        :return: The instance_id of this ResetUserPasswrodRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ResetUserPasswrodRequest.

        实例ID。

        :param instance_id: The instance_id of this ResetUserPasswrodRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def user_name(self):
        """Gets the user_name of this ResetUserPasswrodRequest.

        用户名称。

        :return: The user_name of this ResetUserPasswrodRequest.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ResetUserPasswrodRequest.

        用户名称。

        :param user_name: The user_name of this ResetUserPasswrodRequest.
        :type: str
        """
        self._user_name = user_name

    @property
    def body(self):
        """Gets the body of this ResetUserPasswrodRequest.


        :return: The body of this ResetUserPasswrodRequest.
        :rtype: ResetUserPasswrodReq
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ResetUserPasswrodRequest.


        :param body: The body of this ResetUserPasswrodRequest.
        :type: ResetUserPasswrodReq
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
        if not isinstance(other, ResetUserPasswrodRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
