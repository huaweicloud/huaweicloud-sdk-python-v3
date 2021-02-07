# coding: utf-8

import pprint
import re

import six





class DeleteApplicationRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []
    sensitive_list.append('sp_auth_token')

    openapi_types = {
        'sp_auth_token': 'str',
        'instance_id': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'sp_auth_token': 'Sp-Auth-Token',
        'instance_id': 'Instance-Id',
        'app_id': 'app_id'
    }

    def __init__(self, sp_auth_token=None, instance_id=None, app_id=None):
        """DeleteApplicationRequest - a model defined in huaweicloud sdk"""
        
        

        self._sp_auth_token = None
        self._instance_id = None
        self._app_id = None
        self.discriminator = None

        if sp_auth_token is not None:
            self.sp_auth_token = sp_auth_token
        if instance_id is not None:
            self.instance_id = instance_id
        self.app_id = app_id

    @property
    def sp_auth_token(self):
        """Gets the sp_auth_token of this DeleteApplicationRequest.


        :return: The sp_auth_token of this DeleteApplicationRequest.
        :rtype: str
        """
        return self._sp_auth_token

    @sp_auth_token.setter
    def sp_auth_token(self, sp_auth_token):
        """Sets the sp_auth_token of this DeleteApplicationRequest.


        :param sp_auth_token: The sp_auth_token of this DeleteApplicationRequest.
        :type: str
        """
        self._sp_auth_token = sp_auth_token

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteApplicationRequest.


        :return: The instance_id of this DeleteApplicationRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteApplicationRequest.


        :param instance_id: The instance_id of this DeleteApplicationRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def app_id(self):
        """Gets the app_id of this DeleteApplicationRequest.


        :return: The app_id of this DeleteApplicationRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this DeleteApplicationRequest.


        :param app_id: The app_id of this DeleteApplicationRequest.
        :type: str
        """
        self._app_id = app_id

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
        if not isinstance(other, DeleteApplicationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
