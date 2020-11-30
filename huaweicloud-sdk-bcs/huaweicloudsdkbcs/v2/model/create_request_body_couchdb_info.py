# coding: utf-8

import pprint
import re

import six





class CreateRequestBodyCouchdbInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'user_name': 'str',
        'password': 'str'
    }

    attribute_map = {
        'user_name': 'user_name',
        'password': 'password'
    }

    def __init__(self, user_name=None, password=None):
        """CreateRequestBodyCouchdbInfo - a model defined in huaweicloud sdk"""
        
        

        self._user_name = None
        self._password = None
        self.discriminator = None

        if user_name is not None:
            self.user_name = user_name
        if password is not None:
            self.password = password

    @property
    def user_name(self):
        """Gets the user_name of this CreateRequestBodyCouchdbInfo.

        couchDB用户名

        :return: The user_name of this CreateRequestBodyCouchdbInfo.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this CreateRequestBodyCouchdbInfo.

        couchDB用户名

        :param user_name: The user_name of this CreateRequestBodyCouchdbInfo.
        :type: str
        """
        self._user_name = user_name

    @property
    def password(self):
        """Gets the password of this CreateRequestBodyCouchdbInfo.

        couchDB密码

        :return: The password of this CreateRequestBodyCouchdbInfo.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this CreateRequestBodyCouchdbInfo.

        couchDB密码

        :param password: The password of this CreateRequestBodyCouchdbInfo.
        :type: str
        """
        self._password = password

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
        if not isinstance(other, CreateRequestBodyCouchdbInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
