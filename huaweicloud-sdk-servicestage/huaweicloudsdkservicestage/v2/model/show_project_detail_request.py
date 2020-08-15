# coding: utf-8

import pprint
import re

import six





class ShowProjectDetailRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'x_repo_auth': 'str',
        'clone_url': 'str'
    }

    attribute_map = {
        'x_repo_auth': 'X-Repo-Auth',
        'clone_url': 'clone_url'
    }

    def __init__(self, x_repo_auth=None, clone_url=None):
        """ShowProjectDetailRequest - a model defined in huaweicloud sdk"""
        
        

        self._x_repo_auth = None
        self._clone_url = None
        self.discriminator = None

        self.x_repo_auth = x_repo_auth
        self.clone_url = clone_url

    @property
    def x_repo_auth(self):
        """Gets the x_repo_auth of this ShowProjectDetailRequest.


        :return: The x_repo_auth of this ShowProjectDetailRequest.
        :rtype: str
        """
        return self._x_repo_auth

    @x_repo_auth.setter
    def x_repo_auth(self, x_repo_auth):
        """Sets the x_repo_auth of this ShowProjectDetailRequest.


        :param x_repo_auth: The x_repo_auth of this ShowProjectDetailRequest.
        :type: str
        """
        self._x_repo_auth = x_repo_auth

    @property
    def clone_url(self):
        """Gets the clone_url of this ShowProjectDetailRequest.


        :return: The clone_url of this ShowProjectDetailRequest.
        :rtype: str
        """
        return self._clone_url

    @clone_url.setter
    def clone_url(self, clone_url):
        """Sets the clone_url of this ShowProjectDetailRequest.


        :param clone_url: The clone_url of this ShowProjectDetailRequest.
        :type: str
        """
        self._clone_url = clone_url

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
        if not isinstance(other, ShowProjectDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
